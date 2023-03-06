from models.Human import Human


class Filter:

    def __init__(self, family_tree):
        self.__family_tree = family_tree
        self.__result = self.__family_tree.get_family()

    def search(self, query: str, field: str):
        results = []
        for human in self.__family_tree:
            if isinstance(human, Human):
                value = getattr(human, field, None)
                if value is not None and str(query).lower() in str(value).lower():
                    results.append(human)
        self.__result = results

    def get_result(self):
        return self.__result
