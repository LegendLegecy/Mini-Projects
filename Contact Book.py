import os
from Femspeaker import *

if os.path.exists('Contacts'):
    pass
else:
    with open ("Contacts" , "w") as faizan:
        faizan.write("Name \t\t\t Contact No.")

while True:
    speak("""\nGive me command
                (0 to Exit)
                (1 to Search Contact)
                (2 to Add Contact)
                (3 to Display Contact):""")
    
    cmd= input ("""\nGive me command
                (0.Exit)
                (1.Search Contact)
                (2.Add Contact)
                (3.Display Contact):""")
    
    match cmd:
        case "0":
            break
    
        case "1":
            speak("Enter the name to find:")
            srch= input("Enter the name to find:")
            
            with open ("Contacts" , "r") as Contacts:
                con=Contacts.read()
                contact=con.find(srch)
                print("\n",con[ contact: ( contact+len (con) ) ])
        
        case "2":
            speak ("Enter the name:")
            name= input("\nEnter the name :")
            
            speak("Enter the number:")
            number=input("Enter the number :")
            
            with open ("Contacts" , "a") as c:
                c.write(f"\n{name}\t\t\t{number}")
        
        
        case "3":
            with open ("Contacts" ) as a:
                fa=a.read()
                print("\n",fa)
speak ("Thanks for your time.")

