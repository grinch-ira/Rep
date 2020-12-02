from django.test import TestCase
from shop.validator import Validator


class TestValidator(TestCase):
    def test_check_str_is_not_none_and_not_empty_valid_string_expected_True(self):
        string = 'Course Work'

        actual = Validator.check_str_is_not_none_and_not_empty(string)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_str_is_not_none_and_not_empty_empty_string_expected_False(self):
        string = ''

        actual = Validator.check_str_is_not_none_and_not_empty(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_str_is_not_none_and_not_empty_string_is_None_expected_False(self):
        string = None

        actual = Validator.check_str_is_not_none_and_not_empty(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_length_valid_string_expected_True(self):
        string = "Course Work"

        actual = Validator.check_length(string, 3, 20)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_length_length_is_least_expected_False(self):
        string = "Course Work"

        actual = Validator.check_length(string, 17, 20)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_length_length_is_larger_expected_False(self):
        string = "Course Work"

        actual = Validator.check_length(string, 3, 6)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_length_length_in_interval_expected_True(self):
        string = "Course Work"

        actual = Validator.check_length(string, 3, 18)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_length_string_is_empty_expected_False(self):
        string = ""

        actual = Validator.check_length(string, 3, 18)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_length_string_is_None_expected_False(self):
        string = None

        actual = Validator.check_length(string, 3, 18)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_email_string_is_None_expected_False(self):
        string = None

        actual = Validator.check_email(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_email_string_is_empty_expected_False(self):
        string = ""

        actual = Validator.check_email(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_email_valid_string_expected_True(self):
        string = "ira_hrinyk@mail.ru"

        actual = Validator.check_email(string)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_email_invalid_string_expected_False(self):
        string = "ira_hrinyk@mail"

        actual = Validator.check_email(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_phone_number_invalid_string_expected_False(self):
        string = "ira_hrinyk"

        actual = Validator.check_phone_number(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_phone_number_valid_string_expected_True(self):
        string = "80445789865"

        actual = Validator.check_phone_number(string)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_phone_number_string_is_empty_expected_False(self):
        string = ""

        actual = Validator.check_phone_number(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_phone_number_string_is_None_expected_False(self):
        string = None

        actual = Validator.check_phone_number(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_for_Latin_letters_string_is_None_expected_False(self):
        string = None

        actual = Validator.check_for_Latin_letters(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_for_Latin_letters_string_is_empty_expected_False(self):
        string = ''

        actual = Validator.check_for_Latin_letters(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_for_Latin_letters_valid_string_expected_True(self):
        string = 'qwerty8'

        actual = Validator.check_for_Latin_letters(string)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_for_Latin_letters_invalid_string_expected_False(self):
        string = '123'

        actual = Validator.check_for_Latin_letters(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_on_figures_valid_string_expected_True(self):
        string = '123'

        actual = Validator.check_on_figures(string)
        expected = True

        self.assertEquals(actual, expected)

    def test_check_on_figures_invalid_string_expected_False(self):
        string = 'asdf'

        actual = Validator.check_on_figures(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_on_figures_empty_string_expected_False(self):
        string = ''

        actual = Validator.check_on_figures(string)
        expected = False

        self.assertEquals(actual, expected)

    def test_check_on_figures_None_string_expected_False(self):
        string = None

        actual = Validator.check_on_figures(string)
        expected = False

        self.assertEquals(actual, expected)