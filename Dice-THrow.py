import random 

def dice_roll(num_times):
    for i in range(num_times):
        num1 = random.randint(1,6) 
        num2 = random.randint(1,6)
        print(num1 + num2)

dice_roll(100)