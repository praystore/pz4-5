class TestDataManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.datasets = {}
        return cls._instance
    def add_dataset(self, data_type: str, items: list) -> None:
        if data_type not in self.datasets:
            self.datasets[data_type] = []
        self.datasets[data_type].extend(items)
    def get_dataset(self, data_type: str) -> list:
        return self.datasets.get(data_type, [])
    def get_all_datasets(self) -> dict:
        return self.datasets
    def clear(self) -> None:
        self.datasets.clear()