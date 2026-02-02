class Toyota:# это класс (шаблон, чертёж всех машин этой марки)
    colour = 'красный'
    price = 1e6
    max_speed = 200
    current_speed = 0 #Атрибуты (свойства/данные), характеристики объекта

    def object_class(self): #self — ссылка на текущий объект (конкретную машину car)
        print(self.colour, self.price, self.max_speed, self.current_speed)

    def change_speed(self, new_speed):
        self.current_speed = new_speed # Устанавливает новое значение


car = Toyota() #Работа с экземляром класса. Создаём конкретную машину по чертежу Toyota
car.object_class() # Показывает начальное состояние
car.change_speed(100) # Меняем скорость на 100 км/ч
car.object_class()# Показывает изменённое состояние
print(car.current_speed) # Прямой доступ к атрибуту
