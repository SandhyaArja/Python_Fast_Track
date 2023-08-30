class Mobile:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage


obj = Mobile("iPhone 12 Pro", "128GB")
print(obj.model)
