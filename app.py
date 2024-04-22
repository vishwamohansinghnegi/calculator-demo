from calc_func import do_addition  , do_subtraction
def main():
    print("Welcome to calculator")
    a=int(input('Enter value of a : '))
    b=int(input('Enter value of b : '))
    print('''Select the function from the given options
        1) Addition 
        2)Subtraction''')
    inp = input("Enter input : ")
    if inp=='1':
        result = do_addition(a,b)
    elif inp=='2':
        result = do_subtraction(a,b)
    print('Result : ', result)
if __name__=='__main__':
    main()