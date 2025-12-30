def make_odd(num): # function returns odd number regardless of number entered, if given number is even, it turns it to odd.
    if num%2==1: # checks if entered number is even.
        print(f"num {num} is odd!")
        return True
    else:
        return make_odd(num+1) # adds one to given odd number to make it even and return output.

entered_num = int(input("Enter a number, an odd number output will be returned regardless... let's go!!!: ")) # sample number to check for if even or odd.

if entered_num % 2 == 0: # checks if entered number is even.
    print(f"number {entered_num} entered is even, adding 1 to make it {entered_num + 1} which is odd!")
    
print(make_odd(entered_num))
        