def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiter, numbers = numbers[2:].split("\n", 1)
        numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    return sum([int(num) for num in numbers.split(',')])
