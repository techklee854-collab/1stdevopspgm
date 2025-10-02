try:
    a=int(input("enter first number: "))
    b=int(input("Enter second number: "))
    print(f"Before swapping: a = {a},b ={b}")
    # Swapping
    a,b=b,a
    print(f"after swapping: a ={a}, b={b}")
except ValueError:
    print("Please enter valid integers.")
