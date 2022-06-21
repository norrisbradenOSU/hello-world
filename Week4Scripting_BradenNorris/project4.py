height = int(input("What is the height of the drop?: "))
bounceIndex = float(input("What is the bounciness index?: "))

numberOfBounces = int(input("How many times can it bounce?: "))
distance = 0
bounceCount = 0

while numberOfBounces > 0:
    distance = distance + height
    height = height * bounceIndex
    distance = distance + height
    numberOfBounces = numberOfBounces - 1
    bounceCount = bounceCount + 1
    print("As of drop " + str(bounceCount) + " the ball has traveled a total distance of " + str(distance) + " feet")

