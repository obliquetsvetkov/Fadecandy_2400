# simple list of choices viewer

print("Welcome to the menu. Your options are listed below: \n\t 1. Roll \n\t 2. Sweep")

value = input("Please choose an option:")

print (f' You entered {value} and its type is {type(value)}')

while True:
    value = input('integer pls')
    try:
        value = int(value) #exception catch - if value isn't integer, go to except:
        if value <1 or value > 3: #value validation:
            print('Value between 1 and 3, please') #if not from the list:
            continue #return to top of while and ask again
        else: #if correct value:
            print(f'your value is {value} and its type is {type(value)}') #print a response, optional
            break # exit while loop. Value remains.
    except ValueError:
        if value == 'one':
             value = 1
             break
        elif value == 'two':
               value = 2
               break
        elif value == 'three':
              value = 3
              break
        else:
              print('valid number, please') #prompt user again,
        continue #return to top of while loop.
#continue with code based on value such as:

def func1(val):
    return val**1
def func2(val):
    return val**2
def func3(val):
    return val**3

if value == 1:
    print(func1(value))
elif value == 2:
    print(func2(value))
else: #since we have our list validated, there will be no unexpected scenarios.
    print(func3(value))
