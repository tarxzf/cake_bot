async def format_time(time_left: int) -> str:
    hours_left, remainder = divmod(time_left, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    time_tuple = (hours_left, minutes_left, seconds_left)
    time_suffix = ('ч', 'мин', 'сек')
    return ' '.join(f'{i[0]} {i[1]}' for i in zip(time_tuple, time_suffix) if i[0])
