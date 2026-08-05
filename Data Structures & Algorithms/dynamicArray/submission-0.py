class DynamicArray:
    capacity: int
    arr: list
    real_size: int

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.real_size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.real_size == self.capacity:
            self.resize()
        self.arr[self.real_size] = n
        self.real_size += 1

    def popback(self) -> int:
        self.real_size -= 1
        return self.arr[self.real_size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 

        for i in range(self.real_size):
            newArr[i] = self.arr[i]
        self.arr = newArr

    def getSize(self) -> int:
        return self.real_size
    
    def getCapacity(self) -> int:
        return self.capacity