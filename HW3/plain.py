import random


# Считывание данных из файла
def Read(plain, strArray, i):
    # Должно быть как минимум четыре непрочитанных значения в массиве
    # (скорость, расстояние, дальность полёта и грузоподъёмность)
    if i >= len(strArray) - 3:
        return 0
    plain.append("plain")

    speed = int(strArray[i])  # скорость
    distance = float(strArray[i + 1])  # расстояние
    range_plain = int(strArray[i + 2])  # дальность полёта
    capacity = int(strArray[i + 3])  # грузопдъёмность

    plain.append(speed)
    plain.append(distance)
    plain.append(range_plain)
    plain.append(capacity)

    i += 4
    return i


def Random(plain):
    plain.append("plain")
    plain.append(random.randint(100, 1500))  # скорость
    plain.append(random.random() * 1000 + 1000)  # расстояние
    plain.append(random.randint(2000, 10000))  # дальность полёта
    plain.append(random.randint(1, 20))  # грузопдъёмность
    pass


def Print(plain):
    print("It is a plain: speed = ", plain[1], "; distance = ", plain[2],
          "; time = ", Time(plain), "; range = ", plain[3], "; capacity = ", plain[4], sep="")
    pass


def Write(plain, ostream):
    ostream.write("It is a plain: speed = {}; distance = {}; time = {}; range = {}; capacity = {}"
                  .format(plain[1], round(plain[2], 3), Time(plain), plain[3], plain[4]))
    pass


def Time(plain):
    return plain[2] / plain[1]
    pass

