import random


def generate_user_id() -> int:
    user_id: int = random.randint(1, 1000)
    return user_id
