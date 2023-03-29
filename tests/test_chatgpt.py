from chatgpt import calculate_score
import pytest

def test_45():
    assert calculate_score("45") == 9

def test_11():
    assert calculate_score("11") == 2

def test_multiroll_23_45():
    assert calculate_score("23 45") == 14

def test_spare():
    assert calculate_score("4/ 32") == 18

def test_game():
    assert calculate_score("X 45 4/ 32") == 46

def test_perfect_game():
    assert calculate_score("X X X X X X X X X XXX") == 300

def test_example_game():
    assert calculate_score("54 4/ 70 X X X 53 6/ 4/ XXX") == 178
