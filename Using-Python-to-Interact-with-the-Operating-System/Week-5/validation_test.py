import unittest
from validations import validate_user


class TestValidator(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlength(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


# Run tests
unittest.main()
