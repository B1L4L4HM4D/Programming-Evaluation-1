import math

# Q1) Using a single print() statement, output a multiline ASCII art text banner of your name.

print("""
.______   .______          ___   ____    ____  _______   _______ .__   __.
|   _  \  |   _  \        /   \  \   \  /   / |       \ |   ____||  \ |  |
|  |_)  | |  |_)  |      /  ^  \  \   \/   /  |  .--.  ||  |__   |   \|  |
|   _  <  |      /      /  /_\  \  \_    _/   |  |  |  ||   __|  |  . `  |
|  |_)  | |  |\  \----./  _____  \   |  |     |  '--'  ||  |____ |  |\   |
|______/  | _| `._____/__/     \__\  |__|     |_______/ |_______||__| \__|
""")


#Q2) Write a program that asks the user to enter 3 sides lengths of a triangle and then displays the area of that triangle rounded to 2 decimal spots.

print("Enter 3 side lengths of a triangle and I will calculate the area of the triangle rounded down to 2 decimal spots.")
side1 = float(input("Enter the first side length: "))
side2 = float(input("Enter the second side length: "))
side3 = float(input("Enter the third side length: "))
s = (side1 + side2 + side3) / 2
area = s * (s - side1) * (s - side2) * (s - side3)
areaTrue = round(math.sqrt(area), 2)
print("The area of the triangle is: " + str(areaTrue))
                                         
# Q3) Your program is going to display a persons budget for the month.  Generate realistic values for the following budget items: Food, Clothing, Entertainment, and Rent.

print("I will calculate a monthly budget plan for you!")
food = float(input("Enter the amount you spend on food: $"))
clothing = float(input("Enter the amount you spend on clothing: $"))
entertainment = float(input("Enter the amount you spend on entertainment: $"))
rent = float(input("Enter the amount you spend on rent: $"))
total = food + clothing + entertainment + rent
foodPercent = round((food / total) * 100, 2)
clothingPercent = round((clothing / total) * 100, 2)
entertainmentPercent = round((entertainment / total) * 100, 2)
rentPercent = round((rent / total) * 100, 2)
print("The total amount of money spent is: $" + str(total))
print("The percentage of money spent on food is: " + str(foodPercent) + "%")
print("The percentage of money spent on clothing is: " + str(clothingPercent) + "%")
print("The percentage of money spent on entertainment is: " + str(entertainmentPercent) + "%")
print("The percentage of money spent on rent is: " + str(rentPercent) + "%")
print("I hope this helps you budget your money!")
