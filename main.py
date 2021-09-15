# калькулятор

what = input(" Що робимо(+,-):")

a = float(input( "Введіть перше число:"))
b = float(input( "Введіть друге число:"))

if what== "+":
    c=a+b
    print("Результат: "+ str(c) )
elif what=="-":
    c= a-b
    print("Результат: " + str (c) )
else:
    print("Вибрана на правильна операція!!!!!")

