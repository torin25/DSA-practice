def merge(word1, word2):
    merged = []

    for i in range(min(len(word1), len(word2))):
        merged.append(word1[i])
        merged.append(word2[i])

    merged.append(word1[i+1:] if len(word1) > len(word2) else word2[i+1:])

    return ''.join(merged)

# Example usage
sol = merge("abc", "pqr")
print(sol)  # Output: apbqcr
