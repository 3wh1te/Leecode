from typing import  List
import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == '':
            return True
        res = False
        target = word[0]
        def backtracking(x, y, map, word):
            if word == '':
                return True
            res = False
            old = map[x][y]
            map[x][y] = ''
            target = word[0]
            if x < len(map) - 1 and map[x + 1][y] == target:
                res = backtracking(x + 1, y, map, word[1:])
                if res:
                    return res
            if y < len(map[0]) - 1 and map[x][y + 1] == target:
                res = backtracking(x, y + 1, map, word[1:])
                if res:
                    return res
            if x > 0 and map[x - 1][y] == target:
                res = backtracking(x - 1, y, map, word[1:])
                if res:
                    return res
            if y > 0 and map[x][y - 1] == target:
                res = backtracking(x, y - 1, map, word[1:])
                if res:
                    return res
            map[x][y] = old
            return res
        for row in range(len(board)):
            for l in range(len(board[row])):
                if board[row][l] == target:
                    res = backtracking(row, l, board, word[1:])
                    if res:
                        return res
        return res


    def exist1(self, board: List[List[str]], word: str) -> bool:
        letter_dict = {}
        for row in board:
            for l in row:
                if letter_dict.get(l, -1) == -1:
                    letter_dict[l] = 1
                else:
                    letter_dict[l] += 1
        for l in word:
            if letter_dict.get(l, -1) == -1 or letter_dict.get(l, -1) == 0:
                return False
            else:
                letter_dict[l] -= 1
        return True

if __name__ == '__main__':
    board = [["A","B","C","E"],
             ["S","F","E","S"],
             ["A","D","E","E"]]
    word = "ABCESEEEFS"
    # board = [["A","B","C","E"],
    #          ["S","F","C","S"],
    #          ["A","D","E","E"]]
    # word = "ABCB"
    # word = "AAB"
    print(Solution().exist(board, word))
