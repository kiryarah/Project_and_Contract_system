class DashboardTemplate:

    def down_menu(self):
        print('-----------------------------')
        print('d: Получить список Договоров')
        print('p: Получить список Проектов')
        print('q: Завершить работу')

    def main_menu(self):
        print('Выберите пункт меню:')
        print('1: Работать с Договорами')
        print('2: Работать с Проектами')

    def contract_menu(self):
        print('Выберите пункт меню:')
        print('Договоры:')
        print('1: Создать')
        print('2: Подтвердить Договор')
        print('3: Завершить Договор')
        print('0: Назад')

    def project_menu(self):
        print('Выберите пункт меню:')
        print('Проекты:')
        print('1: Создать')
        print('2: Добавить Договор')
        print('3: Завершить Договор')
        print('0: Назад')
