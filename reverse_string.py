def reverse_string(s):

    reversed_str = ""
    length = len(s)
   
    for i in range(length - 1, -1, -1):
        reversed_str += s[i]
    
    return reversed_str

 
input_str = "hello"
str2 = input("string : ")
result = reverse_string(input_str)
result2 = reverse_string(str2)


print("ورودی:", input_str)
print("خروجی:", result)
print("your string",str2)
print("result your : ", result2)



print("'abc' ->", reverse_string("abc"))
print("'123' ->", reverse_string("123"))
