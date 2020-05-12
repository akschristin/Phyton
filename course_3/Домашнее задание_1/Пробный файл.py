class TrafficLight:
    # атрибут класса
    __color = ["красный", "желтый", "зеленый"]

    # метод класса
    def __running(self, color_1, color_2, color_3):
        print("Запуск")
       #вывод цветов
        from itertools import cycle

        color = ["красный", "желтый", "зеленый"]
        iter = cycle(color)

        # вывод цветов по времени
        import time
        for el in range(7):
            time.sleep(1)
            print("красный")
        for el in range(2):
            time.sleep(1)
            print("желтый")
        for el in range(5):
            time.sleep(1)
            print("зеленый")
#инкапсуляция
tl = TrafficLight()
print(tl._TrafficLight__color)
tl._TrafficLight__running("красный", "желтый", "зеленый")


