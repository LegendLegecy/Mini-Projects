from Femspeaker import speak

class registration():
    speak("Want to register the student's data.")
    print("\nWant to register the student's data.")
    
    speak("This program makes the txt file of grade.")
    print("\tThis program makes the txt file of grade.")
    
    speak("Having all data of students.")
    print("\tHaving all data of students.")
    
    speak("It has one disadvantage that you need to run program again for different grades.")
    print("\tIt has one disadvantage that you need to run program again for different grades.\n")
    SchoolName= input("\nEnter the school name:")
    
    speak(f"The Institution is {SchoolName}.") 
    print(f"\nThe Institution is {SchoolName}.") 
    
    speak("Enter the class along with section:")
    classes= input("\nEnter the class along with section:")
    
    with open (f"{classes}", "a") as f:
        f.write("Name \t\t Father_Name \t\t Contact \t\t Serial No. \t\t Gender")
        
        while True:
            speak("Enter full name of student (0 to exit):")
            name = input("\nEnter full name of student (0 to exit):")
            
            if name =="0":
                break
            
            speak("Enter father name of student:")
            father_name = input("\nEnter father_name of student:")
            
            speak("Enter phone number of student:")
            contact = input("\nEnter phone no. of student:")
            
            speak("Enter the serial number of student:")
            serial = input("\nEnter the serial number of student:")
            
            speak("Enter the gender of student:")
            gender = input("\nEnter the gender of student:")
            
            f.write(f"\n {name} \t\t {father_name} \t\t {contact} \t\t {serial} \t\t {gender}")

f=registration()

speak("Thanks for your time.")