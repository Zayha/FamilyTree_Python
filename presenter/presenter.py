from service import Service


class Presenter:

    def __init__(self):
        self.service = Service()

    def add_human(self, data):
        self.service.add_human(data)

    def show_all(self):
        return self.service.show_all()

    def add_child(self, child_id, parent_id):
        return self.service.add_child(child_id, parent_id)

    def save_tree(self, path):
        return self.service.save_tree(path)

    def load_tree(self, path):
        return self.service.load_tree(path)

    def show_tree(self, id_root):
        return self.service.show_tree(id_root)

    def human_info(self, id_root):
        return self.service.human_info(id_root)

    def del_human(self, id_human):
        return self.service.del_human(id_human)

