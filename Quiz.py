from QuizClass import Quiz
import random
#player variables
player1Score=0
player2Score=0
#Question setup, adding to question list
Questions=list()
question1=Quiz("The Vandals were known for which achievement?","Sacking Rome","Breaking the Geneva Convention","Settling France","Vandalizing places",1)
Questions.append(question1)
question2=Quiz("What year did the Romans found their empire?","45BC","273BC","34AD","27BC",4)
Questions.append(question2)
question3=Quiz("What was the abbreviation for a given year in Ancient Rome?","AFR","AUC","AD","AFC",2)
Questions.append(question3)
question4=Quiz("Alexander the great was the king of which country?","Egypt","Rome","Macedon","Persia",3)
Questions.append(question4)
question5=Quiz("Who did the Spartans battle in 480BC?","Egypt","Persia","Rome","Sicily",2)
Questions.append(question5)
question6=Quiz("What was the geographical area Macedon was located? ","Balkans","Iberia","Western Asia","Baltic",1)
Questions.append(question6)
question7=Quiz("Which king is considered the first Holy Roman Emperor?","Louis III","Charles I","Otto I","Berengar I",3)
Questions.append(question7)
question8=Quiz("What year did the French Revolution start?","1780","1764","1756","1789",4)
Questions.append(question8)
question9=Quiz("When was the first pyramid built?","1650BC","517BC","2630BC","3152BC",3)
Questions.append(question9)
question10=Quiz("What was the name of the famous Spartan King?","Agis","Leonidas","Lacedaemon","Leotychidas",2)
Questions.append(question10)

#Working with users
if __name__=="__main__":
    print("Welcome to the Python intro programming quiz\n--------------------------------------------\n")

    #sets up quiz for 10 questions only
    for i in range(0,10):
        print("Player %d here is your question:" %((i%2)+1))
        question=random.choice(Questions) #Using a random here to make sure that every quiz starts and ends differently
        print(question,"\n")

        #error-trapping user-input for answer (this is my standard error trapping method for a specific range of integer values, used this in lab3)
        valid=False
        while not valid:
            answer=input("Enter your answer:")
            try:
                answer=int(answer)
                if(answer>0 and answer<5):
                    valid=True
              
                else:
                    print("Error: your answer has to be a value between 1 and 4. Try again.")
            except:
                print("Error: your answer has to be a value between 1 and 4. Try again.")
        correct=question.getcorrect() #getting the number value of correct using getter

        #checking if the user-inputted answer is the same as this value, adds to score for specific player 
        if answer==correct:
            print("Excellent! You score!\n")
            if(i%2==0):
                player1Score+=1
            else:
                player2Score+=1
        else:
            print("That is incorrect. Better luck with the next question.\n")

        Questions.remove(question) #removes question so that it won't appear again

    #final score output and winner
    print("And the final scores are:")
    print("Player 1:",player1Score)
    print("Player 2:",player2Score)
    if player1Score>player2Score:
        print("Player 1 wins!")
    elif player2Score>player1Score:
        print("Player 2 wins!")
    else:
        print("Both players tied!")
#Credit to Mark Prucnal mdp83 for giving me the idea to set "correct" to a number to lessen code.