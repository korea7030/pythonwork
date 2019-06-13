# 충돌 대처 - chaining
class LinearMap:
    def __init__(self):
        self.items = list()

    def add(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        data = list()
        for key, val in self.items:
            if key == k:
                data.append(val)
        return data


# 무한 chaining 방지
class BetterMap:
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)


# LinearMap의 최대 크기를 유지하도록 변경
class HashMap:
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    # 충돌대처 - resize
    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)

        self.maps = new_maps


if __name__ == '__main__':
    hash_map = HashMap()
    hash_map.add(1, 2)
    hash_map.add(1, 3)
    print(hash_map.get(1))
