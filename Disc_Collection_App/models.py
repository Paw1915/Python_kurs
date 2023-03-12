import json


class Discs:
    def __init__(self):
        try:
            with open("discs.json", "r") as f:
                self.discs = json.load(f)
        except FileNotFoundError:
            self.discs = []

    def all(self):
        return self.discs

    def get(self, id):
        return self.discs[id]

    def create(self, data):
        data.pop('csrf_token')
        self.discs.append(data)

    def save_all(self):
        with open("discs.json", "w") as f:
            json.dump(self.discs, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.discs[id] = data
        self.save_all()


discs = Discs()