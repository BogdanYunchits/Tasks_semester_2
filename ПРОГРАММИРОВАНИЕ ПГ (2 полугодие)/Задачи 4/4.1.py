import itertools

def find_all_permutations(word):
    permutations = set()
    for i in range(1, len(word) + 1):
        for combo in itertools.permutations(word, i):
            permutations.add(''.join(combo))
    return permutations

word = "abc"
permutations = find_all_permutations(word)
print(permutations)
