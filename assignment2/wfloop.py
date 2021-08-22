# while break statement

i = 1
print("while Break:")
while i < 6:
  print(i)
  if (i == 3):
    
    break

  i += 1
# while continue
i = 0
print("while Continue:")
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#for break
for x in range(7):   
  if x == 5:
    break
  print(x)
# for continue
for x in range(7):
    if x == 5:
        continue
    print(x)
