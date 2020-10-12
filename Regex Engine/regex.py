import sys

sys.setrecursionlimit(10000)

regex, str = input().split('|')


def compare_char(regex, str):
    return regex == str or regex == '.' or not regex


def compare_equal_length_str(regex, str):
    if not regex or (regex == "^" and not str):
        return True
    elif regex[1:].startswith('\\'):
        if regex[0] == str[0]:
            return compare_equal_length_str(regex[3:], str[1:])

    elif not str or not compare_char(regex[0], str[0]):
        if regex[0] == '?':
            if regex == '?.':
                return True
            return zero_one(regex, str)
        elif regex[0] == '*':
            if regex == '*.':
                return True
            return zero_multiple(regex, str)
        elif regex[0] == '+':
            if regex == '+.':
                return True
            return one_multiple(regex, str)

        else:
            return False
    else:
        return compare_equal_length_str(regex[1:], str[1:])


def zero_one(regex, str):
    if regex[1] == '.':
        # no chars before ".":
        if regex[2] == str[0]:
            return compare_equal_length_str(regex[3:], str[1:])
        else:
            return zero_one(regex, str[1:])
    # one char before "?"
    elif regex[1] == str[0]:
        return compare_equal_length_str(regex[2:], str[1:])
    # no chars before "?"
    return compare_equal_length_str(regex[2:], str)


def zero_multiple(regex, str):
    if regex[1] == '.':
        # no chars before "."
        if regex[2] == str[0]:
            return compare_equal_length_str(regex[3:], str[1:])
        else:
            return zero_multiple(regex, str[1:])
    # no chars before "*"
    elif regex[1] != str[0]:
        return compare_equal_length_str(regex[2:], str)
    # 1 or more chars before "*"
    else:
        return compare_equal_length_str(regex, str[1:])

def one_multiple(regex, str):
    if regex[1] == '.':
        if regex[2] == str[0]:
            return compare_equal_length_str(regex[3:], str[1:])
        return one_multiple(regex, str[1:])
    # more than one char before "+":
    if regex[1] == str[0] == str[1]:
        return compare_equal_length_str(regex, str[1:])
    # one char before "+"
    elif regex[1] == str[0]:
        return compare_equal_length_str(regex[2:], str[1:])
    else:
        return False


def compare_regex_str(regex, str):
    if not str and regex:
        return False
    elif compare_equal_length_str(regex, str):
        return True
    elif regex[0] == '$':
        return compare_equal_length_str(regex[1:], str)
    else:
        return compare_regex_str(regex, str[1:])


print(compare_regex_str(regex[::-1], str[::-1]))
