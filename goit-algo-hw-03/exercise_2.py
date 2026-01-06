import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (
        min_value < 1
        or max_value > 1000
        or min_value >= max_value
        or quantity <= 0
        or quantity > (max_value - min_value +1)
    ):
        return []
    
    numbers_ticket = set()

    while len(numbers_ticket) < quantity:
        random_number = random.randint(min_value, max_value)
        numbers_ticket.add(random_number)

        return sorted(numbers_ticket)