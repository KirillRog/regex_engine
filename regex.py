import sys
sys.setrecursionlimit(6000)


# compares ch and pattern. Pattern is another char or . metasymbol
def char_matches_re(pattern, ch):
    if pattern == '.':
        return True

    return pattern == ch


# compares words of equal lengths. Invokes char_matches_re for each symbol
# recursively
def word_matches_re(pattern, string):
    if pattern == '':
        return True

    if string == '':
        if pattern == '$':
            return True
        else:
            return False

    if len(pattern) == 1:
        return char_matches_re(pattern[0], string[0])

    # check \\ symbol
    if pattern[0] == '\\':
        return word_matches_re(pattern[1:], string) or\
               word_matches_re(pattern[1:], string[1:])

    # check ? symbol
    if pattern[1] == '?':
        return word_matches_re(pattern[2:], string) or\
               word_matches_re(pattern[0] + pattern[2:], string)

    # check * symbol
    if pattern[1] == '*':
        return word_matches_re(pattern[2:], string) or\
               word_matches_re(pattern, string[1:])

    # check ? symbol
    if pattern[1] == '+':
        return word_matches_re(pattern[0] + pattern[2:], string) or\
               word_matches_re(pattern, string[1:])

    if not char_matches_re(pattern[0], string[0]):
        return False

    return word_matches_re(pattern[1:], string[1:])


# compares arbitrary length string to a pattern
def string_matches_re(pattern, string):
    if not pattern:
        return True

    if not string:
        return False

    # begins with '^'
    if pattern[0] == '^':
        return word_matches_re(pattern[1:], string)

    if word_matches_re(pattern, string):
        return True

    return string_matches_re(pattern, string[1:])


if __name__ == '__main__':
    user_input = input()
    (rexp, val) = user_input.split('|')

    print(string_matches_re(rexp, val))
