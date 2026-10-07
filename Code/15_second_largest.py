def find_second_largest(numbers):
    """Return the second largest unique number from a list. Returns None if not possible."""
    if len(numbers) < 2:
        return None
        
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None

if __name__ == "__main__":
    elements = input("Enter numbers separated by spaces: ")
    num_list = [int(x) for x in elements.split()]
    print(f"Second largest number: {find_second_largest(num_list)}")