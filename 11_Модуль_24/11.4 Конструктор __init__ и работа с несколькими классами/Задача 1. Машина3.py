class Toyota:# это класс (шаблон, чертёж всех машин этой марки)

    def __init__(self, colour = 'red', price = 1e6, max_speed = 200, current_speed = 0):
        self.colour = colour
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def check_info(self):
        print(self.colour, self.price, self.max_speed, self.current_speed)
    def change_speed(self, new_speed):
        self.current_speed = new_speed

my_car = Toyota()  # создаем экземпляр
my_car.check_info()  # выводим информацию
my_car.change_speed(2)  # меняем скорость
my_car.check_info()  # снова выводим информацию
