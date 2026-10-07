def count_char_frequency(text):
    """Return a dictionary containing the frequency of each character in the text."""
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Character frequencies: {count_char_frequency(s)}")