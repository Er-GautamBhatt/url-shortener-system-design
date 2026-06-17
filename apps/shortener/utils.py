import random
import string

CHARS = string.ascii_letters + string.digits


def generate_code(length=7):
    return "".join(
        random.choice(CHARS)
        for _ in range(length)
    )