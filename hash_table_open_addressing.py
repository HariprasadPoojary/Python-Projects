class MyHash_OD:  # Open Addressing Hash Table class using double hashing method
    def __init__(self, bucket) -> None:
        self.bucket = bucket
        self.offset_bucket = bucket - 1
        self.hash_table = [-1] * bucket  # [-1 for _ in range(bucket)]

    def hash(self, item, probe_time=0):
        index = probe_time if probe_time > 0 else 0
        probe = item % self.bucket
        offset = index * (self.offset_bucket - (item % self.offset_bucket))
        final_hash = (probe + offset) % self.bucket
        return final_hash

    def search(self, item):
        probe_cnt = 0
        hash_val = self.hash(item, probe_cnt)
        hash_table_size = len(self.hash_table)
        while self.hash_table[hash_val] != -1 and hash_table_size < 1:
            if item == self.hash_table[hash_val]:
                return True
            probe_cnt += 1
            hash_val = self.hash(item, probe_cnt)
            hash_table_size -= 1
        # Either found empty space i.e -1 or given item doesn't exists
        return False

    def insert_all(self, data_list):
        probe_cnt = 0
        for data in data_list:
            hash_val = self.hash(data, probe_cnt)
            while self.hash_table[hash_val] != -1:
                probe_cnt += 1
                hash_val = self.hash(data, probe_cnt)

            self.hash_table[hash_val] = data

    def __repr__(self) -> str:
        return "".join(str(self.hash_table))


h = MyHash_OD(10)

print(h)
h.insert_all([49, 63, 56, 52, 54, 48, 15, 53, 77])
print(h)
print(h.search(488))