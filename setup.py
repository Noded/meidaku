import os

user_system_name = os.name

if user_system_name == 'nt':
    print("Начинается скачивание зависимостей")
    os.system("python -m venv venv")
    os.system("venv\Scripts\activate")
    os.system("python -m pip install -r requirements.txt")
else:
    print("Начинается скачивание зависимостей")
    os.system("python -m venv venv")
    os.system("source venv/bin/activate")
    os.system("python -m pip install -r requirements.txt")