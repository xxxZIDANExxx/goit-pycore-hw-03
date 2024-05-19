import re

def normalize_phone(phone_numbers: str) -> str:
    del_chars_pattern = r"[^+^\d]"
    add_country_code_pattern = r"^0"
    add_plus_pattern = r"^38"
    phone_numbers = re.sub(del_chars_pattern,"", phone_numbers)
    phone_numbers = re.sub(add_country_code_pattern, "+380", phone_numbers)
    phone_numbers = re.sub(add_plus_pattern, "+38", phone_numbers)
    return phone_numbers