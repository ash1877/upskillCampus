#project2

import time
import logging
import random
logging.basicConfig(filename = "project2_Quiz_game.log", level = logging.DEBUG, format = ("%(asctime)s %(levelname)s %(message)s"))


# Make function for loading 
def sleep_time():
    print("Loading your question paper", end="")
    a = 0
    while a<100:
        print(".", end="")
        time.sleep(0.03)   #sleep method from time module
        a+=1
    return " "
try:
    # for make a result
    ok = 0
    ng = 0
    wrong = []

    # check you are intersted or not
    ans = input("Are you ready to play Quiz Game? (yes/no) ").lower()

    if ans != "yes" or ans == 'no':
        print("Thank You")
        logging.info("user aren't ready to play Quiz Game")
        pass
    # take user information
    else:
        num = random.random()
        num = (num + 2) * 1384
        num = str(num)
        logging.info("user ready to play")
        name_list = []
        name = input("Please Give Your Name: ")
        logging.info("user name is: %s", name)
        name_list.append(name)
        age = input("please Give Your Date of Birth: like dd/mm/yy ")
        logging.info("user birth day date is: %s", age)
        logging.info(" %s",num)
        name_list.append(age)
        name_list.append(num)
        print("\n" + "="*57 + " Thank You " + "="*57)

        print(f"""
    Your Name is:          {name_list[0]}
    Your Date of Birth is: {name_list[1]}     
        """) 
        ask = input("is everything correct?(yes/no): ")

        if ask != "yes" or ask[0] =='n':
            print("please try again")
        else:
            print("Creating your Gameing ID ", end="")
            a = 0
            while a<102:
                print(".", end="")
                time.sleep(0.03)
                a+=1
            #return " "
            print ("\n\n" + f"Your Quiz Gameing ID is: {name_list[0][0] + num + name_list[1][-4::1]}")
            
            user_id =  name_list[0][0] + num + name_list[1][-4::1]
            
            logging.info("user Quiz Gameing ID is: %s", user_id)

            time.sleep(2)
            print("\n" + "="*53 + " Let's start the Game " + "="*52)

            print("""

    Please Select the Subject ->

    1. Science
    2. Math
    3. Computer
   
                """)
            sub = input("please choose one: ").lower()
            
            logging.info("user choosed %s no subject", sub)

            if sub == "1" or sub == "science":
                    print("\n"+"="*47 + " You have selected Science " + "="*47)
                    sleep_time()

    #Question 1
                    q1 = input("""1. What is the unit of electric current?
    A) Volts (V)
    B) Watts (W)
    C) Ampere (A)
    D) Ohms (Ω)

    
    """).lower()
                    print(f"You selected = {q1}")

                    if q1 == "c" or q1 == "Ampere" or q1[0] =='a' :
                        ok += 1
                    else:
                        ng +=1
                        wrong.append(f"""1. What is the unit of electric current?
    A) Volts (V)
    B) Watts (W)
    C) Ampere (A)
    D) Ohms (Ω)

    Correct Answer: C) Ampere (A)
    you gave: {q1}
    """)

    # Q2 for Science
                    q2 = input("""2. Which of the following is an example of a non-renewable energy source?
A) Solar
B) Wind
C) Coal
D) Hydroelectric


    """).lower()
                    print(f"You selected = {q2}")

                    if q2 == "c" or q2 == "Coal" or q2[0] =='c' :
                        ok += 1
                    else:
                        ng += 1
                        wrong.append(f"""2.Which of the following is an example of a non-renewable energy source?
A) Solar
B) Wind
C) Coal
D) Hydroelectric

Correct Answer: C) Coal
    you gave: {q2}
    """)

    # Q3 for Science
                    q3 = input("""3. Which of the following is an example of a vector quantity?
A) Speed
B) Temperature
C) Mass
D) Velocity


    """).lower()
                    print(f"You selected = {q3}")

                    if q3 == "d" or q3 == "velocity" or q3[0] == 'v':
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""3. Which of the following is an example of a vector quantity?
A) Speed
B) Temperature
C) Mass
D) Velocity

