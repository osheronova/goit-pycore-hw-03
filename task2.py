import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    # We check the validity of the given arguments
    if not (1 <= min <= quantity <= max <= 1000 and quantity > 0): # I do wan't to cover this case  get_numbers_ticket(1, 1, 1)
        return []

    # Generate a random list of numbers
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    # Sort the list
    lottery_numbers.sort()

    return lottery_numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)