"""
This module implements the Vigenere cipher for encryption and decryption.
It provides two main functions:
1. encrypt_vigenere: Encrypts a given plaintext using the Vigenere cipher.
2. decrypt_vigenere: Decrypts a given ciphertext using the Vigenere cipher.
"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()  # Ensure the keyword is in uppercase
    keyword_repeated = keyword * (len(plaintext) // len(keyword))
    keyword_repeated += keyword[: len(plaintext) % len(keyword)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(k_char.upper()) - ord("A")  # Calculate shift from keyword character
            if p_char.isupper():
                ciphertext += chr((ord(p_char) - ord("A") + shift) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(p_char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += p_char  # Non-alphabetic characters remain unchanged

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()  # Ensure the keyword is in uppercase
    keyword_repeated = keyword * (len(ciphertext) // len(keyword))
    keyword_repeated += keyword[: len(ciphertext) % len(keyword)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(k_char.upper()) - ord("A")  # Calculate shift from keyword character
            if c_char.isupper():
                plaintext += chr((ord(c_char) - ord("A") - shift) % 26 + ord("A"))
            else:
                plaintext += chr((ord(c_char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += c_char  # Non-alphabetic characters remain unchanged

    return plaintext
