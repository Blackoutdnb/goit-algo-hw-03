import re

def normalize_phone(phone_number):
    cleaned_number = re.sub("[^0-9+]", "", phone_number)

    if cleaned_number.startswith("+"):
        pass
    elif cleaned_number.startswith("38"):
        cleaned_number = "+" + cleaned_number
    else:
        cleaned_number = "+38" + cleaned_number

        return cleaned_number