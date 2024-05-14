import json

# Добавлю консольный интерфейс с добавлением данных и оптимизирую 


cod = {"start":"старт"}

with open(file="project #5\pollbot\codes.JSON",mode="r") as files:
    tinkoff = json.load(fp=files)
    tinkoff.update(cod)
with open(file="project #5\pollbot\codes.JSON",mode="w") as files:
    json.dump(obj=tinkoff,fp=files,ensure_ascii=False)


