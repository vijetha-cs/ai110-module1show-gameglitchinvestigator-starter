from logic_utils import check_guess, parse_guess, get_range_for_difficulty


def test_check_guess_too_high_says_go_lower():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low_says_go_higher():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_rejects_text():
    ok, value, error = parse_guess("abc")

    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_normal_range_is_1_to_100():
    low, high = get_range_for_difficulty("Normal")

    assert low == 1
    assert high == 100