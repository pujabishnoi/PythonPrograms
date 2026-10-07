def is_palindrome_string(text):
    """Return True if text is a palindrome (ignores case, spaces, punctuation)."""
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Palindrome" if is_palindrome_string(s) else "Not palindrome!")