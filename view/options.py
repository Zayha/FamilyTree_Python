from abc import ABC, abstractmethod


class Options(ABC):

    def __init__(self, console) -> None:
        self.console = console

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def get_console(self):
        return self.console


class Exit(Options):

    def description(self):
        return "Выход из программы"

    def execute(self):
        self.get_console().finish()


class AddHuman(Options):

    def description(self):
        return "Добавить человека"

    def execute(self):
        pass


class LoadTree(Options):
    def description(self):
        return "Загрузить файл"

    def execute(self):
        pass


class SaveTree(Options):
    def description(self):
        return "Сохранить файл"

    def execute(self):
        pass


class EditHuman(Options):
    def description(self):
        return "Изменить человека"

    def execute(self):
        pass


class DellHuman(Options):
    def description(self):
        return "Удалить человека"

    def execute(self):
        pass


class AddChild(Options):
    def description(self):
        return "Добавить ребенка"

    def execute(self):
        pass


class InfoHuman(Options):
    def description(self):
        return "Информация по человеку"

    def execute(self):
        pass


class ShowAll(Options):
    def description(self):
        return "Список всех персон"

    def execute(self):
        pass


class ShowTree(Options):
    def description(self):
        return "Показать дерево"

    def execute(self):
        pass


class AddPartner(Options):
    def description(self):
        return "Добавить супруга"

    def execute(self):
        pass
