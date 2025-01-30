def filter_by_state(data: list[dict[str, str]], state: str = 'EXECUTED') -> list[dict[str, str]]:
    for dictionary in data:
        if dictionary['state'] != state:
            del dictionary
    return data
