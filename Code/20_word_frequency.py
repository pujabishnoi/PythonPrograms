# Code/20_word_frequency.py
def count_word_frequency(text):
    if not text.strip():
        return {}
    
    # Simple split by whitespace and conversion to lowercase
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Clean punctuation from beginning/end of words
        cleaned_word = word.strip(".,!?;:()\"'")
        if cleaned_word:
            frequency[cleaned_word] = frequency.get(cleaned_word, 0) + 1
            
    return frequency