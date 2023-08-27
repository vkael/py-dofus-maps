import json, pickle

d = dict()
with open("input/MapPositions.json", 'r') as f:
    data = json.load(f)

    for map in data["data"]:
        x = map["posX"]
        y = map["posY"]

        d[ int(map["id"]) ] = "{} {}".format(x, y)

with open('output/maps.pkl', 'wb') as f:
    pickle.dump(d, f)
