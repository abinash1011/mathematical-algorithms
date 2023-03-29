def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1



TEXT = "the quick brown fox jumped over a lazy dog"
PATTERN = "fox"

pos = brute_force_string_match(TEXT, PATTERN)
print("String found at index:", pos)