from typing import List
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # task种类不充足 slot就会出现 n-可用种类
        task_dict = collections.Counter(tasks)
        task_list = []
        for task in task_dict:
            task_list.append(task_dict[task])
        task_list = sorted(task_list,reverse=True)
        res = len(tasks)
        last_slot = 0
        while task_list.__len__() != 0:
            last_slot = 0
            if task_list.__len__() < n + 1:
                last_slot = n - task_list.__len__() + 1
                res += (n - task_list.__len__() + 1)
                for i in range(len(task_list) - 1, -1 , -1):
                    task_list[i] -= 1
                    if task_list[i] == 0:
                        task_list.pop(i)
            else:
                for i in range(n , -1, -1):
                    task_list[i] -= 1
                    if task_list[i] == 0:
                        task_list.pop(i)
            task_list = sorted(task_list, reverse=True)
        return res - last_slot
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        task_dict = collections.Counter(tasks)
        for task in task_dict:
            task_dict[task] = [task_dict.get(task),0]
        res = 0
        while task_dict.__len__() != 0:
            find = False
            res += 1
            max_task = ''
            for task in task_dict:
                if task_dict[task][1] == 0:
                    find = True
                    if max_task == '':
                        max_task = task
                    elif task_dict[task][0] > task_dict[max_task][0]:
                        max_task = task
                elif task_dict[task][1] > 0:
                    task_dict[task][1] -= 1
            if find:
                if task_dict[max_task][0] == 1:
                    task_dict.pop(max_task)
                else:
                    task_dict[max_task][0] -= 1
                    task_dict[max_task][1] = n
        return res
if __name__ == '__main__':
    print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
    print(Solution().leastInterval(["A", "A", "B", "B", "C", "C",
                                    "D", "D", "E", "E", "F", "F", "G",
                                    "G", "H", "H", "I", "I", "J", "J",
                                    "K", "K", "L", "L", "M", "M", "N",
                                    "N", "O", "O", "P", "P", "Q", "Q",
                                    "R", "R", "S", "S", "T", "T", "U",
                                    "U", "V", "V", "W", "W", "X", "X",
                                    "Y", "Y", "Z", "Z"],2))
    print(Solution().leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4))