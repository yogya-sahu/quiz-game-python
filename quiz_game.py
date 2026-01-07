game =[
    ["What is the capital of Japan?","Beijing","Tokyo","Seoul","Bangkok", "2"],

    ["Which planet is known as the 'Red Planet'?","Venus","earth","mars","saturn","3"],

    ["Which animal is the largest mammal in the world?"," Elephant"," blue whale"," Giraffe","bear","2"],

    ["Who wrote the Harry Potter series?,""J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "Suzanne Collins","1"]
]
prizes = [10000,20000,5000000,80000000,60000000]

i = 0

for game in game:
   
    print(game[0])
          
    print(f"a. {game[1]}")
    print(f"b. {game[2]}")
    print(f"c. {game[3]}")
    print(f"d. {game[4]}")
    
    a = (input("please select your option.\npress 1 for a\npress 2 for b\npress 3 for c\npress 4 for d\n "))
    
    if(game[5]==a):
        print("CONGRATS","your answer is correct")
    else:
        print("SORRY","incorrect answer")
        print("better luck next time ")
        break 
    print(f"you won {prizes[i]}")
    i +=1 
    
    
