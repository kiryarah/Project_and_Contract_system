from DB_tables import ContractDBTable, ProjectDBTable, BaseDBTable
from datetime import datetime


class BaseModel:
    objects: BaseDBTable
    __id: int = None
    __name: str = None
    __create_date: str = None
    _row: tuple = None

    def create_model(self, name: str):
        self.__name = name
        self.__save_model()
        self._row = self.__get()
        self.__id = self._row[0]
        self.__create_date = self._row[2]
        return self

    def get_model(self, row: tuple):
        self._row = row
        self.__id, self.__name, self.__create_date = row[:3]

    def __get(self):
        return self.objects.search_by_name(self.name)

    def __save_model(self) -> None:
        self.objects.insert(self.name)

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def create_date(self):
        return self.__create_date

    def __repr__(self) -> str:
        return self.name


class Contract(BaseModel):
    objects = ContractDBTable()

    status = 'DRAFT'
    project_id = None
    project = None
    signature_date = None

    def get_model(self, row: tuple):
        super().get_model(row)
        self.signature_date, self.status, self.project_id = row[3:]
        return self

    def save(self):
        self.objects.update_by_id(table_id=self.id, date=self.signature_date,
                                  status=self.status, project_id=self.project_id)

    def confirm_contract(self):
        if self.status != 'DRAFT':
            print('Только Черновик можно подтвердить!')
            return
        self.status = 'ACTIVE'
        self.signature_date = datetime.now()

    def finish_contract(self):
        if not self.project_id:
            print('Для завершения договора нужно его добавить к проекту.')
            return
        self.project.finish_contract(self)


class Project(BaseModel):
    objects = ProjectDBTable()
    __has_active = False
    __contracts = {}

    def get_model(self, row: tuple):
        super().get_model(row)
        self.__contracts = self.__get_contracts()
        return self

    def add_contract(self, contract: Contract, init=False):
        if init:
            self.__contracts[contract.id] = contract
            self.__has_active = True if contract.status == 'ACTIVE' else self.__has_active
            return

        if self.__has_active:
            print('В данном проекте уже есть Активный договор!')
            print('Завершите работу с ним и сможете добавить новый!')
            return

        if contract.status != 'DRAFT':
            print('Добавлять можно только Активные договоры!')
            return

        if contract.project_id:
            print('Этот договор уже используется в другом проекте!')
            return

        if contract.id not in self.__contracts:
            self.__has_active = True
            self.__contracts[contract.id] = contract
            contract.project_id = self.id
            contract.project = self

    def finish_contract(self, contract: Contract):
        if contract.status != 'ACTIVE':
            print('Завершить можно только Активный договор!')
            return
        contract.status = 'FINISHED'
        self.__has_active = False

    @property
    def contracts(self):
        return self.__contracts
