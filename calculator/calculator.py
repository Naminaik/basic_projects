history_files = "history.txt"

def show_history():
    file = open(history_files, 'r')
    lines = file.readlines()
    if len(lines) ==0:
        print("no history yet.")
    else:
        for line in lines:
            print(line.strip())
        file.close()
        
def delete_history():
    file = open(history_files, 'w')
    file.close()
    print("history is deleted")
    
def save_history(equation , result):
    file = open(history_files, 'a')
    file.write(f"{equation} = ({str(result)}) \n")
    file.close()
    
def calculator(user_input):
    parts = user_input.split()
    if len(parts) !=3:
        print("invalid input format.please enter in the format: ")
        return 
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    
    if op == "+":
       result = num1 + num2
    elif op == "-":
        result = num1 -num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 ==0:
            print("error: cant divide by zero")
            return 
        result = num1 / num2
    else:
        print("invalid operator. use only +,-,/,*. : ")
        return
    
    if int(result) == result:
        result = int(result)
        print(f"result: {result}")
        save_history(user_input, result)
        
def main():
    print("WELCOME TO THE CALCULATOR!")
    while True:
        user_input = input("\n enter an calcilation (+,-*,/) \n or cammand(history,delete,quit)--> \n")
        if user_input.lower() == "exit":
            print("goodbye!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "delete":
            delete_history()
        elif user_input == "quit":
            print("goodbye!")
            break
        else:
            calculator(user_input)
        
main()
        
            
                
       
  
       
   