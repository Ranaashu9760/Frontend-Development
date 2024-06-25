# while my_variable<10: // nameerror my_var value not initialised
#     print("Hello")
#     my_variable +=1


my_variable = 5
while my_variable<10:
    print("Hello")
    my_variable +=1


x=1
sum=0
while x<10:
    sum += x
    x += 1
    print(sum)

y = 0
product = 1
while y < 10:
    product = product *y
    y+=1
    print(product)
print()
print(sum, product)
print()
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)
