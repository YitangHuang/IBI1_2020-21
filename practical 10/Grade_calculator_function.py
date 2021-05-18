def calculator(name, code, poster, exam):
    name = input("Student Name:")
    code = float(input("Please input the code grade:"))
    poster = float(input("Please input the poster grade:"))
    exam = float(input("Please input the final exam grade:"))
    total = 0.4 * code + 0.3 * poster + 0.3 * exam
    result = str(name)+"'s final grade is "+str(total)
    return result
print(calculator(1,2,3,4))

#  example:
# enter Mike
# enter 80
# enter 90
# enter 60


#results:
# C:\Users\Razer\AppData\Local\Programs\Python\Python38\python.exe "C:/Users/Razer/PycharmProjects/practical 10/Grade_calculator_function.py"
# Student Name:Mike
# Please input the code grade:80
# Please input the poster grade:90
# Please input the final exam grade:60
# Mike's final grade is 77.0
#
# Process finished with exit code 0