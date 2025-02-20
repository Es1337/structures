
class SimpleMap:
    def __init__(self):
        self.map = [None] * 10

    def add(self, key: int, val: int):
        self.map[key] = val            

    def remove(self, key: int) -> int:
        if self.contains(key):
            self.map[key] = None

    def get(self, key: int) -> int:
        if self.contains(key):
            return self.map[key]

    def contains(self, targetKey: int) -> bool:
        for key, val in enumerate(self.map):
            if key == targetKey and val != None:
                return True
            
        return False
    
    def print(self):
        res = ""
        for key, val in enumerate(self.map):
            if val is not None:
                res += "{k=" + str(key) + ", v=" + str(val) + "},"

        print(res)



if __name__ == "__main__":
    simpleMap = SimpleMap()

    simpleMap.add(0, 7)
    simpleMap.add(1, 3)
    simpleMap.add(5, 1)
    simpleMap.print()

    print(f"contains 5? {simpleMap.contains(5)}")
    print(f"contains 4? {simpleMap.contains(4)}")

    simpleMap.remove(1)
    simpleMap.print()
    simpleMap.remove(2)
    simpleMap.print()

    print(simpleMap.get(5))
