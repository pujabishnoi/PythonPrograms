def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


if __name__ == "__main__":
    print(missing_number([1, 2, 3, 5], 5))