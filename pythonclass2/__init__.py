#type casting
#int()
#float()
#str()
salary = 18000.25 # float
print(1,type(salary))
convert_int = int(salary) #18000
print("convert int value=",convert_int,"type =",type(convert_int))

salary = '18000.0' #str
print(2,type(salary)) #string
convert_int = int(salary) #ValueError: invalid literal for int() with base 10: '18000.0'
print(convert_int ,type(convert_int))

salary = 0.18000j #complex
print(3,type(salary)) #complex
convert_int =int(salary)
print("convert int value=",convert_int,"type =" ,type(convert_int))

