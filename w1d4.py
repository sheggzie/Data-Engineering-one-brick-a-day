def make_odd(num):
    if num%2==1:
        print(f"num {num} is odd!")
        return True
    else:
        return make_odd(num+1)
entered_num = 6
if entered_num % 2 == 0:
    print(f"number {entered_num} entered is even, adding 1 to make it {entered_num + 1} which is odd!")
print(make_odd(entered_num))
        