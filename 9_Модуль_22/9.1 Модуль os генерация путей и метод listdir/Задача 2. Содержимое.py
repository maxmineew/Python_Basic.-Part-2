import os

for path in os.listdir('C:/7_Hyundai Creta'):
    print(os.path.join(os.path.abspath('C:/7_Hyundai Creta'), path))