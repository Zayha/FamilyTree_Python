from view.options import Exit, AddHuman, LoadTree, SaveTree, EditHuman, DellHuman, AddChild, InfoHuman, ShowAll, \
    ShowTree, AddPartner


class Menu:

    def __init__(self, console):
        self.commands = [AddHuman(console),
                         AddChild(console),
                         AddPartner(console),
                         InfoHuman(console),
                         ShowAll(console),
                         ShowTree(console),
                         LoadTree(console),
                         SaveTree(console),
                         EditHuman(console),
                         DellHuman(console),
                         Exit(console)
                         ]

    def print_menu(self):
        result = []
        for i in range(len(self.commands)):
            result.append(f"{i + 1}: {self.commands[i].description()} \n")
        print("".join(result))

    def execute(self, num: int):
        if 1 <= num <= len(self.commands):
            self.commands[num - 1].execute()