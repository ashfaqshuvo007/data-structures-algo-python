# hashMap is used behind the scenes while using dictionary in python
#lets see how it implements hashmap
# Sometimes with bad hash function hash for two elements might return same index. Hence, chaining is used .
# Code snippet below shows implementation of chaining in python

class HashMap:
    def __init__(self):
        self.MAX = 100
        #to implementing chaining
        self.arr = [[]for i in range(self.MAX)]

    #Hash function to get location from Ram
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX


    #python builtin function replaces add to allow dictionary sysntax
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    #python builtin function replaces add to allow dictionary sysntaxx
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]


    #Similarly
    def __delitem__(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
                break



if __name__ == '__main__':
    hm = HashMap()
    print(hm.arr)
    hm['march 6'] =  130
    hm['june 28'] = 1110
    hm['june 8'] = 10
    hm['march 6'] = 101
    print("After Insertion: ")
    print("==================")

    print(hm.arr)
    print("==================")

    print(hm['march 6'])
    print("==================")

    del hm["june 8"]
    print(hm.arr)


    
