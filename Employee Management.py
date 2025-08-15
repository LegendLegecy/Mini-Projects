import os 
import random
from Femspeaker import speak

if os.path.exists("Legends Legecy Employee"):
    pass
else :
    with open ("Legends Legecy Employee" , "w") as file:
        file.write("|Name  \t|\t\tQualification\t\t|\t  Salary  \t|\t\t   ID |")

class Employee():
    
    def add_employee(self):
        speak("Enter your name.")
        self.name= input ("\nEnter your Name:")
        
        speak("Enter your Qualification Degree.")
        self.qualification= input ("\nEnter your Qualification Degree:")
        
        speak("Enter your age or any working experience .")
        self.age_experience = int(input ("\nEnter your Age OR Experience (0-9 years):"))
    
    
    def salary(self):
        
        speak("""Enter your Qualification:
                    1 for Matriculation(10 grade)
                    2 for Intermediate(12 grade)
                    3 for Bachelor 
                    4 for Master
                    5 for M.Phl / Ph.D  :""")
        inp= int( input("""\nEnter your Qualification:
                    1. Matriculation(10 grade)
                    2. Intermediate(12 grade)
                    3. Bachelor 
                    4. Master
                    5. M.Phl / Ph.D  :"""))
        
        match inp:
                case 1:
                    self.pension = "15k-30k"
                case 2:
                    self.pension = "20k-40k" 
                case 3:
                    self.pension = "30k-60k" 
                case 4:
                    self.pension = "50k-100k" 
                case 5:
                    self.pension = "80k or above" 
        
        speak(f"\nYour PAY will be is {self.pension}.")
        print(f"\nYour PAY will be is {self.pension}.")
    
    def id(self):
        options= "asdfghjklpoiuytrewqzxcvbnm0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
        self.pas="" .join(random.choice(options) for i in range (7))
        
        speak(f"Your ID is {self.pas}.")
        print(f"\nYour ID is {self.pas}.")
        
        with open ("Legends Legecy Employee" , "a") as file:
            file.write(f"\n|{self.name}\t|\t\t{self.qualification}\t|\t\t{self.pension}\t|\t\t{self.pas}|")
            speak ("Greetings! my friend. to Legends Legecy.")
    
    def delete(self):
        with open("Legends Legecy Employee", "r") as file:
            
            speak("Enter Employee name for resignation letter ")
            name_srch = input("\nEnter Employee name for resignation letter: ")
            lines = file.readlines()
        
        for index in enumerate(lines):
            line_numbers = [index + 1]
        
        if line_numbers:
            speak(f"Found in: {line_numbers} number.")
            print(f"Found in: {line_numbers} number.")

            speak("Enter line number to confirm resign:")
            num_srch = int(input(f"Enter line number to confirm resign: "))
            
            if len(lines) <= num_srch <= 1 :
                del lines[num_srch - 1]
                
                with open("Legends Legecy Employee", "w") as new_file:
                    new_file.writelines(lines)
                
                speak(f"Employee {num_srch} fired successfully.")
                print(f"Employee {num_srch} fired successfully.")
            else:
                speak(f"Invalid line number: {num_srch}. No changes made.")
                print(f"Invalid line number: {num_srch}. No changes made.")
        else:
            speak(f"Employee with name '{name_srch}' isn't present.")
            print(f"Employee with name '{name_srch}' isn't present.")




LL= Employee()
while True:
    speak("""Enter:
                0 to Exit
                1 to Add Employee
                2 to Fire Employee9 :""")
    cmd= input("""\nEnter:
                0. Exit
                1. Add Employee
                2. Fire Employee :""")
    
    match(cmd):
        case '1':
            LL.add_employee()
            LL.salary()
            LL.id()
        
    if cmd=="0":
        break

speak("Thanks for your time. Sir")