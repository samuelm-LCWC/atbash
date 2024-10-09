import pytest
from Atbash import atbash  # Assuming the function is defined in 'task.py'

def test_atbash_lowercase():
    # Test for a basic lowercase word
    result = atbash("apple")
    assert result == "zkkov"

def test_atbash_mixed_case():
    # Test for a mixed case sentence with punctuation
    result = atbash("Hello world!")
    assert result == "Svool dliow!"

def test_atbash_with_numbers():
    # Test for a sentence with numbers and punctuation
    result = atbash("Christmas is the 25th of December")
    assert result == "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"

def test_atbash_only_special_characters():
    # Test for a string with only special characters
    result = atbash("12345!@#$%")
    assert result == "12345!@#$%"

def test_atbash_empty_string():
    # Test for an empty string
    result = atbash("")
    assert result == ""

def test_atbash_single_character():
    # Test for a single letter
    result = atbash("A")
    assert result == "Z"

def test_atbash_full_alphabet():
    # Test for the full alphabet to ensure all letters are correctly mirrored
    result = atbash("abcdefghijklmnopqrstuvwxyz")
    assert result == "zyxwvutsrqponmlkjihgfedcba"

def test_atbash_mixed_letters_and_special_characters():
    # Test for a string with mixed letters and special characters
    result = atbash("Atbash Cipher, 2024!")
    assert result == "Zgyzhs Xrksvi, 2024!"
