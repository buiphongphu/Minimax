# main.py

from minimax import minimax

# Ví dụ về trạng thái trò chơi Tic-Tac-Toe (trạng thái khởi đầu)
initial_position = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]

depth = 3  # Số độ sâu của cây tìm kiếm

# Gọi hàm minimax với trạng thái khởi đầu và người chơi tối đa
result = minimax(initial_position, depth, True)
# Kết quả của thuật toán Minimax: 0
# Điểm của trạng thái khởi đầu là 0, tức là hòa
# Trong trò chơi Tic-Tac-Toe, trạng thái khởi đầu là trạng thái hòa
# Điều này là do cả hai người chơi đều chơi tốt nhất của mình
# và không thể thắng lẫn nhau nếu không mắc lỗi
# (và trò chơi không có người chơi thứ ba để tận dụng lỗi đó)


# In kết quả của thuật toán Minimax
print(f"Kết quả của thuật toán Minimax: {result}")
