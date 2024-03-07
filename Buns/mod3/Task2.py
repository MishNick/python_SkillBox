import unittest

def decrypt(encryption: str) -> str:
    result: list = []
    dots: int = 0
    for symbol in encryption:
        if symbol != ".":
            result.append(symbol)
            dots = 0
            continue

        dots += 1
        if dots == 2 and result:
            result.pop()
            dots = 0

    return "".join(result)


class DecryptTestCase(unittest.TestCase):
    def test_no_dots(self):
        encrypted = "абра-кадабра."
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "абра-кадабра")

    def test_one_dot(self):
        encrypted = "абраа..-кадабра"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "абра-кадабра")

        encrypted = " абраа..-.кадабра"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "абра-кадабра")

        encrypted = "абра--..кадабра"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "абра-кадабра")

    def test_two_dots(self):
        encrypted = "абрау...-кадабра"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "абра-кадабра")

    def test_empty_string(self):
        encrypted = "абра........"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "")

    def test_one_character(self):
        encrypted = "абр......a."
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "a")

    def test_numbers(self):
        encrypted = "1..2.3"
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "23")

    def test_only_dots(self):
        encrypted = "."
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "")

    def test_many_dots(self):
        encrypted = "1......................."
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, "")


if __name__ == "__main__":
    unittest.main()

