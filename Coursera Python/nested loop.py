for left in range(8):
     for right in range( 8):
         print("[" + str(left) + "|" + str(right) + "]", end=" ")    
     print()

print()
print()
for left in range(8):
     for right in range(left,8):
         print("[" + str(left) + "|" + str(right) + "]", end=" ")    
     print()

print()
print()

for left in range(8):
    for right in range(left, 8):
        print("[" + str(left) + "]" , end=" ")
    print()

print()
print()

for left in range(4):  # matrix
    for right in range( 4):
        print("[" + str(left) + "]" , end=" ")
    print()

# for left in range(8):
#     print("[" + str(left) +"]", end" "):