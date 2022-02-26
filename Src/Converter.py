from Types import Types

class Converter:
    def __init__(self):
        self.cModel = []
        self.tsModel = []
        self.types = Types()

    def Clean(self):
        tempCModel = []
        for line in self.cModel:
            line = line.strip().replace("?", "").replace("{", "").replace("}", "")
            if line:
                tempCModel.append(line)
        self.cModel = tempCModel

    def Convert(self, cModel):
        if isinstance(cModel, str):
            cModel = cModel.split("\n")
        self.cModel = cModel
        self.Clean()
        self.tsModel = []
        self.GetTitle()
        if self.tsModel:
            self.GetBody()
        return "\n".join(self.tsModel)

    def GetTitle(self):
        for line in self.cModel:
            if "class" in line:
                title = line.split(" ")[2]
                curlyBracket = "{"
                self.tsModel.append(f"export class {title} {curlyBracket}")

    @staticmethod
    def GetVarName(line):
        return line.split(" ")[2]

    def ConvertType(self, line):
        cType = line.split(" ")[1]
        if "List<" in cType:
            cType = self.types.Read(cType.replace("List<", "").replace(">", ""))
            return f"{cType}[]"
        return self.types.Read(cType)

    def GetBody(self):
        for line in self.cModel:
            if "get;set;" in line.replace(" ", ""):
                self.tsModel.append(f"  {self.GetVarName(line)}: {self.ConvertType(line)};")
        self.tsModel.append("}")
