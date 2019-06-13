class HashMap:
    def __init__(self):
        self.items = list([0 for i in range(8)])

    def __hash_function(self, string):
        return hash(string) % 8

    def __add(self, key, value):
        self.items[key] = value

    def save(self, value):
        key = self.__hash_function(value)
        self.__add(key, value)
        return key

    def get(self, key):
        return self.items[self.__hash_function(key)]


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.save('aaa', 'bbb')
    print(hashmap.get('aaa'))
