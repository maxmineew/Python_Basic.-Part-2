import pandas as pd

class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 0


class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = True


monitors = [Monitor() for i in range(4)]
headphones = [Headphones() for y in range(3)]

for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].monitor_freq = number

headphones[0].headphones_micro = False

print("Информация о мониторах:")
for i, monitor in enumerate(monitors):
    print(f"Монитор {i+1}: {monitor.monitor_name}, матрица: {monitor.monitor_matrix}, "
          f"разрешение: {monitor.monitor_res}, частота: {monitor.monitor_freq} Гц")

print("\nИнформация о наушниках:")
for i, headphone in enumerate(headphones):
    print(f"Наушники {i+1}: {headphone.headphones_name}, чувствительность: {headphone.headphones_sensitivity} дБ, "
          f"микрофон: {'есть' if headphone.headphones_micro else 'нет'}")

    # Создаем DataFrame из ваших данных
    data = {
        'Тип': ['Монитор', 'Монитор', 'Монитор', 'Монитор', 'Наушники', 'Наушники', 'Наушники'],
        'Название': ['Samsung', 'Samsung', 'Samsung', 'Samsung', 'Sony', 'Sony', 'Sony'],
        'Матрица': ['VA', 'VA', 'VA', 'VA', '-', '-', '-'],
        'Разрешение': ['WQHD', 'WQHD', 'WQHD', 'WQHD', '-', '-', '-'],
        'Частота/Чувствительность': [60, 144, 70, 60, 108, 108, 108],
        'Микрофон': ['-', '-', '-', '-', 'Да', 'Да', 'Нет']
    }

    df = pd.DataFrame(data)

    # Сохраняем в Excel
    df.to_excel('техника.xlsx', index=False, sheet_name='Оборудование')

    # Можно сохранить с несколькими листами
    with pd.ExcelWriter('полный_отчет.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Все устройства', index=False)

        # Отдельные листы для каждого типа
        мониторы = df[df['Тип'] == 'Монитор']
        наушники = df[df['Тип'] == 'Наушники']

        мониторы.to_excel(writer, sheet_name='Мониторы', index=False)
        наушники.to_excel(writer, sheet_name='Наушники', index=False)

    print("Данные успешно экспортированы в Excel!")



