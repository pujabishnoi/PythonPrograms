def remove_duplicates(lst):
    """Return a new list with duplicate elements removed, preserving the original order."""
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

if __name__ == "__main__":
    elements = input("Enter elements separated by spaces: ")
    input_list = elements.split()
    print(f"List after removing duplicates: {remove_duplicates(input_list)}")