from calc_func import do_addition  , do_subtraction , do_division
from multiply import do_multiply
from area import calculate_rectangle_area
def main():
    print("Welcome to calculator")
    a=int(input('Enter value of a : '))
    b=int(input('Enter value of b : '))
    print('''Select the function from the given options
        1) Addition 
        2)Subtraction
        3)Multilpy
        4)Division''')
    inp = input("Enter input : ")
    if inp=='1':
        result = do_addition(a,b)
    elif inp=='2':
        result = do_subtraction(a,b)
    elif inp=='3':
        result = do_multiply(a,b)
    elif inp=='4':
        result = do_division(a,b)
    print('Result : ', result)
if __name__=='__main__':
    main()