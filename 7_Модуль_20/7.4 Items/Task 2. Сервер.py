'''У вас есть данные о сервере, которые хранятся в виде вот такого словаря:'''

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}
# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно, как они представлены в словаре.
# Результат работы программы:
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty

for tag, info in server_data.items():
    print(tag + ':')
    for key, value in info.items():
        print('\t'+ key + ':', value)
