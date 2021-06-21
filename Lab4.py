import random as rand


def fibonacciFinder (max):
    i = 0
    j = 1
    k = 0
    while i < max:
        print(k)
        k = i + j
        i = j
        j = k
    return("fibonacci YAY!")


def primeFinder (max):
    for i in range(2,max):
        for j in range(2,i):
            if i % j == 0:
                break
            else:
                print(i)
        return(max)





def triangleArea(base, height):
    area = base*height/2
    return area




n = 5
m = 5 
areaList = []
for b in range(0,n):
    for h in range(0,m):
        areaList.append(triangleArea(b,h))
print(areaList)


menu = {"Burgers":12.99, "Fries":3.99, "Shakes":1.50}
def foodSum(item1, item2):
    sum = item1 + item2
    print("The total sum of your order of " + item1 + " and " + item2 + " its $" + str(sum))
foodSum("Burgers", "Shakes")






listPlayers = [1,2,3,4,5,6,7]
length = len(listPlayers)
for i in range(length):
    length = len(listPlayers)
    randomNumber = rand.randint(1,length-1)
    listPlayers.pop(randomNumber)
    print(listPlayers)
