import csv

# ایجاد فایل CSV فرضی
data = [
    ["تاریخ", "مبلغ", "محصول"],
    ["1403-01-15", 100000, "لپ تاپ"],
    ["1403-01-16", 50000, "موبایل"],
    ["1403-01-17", 75000, "تبلت"],
    ["1403-01-18", 120000, "لپ تاپ"],
    ["1403-01-19", 30000, "هدفون"]
]

# ذخیره داده‌ها در فایل CSV
with open('فروش.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("فایل CSV ایجاد شد.")

# خواندن و تحلیل داده‌ها
with open('فروش.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # رد کردن سطر عنوان
    
    sales = []
    amounts = []
    
    for row in reader:
        if row:  # اطمینان از اینکه سطر خالی نیست
            date = row[0]
            amount = int(row[1])
            product = row[2]
            
            sales.append({"تاریخ": date, "مبلغ": amount, "محصول": product})
            amounts.append(amount)

# محاسبات
total_sales = sum(amounts)
average_sale = total_sales / len(amounts)
max_sale = max(amounts)

# پیدا کردن روز با بیشترین فروش
max_sale_day = ""
for sale in sales:
    if sale["مبلغ"] == max_sale:
        max_sale_day = sale["تاریخ"]
        break

# نمایش نتایج
print("\nنتایج تحلیل فروش:")
print(f"مجموع کل فروش: {total_sales:,} تومان")
print(f"میانگین مبلغ فروش: {average_sale:,.0f} تومان")
print(f"بیشترین فروش در یک روز: {max_sale:,} تومان")
print(f"تاریخ بیشترین فروش: {max_sale_day}")