Correct Answer: D) Velocity
    you gave: {q3}
    """)

    # Q4 for Science
                    q4 = input("""4. Which of the following is an example of a semiconductor material?
    A) Copper(Cu)
    B) Silver(Ag)
    C) Silicon(Si)
    D) Aluminum(Al)

        
    """).lower()
                    print(f"You selected = {q4}")

                    if q4 == "c" or q4 == "silicon (si)" or q4[0] == "s":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""4. Which of the following is an example of a semiconductor material?
    A) Copper (Cu)
    B) Silver (Ag)
    C) Silicon (Si)
    D) Aluminum (Al)

    Correct Answer: C) Silicon (Si)
    you gave: {q4}
    """)

    # Q5 for Science
                    q5 = input("""5. Which of the following is used as a lubricant?
    a) Graphite
    b) Silica
    c) Iron Oxide
    d) Diamond           
    """).lower()
                    print(f"You selected = {q5}")

                    if q5 == "a" or q5 == "graphite" or q5[0] =='g':
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""5. Which of the following is used as a lubricant?
    a) Graphite
    b) Silica
    c) Iron Oxide
    d) Diamond           

 
    you gave: {q5}
    """)
            elif sub == "2" or sub == "math":
                    print("\n" + "="*47 + " You have Selected Math " + "="*47)
                    sleep_time()

   
    #Q1 for math
                    q1 = input("""1. Find the sum of 22 + 53
    a) 75
    b) 2253
    c) 123
    d) 78
    """).lower()
                    print(f"You selected = {q1}")

                    if q1 == "a" or q1 == "75":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""1. Find the sum of 22 + 53
    a) 75
    b) 2253
    c) 123
    d) 78

    Correct ans is:- a)75
    you gave: {q1}
    """)

    #Q2 for math
                    q2 = input("""2. a = 10 & b = 5 then 2a+2b = ?
    a) 20
    b) 15
    c) 30
    d) 25
    """).lower()
                    print(f"You selected = {q2}")

                    if q2 == "c" or q2 == "30":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""2. a = 10 & b = 5 then 2a+2b = ?
    a) 20
    b) 15
    c) 30
    d) 25

    Correct ans is:- c)30
    you gave: {q2}
    """)

    #Q3 for math
                    q3 = input("""3. a = 5 & b = 10 then (2a+2b)^2 = ?
    a) 400
    b) 150
    c) 300
    d) 900
    """).lower()
                    print(f"You selected = {q3}")

                    if q3 == "d" or q3 == "900":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""3. a = 5 & b = 10 then (2a+2b)^2 = ?
    a) 400
    b) 150
    c) 300
    d) 900

    Correct ans is:- d)900
    you gave: {q3}
    """)

    #Q4 for math
                    q4 = input("""4. a = 5 & b = 10 then (2a-2b)^2 = ?
    a) 100
    b) 400
    c) 800
    d) 900
    """).lower()
                    print(f"You selected = {q4}")

                    if q4 == "a" or q4 == "100":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""4. a = 5 & b = 10 then (2a-2b)^2 = ?
    a) 100
    b) 400
    c) 800
    d) 900

    Correct ans is:- a)100
    you gave: {q4}
    """)

    #Q5 for math
                    q5 = input("""5. a = 5 & b = 10 & c= 1 then (2a+2b+c)^2 = ?
    a) 100
    b) 300
    c) 49
    d) 900
    """).lower()
                    print(f"You selected = {q5}")

                    if q5 == "d" or q5 == "900":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""5. a = 5 & b = 10 & c= 1 then (2a+2b+c)^2 = ?
    a) 100
    b) 300
    c) 49
    d) 900

    Correct ans is:- d)900
    you gave: {q5}
    """)
            elif sub == "3" or sub == "computer":
                    print("\n" + "="*47 + "  you have  selected Computer " + "="*47)
                    sleep_time()

    #Q1 for computer
                    q1 = input("""1. When was the first computer invented?
    a) 1945
    b) 1943
    c) 1918
    d) 1937
    """).lower()
                    print(f"You selected = {q1}")

                    if q1 == "b" or q1 == "1943":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""1. When was the first computer invented?
    a) 1945
    b) 1943
    c) 1918
    d) 1937

    Correct ans is:- b)1943
    you gave: {q1}
    """)


    #Q2 for computer
                    q2 = input("""2. In Java, which keyword is used to define a subclass?
