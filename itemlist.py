class ItemList:
    def __init__(self, list=[]):
        self.list = list

    def __getitem__(self, item):
        return self.list[item]

    def __len__(self):
        return len(self.list)

    def store(self, item):
        self.list.append(item)

    def clear(self):
        self.list = []