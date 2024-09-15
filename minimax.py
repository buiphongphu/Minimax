# minimax.py

def minimax(position, depth, maximizingPlayer):
    # Điều kiện dừng: độ sâu đạt 0 hoặc trò chơi kết thúc
    if depth == 0 or is_terminal(position):
        return evaluate(position)

    # Nếu là lượt của người chơi tối đa
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in get_children(position, maximizingPlayer):
            eval = minimax(child, depth - 1, False)  # Lượt của người chơi tối thiểu
            maxEval = max(maxEval, eval)  # Tìm giá trị lớn nhất
        return maxEval
    # Nếu là lượt của người chơi tối thiểu
    else:
        minEval = float('inf')
        for child in get_children(position, maximizingPlayer):
            eval = minimax(child, depth - 1, True)  # Lượt của người chơi tối đa
            minEval = min(minEval, eval)  # Tìm giá trị nhỏ nhất
        return minEval


# Hàm kiểm tra xem trò chơi đã kết thúc chưa (có người thắng hoặc hòa)
def is_terminal(position):
    return check_win(position) or check_draw(position)


# Hàm đánh giá vị trí trò chơi hiện tại
def evaluate(position):
    if check_win(position):
        return 10  # Điểm cao cho người chơi tối đa thắng
    elif check_loss(position):
        return -10  # Điểm thấp cho người chơi tối thiểu thắng
    return 0  # Điểm hòa


# Kiểm tra người chơi tối đa thắng
def check_win(position):
    # Kiểm tra các dòng
    for row in position:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True
    # Kiểm tra các cột
    for col in range(3):
        if position[0][col] == position[1][col] == position[2][col] and position[0][col] is not None:
            return True
    # Kiểm tra các đường chéo
    if position[0][0] == position[1][1] == position[2][2] and position[0][0] is not None:
        return True
    if position[0][2] == position[1][1] == position[2][0] and position[0][2] is not None:
        return True
    return False


# Kiểm tra người chơi tối thiểu thắng (đối lập với check_win)
def check_loss(position):
    # Logic kiểm tra tương tự như check_win
    return check_win(swap_position(position))


# Đổi vị trí người chơi (chuyển X thành O và ngược lại)
def swap_position(position):
    new_position = []
    for row in position:
        new_row = []
        for cell in row:
            if cell == 'X':
                new_row.append('O')
            elif cell == 'O':
                new_row.append('X')
            else:
                new_row.append(None)
        new_position.append(new_row)
    return new_position


# Kiểm tra xem trò chơi có hòa không (hết nước đi mà không có người thắng)
def check_draw(position):
    # Kiểm tra tất cả các ô trên bảng có bị lấp đầy chưa
    return all(cell is not None for row in position for cell in row)


# Hàm sinh các trạng thái con từ trạng thái hiện tại (nước đi có thể có)
def get_children(position, maximizingPlayer):
    children = []
    for i in range(3):
        for j in range(3):
            if position[i][j] is None:  # Nước đi hợp lệ (ô trống)
                new_position = [row[:] for row in position]  # Sao chép bảng
                new_position[i][j] = 'X' if maximizingPlayer else 'O'
                children.append(new_position)
    return children
