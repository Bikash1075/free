import random

class Test:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

f=open('q_ans.txt')
q=f.read()

mcq=[
    Test (q[1:104],"A"),Test (q[104:186],"D"),
    Test (q[186:275],"B"),Test (q[275:347],"B"),
    Test (q[347:433],"D"),Test (q[433:504],"D"),
    Test (q[504:667],"B"),Test (q[667:767],"A"),
    Test (q[767:901],"A"),Test (q[901:997],"C"),
    Test (q[997:1042],"A"),Test (q[1042:1079],"A"),
    Test (q[1079:1129],"A"),Test (q[1129:1194],"B"),
    Test (q[1194:1259],"A"),Test (q[1259:1315],"B"),
    Test (q[1315:1359],"A"),Test (q[1359:1488],"A"),
    Test (q[1488:1550],"B"),Test (q[1550:1597],"B"),
    Test (q[1597:1655],"A"),Test (q[1655:1703],"A"),
    Test (q[1703:1781],"B"),Test (q[1781:1862],"B"),
    Test (q[1862:1947],"B"),Test (q[1947:2033],"A"),
    Test (q[2033:2111],"B"),Test (q[2111:2171],"A"),
    Test (q[2171:2251],"A"),Test (q[2251:2322],"A"),
    Test (q[2322:2381],"B"),Test (q[2519:2602],"A"),
    Test (q[2381:2448],"D"),Test (q[2448:2519],"C"),
    Test (q[2602:2663],"D"),Test (q[2663:2735],"C"),
    Test (q[2735:2805],"D"),Test (q[2805:2890],"C"),
    Test (q[2890:2963],"C"),
    Test (q[2963:3059],"C"),Test (q[3059:3148],"A"),
    Test (q[3148:3221],"C")]

random.shuffle(mcq)
def mcq_test(mcq):
    score = 0
    for q in mcq:
        a=input(q.question)
        if a== q.answer:
            score=score+1
    print(f'{name},You scored {score} out of {len(mcq)}')
    if score<=23:
        print("you faied in quiz")
        print("Better luck next time!")
    else:
        print(f"{name} You passed with {score} score out of {len(mcq)}")

if __name__ == "__main__":
    while True:
        print('*'*10,'Welcome To Quiz Game','*'*10)
        name = input("Enter Your name : ")
        option = int(input("Enter your Option : \n(1)Start Quiz\n(2)Exit\n"))
        if option == 1:
            print("Quiz Started")
            mcq_test(mcq)
            
        elif option==2:
            print('/'*10,'Test Your Knowledge, You are Welcome Anytime \\\\\\\\\\\'')
            break


            

