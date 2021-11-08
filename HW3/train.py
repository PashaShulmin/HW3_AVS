import random


# Считывание данных из файла
def Read(train, strArray, i):
    # Должно быть как минимум три непрочитанных значения в массиве
    # (скорость, расстояние и количество вагонов)
    if i >= len(strArray) - 2:
        return 0
    train.append("train")

    speed = int(strArray[i])  # скорость
    distance = float(strArray[i + 1])  # расстояние
    range_plain = int(strArray[i + 2])  # количество вагонов

    train.append(speed)
    train.append(distance)
    train.append(range_plain)

    i += 3
    return i


def Random(train):
    train.append("train")
    train.append(random.randint(100, 1500))  # скорость
    train.append(random.random() * 1000 + 1000)  # расстояние
    train.append(random.randint(1, 100))  # количество вагонов
    pass


def Print(train):
    print("It is a train: speed = ", train[1], "; distance = ", train[2],
          "; time = ", Time(train), "; number of railway carriages = ", train[3], sep="")
    pass


def Write(train, ostream):
    ostream.write("It is a train: speed = {}; distance = {}; time = {}; number of railway carriages = {}"
                  .format(train[1], round(train[2], 3), Time(train), train[3]))
    pass


def Time(train):
    return train[2] / train[1]
    pass
