# def len_string(s): #1 задание А
#     return len(s)
# input_string="Привет,меня зовут Игорь!"
# print("Длина строки:",len_string(input_string))

# def len_string(int1,int2): #1 Задание B
#     return len (int1+int2)
# int1="Привет,меня зовут Игорь!"
# int2="И я студент!"
# print("длина двух строк:",len_string(int1,int2))

# def kvadrat_number(num): #2 задание А
#     return num **2
# number = 6
# print("Число:",number ,"квадрат числа",kvadrat_number(number))

# def sum_number(num1,num2): #2 Задание B
#     return num1+num2
# num1=float(input("Ведите 1 число:"))
# num2=float(input("Ведите 2 число:"))
# print("Сума двух чисел:",sum_number(num1,num2))

# def sun_numbers(num1,num2): #2 задание С
#     quotient = num1 // num2
#     remainder = num1 % num2
#     return quotient,remainder
#
# num1=int(input("Ведите 1 число:"))
# num2=int(input("Ведите 2 число:"))
#
# result_quotient,result_remainder=sun_numbers(num1,num2)
# print("Целое:",result_quotient)
# print("Остаток:",result_remainder)


# def environment_value(lst): #3 задание А
#     sum_elem=sum(lst)
#     average=sum_elem/len(lst)
#     return average
# numbers=[1,2,3,4,5]
# average=environment_value(numbers)
# print("Среднее значение списка:",average)


def sum_list(lst1,lst2): #3 Задание В
    return list(set(lst1)& set(lst2))
list1=[1,3,5,7,8]
list2=[2,3,4,5,1]
element=sum_list(list1,list2)
print("Одинаковые цифры:",element)