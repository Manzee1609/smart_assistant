import os
import time
import pyttsx3

def app_closer(words):
    for word in words:
        if word in exit_keys:
            return True
    return False


def app_opener(words):
    for key in app_opener_keys:
        if key in words:
            return True
    return False
         

def google():
    while True:
        print("Enter your google query: ", end = '')
        query = input()
        if app_closer(query.split(' ')):
            print("Byee!! See you soon")
            exit()
            final_query = "chrome " + query
            os.system(final_query)
            print("Your query executed successfully")

def reminder():
    print("What is that shall I remind you about?", end = '')
    msg = input()
    print("In how many minutes shall I remind you?", end = '')
    mins = int(input())
    time.sleep(mins * 60)
    print("You have a reminder: " + msg)
    

def calculate(operator_keys, s):
    for key in operator_keys:
        if key in s:
            return True
    return False


def smart_calc():
    while True:
        print("Enter your calculation query: ", end = '')
        s = input()
        if app_closer(s.split(" ")):
            print("Byee!! See you soon.")
            exit()
        words = s.split(" ")
        numbers = []
        for word in words:
            if word.isnumeric():
                numbers.append(int(word))
	
        if calculate(sum_keys, s):
            print(sum(numbers))

        elif calculate(subtract_keys, s):
            if 'from' in s:
                print(numbers[-1] - numbers[0])
            else:
                print(numbers[0] - numbers[-1])
    
        elif calculate(multiply_keys, s):
            print(numbers[0] * numbers[1])

        elif calculate(divide_keys, s):
            print(numbers[0]/numbers[1])
        else:
            print("Sorry! I could not recognize your query")



sum_keys = ['+', 'sum', 'plus', 'add', 'join', 'put together', 'total', 'and', 'append']
subtract_keys = ['-', 'subtract', 'minus', 'diiference', 'deduct', 'take away', 'take from', 'take off']
multiply_keys = ['*','x', 'X', 'multiply','multiplied', 'multiplied by', 'multiplication', 'into']
divide_keys = ['division', '/', 'divide', 'divided by', 'by']
app_opener_keys = ['open', 'execute', 'run']
apps_list = ['chrome', 'settings', 'whatsapp', 'command prompt', 'recycle bin', 'wmplayer', 'calculator', 'calender', 'camera', 'notepad', 'my pc', 'mail']
exit_keys = ['close', 'exit', 'bye', 'terminate', 'finish', 'quit']

print("Hello!!! welcome to smart helper")
print("You can type 'What can you do' to know more about me'")
print("You can type away your queries")

while True:
    print("Your Query: ", end = '')
    s = input()
    words = s.split(" ")

    if s == "What can you do" or s == "what can you do":
        print("Heyy!! I am your smart helper. \n I can help you with some of your tasks")
        print("I can open any application installed on your pc.")
	print("You can type 'apps' to get a list of all supported apps. \n")
        print("I can also perform some basic mathematical calculations.")
        print("Type 'smart calc' to activate smart calculator. \n")
        print("I can search queries on google.")
        print("Type 'google' to search for any queries on the web. \n")
        print("I can also remind you of your tasks.")
        print("Type 'reminder' to set a reminder. \n")

    elif 'google' in words:
        google()
    elif 'smart calc' in s:
        smart_calc()
    elif 'apps' in words:
        print(apps_list)	
    elif 'reminder' in words:
        reminder()
    elif app_opener(words):
        for app in apps_list:
            if app in words:
                os.system(app)
    else:
        print("Sorry! I could not recognize your query")
       
 

