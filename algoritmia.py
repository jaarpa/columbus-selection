class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        used_nums = {str(number): [[],[],[]] for number in range(1,10)}
        size = len(board)
        for i in range(size):
            for j in range(size):
                value = board[i][j]
                if value != ".":
                    # Check or add box, i, and j, to hash table
                    subox = (i // 3)*size + (j // 3)
                    number_status = used_nums[value]
                    if subox in number_status[0] or i in number_status[1] or j in number_status[2]:
                        return False
                    number_status[0].append(subox)
                    number_status[1].append(i)
                    number_status[2].append(j)
        # If no errrors
        return True
