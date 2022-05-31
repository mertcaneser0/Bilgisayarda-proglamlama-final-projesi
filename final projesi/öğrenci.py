import json

class Student:
    def __init__(self):
        self.count = 0
        self.dct = {}

    def dictToJson(self, data):
        # Sözlük tipindeki veriyi json'a çevirir.
        return json.dumps(data)

    def jsonToDict(self, data):
        # Json formatındaki veriyi sözlüğe çevirir.
        self.count = 0
        null = {}
