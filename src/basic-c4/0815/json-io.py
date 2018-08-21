import json

data = {

        "no":5,
        "code": ("jas", 1,19),
        "scr": "be quick to listen, slow to speak, slow to anger",

}

filename = "test.json"
with open(filename, "w") as fp:
    json.dump(data, fp)

with open(filename, "r") as fp:
    r = json.load(fp)
    print("no", r["no"])
    print("code", r["code"])
    print("scr", r["scr"])
