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
try:
            for i in json.loads(data).keys():
                if int(i) > self.count:
                    self.count = int(i)
            self.count += 1
        except:
            return null
        return json.loads(data)

    def readFile(self, filePath):
        # Dosyayı okuyup içeriğini geri döndürecek
        try:
            f = open(filePath, "r")
            data = f.read()
            f.close()
            return data
        except FileNotFoundError:
            return None
