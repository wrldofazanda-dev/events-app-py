# ask the user 10 questions about their event and determine the cost of the event
def ten_random_questions(questionList):
    response = ''
    total = 0.00
    for question_name, question_price in questionList:
        response = input(question_name + ' (yes/no):')
        if response == 'yes':
            total += question_price
        else:
            continue

    return total    

# declare a list of questions and their prices
questionList = [
    ('Will you need a DJ?', 100.00),
    ('Will you need a photographer?', 150.00),
    ('Will you need a caterer?', 200.00),
    ('Will you need a decorator?', 250.00),
    ('Will you need a bartender?', 300.00),
    ('Will you need a florist?', 350.00),
    ('Will you need a baker?', 400.00),
    ('Will you need a planner?', 450.00),
    ('Will you need a valet?', 500.00),
    ('Will you need a security?', 550.00)
]

# call the function and pass the list of questions
total = ten_random_questions(questionList)
print('The total cost of your event is: R', total)