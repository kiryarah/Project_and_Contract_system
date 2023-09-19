from models import Project, Contract


class DashboardView:
    __contracts = []
    __projects = []

    def __init__(self) -> None:
        self.__contracts = [Contract().get_model(row) for row in Contract.objects.view()]
        self.__projects = [Project().get_model(row) for row in Project.objects.view()]

        for prj in self.__projects:
            for contract in self.__contracts:
                if contract.project_id == prj.id:
                    contract.project = prj
                    prj.add_contract(contract, init=True)

    def create_contract(self, name: str):
        contract = Contract().create_model(name)
        self.__contracts.append(contract)

    def create_project(self, name: str):
        for item in self.__contracts:
            if item.status == 'ACTIVE':
                active_contract = True

        if not active_contract:
            print('Для работы в проекте нужен хотя бы один Активный договор!')
            return

        project = Project.create_model(name)
        self.__projects.append(project)
        return project

    def view_contracts(self):
        if self.__contracts:
            return self.__contracts
        return ['Договоров пока нет в работе. Добавьте договор']

    def view_projects(self):
        if self.__projects:
            return self.__projects
        return ['Проектов пока нет в работе. Добавьте проект']

    def get_contract(self, index):
        try:
            return self.__contracts[index - 1]
        except IndexError:
            print('Договор с таким номером не существует')

    def get_project(self, index):
        try:
            return self.__projects[index - 1]
        except IndexError:
            print('Проект с таким номером не существует')
