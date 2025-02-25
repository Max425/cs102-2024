"""
Реализация шифра Цезаря.
Функции:
- encrypt_caesar: шифрует текст с заданным сдвигом.
- decrypt_caesar: дешифрует текст.
"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if "A" <= char <= "Z":  # Заглавные буквы
            ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= char <= "z":  # Строчные буквы
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char  # Остальные символы не меняем
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if "A" <= char <= "Z":  # Заглавные буквы
            plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= char <= "z":  # Строчные буквы
            plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += char  # Остальные символы не меняем
    return plaintext
