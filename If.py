# creating a program that is even
num = 20
if num % 2 == 0:  # if the remainder when num divided by 2 is 0, it's even
    print("number is even") 
else:
    print("number is odd")

# creating a program to check if someone is eligible to vote
age = 20
is_citizen = False

if age >= 18 and is_citizen == True:
    print("they can vote")
else:
    print("you can't vote")

# program that generates random number and has user guess what it is
randon_num = random.randint(0, 100)
# update program to keep rack of how many guesses user made and let them konow at the end 
while True:
    guess = int(input("guess a number \n"))
    if guess < random_num:
        print("the nubmer you want it higher")
    elif guess > random_num:
        print("the number you want is lwoer")
    else:
        print("congrats! you guessed it")
        break