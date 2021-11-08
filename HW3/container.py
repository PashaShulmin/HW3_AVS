import random
from extender import *

# чтение из потока
def Read(cont, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    transportNum = 0  # Счетчк транспорта
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        if key == 1:  # признак самолёта
            i += 1
            plainParams = []  # самолёт - это список с признаком и значениями
            i = plain.Read(plainParams, strArray, i)  # Заполнение транспорта значением и получение следующей позиции
            cont.append(plainParams)  # самолёт поступает в контейнер
        elif key == 2:  # признак поезда
            i += 1
            trainParams = []  # поезд - это список с признаком и значениями
            i = train.Read(trainParams, strArray, i)  # Заполнение транспорта значением и получение следующей позиции
            cont.append(trainParams)  # поезд поступает в контейнер
        elif key == 3:
            i += 1
            shipParams = []  # корабль - это список с признаком и значениями
            i = ship.Read(shipParams, strArray, i)  # Заполнение транспорта значением и получение следующей позиции
            cont.append(shipParams)  # корабль поступает в контейнер
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return transportNum
        # Количество фигур увеличивается на 1
        if i == 0:
            return transportNum
        transportNum += 1
    return transportNum


# рандомное заполнение контейнера
def Random(cont, elementsNumber):
    for i in range(elementsNumber):
        typeOfTransport = random.randint(1, 3)
        if typeOfTransport == 1:
            plainParams = []
            plain.Random(plainParams)
            cont.append(plainParams)
        if typeOfTransport == 2:
            trainParams = []
            train.Random(trainParams)
            cont.append(trainParams)
        if typeOfTransport == 3:
            shipParams = []
            ship.Random(shipParams)
            cont.append(shipParams)
    pass


# вывод в консоль
def Print(cont):
    print("Container stores", len(cont), "transports:")
    counter = 0
    for transport in cont:
        counter += 1
        print(counter, ":", sep="", end=" ")
        if transport[0] == "plain":
            plain.Print(transport)
        elif transport[0] == "train":
            train.Print(transport)
        elif transport[0] == "ship":
            ship.Print(transport)
        else:
            print("Incorrect transport ", transport)
    pass


# вывод в поток
def Write(cont, ostream):
    ostream.write("Container stores {} transports:\n".format(len(cont)))
    counter = 0
    for transport in cont:
        counter += 1
        ostream.write("{}: ".format(counter))
        if transport[0] == "plain":
            plain.Write(transport, ostream)
        elif transport[0] == "train":
            train.Write(transport, ostream)
        elif transport[0] == "ship":
            ship.Write(transport, ostream)
        else:
            ostream.write("Incorrect figure ")
            ostream.write(transport)
        ostream.write("\n")
    pass


def SpecialFunction(cont):
    average = 0
    for transport in cont:
        average += Time(transport)
    average /= len(cont)
    i = 0
    # двигаемся по списку
    while i < len(cont):
        # если элемент удовлетворяет условию, удаляем его
        if Time(cont[i]) > average:
            del cont[i]
        # иначе двигаем указатель
        else:
            i += 1

    pass


def Time(transport):
    return transport[2] / transport[1]
    pass
