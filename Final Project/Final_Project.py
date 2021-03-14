"""
Knowledge competition

Write a knowledge competition program. 
• It should consist of 10 questions in total. 
• Each question will have only one answer. 
• Adjust the answers of the questions according to case sensitivity. 
• Each question should be worth 10 points. 
• If User answers 5 or fewer questions, it will be considered unsuccessful. 
• If the user answers more than 5 questions correctly, it will be considered successful.  10 quizluk bilgi yarismasi. 5 ve üzeri dogru basarili.
"""

'''
Quiz questions taken from cfr.org website

'''
print("\nQuiz of 10 questions\n" , 
      "Each question will have only one answer.\n", 
      "Answers of the questions are case sensitive.\n", 
      "Each question worths 10 points.\n",
      "Users gained lower than 50 points are unsuccessful.\n",
      "Let's begin!\n")
point = 0

quiz1 = str(input("1- What is the name of the strategic waterway that traverses Turkey’s largest city and separates Europe from Asia? \n"))
quiz2 = int(input("2- Turkey’s estimated population ranks approximately ____th globally. \n"))
quiz3 = str(input("3- Turkey’s 2017 gross domestic product, a measure of the total size of the economy, was slightly larger than that of which country? \n"))
quiz4 = str(input("4- The modern Republic of Turkey came about in the years after which war? \n"))
quiz5 = str(input("5- For his leadership in founding the Republic of Turkey, Mustafa Kemal became known as “Ataturk,” meaning what?  \n"))
quiz6 = str(input("6- Recep Tayyip Erdogan has served as Turkey’s foremost political leader since what year? \n"))
quiz7 = str(input("7- When did Turkey join the North Atlantic Treaty Organization (NATO)? \n"))
quiz8 = str(input("8- Which of the following describes Turkey’s relationship with the European Union? \n"))
quiz9 = str(input("9- Which type of concurrency is best for CPU-bound programs? \n"))
quiz10 = str(input("10- Which statement best defines “concurrency” in Python? \n"))

##1.quiz
if quiz1 == "Bosporus": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")     
else:
    print("xx Incorrect!", "Total points:", point*10)

##2.quiz
if quiz2 == 18: 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")
else:
    print("xx Incorrect!", "Total points:", point*10)

##3.quiz
if quiz3 == "Netherlands": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")    
else:
    print("xx Incorrect!", "Total points:", point*10)

##4.quiz
if quiz4 == "World War I": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")
else:
    print("xx Incorrect!", "Total points:", point*10)

##5.quiz
if quiz5 == "Father of the Turks": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")   
else:
    print("xx Incorrect!", "Total points:", point*10)

##6.quiz
if quiz6 == "2003": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")
else:
    print("xx Incorrect!", "Total points:", point*10)

##7.quiz
if quiz7 == "1952": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")   
else:
    print("xx Incorrect!", "Total points:", point*10)

##8.quiz
if quiz8.casefold() == "official candidate": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")
else:
    print("xx Incorrect!", "Total points:", point*10)

##9.quiz
if quiz9.casefold() == "multiprocessing": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")    
else:
    print("xx Incorrect!", "Total points:", point*10)

##10.quiz
if quiz10 == "Doing multiple things simultaneously": 
    point += 1
    print("Correct, 10 Points!", "Total points", point*10, "gained\n")
else:
    print("xx Incorrect!", "Total points:", point*10)
    
####
if point >= 5:
    print("\n Congratulations!!!", "You gained total", point*10, "points")
else:
    print("\n Unfortunately,:( ", "you must gain at least 50 points.")
