"""test_app.py - Tests for app.py.

REQ: Test pure functions that return values.

WHY: Pure functions are easy to verify; ensures code works as expected.
"""

from datafun_01_foundations.app_case import get_summary


def test_generate_summary_contains_expected_fields() -> None:
    """Verify that generate_summary() returns a formatted string containing key expected values."""
    result = get_summary()

    # Basic type check - verify we got a string back
    assert isinstance(result, str)

    # Verify the string is not empty
    assert len(result) > 0

    # Verify important content appears in the output
    assert "Course name:" in result
    assert "Course number:" in result
    assert "True" in result or "False" in result  # Boolean value check
