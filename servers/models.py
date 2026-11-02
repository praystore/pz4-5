class TestData:
    def __init__(self, count: int):
        self.count = count

    def generate(self) -> list:
        raise NotImplementedError()

    def get_info(self) -> str:
        raise NotImplementedError()

class UsersDataGenerator(TestData):
    def generate(self) -> list:
        return [f"user_{i}@test.local" for i in range(1, self.count + 1)]

    def get_info(self) -> str:
        return f"UsersGenerator: {self.count} пользователей"

class OrdersDataGenerator(TestData):
    def generate(self) -> list:
        return [{"order_id": i, "amount": i * 100} for i in range(1, self.count + 1)]

    def get_info(self) -> str:
        return f"OrdersGenerator: {self.count} заказов"

class ProductsDataGenerator(TestData):
    def generate(self) -> list:
        return [f"Product_{i}" for i in range(1, self.count + 1)]

    def get_info(self) -> str:
        return f"ProductsGenerator: {self.count} товаров"

class DataGeneratorFactory:

    _registry = {
        "users": UsersDataGenerator,
        "orders": OrdersDataGenerator,
        "products": ProductsDataGenerator,
    }

    @classmethod
    def create(cls, data_type: str, count: int) -> TestData:
        if data_type not in cls._registry:
            raise ValueError(
                f"Неизвестный тип данных: '{data_type}'. "
                f"Доступные: {list(cls._registry.keys())}"
            )
        return cls._registry[data_type](count)

    @classmethod
    def available_types(cls) -> list:
        return list(cls._registry.keys())