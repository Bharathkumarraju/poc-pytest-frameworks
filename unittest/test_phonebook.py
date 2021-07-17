import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

# setUp is called before every test method and tearDown is called afterwards.
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
            self.phonebook.add("Bharath", "123456")
            number =  self.phonebook.lookup("Bharath")
            self.assertEqual("123456", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Bharath", "12345")
        self.phonebook.add("Raju", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("Bharath", "12345")
        self.phonebook.add("Kumar", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("Bharath", "12345")
        self.phonebook.add("Kumar", "123")
        self.assertFalse(self.phonebook.is_consistent())

'''
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Kumar", "123343")
        self.assertIn("Kumar", self.phonebook.get_names())
        self.assertIn("123343", self.phonebook.get_numbers())
'''