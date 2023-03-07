from datetime import datetime


class Filter:

    def __init__(self, family_tree):
        self.__family_tree = family_tree
        self.__result = self.__family_tree.get_family()

    def filter_str(self, query: str, field: str):
        results = []
        if query != "*":
            for human in self.__result:
                value = getattr(human, field, None)()
                if value is not None and str(query).lower() == str(value).lower():
                    results.append(human)
            self.__result = results

    def filter_date(self, date_from: str, date_to: str, field: str):
        result = []
        if date_from == "*":
            date_f = datetime.strptime("01.01.0001", "%d.%m.%Y")
        else:
            date_f = datetime.strptime(date_from, "%d.%m.%Y")
        if date_to == "*":
            date_t = datetime.now()
        else:
            date_t = datetime.strptime(date_from, "%d.%m.%Y")

        for human in self.__result:
            value = getattr(human, field, None)()
            if value is None:
                date_in_value = datetime.now()
            else:
                date_in_value = datetime.strptime(value, "%d.%m.%Y")
            if date_f <= date_in_value <= date_t:
                result.append(human)
        self.__result = result

    def get_result(self):
        result = []
        for human in self.__result:
            result.append(str(human))
        print(len(result))
        return result
