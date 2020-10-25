'''
Area of a Rectangle
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def calculate_area(l, w):
    area = l * w
    return area

def draw_rectangle(l, w):
    if l.isnumeric() and w.isnumeric():
        length = int(l)
        width = int(w)
        for i in range(width):
            print("*" * length)

def print_area(l, w, a):
    print(f"The area of the rectangle with dimensions:")
    print(f"- Length of {l} units")
    print(f"- Width of {w} units")
    print(f"is {a:.2f} square units.")

def main():
    userCont = input("To exit type 'END': \n")
    while userCont.lower() != "end":
        user_length = input("1. What is the length of the rectangle?\n")
        while is_number(user_length) == False:
            print("Please enter a numerical value for the dimension.")
            user_length = input("1. What is the length of the rectangle?\n")
        length = eval(user_length)
        
        user_width = input("1. What is the width of the rectangle?\n")
        while is_number(user_width) == False:
            print("Please enter a numerical value for the dimension.")
            user_width = input("1. What is the width of the rectangle?\n")
        width = eval(user_width)

        area_of_rectangle = calculate_area(length, width)
        print_area(length, width, area_of_rectangle)
        draw_rectangle(user_length, user_width)
        
        userCont = input("To exit type 'END': \n")
    print("The program has ended.")

main()
