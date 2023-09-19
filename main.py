from templates import DashboardTemplate
import os


def clear():
    return os.system('clear')


def down_menu_event(ans):
    events = {
        'd': 'Список Договоров',
        'p': 'Список Проектов',
        'q': 'Завершение',
    }

    print(events[ans])
    return ans


def contract_menu_event(_):
    clear()

    events = {
        '1': 'Создаем Договор',
        '2': 'Подтверждаем Договор',
        '3': 'Завершаем Договор',
        'd': down_menu_event,
        'p': down_menu_event,
        'q': down_menu_event,
    }

    dash.contract_menu()
    dash.down_menu()

    ans = input()

    if ans == '0':
        return

    if ans not in events:
        print(f'Нет такого пункта меню - {ans}')
        return

    if isinstance(events[ans], str):
        print(events[ans])
        return ans

    return events[ans](ans)


def project_menu_event(_):
    clear()

    events = {
        '1': 'Создаем Проект',
        '2': 'Добавляем Договор',
        '3': 'Завершаем Договор',
        'd': down_menu_event,
        'p': down_menu_event,
        'q': down_menu_event,
    }

    dash.project_menu()
    dash.down_menu()

    ans = input()

    if ans == '0':
        return

    if ans not in events:
        print(f'Нет такого пункта меню - {ans}')
        return

    if isinstance(events[ans], str):
        print(events[ans])
        return ans

    return events[ans](ans)


def main_menu_event():
    clear()

    events = {
        '1': contract_menu_event,
        '2': project_menu_event,
        'd': down_menu_event,
        'p': down_menu_event,
        'q': down_menu_event,
    }
    dash.main_menu()
    dash.down_menu()

    ans = input()

    if ans not in events:
        print(f'Нет такого пункта меню - {ans}')
        return
    return events[ans](ans)


dash = DashboardTemplate()


ans = ''
while ans != 'q':
    ans = main_menu_event()
