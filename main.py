import os
from utils.helpers import register_url, get_home_page, get_standard_url, get_all_urls

def main():
    while True:
        print("\n1. Регистрация короткого интернет-адреса по стандартному URL")
        print("2. Получение и проверка домашней страницы интернет-адреса по псевдониму")
        print("3. Получение и проверка стандартного интернет-адреса по короткому URL")
        print("4. Вывод информации о всех сокращённых URL")
        print("5. Выход")
        choice = input("Выберите действие: ").strip()
        
        if choice == '1':
            register_url()
        elif choice == '2':
            get_home_page()
        elif choice == '3':
            get_standard_url()
        elif choice == '4':
            get_all_urls()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    if not os.path.exists('storage'):
        os.makedirs('storage')
    main()
