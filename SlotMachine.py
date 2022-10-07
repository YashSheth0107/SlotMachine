import random

#Correct username and password
user = "Patrick"
passw = "Starr"

username = ""
password = ""

#Any error while inputting the username and/or password will display an error message
while username != user or password != passw:
    username = input("Username: ")
    password = input("Password: ")
    if username != user and password != passw:
        print("You have entered an invalid username and password. Please try again.\n")
    elif username != user:
        print("You have entered an invalid username. Please try again.\n")
    elif password != passw:
        print("You have entered an invalid password. Please try again.\n")

#After entering the correct login information, the user is welcomed into the game
print("Welcome to the Slot Machine Game!\n")

#User is asked if they want to play or not, any invalid response will result in the question being looped
answer = ""
while True:
    answer = input("\nDo you want to play (yes/no): ")
    if answer == "yes" or answer == "Yes" or answer == "no" or answer == "No":
        break

#When the user is asked to play again after the first round, they are able to say "yes" or "no". 
#The question is looped if an invalid response is given
round_num = 0
play_again = "yes"

if answer == "no" or answer == "No":
    play_again = "no"

#The game officially starts here
#The game loops back here if the user wants to play again after first round
while play_again == "yes" or play_again == "Yes":
    score = 500
    print("\nStarting score:", score,"\n")
    while (answer == "yes" or answer == "Yes") and score > 0:
        round_num += 1
        #s1 = slot 1, s2 = slot 2, s3 = slot 3
        #Randomization is from 1-3 because there are only 3 possible symbols
        s1 = random.randint(1,3)
        s2 = random.randint(1,3)
        s3 = random.randint(1,3)
        
        #s1_sym = slot 1 symbol, s2_sym = slot 2 symbol, s3_sym = slot 3 symbol
        s1_sym = ""
        s2_sym = ""
        s3_sym = ""
        
        #Integers from 1-3 directly correlate to a specific symbol
        if s1 == 1:
            s1_sym = "🍒"
        elif s1 == 2:
            s1_sym = "7️⃣"
        else:
            s1_sym = "🍋"
    
        if s2 == 1:
            s2_sym = "🍒"
        elif s2 == 2:
            s2_sym = "7️⃣"
        else:
            s2_sym = "🍋"
            
        if s3 == 1:
            s3_sym = "🍒"
        elif s3 == 2:
            s3_sym = "7️⃣"
        else:
            s3_sym = "🍋"
        
        #Round number and slot symbols are displayed   
        print("Round", round_num, ":", s1_sym, s2_sym, s3_sym)
        
        #The slot integers correlate to how many points are either earned or lost
        if s1 == 1 and s2 == 1 and s3 == 1:
            score += 300
        elif s1 == 2 and s2 == 2 and s3 == 2:
            score += 200
        elif s1 == 3 and s2 == 3 and s3 == 3:
            score += 100
        else:
            score -= 50
        
        #Game ends once the user reaches 0 points. Game resets if user would like to play again
        if score <= 0:
            play_again = input("\nGAME OVER! You have zero points left! Would you like to play again?: ")
            if play_again == "no" or play_again == "No":
                print("Thanks for playing! Good bye!")
            break
        
        #Current score each round is displayed
        print("Score:", score)
        
        #User is asked if they would like to continue playing after each round
        #This question is looped if user answers with an invalid response
        answer = ""
        while True:
            answer = input("\nDo you want to play (yes/no): ")
            if answer == "yes" or answer == "Yes" or answer == "no" or answer == "No":
                break
        
        if answer == "no" or answer == "No":
            play_again = "no"
            print("\nScore:", score)
            print("We hope to see you again!")
            break
        elif answer == "yes" or answer == "Yes":
            continue
        else:
            print("\nInvalid response")

#BONUS - User asked to rate their experience
rating = int(input("How would you rate your experience today from 1-5?: "))

#BONUS - User is asked if they would like to convert their points to money
#This question is repeated until a valid response (yes or no) is given
convert = ""
while True:
    convert = input("Would you like to convert your points into money?: ")
    if convert == "yes" or convert == "Yes" or convert == "no" or convert == "No":
        break

if convert == "yes" or convert == "Yes":
    print("Success! Your money has been transferred to your account!")