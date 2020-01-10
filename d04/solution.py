from itertools import permutations


def count_valid(passphrases):
    """Count the amount of passphrases that contain no duplicate words."""
    count = 0
    for passphrase in passphrases:
        words = passphrase.split(" ")
        valid = True
        for word in words:
            rest = passphrase.replace(word, "", 1).split(" ")
            if word in rest:
                valid = False
                break
        if valid:
            count += 1
    return count


def contains_anagram(rest, word):
    """Check if rest contains an anagram of the given word."""
    for other in rest:
        anagrams = [''.join(p) for p in permutations(other)]
        if word in anagrams:
            return True
    return False


def count_valid_without_anagrams(passphrases):
    """Count the amount of passphrases that contain no anagram of words."""
    count = 0
    for passphrase in passphrases:
        words = passphrase.split(" ")
        valid = True
        for word in words:
            rest = passphrase.replace(word, "", 1).split(" ")
            if contains_anagram(rest, word):
                valid = False
                break
        if valid:
            count += 1
    return count


if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
    passphrases = input.splitlines()
    print(count_valid(passphrases))
    print(count_valid_without_anagrams(passphrases))
