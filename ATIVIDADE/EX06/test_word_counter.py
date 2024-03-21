# test_word_counter.py
import pytest
from word_counter import count_words

def test_count_words_empty_string():
    assert count_words("") == 0

def test_count_words_single_word():
    assert count_words("Hello") == 1

def test_count_words_multiple_words():
    assert count_words("Hello world") == 2
    assert count_words("The quick brown fox jumps over the lazy dog") == 9

def test_count_words_with_special_characters():
    assert count_words("The #quick brown fox jumps over the lazy dog!") == 9
    assert count_words("Hello12345") == 1
