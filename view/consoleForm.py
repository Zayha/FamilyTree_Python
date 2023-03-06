class ConsoleForm:
    def console_human(self):
        result = {}
        lst_console = [
            "Пол M/F",
            "Имя",
            "Отчество",
            "Фамилия",
            "Дата рождения",
            "Дата смерти",
            "Место рождения"
        ]
        lst_key = [
            "gender",
            "first_name",
            "patronymic",
            "last_name",
            "b_date",
            "d_date",
            "place_of_b"
        ]

        print("Укажите запрашиваемые данные, если их нет, укажите 0")

        for i in range(len(lst_console)):
            result[lst_key[i]] = input(lst_console[i] + ": ")

        return result


