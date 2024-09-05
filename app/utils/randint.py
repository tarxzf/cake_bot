from asyncio import get_event_loop
from random import randint as _rnd


async def randint(min_: int, max_: int) -> int:    
    loop = get_event_loop()
    result = await loop.run_in_executor(None, _rnd, min_, max_)
    return result
