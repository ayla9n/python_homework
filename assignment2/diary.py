import traceback

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
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

