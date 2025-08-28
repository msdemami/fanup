def sum_main_diagonal(matrix):
    
    total = 0
    n = len(matrix)  # اندازه ماتریس
    
    for i in range(n):
        total += matrix[i][i]  # عنصر قطر اصلی
    
    return total


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# محاسبه و نمایش نتیجه
result = sum_main_diagonal(matrix)
print("ماتریس:")
for row in matrix:
    print(row)
print(f"مجموع قطر اصلی: {result}")