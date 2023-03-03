import datetime
from typing import List

from file_l_s import Ser_file
from models.FamilyTree import FamilyTree
from models.Human import Human
from presenter.presenter import Presenter
from validator import Validator
from view.console import Console
from view.consoleForm import ConsoleForm
from view.menu import Menu


def main():
    # h1 = Human(gender="М", first_name="Ivan", patronymic="Vasil`evich", last_name="Tritonov", b_date="10.10.1956",
    #            place_of_b="Москва")
    # h2 = Human(gender="М", first_name="Vasiliy", patronymic="Fedorovich", last_name="Tritonov", b_date="10.12.1920")

    h2 = Human()
    s = Ser_file()
    h2 = s.load_file("h2")
    # h2.add_child(h1)

    print(h2.set_date_of_d("31.12.1990"))
    print(h2.get_age())

    print(h2)
    for i in h2.children:
        print("  --  ", i)

    # p1 = Presenter()
    # c1 = Console(p1)
    # c1.start()

    # c1 = ConsoleForm()
    # # c1.console_human()
    # h3 = Human(**c1.console_human())
    t1 = FamilyTree()
    t1.add_to_family(h2)
    print(t1)


if __name__ == "__main__":
    main()
