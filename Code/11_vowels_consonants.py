def count_vowels_consonants(s):
    """Counts the number of vowels and consonants in a string."""
    vowels = "aeiou"
    v_count = 0
    c_count = 0
    
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    return v_count, c_count

if __name__ == "__main__":
    # Example check
    print(count_vowels_consonants("Hello World"))