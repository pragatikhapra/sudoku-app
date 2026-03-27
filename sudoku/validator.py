def is_valid_board(board):

    def valid_group(nums):
        nums = [n for n in nums if n != 0]
        return len(nums) == len(set(nums))

    # check rows
    for row in board:
        if not valid_group(row):
            return False

    # check columns
    for col in zip(*board):
        if not valid_group(col):
            return False

    # check 3x3 boxes
    for box_x in range(3):
        for box_y in range(3):
            box = []
            for i in range(box_y*3, box_y*3+3):
                for j in range(box_x*3, box_x*3+3):
                    box.append(board[i][j])
            if not valid_group(box):
                return False

    return True