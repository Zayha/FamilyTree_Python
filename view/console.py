from presenter.presenter import Presenter
from services import Services
from view.menu import Menu
from view.view import View


class Console(View):

    def __init__(self, presenter_ex) -> None:
        self.serv = Services()
        self.menu = Menu(self)
        self.presenter = presenter_ex
        self.work = True

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

    # def show_human(self, id_n):
    #     if :
    #         print(self.presenter.show_human(id_n))