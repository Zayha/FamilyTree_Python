from datetime import datetime


class Validator:

    def check_date(self, date: str) -> bool:
        date_format = "%d.%m.%Y"
        if date is None:
            return True

        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False

    def check_gender(self, gender: str) -> bool:
        return gender == "M" or gender == "F"

    def check_type_in_list(self, lst: list, type_v: type) -> bool:
        for i in lst:
            if not isinstance(i, type_v):
                return False
        return True
