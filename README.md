## Система Проектов и Договоров
### Задача
Используя Python 3+, любую БД, использовать ООП подход, реализовать консольное приложение «Система Проектов и Договоров»

### Общие требования:
#### 1. Реализовать сущности Договор и Проект.

В договоре должны быть представлены следующие поля:
   - Название договора.
   - Дата создания(присваивается в момент создания сущности).
   - Дата подписания договора.
   - Статус договора(черновик, активен, завершен).
   - Проект(в котором используется данный договор).
   </br>

В проекте должны быть представлены следующие поля:
 - Название проекта.
 - Дата создания(присваивается в момент создания сущности).
 - Ссылки на договора(O2M).

#### 2. Реализовать бэк логику
По умолчанию договор создается в статусе черновик, пользователь имеет возможность сменить ему статус посредству действий: «Подтвердить договор»(активен), «Завершить договор»(завершен). </br>
В момент подтверждения договора проставляется дата подписания договора. Поле проект из сущности Договор не проставляется.</br>

Из сущности проект должна быть возможность добавлять договора со следующей логикой:
- Нельзя добавить один и тот же договор
- Добавлять в проект можно только активные договоры
- В проекте не может быть более одного активного договора
- Из проекта можно завершить действие любого договора, принадлежащему этому проекту
- Один договор не может использоваться более чем в одном проекте
- В момент добавления договора к проекту, со стороны договора проставляется выбранный для него проект

#### 3. Требования к консольному интерфейсу
- Программа предлагает на выбор создавать договоры или проекты, пока пользователь не захочет завершить работу с программой.
- Нельзя начать заполнять проект без существования хотя бы одного активного договора
- На любом этапе взаимодействия с программой должна быть возможность просмотреть список проектов и договоров
- Действия «Подтвердить договор», «Завершить договор» должны быть доступны из меню заполнения договора, «Завершить договор» так же доступен из проекта, согласно п.2.
