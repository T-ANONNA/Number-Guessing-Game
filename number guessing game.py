import random
logo="""

$$\   $$\                         $$\                                  $$$$$$\                                          $$\                            $$$$$$\                                    
$$$\  $$ |                        $$ |                                $$  __$$\                                         \__|                          $$  __$$\                                   
$$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\        $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\       $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
$$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
\__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \______/  \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |       \______/  \_______|\__| \__| \__| \_______|
                                                                                                                                      $$\   $$ |                                                  
                                                                                                                                      \$$$$$$  |                                                  
                                                                                                                                       \______/                                                   

"""
print(logo)
computer_guess=random.randint(1,101)
print(computer_guess)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty=input("choose a difficulty.Type 'Easy' or Hard': ").lower()
if choose_difficulty=="easy":
    
    attempts=10
    
    while not attempts ==0:
        print(f"You have {attempts} attempts to guess the number. ")
        number_choice=int(input("Make a guess: "))
        if number_choice < computer_guess:
                print("Two low.")
                attempts-=1
               
        elif number_choice > computer_guess:
                print("Two high. ")
                attempts -= 1
              
        else:
             attempts-=attempts
             print(f"You got it! The answer was {computer_guess}")
        if attempts==0 and number_choice != computer_guess:             
          print(f"yo've run out of guesses.The correct number is {computer_guess}. Refresh the page to run again.")
        if attempts != 0 and number_choice != computer_guess:
              print("Guess again")
   
  

else:
    attempts =5  
    while not attempts ==0:
        print(f"You have {attempts} attempts to guess the number. ")
        number_choice=int(input("Make a guess: "))
        if number_choice < computer_guess:
                print("Two low.")
                attempts-=1
               
        elif number_choice > computer_guess:
                print("Two high. ")
                attempts -= 1
              
        else:
             attempts-=attempts
             print(f"You got it! The answer was {computer_guess}")
                    
        if attempts==0 and  number_choice != computer_guess:
             
              print(f"You've run out of guesses.The correct number is {computer_guess}. Refresh the page to run again")  
        if attempts != 0 and number_choice != computer_guess:
              print("Guess again")