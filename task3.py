import re

def normalize_phone(phone_number: str) -> str:
    del_chars_pattern = r"[^+^\d]"
    add_country_code_pattern = r"^0"
    add_plus_pattern = r"^38"
    phone_number = re.sub(del_chars_pattern,"", phone_number)
    phone_number = re.sub(add_country_code_pattern, "+380", phone_number)
    phone_number = re.sub(add_plus_pattern, "+38", phone_number)
    return phone_number