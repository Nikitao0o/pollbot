import json
from pprint import pprint
class FCodes:
    def __init__(self,file = "project #5\pollbot\codes.JSON"):
        self.file= file
        with open(file=self.file,mode="r") as file:
            self.dicter = json.load(fp=file)

class Codes(FCodes):
    def writer(self,key_cls = None,value_cls = None):
        if key_cls != None:
            obj = {key_cls:value_cls}
            self.dicter.update(obj)
        with open(file=self.file,mode="w") as file:
            json.dump(obj=self.dicter,fp=file,ensure_ascii=False)
    def deleter(self,key_del):
        try:
            self.dicter.pop(key_del) 
        except KeyError:
            print("Ключ не найден")
            pass
        self.writer()


#Быстро добавление через консоль
if __name__ == '__main__':
    print("Консоль управления JSON файлом\n","Введите номер команды:")
    while True:
        comd= input("1. Добавить значение 2. Вывести список ключей 3. Удалить элемент\n")
        if comd == "1":
            key_in = input("Key:\n")
            value_in = input("Value:\n")
            Codes.writer(self=Codes(),key_cls=key_in,value_cls=value_in)
            pass
        elif comd == "2":
            pprint(FCodes().dicter)
            pass
        elif comd == "3":
            kdel = input("Жду ключ объекта удаления:\n")
            Codes.deleter(self=Codes(),key_del=kdel)
            pass
        elif comd == "x":
            break
        else: print("Неизвестная команда\n")
