import json


def writeToJSON(path, fileName, data):
    filePath = "./" + path + "./" + fileName + ".json"
    with open(filePath, "w") as file:
        json.dump(data, file)
