"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""
import skills


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    most_common_alpha = []
    letter_counts = {}

    for letter in input_string:
        # continue to the next word if this is a space.
        if letter == ' ':
            continue
        current_count = letter_counts.get(letter, 0)
        new_count = current_count + 1

        if most_common_alpha == []:
            most_common_alpha.append(letter)
        elif letter_counts[most_common_alpha[0]] == new_count:
            most_common_alpha.append(letter)
        elif new_count > letter_counts[most_common_alpha[0]]:
            most_common_alpha = [letter]

        letter_counts[letter] = new_count

    return list(set(sorted(most_common_alpha)))


# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    words_by_length = skills.sort_by_word_length(words)

    for index, word_tuple in enumerate(words_by_length):
        word_count, words = word_tuple
        words_by_length[index] = (word_count, sorted(words))

    return words_by_length


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
