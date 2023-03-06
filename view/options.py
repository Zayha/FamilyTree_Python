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
        self.get_console().add_human()


class LoadTree(Options):
    def description(self):
        return "Загрузить файл"

    def execute(self):
        self.get_console().load_tree()


class SaveTree(Options):
    def description(self):
        return "Сохранить файл"

    def execute(self):
        self.get_console().save_tree()


class EditHuman(Options):
    def description(self):
        return "Изменить человека"

    def execute(self):
        pass


class DellHuman(Options):
    def description(self):
        return "Удалить человека"

    def execute(self):
        return self.get_console().del_human()


class AddChild(Options):
    def description(self):
        return "Добавить ребенка"

    def execute(self):
        self.get_console().add_child()


class InfoHuman(Options):
    def description(self):
        return "Информация по человеку"

    def execute(self):
        self.get_console().human_info()


class ShowAll(Options):
    def description(self):
        return "Список всех персон"

    def execute(self):
        self.get_console().show_all()


class ShowTree(Options):
    def description(self):
        return "Показать дерево"

    def execute(self):
        self.get_console().show_tree()


class AddPartner(Options):
    def description(self):
        return "Добавить супруга"

    def execute(self):
        pass


class FindHuman(Options):
    def description(self):
        return "Найти человека"

    def execute(self):
        pass
