from validate_email import validate_email
import re


def validate_email_address(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, email):
        is_validate = validate_email(
            email_address=email,
            check_format=True,
            check_smtp=True,
            smtp_timeout=10, 
            dns_timeout=10
        )
        return is_validate
    return False


email = input("Please enter an email address : ")
result = validate_email_address(email)

print(result)
