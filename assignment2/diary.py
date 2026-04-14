#Task 1: Diary

try: 
    with open("assignment2/diary.txt", "a") as file:
        user_input = input("What happened today?")
        end_statement = "done for now"

        while user_input != end_statement:
            file.write(user_input + "\n")
            user_input = input("What else?")

        file.write(end_statement + "\n")

except Exception as e:
    print(f"An exception occurred {e}")

