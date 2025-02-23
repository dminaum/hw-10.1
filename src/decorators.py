import functools
import logging
import sys
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.
    Логи записываются в файл (если указан filename) или выводятся в консоль.
    """
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        logger.propagate = False  # Отключаем повторную обработку логов

        handler = logging.FileHandler(filename, mode='a', encoding='utf-8') if filename else logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))

        if not logger.handlers:  # Чтобы не дублировать обработчики при многократном декорировании
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                logger.info(message)
                if not filename:
                    print(message, flush=True)  # Вывод в консоль с очисткой буфера
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                logger.error(error_message)
                if not filename:
                    print(error_message, file=sys.stderr, flush=True)  # Выводим в stderr
                raise e
            finally:
                handler.close()
                logger.removeHandler(handler)  # Обязательно удаляем handler

        return wrapper

    return decorator
