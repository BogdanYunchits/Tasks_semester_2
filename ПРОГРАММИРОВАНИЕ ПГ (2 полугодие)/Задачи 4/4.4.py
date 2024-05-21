def find_longest_nonincreasing_subsequence(sequence):
    if not sequence:
        return []

    dp = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[j] >= sequence[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    subsequence = []
    for i in range(len(sequence) - 1, -1, -1):
        if dp[i] == max_length:
            subsequence.append(sequence[i])
            max_length -= 1

    return subsequence[::-1]

sequence = [7, 8, 6, 5, 4, 3]
print(find_longest_nonincreasing_subsequence(sequence))
