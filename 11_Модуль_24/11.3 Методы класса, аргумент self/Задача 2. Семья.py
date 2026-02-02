class Family:
    surname = 'Ivanov'
    money = 1e6
    have_a_house = False

    def info(self):
        print(self.surname, self.money, self.have_a_house)

    def earn_money(self, change_money):
        self.money += change_money
        print(self.surname, self.money, self.have_a_house)

    def buy_home(self, home_price, sale = 0):
        home_price -= home_price * sale/100 # Применяем скидку (если есть)
        if self.money >= home_price: # Если денег хватает
            self.money -= home_price # Платим за дом
            self.have_a_house = True # Теперь есть дом!
            print('Дом куплен!', self.money)
        else:
            print('Нет денег(')

my_family = Family() # Создаём семью Ивановых с 1 млн денег
my_family.info() # Вывод: Ivanov 1000000.0 False

print('Попробуйте заработать денег...')
my_family.buy_home(1e6) # Цена дома = 1 млн, денег у нас тоже 1 млн
# Результат: Дом куплен! Деньги: 0. Теперь have_a_house = True
# Проверяем, есть ли дом, и если да — зарабатываем деньги
if my_family.have_a_house:
    my_family.earn_money(8e5)
    my_family.buy_home(1e6, 10) # Пытаемся купить дом за 1 млн со скидкой 10%
# Расчёт:
#
# Цена дома с 10% скидкой: 1,000,000 - 10% = 900,000
#
# Денег у нас: 800,000
#
# Результат: "Нет денег("
my_family.info()