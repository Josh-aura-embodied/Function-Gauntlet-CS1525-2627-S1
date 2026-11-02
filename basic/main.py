def is_even(number):
    """ Return True if number is even and False if it is odd.

    :param number:
    :return:
    """
    if number % 2 == 0:
        return True
    else:
        return False


def count_vowels(text):
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text:
    :return:
    """
    vowels = "aeiou"
    count = 0

    for letter in text.lower():
        if letter in vowels:
            count += 1

    return count


def celsius_to_fahrenheit(celsius):
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius:
    :return:
    """
    return (celsius * 9 / 5) + 32


def reverse_text(text):
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text:
    :return:
    """
    return text[::-1]


def larger_number(a, b):
    """Return whichever of the two integers is larger.

    :param a:
    :param b:
    :return:
    """
    if a > b:
        return a
    else:
        return b


def average_two(a, b):
    """
    """
    return (a + b) / 2


def can_afford(balance, cost):
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance:
    :param cost:
    :return:
    """
    return balance >= cost


def repeat_text(text, times):
    """Return one string containing text repeated the given
    number of times.

    Example:
        repeat_text("Go!", 3) returns "Go!Go!Go!"

    :param text:
    :param times:
    :return:
    """
    return text * times


def contains_word(sentence, word):
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.

    :param sentence:
    :param word:
    :return:
    """
    return word in sentence


def calculate_tip(cost, percent):
    """Calculate and return the amount of tip.

    Example:
        A cost of 20.0 and percent of 15 returns 3.0.

    :param cost:
    :param percent:
    :return:
    """
    return cost * percent / 100


def make_initials(first_name, last_name):
    """
    """
    return first_name[0].upper() + last_name[0].upper()


def percent_score(score, total):
    """Calculate and return a score as a percentage.

    Example:
        A score of 8 out of 10 returns 80.0.

    :param score:
    :param total:
    :return:
    """
    if total == 0:
        raise ValueError("total cannot be zero")
    return score / total * 100


def is_between(number, lower, upper):
    """Return True if number is between lower and upper.
    Otherwise, return False.

    :param number:
    :param lower:
    :param upper:
    :return:
    """
    return lower <= number <= upper


def all_different(a, b, c):
    """Return True if all three values are different.
    Otherwise, return False.

    :param a:
    :param b:
    :param c:
    :return:
    """
    return a != b and a != c and b != c


def average_three(a, b, c):
    """Calculate and return the average of three integers.

    :param a:
    :param b:
    :param c:
    :return:
    """
    return (a + b + c) / 3


def describe_temperature(temperature, cold_limit, hot_limit):
    """Returns a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.

    :param temperature:
    :param cold_limit:
    :param hot_limit:
    :return:
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"