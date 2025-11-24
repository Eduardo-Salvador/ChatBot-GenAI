import json

data = {
    "name":"IFood",
    "founder": 2011,
    "companies":[{
            "name": "Sympla",
            "founder": 2011
        }, 
        {
            "name":"Zoop",
            "founder": 2013
        }, 
        {
            "name": "MovilePay",
            "founder": 1999
        },
        {
            "name":"Moova",
            "founder": 2019
        }]
}

with open('TestingJSON/ifood.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

with open('TestingJSON/ifood.json', 'r', encoding="UTF-8") as arq:
    dataFilter = json.load(arq)

founder2012orBetter = list(filter(lambda c: c["founder"] >= 2012, dataFilter["companies"]))
print(founder2012orBetter)