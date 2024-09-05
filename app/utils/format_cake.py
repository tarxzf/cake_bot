async def format_cake(cake: int) -> str:
    if cake >= 1000:
        cake_amount = float(f'{(cake / 1000):.1f}')
        if cake_amount.is_integer():
            cake_amount = int(cake_amount)
        suffix = 'кг'
    else:
        suffix = 'г'
        cake_amount = cake
    
    return f'{cake_amount} {suffix}'
