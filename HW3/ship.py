import random


# тип корабля
ship_type = {1: "liner", 2: "tow", 3: "tanker"}

def Read(ship, strArray, i):
    # Должно быть как минимум четыре непрочитанных значения в массиве
    # (скорость, расстояние, водоизмещение и тип корабля)
    if i >= len(strArray) - 3:
        return 0
    ship.append("ship")

    speed = int(strArray[i])  # скорость
    distance = float(strArray[i + 1])  # расстояние
    displacement = int(strArray[i + 2])  # водоизмещение
    ship_type_input = int(strArray[i + 3])  # тип корабля

    ship.append(speed)
    ship.append(distance)
    ship.append(displacement)
    ship.append(ship_type[ship_type_input])

    i += 4
    return i


def Random(ship):
    ship.append("plain")
    ship.append(random.randint(100, 1500))  # скорость
    ship.append(random.random() * 1000 + 1000)  # расстояние
    ship.append(random.randint(500, 2000))  # водоизмещение
    ship.append(ship_type[random.randint(1, 3)])  # тип корабля
    pass


def Print(ship):
    print("It is a ship: speed = ", ship[1], "; distance = ", ship[2],
          "; time = ", Time(ship), "; displacement = ", ship[3], "; type of ship is ", ship[4], sep="")
    pass


def Write(ship, ostream):
    ostream.write("It is a ship: speed = {}; distance = {}; time = {}; displacement = {}; type of ship is "
                  .format(ship[1], round(ship[2], 3), Time(ship), ship[3], ship[4]))
    pass


def Time(ship):
    return ship[2] / ship[1]
    pass
