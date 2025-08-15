# import pyttsx3

# def speak_text(text):
#     # Initialize the TTS engine
#     engine = pyttsx3.init()

#     # Get available voices and set the female voice
#     voices = engine.getProperty('voices')

#     for voice in voices:
#         print(voice)
#         skip=True
#         if "female" in voice.name.lower():
#             engine.setProperty('voice', voice.id)
            
#     else:
#         print("Female voice not found. Using the default voice.")

#     # Set speaking rate (optional, adjust for preference)
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate )  # Decrease rate for a slower speech

#     # Set volume (optional, adjust for preference)
#     volume = engine.getProperty('volume')
#     engine.setProperty('volume', 1.0)  # Max volume

#     # Speak the text
#     engine.say(text)
#     engine.runAndWait()

# # Example usage
# text_to_speak = "Hello, I am a female voice. How can I help you today?"
# speak_text(text_to_speak)





class Account:
    def __init__(self , AccNo , balance ):
        self.balance= balance
        self.AccNo= AccNo
    
    def Balance(self):
        print(f"You Bank Balance is {self.balance}.")
    
    def Credit(self , amount):
        self.amount= amount
        self.balance= self.balance + self.amount
        print(f"Creditted: {self.amount}")
    
    def Debit(self , amount):
        self.amount= amount
        self.balance= self.balance - self.amount
        print(f"Debitted: {self.amount}")


a= Account( 3581684158618651 ,25000 )
a.Balance()
a.Credit(5000)
a.Balance()
a.Debit(10000)
a.Balance()
