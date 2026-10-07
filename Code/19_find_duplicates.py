def find_duplicates(numbers):
    seen = set()
    duplicates = []

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates


if __name__ == "__main__":
    print(find_duplicates([1, 2, 2, 3, 4, 4, 5]))