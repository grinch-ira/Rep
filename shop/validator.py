import re


class Validator:

	@staticmethod
	def check_str_is_not_none_and_not_empty(string):
		result = False
		if string is not None and string != '':
			result = True
		return result

	@staticmethod
	def check_length(string, min, max):
		result = False
		if string is not None:
			result = min <= len(string) <= max
		return result

	@staticmethod
	def check_email(string):
		result = False
		if string is not None and re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string, re.MULTILINE):
			result = True
		return result

	@staticmethod
	def check_phone_number(string):
		result = False
		if string is not None and re.match(r"(^(80|[+](375))(29|44|25|33)[0-9]{7}$)", string, re.MULTILINE):
			result = True
		return result

	@staticmethod
	def check_for_Latin_letters(string):
		result = False
		if string is not None and re.match(r"[a-zA-Z]", string, re.MULTILINE):
			result = True
		return result

	@staticmethod
	def check_on_figures(string):
		result = False
		if string is not None and re.match(r"[0-9]", string, flags=re.MULTILINE):
			result = True
		return result
