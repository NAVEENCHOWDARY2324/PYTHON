menu = """
----- Choose from the following -----
1. Area of Circle.
2.Area of Rectangle.
3.Area of Triangle.
Enter your choice : 
"""
print(menu, end="")
n = input()
if n == '1':
    print("Enter the radius of circle : ")
    radius = float(input())
    area = 22/7*(radius**2)
    print(f"The area of circle is : {area:.5f}")
elif n == '2':
    print("Enter the length and breadth of rectangle : ")
    length, breadth = list(map(float, input().split()))
    print("Area of rectangle is", length*breadth)
elif n == '3':
    print("Enter the 3 sides of triangle : ")
    a, b, c = list(map(float, input().split()))
    if (a+b) > c and (b+c) > a and (a+c) > b:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of triangle is : {area:.5f}")
    else:
        print("Given input doesn't form a triangle.")

else:
    print("Invalid input")
    print("-----------------------------")
