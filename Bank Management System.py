from Femspeaker import speak
import random
import os

try: 
    class account():
        
        def create_account(self):
            speak("Enter your Name:")
            self.name= input ("\nEnter your Name:")
            
            speak ("Enter your birthdate (date colon month colon year):")
            self.birthdate= input ("\nEnter your birthdate (DD : MM : YYYY):")
            
            speak ("Enter your Mobile Number")
            self.mobile= int(input ("\nEnter your Mobile No. :"))
            
            speak("Enter your City:")
            self.city= input ("\nEnter your City:")
            
            speak("Enter the Username:")
            self.username= input ("\nEnter the Username:")
            
            speak("Enter your password (0 to 9 but only six letters):")
            self.password= input("\nEnter your password (0-9 six letters):")
            
            
            l= "qwertyuioplaksjdhfgvbcnmxz0123456789"
            self.a= "".join(random.choice(l) for i in range (7))
            
            print(f"\nYour account number is {self.a}.")
            
            with open (self.username , "w") as file:
                file.write(f"Name   \t\t ----->  {self.name}\nBirth Date   ----->  {self.birthdate}\nMobile\t\t ----->  {self.moble}\nCity\t\t ----->  {self.city}\nUsername\t ----->  {self.password}\nID\t -----> {self.no}")
            
            speak("Your account is created successfully.")
            print("Your account is created successfully.")
        
        
        def delete(self):
            speak("Enter your account username:")
            self.dlt= input ("\nEnter your account username:")
            
            speak("Enter your account password:")
            self.pas= int( input ("\nEnter your account password:"))
            
            if os.path.exists(self.dlt):
                os.remove(self.dlt)
                speak("Your account deleted successfully.")
                print("\nYour account deleted successfully.")
            else:
                speak(f"No account name {self.dlt} having {self.pas} exists.")
                print(f"\nNo account name {self.dlt} having {self.pas} exists.")
        
        
        def deposite(self):
            speak("Enter your Username:")
            self.Username= input("\nEnter your Username:")
            
            speak("Enter your Password:")
            self.Password= int(input("\nEnter your Password:"))
            
            speak("Enter the receiver's Username OR Account number ")
            self.RUsername= input("\nEnter the receiver's Username OR Account no. :")
            
            speak("Enter the amount to deposite:")
            self.Amount= int(input("\nEnter the amount to deposite:"))
            
            speak("The amount deposite successfully.")
            print("\nThe amount deposite successfully.")
        
        
        def withdraw(self):
            speak("Enter your Username:")
            self._Username= input("\nEnter your Username:")
            
            speak("Enter your Password:")
            self._Password= int(input("\nEnter your Password:"))
            
            speak("Enter the amount to withdraw:")
            self._Amount= int(input("\nEnter the amount to withdraw:"))
            
            speak("Check! you must got your amount.")
            print("\nCheck! you must got your amount.")
    
    
    
    L = account()
    while True:
        speak("Enter: 0 to Exit, 1 to Create Account, 2 to Delete Account, 3 to Deposite Money, 4 to Withdraw Money :")
        cmd= input("""Enter:
                    0. Exit
                    1. Create Account 
                    2. Delete Account
                    3. Deposite Money
                    4. Withdraw Money :""")
        
        match cmd:
            case "1":
                L.create_account()
            case "2":
                L.delete()
            case "3":
                L.deposite()
            case "4":
                L.withdraw()
        
        if cmd == '0':
            break

except:
    speak ("Sorry Some Error Occur.")
    print("Sorry Some Error Occur (*__*).")

speak ("Thanks for your time.")