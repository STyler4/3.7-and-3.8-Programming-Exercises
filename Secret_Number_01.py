pin = input("Enter your secret 4 digit pin: ")


while len(pin) != 4 or not pin.isnumeric():
    pin = input("Enter your secret 4 digit pin: ")

else:
    print(f'Your secret PIN is {pin}')



