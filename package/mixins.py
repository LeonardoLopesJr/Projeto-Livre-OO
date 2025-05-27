import pickle

class SerializableMixin:
    def salvar(self, caminho):
        with open(caminho, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def carregar(cls, caminho):
        with open(caminho, 'rb') as f:
            return pickle.load(f)
