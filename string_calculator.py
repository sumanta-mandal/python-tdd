def add(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers.startswith("//"):
        delimiters, numbers = numbers[2:].split("\n", 1)
        delimiters = delimiters.strip('[]').split('][')
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
    numbers = numbers.replace("\n", ",")
    nums = [int(num) for num in numbers.split(',')]
    nums = [num for num in nums if num <= 1000]
    negatives = [n for n in nums if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed: {','.join(map(str, negatives))}")
    return sum(nums)
