teams = [ 'Dragon', 'Wolves', 'Pandas', 'Unicorn']
for first_team in teams:
    for second_team in teams:
        if first_team != second_team:
            print(first_team + " Vs " + second_team)
                                                                     
# print()
# for element in long_list:
#     do_something(element)     # executes in 1ms x 10000 = 10 seconds

# print()
# for element1 in long_lsit:
#     for element2 in long_list:
#         do_something(element1, element2)   # execute in 10s X 10000 = 27 hours! so less use of nested lprint(x)

for x in range (25):
    print(x)

print()
for x in [25]:
    print(x)

print()
def greet_friends(friends):
    for friend in friends:
        print("Hi "+ friend)
greet_friends(['Ashu', 'Shashi', 'Keshav', 'Priyanka'])
greet_friends("Barry")

print()
for number in range(1, 6+1, 2):
    print(number*3)

print()
for number in range(2 ,8):
    print(number**2)

print()
for x in range(2):
    print("This is the outer loop iteration number" +str(x))
    for y in range(3+1):
        print("Inner loop iteration nunber" +str(y))
    print("Exit inner loop")

print()
for x in range(7):
    if x % 2 == 0:
        print(x)


for n in range(6, 18, 3):
    print(n*2)

print()
for n in range (6, 18, 3):
    print(n+2)

print()
for n in range (6, 18+1, 3):
    print(n*2)