A) extends
B) inherits
C) subclass
D) implements



    
    """).lower()
                    print(f"You selected = {q2}")

                    if q2 == "a" or q2 == "ectends" or q2[0] == 'e':
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""2.In Java, which keyword is used to define a subclass?
A) extends
B) inherits
C) subclass
D) implements

Correct Answer: A) extends

     
    you gave: {q2}
    """)

    #Q3 for computer
                    q3 = input("""3. Who is known as the father of computers?
    a) Pascal
    b) Hollerith
    c) Newman
    d) Charles Babbage
    """).lower()
                    print(f"You selected = {q3}")

                    if q3 == "d" or q3 == "charles babbage":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""3. Who is known as the father of computers?
    a) Pascal
    b) Hollerith
    c) Newman
    d) Charles Babbage

    Correct ans is:- d)Charles Babbage
    you gave: {q3}
    """)

    #Q4 for computer
                    q4 = input("""4.Which of the following programming languages is statically typed?
    a) Python
    b) JavaScript
    c) C++
    d) Ruby

   
    """).lower()
                    print(f"You selected = {q4}")

                    if q4 == "c" or q4 == "C++":
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""4. Which of the following programming languages is statically typed?
a) Python
b) JavaScript
c) C++
d) Ruby

Correct Answer: C) C++
    you gave: {q4}
    """)

    #Q5 for computer
                    q5 = input("""5. Which of the following data types is mutable in Python?
A) int
B) float
C) tuple
D) list


    """).lower()
                    print(f"You selected = {q5}")

                    if q5 == "d" or q5 == "list" or q5[0] == 'l':
                        ok +=1
                    else:
                        ng +=1
                        wrong.append(f"""5. Which of the following data types is mutable in Python?
A) int
B) float
C) tuple
D) list

Correct Answer: D) list
    you gave: {q5}
    """)
            

    
            else:
                    print("you have selected the wrong subject, please try again")
                    logging.info("user have selected wrong subject")

            if sub == "1" or sub == "2" or sub == "3" :
                result_ok = int((ok/5)*100)
                result_ng = int((ng/5)*100)
                if result_ok == 100:
                    print ("\nCongratulations ^V^ ")
                    print(f"you gave {result_ok} % correct answers")
                    logging.info(f"user gave {result_ok} % correct answers")
                elif result_ok > 50 and result_ok <100:
                    print ("\nCongratulations (*V*) ")
                    print(f"you gave {result_ok} % correct answers & {result_ng} % wrong answers")
                    logging.info(f"user gave {result_ok} % correct answers")
                    logging.info(f"user gave {result_ng} % wrong answers")
                else:
                    print("\n ^~^")
                    print(f"you gave {result_ok} % correct answers & {result_ng} % wrong answers")
                    logging.info(f"user gave {result_ok} % correct answers")
                    logging.info(f"user gave {result_ng} % wrong answers")

                if len(wrong) != 0:

                    ask1 = input("Do you want to see which question you gave the wrong answer to? ")
                    if ask1 != "yes":
                        logging.info("user Doesnt want to see wrong answers")
                        pass
                    else:
                        logging.info("user want to see wrong answers")
                        for i in wrong:
                            print(i)
                            logging.info("%s",i)
                else:
                    print("^-^ ^O^")

                    
except Exception as e:
    print(e)
    logging.error("Error is happend")
    logging.exception("error is %s",e) 
    




