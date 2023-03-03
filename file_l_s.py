import pickle


class Ser_file:

    def save_file(self, obj, path):
        serializable_object = pickle.dumps(obj)

        file_name = f"{path}.pkl"
        with open(file_name, 'wb') as file:
            pickle.dump(serializable_object, file)

    def load_file(self, path):
        file_name = f"{path}.pkl"
        with open(file_name, 'rb') as file:
            serialized_object = pickle.load(file)
        return pickle.loads(serialized_object)
