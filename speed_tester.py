from sympy import *
import random
def get_questions():
    questions = input("How many questions do you want: ")
    return int(questions)
def create_question():
    possible_angles = ["0/1","1/6", "1/4", "1/3", "1/2","2/3","3/4","5/6", "1/1", "7/6","5/4", "4/3", "3/2", "5/3", "7/4","11/6", "2/1"]
    question = random.choice(possible_angles)
    first_num = question.split("/")[0]
    second_num = question.split("/")[1]
    type_of_question = [sin,cos,tan,sec,csc,cot]
    return [first_num, second_num, random.choice(type_of_question)]
    

def main():
    print("Use u for undefined")
    question_amount = get_questions()
    for question in range(question_amount):
        question_nums = create_question()
        print("Solve: " +str(question_nums[2])+"("+question_nums[0]+"*pi/"+question_nums[1]+")")
        answer = input("Answer: ")
        actual_answer = simplify(question_nums[2](str("("+question_nums[0]+"*pi)/"+question_nums[1])))
        print(actual_answer)
        
        


if __name__ == "__main__":
    main()