value = input("Welcome to the menu. Options are listed below:",
              "\n\t 1. Roll \n\t 2. Sweep \n\t 3. Scroll \n Type the",
              "number of your choice and press Enter.") #\n - newline; \t - tab

#print("The value you input is:", value)
#print(f'it is of type {type(value)}.')


while True:
    if value.isdigit() == True: # .isdigit() 
        value = int(value)
        break # on correct value datatype: exit the loop
    else:
        value=input("invalid input, please provide an integer:") #ask for a new value
#print("The converted is:", value)
#print(f'it is of type {type(value)}.')
