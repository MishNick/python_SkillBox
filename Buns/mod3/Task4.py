import unittest
import datetime


class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name: str = name
        self.yob: int = year_of_birth
        self.address: str = address

    def get_age(self) -> int:
        now: datetime.datetime = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        return self.address == ''


class PersonTestCase(unittest.TestCase):
    def test_get_age(self):
        person = Person('John', 1990)
        age = person.get_age()
        current_year = datetime.datetime.now().year
        expected_age = current_year - 1990
        self.assertEqual(age, expected_age)

    def test_get_name(self):
        person = Person('John', 1990)
        name = person.get_name()
        self.assertEqual(name, 'John')

    def test_set_name(self):
        person = Person('John', 1990)
        person.set_name('Mike')
        name = person.get_name()
        self.assertEqual(name, 'Mike')

    def test_set_address(self):
        person = Person('John', 1990)
        person.set_address('123 Main Street')
        address = person.get_address()
        self.assertEqual(address, '123 Main Street')

    def test_is_homeless_with_address(self):
        person = Person('John', 1990, '123 Main Street')
        is_homeless = person.is_homeless()
        self.assertFalse(is_homeless)

    def test_is_homeless_without_address(self):
        person = Person('John', 1990)
        is_homeless = person.is_homeless()
        self.assertTrue(is_homeless)


if __name__ == '__main__':
    unittest.main()

