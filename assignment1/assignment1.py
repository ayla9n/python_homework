#Task 1: Hello
def hello():
    return("Hello!")


#Task 2: Greet with a Formatted String
def greet(name):
    return(f"Hello, {name}!")


# Task 3: Calculator
def calc(a, b, c ="multiply"):
    try:
        match c:
            case "add":
                return(a + b)
            case "subtract":
                return(a - b)
            case "multiply":
                return(a * b)
            case "divide":
                return(a // b)
            case "modulo":
                return(a % b)
            case "int_divide":
                return(int(a) // int(b))
            case "power":
                return(a ** b)
    except ZeroDivisionError:
        return("You can't divide by 0!")
    except TypeError:
        return("You can't multiply those values!")
   

#Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                return(int(value))
            case "str":
                return(str(value))
            case "float":
                return(float(value))
    except ValueError:
        return(f"You can't convert {value} into a {type}.")
    


#Task 5: Grading System, Using *args
def grade(*args):
    try:
        average = sum(args) // len(args)
        if average > 90:
            return("A")
        elif (average >= 80) and (average < 90):
            return("B")
        elif (average >= 70) and (average < 80):
            return("C")
        else:
            return("D")
    except TypeError:
        return("Invalid data was provided.")



#Task 6: Use a For Loop with a Range
def repeat(string, count):
    new_string = ""
    for i in range(count):
        new_string += string
    return new_string


#Task 7: Student Scores, Using **kwargs
def student_scores(a, **kwargs):
    match a:
        case 'best':
            return(max(kwargs, key=kwargs.get))
        case "mean":
            return(sum(kwargs.values()) // len(kwargs))
        

#Task 8: Titleize, with String and List Operations
'''
First and last words are always capitalized
'''
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    title_split = title.split()
    new_title = ""
    for index, word in enumerate(title_split):
        if (index == 0) or (index == len(title_split)-1):
            new_title += word.capitalize()
        elif word in little_words:
            new_title += word
        else:
            new_title += word.capitalize()
        new_title += " "
    return new_title.strip()


#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    secret_list = list(secret)
    guess_list = list(guess)
    new_string = ""
    for letter in secret_list:
        if letter in guess_list:
            new_string += letter
        else:
            new_string+= "_"
    return new_string


#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(term):
    vowels = ["a", "e", "i", "o", "u"]
    term_list = term.split()
    new_string = ""
    
    for word in term_list:
        if word[0] in vowels:
            new_string+= (word + "ay")
        else:
            con_string = ""
            i = 0
            while word[i] not in vowels:
                if (word[i] == "q") and (word[i+1] == "u"):
                    con_string += word[i] + word[i+1]
                    i+=2
                else:
                    con_string += word[i]
                    i+= 1
            con_len = len(con_string)
            new_string += word[con_len:] + con_string + "ay"
        new_string += " "
    
    return new_string.strip()



