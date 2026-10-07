def reverse_string(text: str) -> str:
    # Reverses a string using a loop instead of [::-1]
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text