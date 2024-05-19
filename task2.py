import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list[int]:
    # validate inputs
    if min<1 or max>1000 or not(min<=quantity<=max):
        return []
    numbers = random.sample(range(min, max+1), quantity)
    numbers.sort()
    return numbers