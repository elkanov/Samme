sign = input("Welcome citizen, please write your name here and you'll be considered to enter. ")
print("For your information, points will be divided by 3 (now 4 since you might be in) and if you would ever want to leave, it will be available at about 15 pts.")

age = input("Do you still want to continue? Type yes or no: ")

if age == 'no':
    print("OK. Goodbye, your entry try has been recorded and you may leave.")
    
elif age == 'yes':
    print("OK, no turning back.")
    print("But before, please rate your coding skills bellow: ")
    
pie = int(input("1-5 Intermediate | 5-9 Expert | 10 Genius " ))

if pie < 3:
    print("Sorry, but we have more skilled professionals, we will have to decline. ")
    print("Anything to say? ")
    print("OK, Goodbye " +sign)
    
elif pie > 3:
    print("You will be going in voting trial, please prepare your expertise. ")
    print("Welcome " +sign)
    
print("HAIL SAM CORP.!")