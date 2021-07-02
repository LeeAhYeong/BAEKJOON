su_list = []
small_su = []
while True:
    N , X = map(int,input("").split()) # ["10", "5"]
    if 1 <= N <= 10000 and 1 <= X <= 10000:
        break

su = input()

su_list = su.split(" ")

for item in su_list:
    if int(item) < X:
       small_su.append(item)
    
for su in small_su:
    print(su, end = ' ')
