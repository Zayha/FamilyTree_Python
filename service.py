import datetime

from file_l_s import Ser_file
from filter import Filter
from models.FamilyTree import FamilyTree
from models.Human import Human
from validator import Validator


class Service:

    def __init__(self) -> None:
        self.family_tree = FamilyTree()
        self.sf = Ser_file()

    def show_human(self, human):
        return f"{human}"

    def add_human(self, data):
        self.family_tree.add_to_family(Human(**data))

    def show_all(self):
        return self._create_str_from_list(self.family_tree)

    def _create_str_from_list(self, lst):
        result = "Общий список:\n"
        for i in lst:
            result += f"{i}\n"
        return result

    def get_unit_by_id(self, unit_id):
        for i in self.family_tree:
            if str(i.id_num) == unit_id:
                return i

    def add_child(self, child_id, parent_id):
        child: Human = self.get_unit_by_id(child_id)
        parent: Human = self.get_unit_by_id(parent_id)
        if child not in parent.children:
            parent.add_child(child)
            if parent.get_gender() == "M":
                child.set_father(parent)
            if parent.get_gender() == "F":
                child.set_mother(parent)
            return True
        return False

    def save_tree(self, path: str):
        return self.sf.save_file(self.family_tree, path)

    def load_tree(self, path):
        temp_family = self.sf.load_file(path)
        if temp_family is not None:
            self.family_tree = temp_family
            return True
        else:
            return False

    def show_tree(self, root_id, indent=0):
        root: Human = self.get_unit_by_id(root_id)
        tree_str = " " * indent + f"{'└─── ' if indent > 0 else ''}" + str(root) + "\n"
        if len(root.children) > 0:
            for child in root.children:
                tree_str += self.show_tree(str(child.id_num), indent + 5)
        return tree_str

    def check_id_in_family(self, id_check):
        for i in self.family_tree:
            if str(i.id_num) == id_check:
                return True
        return False

    def human_info(self, root_id):
        if self.check_id_in_family(root_id):
            human = self.get_unit_by_id(root_id)
            result = f"{human}" + "\n"
            if human.get_d_date() is None:
                result += f"Возраст {human.get_age()} лет" + "\n"
            else:
                result += f"Прожил {human.get_age()} лет" + "\n"
            if human.partner is None:
                result += "Информация по супругу/супруге отсутствует\n"
            else:
                result += "Супруг/супруга:\n" + human.partner
            if len(human.children) > 0:
                result += f'Имеет: {len(human.children)} детей/ребенка'
                counter = 0
                for i in human.children:
                    if i.children is not None:
                        counter += len(i.children)
                if counter > 0:
                    result += "\n" + f"Имеет: {counter} внуков(а)"
            else:
                result += 'Детей нет'
            if human.father is not None:
                result += "\n" + f"Отец: {human.father}"
            else:
                result += "\n" + f"Отец: информация отсутствует"
            if human.mother is not None:
                result += "\n" + f"Мать: {human.mother}"
            else:
                result += "\n" + f"Мать: информация отсутствует"
            return result
        else:
            return "Информация отсутствует!"

    def del_human(self, id_human):
        if self.check_id_in_family(id_human):
            human = self.get_unit_by_id(id_human)
            self.family_tree.del_from_family(human)
            return True
        else:
            return False

    def add_partner(self, id_partner1, id_partner2):
        if self.check_id_in_family(id_partner1) and self.check_id_in_family(id_partner2):
            partner1: Human = self.get_unit_by_id(id_partner1)
            partner2: Human = self.get_unit_by_id(id_partner2)
            partner1.set_partner(partner2)
            partner2.set_partner(partner1)
            return True
        else:
            return False

    def sort_by_birth_date(self):
        self.family_tree = sorted(self.family_tree, key=lambda x: datetime.datetime.strptime(x.b_date, '%d.%m.%Y'))

    def find_human(self, data: dict):
        result = "Результаты поиска: \n"
        val = Validator()
        filter_family = Filter(self.family_tree)
        if val.check_date(data.get("b_date_from")) or data.get("b_date_from") == "*":
            if val.check_date(data.get("b_date_to")) or data.get("b_date_to") == "*":
                if val.check_date(data.get("b_date_from")) or data.get("b_date_from") == "*":
                    if val.check_date(data.get("b_date_to")) or data.get("b_date_to") == "*":
                        filter_family.filter_date(data.get("b_date_from"), data.get("b_date_to"), "get_b_date")
                        filter_family.filter_date(data.get("d_date_from"), data.get("d_date_to"), "get_d_date")
                        filter_family.filter_str(data.get("gender"), "get_gender")
                        filter_family.filter_str(data.get("first_name"), "get_first_name")
                        filter_family.filter_str(data.get("patronymic"), "get_patronymic")
                        filter_family.filter_str(data.get("last_name"), "get_last_name")
                        filter_family.filter_str(data.get("place_of_b"), "get_place_of_b")

        if len(filter_family.get_result()) > 0:
            result += '\n'.join(filter_family.get_result())
        else:
            result += "\nНет результатов удовлетворящих критериям поиска!"
        return result
