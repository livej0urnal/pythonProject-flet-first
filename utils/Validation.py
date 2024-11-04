import re


class Validation:
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_password(self, password):
        if len(password) < 5:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not re.search(r"[@_!#$%^&*()<>/\|}{~:]", password):
            return False

        return True
