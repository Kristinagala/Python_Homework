from stringUtils import StringUtils
import pytest
processor = StringUtils()

# 1 заглавная первая буква


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("house", "House"),
        ("дом", "Дом"),
        ("s", "S"),
    ],
)
def test_capitilize_positive(input_text, expected_output):
    assert processor.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text",
    [
        (123),
        ([])
    ],
)
def test_capitilize_negative(input_text):
    with pytest.raises(AttributeError):
        processor.capitilize(input_text)

# 2 удаление пробелов


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" Нouse", "Нouse"),
        ("     Нouse", "Нouse"),
        ("  1 января 2021", "1 января 2021"),
    ],
)
def test_space_positive(input_text, expected_output):
    assert processor.trim(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text",
    [
        (None),
        (123),
        ([])
    ],
)
def test_space_negative(input_text):
    with pytest.raises((TypeError, AttributeError)):
        processor.trim(input_text)

# 3 текст с разделителем


@pytest.mark.parametrize(
    "string, delimeter, expected",
    [
        ("Sun/Moon/Mars", "/", ["Sun", "Moon", "Mars"]),
        ("Sun:Moon:Mars", ":", ["Sun", "Moon", "Mars"]),
    ],
)
def test_separator_positive(string, delimeter, expected):
    assert processor.to_list(string, delimeter) == expected


@pytest.mark.parametrize(
    "string, delimeter",
    [
        (None, "/"),
        (123, "/"),
    ],
)
def test_separator_negative(string, delimeter):
    with pytest.raises(AttributeError):
        processor.to_list(string, delimeter)


# 4 содержит символ

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("The Matrix", "M", True),
        ("The Matrix", "U", False),
        ("The Matrix", "h", True),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert processor.contains(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Pulp Fiction", "U", False),
        ("", "U", False),
    ],
)
def test_contains_negative(string, symbol, expected):
    assert processor.contains(string, symbol) == expected


# 5 удаляет символ

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("The Matrix", "M", "The atrix"),
        ("The Matrix", "x", "The Matri"),
        ("Matrix Matrix", "M", "atrix atrix"),
        ("Matrix matrix", "Mat", "rix matrix"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert processor.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        (None, "n", None),
        (123, 1, 23),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    with pytest.raises(AttributeError):
        processor.delete_symbol(string, symbol) == expected


# 6 строка начинается с заданного символа

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Fight Club", "F", True),
        ("Fight Club", "U", False),
        ("127 Hours", "1", True),
        ("Fight Club", "Fi", True),
    ],
)
def test_starts_with_positive(string, symbol, expected):
    assert processor.starts_with(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        (" Fight Club", "F", False),
        ("Fight Club", "f", False),
        ("", "F", False),
    ],
)
def test_starts_with_negative(string, symbol, expected):
    assert processor.starts_with(string, symbol) == expected

# 7 строка заканчивается заданным символом


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Interstate 60", "0", True),
        ("Interstate 60", "U", False),
        ("Interstate 60", "60", True),
    ],
)
def test_end_with_positive(string, symbol, expected):
    assert processor.end_with(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("Interstate 60 ", "0", False),
        ("Fight Club", "B", False),
    ],
)
def test_end_with_negative(string, symbol, expected):
    assert processor.end_with(string, symbol) == expected

# 8 пустая строка


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", True),
        ("  ", True),
        (" ",  True),
    ],
)
def test_is_empty_positive(string, expected):
    assert processor.is_empty(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("FightClub", False),
        ("  Interstate 60   ", False),
        ("123", False),
    ],
)
def test_is_empty_negative(string, expected):
    assert processor.is_empty(string) == expected

# 9 список с разделителем


@pytest.mark.parametrize(
    "lst, joiner, expected",
    [
        (["Sun", "Moon", "Mars"], "/", "Sun/Moon/Mars"),
        (["Sun", "Moon", "Mars"], "-", "Sun-Moon-Mars"),
        (["123"], ":", "123"),
        ([], ":", ""),
    ],
)
def test_list_to_string_positive(lst, joiner, expected):
    assert processor.list_to_string(lst, joiner) == expected


@pytest.mark.parametrize(
    "lst, joiner",
    [
        (None, "-"),
        (5, "/"),
    ],
)
def test_list_to_string_negative(lst, joiner):
    with pytest.raises(TypeError):
        processor.list_to_string(lst, joiner)
