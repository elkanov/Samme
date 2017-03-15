import time

print("~       Welcome to:      ~")
time.sleep(2)
print("~         Samme™         ~")
time.sleep(2)
print("__________________________")
print("• A Sam Corp. Production •")
print("         Credits:         ")
time.sleep(1)
print("• Developer & CTO: Elkan Bruha")
time.sleep(1)
print("• CEO & Storyline by: Kyan Mathysen")
time.sleep(1)
print("• Representative & CFO: Alexander Walker")
time.sleep(1)

start = input("Press Start (Type 'Start'): ")

if start.lower() == 'start':
    
    sign = input("Welcome Samme, your adventures are great, but your times are short. What path do you want to take: The Game Path or the Anti-Game Path? (Type: 'Game' or 'Anti-Game'): ")
    
    if sign.lower() == 'game':
        print("Ok, no turning back...")
        print("OK. You have chosen a wise gaming path, you will experience a fun adventure to spread the gaming experience worldwide.")
        print("You will have to pass lots of difficulties concerning people not wanting games to spread.")
        VR = input("How would you like to spread the amazing experience? VR (Virtual-Reality or by Console Games? (Type 'VR' or 'Console':) ")

        if VR.lower() == 'vr':
            print("You've chose wisely, VR is amazing but expensive, you will loose about 2 coins per question. If you're wondering, you start with 50 coins. (You will also win coins by selling the game!) ")
            print("Also, if you're wondering who I am, I am Ą̴̗͙̘̻̼̲̲̮̈́̿̃̎̿͊̈́̓̈́̈͊̎̉͠ͅņ̶̠̬̯͕̘͔̳̃͌̏͘͝ô̴̩̤̣̠͋̈́̃̓͐n̷̢͕̟̤̥͔̗͖͐͛̒͋͆̈́��̊̇̚͜͝y̵̩͌̆́͘m̷̢̙̘̦͚͔͚̹͔̰̠͕̜̰̣̏̿̒o̴̥̫̖͓͂̄̅͛̾̐͆̕͠ű̷̠̣͖͍̮̗̹͎͚͎̪̀͛̌̾̈́̾͂̀͆͑͗̚͝ͅͅş̴̣̟̟̣̟̠̜̩͆̿͊́͛̅̉̓͒̚͘͜͝ͅ")
            print("I have no name, so call me so.")
            Co = input("What shall be your company name? ")
            print("Nice to meet the company: " +Co)
            
            dest = input("Where would you like to start your company? Available destination: New York, Beijing or Los Angeles. (Type NY, BJ, or LA): ")
        
            if dest.lower() == 'ny':
               print("New York, New York! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 8, 2001 at JFK! Enjoy!")
                
            elif dest.lower() == 'la':
                print("Heads in the clouds! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 7, 2001 at LA International Airport! Enjoy! ")
            
            elif dest.lower() == 'bj':
                print("This year is the Rooster! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 6, 2001 at PEK! Enjoy! ")
                    
            else:
                print("Error: 319 == Unable to compute, rebooting...")

        
        if VR.lower() == 'console':
            print("You've chose wisely, Console is fun and cheap, although, you will loose 0.5 coins per question. If you're wondering, you start with 50 coins. (You will also win coins by selling the game!) ")
            print("Also, if you're wondering who I am, I am Ą̴̗͙̘̻̼̲̲̮̈́̿̃̎̿͊̈́̓̈́̈͊̎̉͠ͅņ̶̠̬̯͕̘͔̳̃͌̏͘͝ô̴̩̤̣̠͋̈́̃̓͐n̷̢͕̟̤̥͔̗͖͐͛̒͋͆̈́̅̊̇̚͜͝y̵̩͌̆́͘m̷̢̙̘̦͚͔͚̹͔̰̠͕̜̰̣̏̿̒o̴̥̫̖͓͂̄̅͛̾̐͆̕͠ű̷̠̣͖͍̮̗̹͎͚͎̪̀͛̌̾̈́̾͂̀͆͑͗̚͝ͅͅş̴̣̟̟̣̟̠̜̩͆̿͊́͛̅̉̓͒̚͘͜͝ͅ")
            print("I have no name, so call me so.")
            Co = input("What shall be your company name? ")
            print("Nice to meet the company: " +Co)
            
            dest = input("Where would you like to start your company? Available destination: New York, Beijing or Los Angeles. (Type NY, BJ, or LA): ")
        
            if dest.lower() == 'ny':
               print("New York, New York! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 8, 2001 at JFK! Enjoy!")
                
            elif dest.lower() == 'la':
                print("Heads in the clouds! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 7, 2001 at LA International Airport! Enjoy! ")
            
            elif dest.lower() == 'bj':
                print("This year is the Rooster! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 6, 2001 at PEK! Enjoy! ")
                    
            else:
                print("Error: 319 == Unable to compute, rebooting...")


        else:
            print("Error: 319 == Unable to compute, rebooting... ")

    elif sign.lower() == 'anti-game':
        print("Ok, no turning back.")
        print("You chose a path with a short adventure, since many parents already think that way. ")
        Social = input("But, how are you going to spread that message? By Social Media, or by simple signs and talk? (Type 'Media' or 'Talk':) ")
    
        if Social.lower() == 'media':
            print("Wise choice, but it will be expensive, it will be 1 coin per question but it will be a fast reputation. (You will also win coins by donations!)")
            print("Also, if you're wondering who I am, I am Ą̴̗͙̘̻̼̲̲̮̈́̿̃̎̿͊̈́̓̈́̈͊̎̉͠ͅņ̶̠̬̯͕̘͔̳̃͌̏͘͝ô̴̩̤̣̠͋̈́̃̓͐n̷̢͕̟̤̥͔̗͖͐͛̒͋͆̈́̅̊̇̚͜͝y̵̩͌̆́͘m̷̢̙̘̦͚͔͚̹͔̰̠͕̜̰̣̏̿̒o̴̥̫̖͓͂̄̅͛̾̐͆̕͠ű̷̠̣͖͍̮̗̹͎͚͎̪̀͛̌̾̈́̾͂̀͆͑͗̚͝ͅͅş̴̣̟̟̣̟̠̜̩͆̿͊́͛̅̉̓͒̚͘͜͝ͅ")
            print("I have no name, so call me so.")
            Co = input("What shall be your activist group name? ")
            print("Nice to meet the activist group named: " +Co)
            
            dest = input("Where would you like to start your company? Available destination: New York, Beijing or Los Angeles. (Type NY, BJ, or LA): ")
        
            if dest.lower() == 'ny':
               print("New York, New York! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 8, 2001 at JFK! Enjoy!")
                
            elif dest.lower() == 'la':
                print("Heads in the clouds! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 7, 2001 at LA International Airport! Enjoy! ")
            
            elif dest.lower() == 'bj':
                print("This year is the Rooster! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 6, 2001 at PEK! Enjoy! ")
                    
            else:
                print("Error: 319 == Unable to compute, rebooting...")

    
        if Social.lower() == 'talk':
            print("Good choice, and it will be free! Although, it will be slow, not many people will know, but their knowledge will be great. (You will not win any coins back, since you pay nothing.)")
            print("Also, if you're wondering who I am, I am Ą̴̗͙̘̻̼̲̲̮̈́̿̃̎̿͊̈́̓̈́̈͊̎̉͠ͅņ̶̠̬̯͕̘͔̳̃͌̏͘͝ô̴̩̤̣̠͋̈́̃̓͐n̷̢͕̟̤̥͔̗͖͐͛̒͋͆̈́̅̊̇̚͜͝y̵̩͌̆́͘m̷̢̙̘̦͚͔͚̹͔̰̠͕̜̰̣̏̿̒o̴̥̫̖͓͂̄̅͛̾̐͆̕͠ű̷̠̣͖͍̮̗̹͎͚͎̪̀͛̌̾̈́̾͂̀͆͑͗̚͝ͅͅş̴̣̟̟̣̟̠̜̩͆̿͊́͛̅̉̓͒̚͘͜͝ͅ")
            print("I have no name, so call me so.")
            Co = input("What shall be your campaign name? ")
            print("Nice to meet the campaign named: " +Co)
            
            dest = input("Where would you like to start your company? Available destination: New York, Beijing or Los Angeles. (Type NY, BJ, or LA): ")
        
            if dest.lower() == 'ny':
               print("New York, New York! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 8, 2001 at JFK! Enjoy!")
                
            elif dest.lower() == 'la':
                print("Heads in the clouds! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 7, 2001 at LA International Airport! Enjoy! ")
            
            elif dest.lower() == 'bj':
                print("This year is the Rooster! Have fun in the wonderful city! Tickets for 5 passengers on a plane on Sep 6, 2001 at PEK! Enjoy! ")
                    
            else:
                print("Error: 319 == Unable to compute, rebooting...")

        
        else:
            print("Error: 319 == Unable to compute, rebooting... ")
            #Wo bu shi Zhonguo, wo shi Taiwan!
            
    else:
            print("Error: 420")
            #Weed code word for police (public)
        
else:
    print("Error: A113")
    #Pixar referance...