from widget import get_date

def filter_by_state(data: list[dict[str, str]], state: str = 'EXECUTED') -> list[dict[str, str]]:
    for dictionary in data:
        if dictionary['state'] != state:
            del dictionary
    return data


def sort_by_date(data: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    sorted_data = sorted(data, key=get_date['date'], reverse=reverse)
    return sorted_data
