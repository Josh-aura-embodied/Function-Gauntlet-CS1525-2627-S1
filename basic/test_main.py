import pytest

from main import (
    is_even,
    count_vowels,
    celsius_to_fahrenheit,
    reverse_text,
    larger_number,
    average_two,
    can_afford,
    repeat_text,
    contains_word,
    calculate_tip,
    make_initials,
    percent_score,
    is_between,
    all_different,
    average_three,
    describe_temperature,
)


# --------------------------------------------------
# is_even()
# --------------------------------------------------

@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-7, False),
    ],
)
def test_is_even(number, expected):
    assert is_even(number) is expected


# --------------------------------------------------
# count_vowels()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
        ("Programming is fun", 5),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected


# --------------------------------------------------
# celsius_to_fahrenheit()
# --------------------------------------------------

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (25, 77.0),
        (10, 50.0),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)


# --------------------------------------------------
# reverse_text()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, expected",
    [
        ("robot", "tobor"),
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
    ],
)
def test_reverse_text(text, expected):
    assert reverse_text(text) == expected


# --------------------------------------------------
# larger_number()
# --------------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 7, 7),
        (10, 2, 10),
        (-1, -5, -1),
        (4, 4, 4),
    ],
)
def test_larger_number(a, b, expected):
    assert larger_number(a, b) == expected


# --------------------------------------------------
# average_two()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 20, 15.0),
        (0, 0, 0.0),
        (-10, 10, 0.0),
        (5, 6, 5.5),
        (100, 50, 75.0),
    ],
)
def test_average_two(first, second, expected):
    assert average_two(first, second) == pytest.approx(expected)


# --------------------------------------------------
# can_afford()
# --------------------------------------------------

@pytest.mark.parametrize(
    "balance, cost, expected",
    [
        (100.0, 50.0, True),
        (50.0, 50.0, True),
        (49.99, 50.0, False),
        (0.0, 0.0, True),
        (10.0, 10.01, False),
    ],
)
def test_can_afford(balance, cost, expected):
    assert can_afford(balance, cost) is expected


# --------------------------------------------------
# repeat_text()
# --------------------------------------------------

@pytest.mark.parametrize(
    "text, times, expected",
    [
        ("Go!", 3, "Go!Go!Go!"),
        ("a", 2, "aa"),
        ("x", 0, ""),
        ("Hi", 1, "Hi"),
    ],
)
def test_repeat_text(text, times, expected):
    assert repeat_text(text, times) == expected


# --------------------------------------------------
# contains_word()
# --------------------------------------------------

@pytest.mark.parametrize(
    "sentence, word, expected",
    [
        ("Python is fun", "Python", True),
        ("Hello there", "bye", False),
        ("catapult", "cat", True),
        ("", "", True),
    ],
)
def test_contains_word(sentence, word, expected):
    assert contains_word(sentence, word) is expected


# --------------------------------------------------
# calculate_tip()
# --------------------------------------------------

@pytest.mark.parametrize(
    "cost, percent, expected",
    [
        (20.0, 15, 3.0),
        (100.0, 20, 20.0),
        (50.0, 10, 5.0),
        (0.0, 18, 0.0),
        (25.5, 20, 5.1),
    ],
)
def test_calculate_tip(cost, percent, expected):
    assert calculate_tip(cost, percent) == pytest.approx(expected)


# --------------------------------------------------
# make_initials()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first_name, last_name, expected",
    [
        ("Ada", "Lovelace", "AL"),
        ("alan", "turing", "AT"),
        ("Grace", "Hopper", "GH"),
        ("John", "SMITH", "JS"),
        ("x", "y", "XY"),
    ],
)
def test_make_initials(first_name, last_name, expected):
    assert make_initials(first_name, last_name) == expected


# --------------------------------------------------
# percent_score()
# --------------------------------------------------

@pytest.mark.parametrize(
    "score, total, expected",
    [
        (8, 10, 80.0),
        (1, 4, 25.0),
        (0, 10, 0.0),
        (10, 10, 100.0),
    ],
)
def test_percent_score(score, total, expected):
    assert percent_score(score, total) == pytest.approx(expected)


# --------------------------------------------------
# is_between()
# --------------------------------------------------

@pytest.mark.parametrize(
    "number, lower, upper, expected",
    [
        (5, 1, 10, True),
        (1, 1, 10, True),
        (10, 1, 10, True),
        (0, 1, 10, False),
        (11, 1, 10, False),
    ],
)
def test_is_between(number, lower, upper, expected):
    assert is_between(number, lower, upper) is expected


# --------------------------------------------------
# all_different()
# --------------------------------------------------

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, True),
        (1, 1, 3, False),
        (1, 2, 1, False),
        (4, 4, 4, False),
    ],
)
def test_all_different(a, b, c, expected):
    assert all_different(a, b, c) is expected


# --------------------------------------------------
# average_three()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first, second, third, expected",
    [
        (1, 2, 3, 2.0),
        (0, 0, 0, 0.0),
        (-3, 0, 3, 0.0),
        (10, 20, 30, 20.0),
    ],
)
def test_average_three(first, second, third, expected):
    assert average_three(first, second, third) == pytest.approx(expected)


# --------------------------------------------------
# describe_temperature()
# --------------------------------------------------

@pytest.mark.parametrize(
    "temperature, cold_limit, hot_limit, expected",
    [
        (5.0, 10.0, 25.0, "cold"),
        (30.0, 10.0, 25.0, "hot"),
        (20.0, 10.0, 25.0, "comfortable"),
        (10.0, 10.0, 25.0, "comfortable"),
        (25.0, 10.0, 25.0, "comfortable"),
    ],
)
def test_describe_temperature(temperature, cold_limit, hot_limit, expected):
    assert describe_temperature(
        temperature, cold_limit, hot_limit
    ) == expected