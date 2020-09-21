from typing import List

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.one = {}
        self.many = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for num in self.one:
            return num
        return -1

    def add(self, value: int) -> None:
        if self.one.get(value, -1) == -1 and self.many.get(value, -1) == -1:
            self.one[value] = 1
        elif self.one.get(value, -1) != -1:
            self.one.pop(value)
            self.many[value] = 1


