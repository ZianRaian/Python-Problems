def findSubstring(s: str, k: int) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initial window count
    max_vowel_count = 0
    current_vowel_count = sum(1 for i in range(k) if s[i] in vowels)
    max_substring = s[:k] if current_vowel_count > 0 else "Not found!"
    
    # Store max vowels found
    max_vowel_count = current_vowel_count

    # Sliding window over the string
    for i in range(k, len(s)):
        # Remove left character and add new right character
        if s[i - k] in vowels:
            current_vowel_count -= 1
        if s[i] in vowels:
            current_vowel_count += 1
        
        # Update max if needed
        if current_vowel_count > max_vowel_count:
            max_vowel_count = current_vowel_count
            max_substring = s[i - k + 1 : i + 1]
    
    return max_substring

# Input handling for HackerRank
s = input().strip()
k = int(input().strip())
print(findSubstring(s, k))
