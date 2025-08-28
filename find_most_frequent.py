def find_most_frequent(numbers):
    
    if not numbers:
        return None  # اگر لیست خالی باشد
    
    # ساخت یک دیکشنری برای شمارش تکرار اعداد
    count_dict = {}
    
    # شمارش تکرار هر عدد
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # پیدا کردن عدد با بیشترین تکرار
    max_count = 0
    most_frequent_num = None
    
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_num = num
    
    return most_frequent_num

# تست تابع با مثال داده شده
input_list = [1, 2, 2, 3, 3, 3, 4]
result = find_most_frequent(input_list)

print("ورودی:", input_list)
print("خروجی:", result)

# تست‌های اضافی
print("\nتست‌های دیگر:")
test_cases = [
    [1, 1, 2, 2, 2],
    [5],
    [1, 2, 3, 4, 5],
    [1, 1, 1, 2, 2, 2],  # اگر مساوی باشد اولین عدد با بیشترین تکرار را برمی‌گرداند
    []
]

for test in test_cases:
    result = find_most_frequent(test)
    print(f"{test} -> {result}")