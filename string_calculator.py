def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    return sum([int(num) for num in numbers.split(',')])
