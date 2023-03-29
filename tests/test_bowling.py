from main import get_score
import pytest

def test_45():
    assert get_score("45") == 9

def test_11():
    assert get_score("11") == 2

def test_multiroll_23_45():
    assert get_score("23 45") == 14

def test_spare():
    assert get_score("4/ 32") == 18

def test_kata_example():
    assert get_score("X 45 4/ 32") == 46

def test_perfect_game():
    assert get_score("X X X X X X X X X XXX") == 300

def test_how_ric_plays():
    assert get_score("00 00 00 00 00 00 00 00 00 00 ") == 0

def test_example_game():
    assert get_score("54 4/ 70 X X X 53 6/ 4/ XXX") == 178

def test_another_example_game():
    assert get_score("5/ 45 8/ X 0/ X 62 X 4/ XX") == 169

def test_another_example_no_strikes_in_final():
    assert get_score("5/ 45 8/ X 0/ X 62 X 4/ 44") == 151
