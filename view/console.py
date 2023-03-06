from presenter.presenter import Presenter
from service import Service
from view.consoleForm import ConsoleForm
from view.menu import Menu
from view.view import View


class Console(View):

    def __init__(self, presenter_ex) -> None:
        self.serv = Service()
        self.menu = Menu(self)
        self.presenter = presenter_ex
        self.work = True
        self.form = ConsoleForm()

    def start(self):
        while self.work:
            self.menu.print_menu()
            self.use_command(input("Выберите пункт меню: "))

    def finish(self):
        self.work = False

    def use_command(self, num):
        if num.isdigit():
            self.menu.execute(int(num))

    def set_presenter(self, presenter):
        self.presenter = presenter

    def add_human(self):
        self.presenter.add_human(self.form.console_human())

    def show_all(self):
        print(self.presenter.show_all())

    def add_child(self):
        child_id = input("Укажите ID ребенка: ")
        parent_id = input("Укажите ID родителя которому хотите добавить ребенка: ")

        if self.presenter.add_child(child_id, parent_id):
            print("Добавлен успешно")
        else:
            print("Не был добавлен")

    def save_tree(self):
        file = input("Укажите название файла: ")
        if self.presenter.save_tree(file):
            print(f"Файл {file}.pkl сохранен!")
        else:
            print(f"Файл {file}.pkl не был сохранен!")

    def load_tree(self):
        file = input("Укажите название файла: ")
        if self.presenter.load_tree(file):
            print(f"Файл {file}.pkl загружен!")
        else:
            print(f"Файл {file}.pkl не был загружен!")

    def show_tree(self):
        print(self.presenter.show_tree(input("Укажите id от которого хотите выстроить дерево: ")))

    def human_info(self):
        print(self.presenter.human_info(input("Укажите id по которому хотите получить информацию: ")))

    def del_human(self):
        del_id = input("Укажите ID персоны которую хотите удалить: ")
        if self.presenter.del_human(del_id):
            print(f"ID: {del_id} успешно удален!")
        else:
            print(f"ID: {del_id} не был удален!")

    def add_partner(self):
        if self.presenter.add_partner(input("Укажите ID супруга 1 для присоединения к супругу 2: "),
                                      input("Укажите ID супруга 2 для присоединения к супругу 1: ")):
            print("Информация добавлена!")
        else:
            print("Информация не была добавлена!")

    def sort_by_birth_date(self):
        print(self.presenter.sort_by_birth_date())
