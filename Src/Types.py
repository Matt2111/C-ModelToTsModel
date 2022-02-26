from json import dumps, loads

class Types:
    def __init__(self):
        with open("types.json", "r") as file:
            self.types = loads(file.read())

    def _Write(self):
        with open("types.json", "w") as file:
            file.write(dumps(self.types))

    def Set(self, selector, value):
        self.types[selector] = value
        self._Write()

    def Remove(self, typeToRemove):
        newTypes = {}
        for selector in self.types:
            if selector != typeToRemove:
                newTypes[selector] = self.types[selector]
        self.types = newTypes
        self._Write()

    def Read(self, selector):
        if selector in self.types:
            return self.types[selector]
        return selector
