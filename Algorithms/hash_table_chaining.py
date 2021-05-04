class MyHash:
    def __init__(self, bucket) -> None:
        self.bucket = bucket
        self.hash_table = [[] for _ in range(bucket)]

    # def __repr__(self) -> str:
    #     return "-".join(self.hash_table[0])

    def hash(self, value) -> int:
        return value % self.bucket

    def search(self, item) -> bool:
        hash_val = self.hash(item)
        return item in self.hash_table[hash_val]

    def insert(self, item) -> None:
        hash_val = self.hash(item)
        self.hash_table[hash_val].append(item)

    def remove(self, item) -> bool:
        hash_val = self.hash(item)
        try:
            self.hash_table[hash_val].remove(item)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    h = MyHash(7)
    h.insert(12)
    h.insert(62)
    h.insert(82)
    # print(h)
    print(h.search(12))
    h.remove(12)
    print(h.search(12))
