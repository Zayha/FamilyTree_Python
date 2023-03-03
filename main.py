import datetime
from typing import List

from models.Human import Human
from validator import Validator


def main():
    h1 = Human(gender="М", first_name="Ivan", patronymic="Vasil`evich", last_name="Tritonov", b_date="10.10.1956",
               place_of_b="Москва")
    h2 = Human(gender="М", first_name="Vasiliy", patronymic="Fedorovich", last_name="Tritonov", b_date="10.12.1920")

    h2.add_child(h1)
    print(h2.set_date_of_d("31.12.1990"))
    print(h2.get_age())

    for i in h2.children:
        print(i)


if __name__ == "__main__":
    main()
