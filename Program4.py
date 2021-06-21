from typing import List


def triangleArea(base,height):
    area = base*height/2
    print(area)
    return area


n = 5 
m = 5
areaList = []
i = 0
for b in range(0,5):
    for h in range(0,m):
        areaList.append(triangleArea(b,n))
        i += 1
print(areaList)

ListA = []
print(ListA)

ListA.append(5)
print(ListA)


Menu = {"Burgers": 12.99, "Fries":3.99, "Shakes":1.50}

def foodSum(item1,item2):
    sum = item1 + item2
    print("The total price of your order of " + str(item1) + " and " + str(item2) + " is " + str(sum))

foodSum(Menu["Burgers"], Menu["Fries"])
