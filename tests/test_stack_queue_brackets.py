import pytest
from stack_queue_brackets.stack_queue_brackets import(
    Stack,
    validate_brackets
)


@pytest.mark.parametrize("string, expected", [
    ("{}", True),
    ("{}(){}", True),
    ("()[[Extra Characters]]", True),
    ("(){}[[]]", True),
    ("{}{Code}[Fellows](())", True),
    ("[({}])", False),
    ("(](", False),
    ("{(})", False),
    ("", True),  # Empty string
    ("(", False),  # Unbalanced opening bracket
    (")", False),  # Unbalanced closing bracket
    ("((", False),  # Unbalanced opening brackets
    ("))", False),  # Unbalanced closing brackets
    ("[({})]", True),  # Nested brackets
    ("[({)}]", False),  # Mismatched brackets
    ("({[}])", False),  # Mismatched brackets
    ("({}[])", True),  # Balanced brackets
])
def test_validate_brackets(string, expected):
    assert validate_brackets(string) == expected


    