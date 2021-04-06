# hashMap is used behind the scenes while using dictionary in python
#lets see how it implements hashmap

class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    #Hash function to get location from Ram
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # def add(self, key, value):
    #     h = self.get_hash(key)
    #     self.arr[h] = value

    #python builtin function replaces add to allow dictionary sysntaxx
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    # def get(self, key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    #python builtin function replaces add to allow dictionary sysntaxx
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    #Similarly
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    hm = HashMap()
    print(hm.arr)
    hm['june 6'] =  130
    hm['june 28'] = 1110
    hm['june 8'] = 10
    hm['june 18'] = 101
    hm['dec 1'] = 198
    hm['aug 23'] = 444
    print(hm.arr)
    del hm['aug 23']
    print(hm.arr)


    
