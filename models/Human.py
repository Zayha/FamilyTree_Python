import datetime
import uuid
from typing import List

from validator import Validator


class Human:

    def __init__(self, **kwargs) -> None:
        self.children = []
        v1 = Validator()
        self.id_num = uuid.uuid4()
        self.first_name = kwargs.get("first_name")
        self.patronymic = kwargs.get("patronymic")
        self.last_name = kwargs.get("last_name")

        if v1.check_date(kwargs.get("b_date")):
            self.b_date = kwargs.get("b_date")
        if v1.check_date(kwargs.get("d_date")):
            self.__d_date = kwargs.get("d_date")
        else:
            self.__d_date = None

        if isinstance(kwargs.get("father"), Human):
            self.father = kwargs.get("father")
        else:
            self.father = None
        if isinstance(kwargs.get("mother"), Human):
            self.mother = kwargs.get("mother")
        else:
            self.mother = None
        if isinstance(kwargs.get("children"), List) and v1.check_type_in_list(kwargs.get("children"), Human):
            self.children = kwargs.get("children")

        self.partner = kwargs.get("partner")
        if v1.check_gender(kwargs.get("gender")):
            self.__gender = kwargs.get("gender")
        else:
            self.__gender = "0"
        self.place_of_b = kwargs.get("place_of_b")

    def __str__(self):
        return f"ID: {self.id_num}, {self.get_gender()}, {self.first_name} " \
               f"{self.patronymic} {self.last_name} ({self.b_date} - " \
               f"{self.__d_date if self.__d_date is not None else 'по сей день'}), {self.place_of_b}"

    def __iter__(self):
        return iter(self.children)

    def __gt__(self, other):
        if hasattr(self, 'b_date') and hasattr(other, 'b_date'):
            return self.get_age() > other.get_age()
        else:
            return False

    def get_age(self):
        if hasattr(self, 'b_date'):
            b_date = datetime.datetime.strptime(self.b_date, '%d.%m.%Y')
            if self.__d_date is not None:
                age = datetime.datetime.strptime(self.__d_date, '%d.%m.%Y') - b_date
            else:
                age = datetime.datetime.now() - b_date
            return int(age.days / 365.25)
        else:
            return None

    def add_child(self, human):
        if isinstance(human, Human):
            child_b_date = datetime.datetime.strptime(human.b_date, '%d.%m.%Y')
            parent_b_date = datetime.datetime.strptime(self.b_date, '%d.%m.%Y')
            if child_b_date > parent_b_date:
                self.children.append(human)

    def set_date_of_d(self, date_of_death: str) -> bool:
        val = Validator()
        if val.check_date(date_of_death):
            if datetime.datetime.strptime(date_of_death, '%d.%m.%Y') > datetime.datetime.strptime(self.b_date,
                                                                                                  '%d.%m.%Y'):
                self.__d_date = date_of_death
                return True
            else:
                return False

    def get_gender(self):
        return self.__gender

    def set_father(self, human):
        self.father = human

    def set_mother(self, human):
        self.mother = human

    def get_children(self):
        return self.children

    def get_d_date(self):
        return self.__d_date

    def get_b_date(self):
        return self.b_date

    def set_partner(self, partner):
        self.partner = partner

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_patronymic(self):
        return self.patronymic

    def get_place_of_b(self):
        return self.place_of_b
