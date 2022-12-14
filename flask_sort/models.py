"""This file contains the functions used in each route. They are simple
vowel count and sort functions, the logic used is detailed in each function."""


def vowel_count(words):
    """Vowel count method"""
    result = {}

    # Iterates the words array
    for value in words:
        total_vowels = 0

        # Iterates each character of the lowered case string
        for vowel in value.lower():
            # Checks for the vowel and add to the total vowels variable
            if vowel in ('a', 'i', 'u', 'e', 'o'):
                total_vowels = total_vowels + 1

        result[value] = total_vowels

    return result


def sort(words, reverse):
    """Sort method"""
    # Sort the array, the reverse flag is used for reverse sorting
    if reverse == 'asc':
        result = sorted(words, reverse=False)

        return result

    result = sorted(words, reverse=True)
    return result
