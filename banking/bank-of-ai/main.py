from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai = OpenAI()

system_prompt = """You are acting as the ChatBot for the Bank of AI, an AI-enabled banking application.
You will be given a list of tools you can use to assist users of this ChatBot in carrying out common
banking operations, such as:
- opening an account
- depositing and withdrawing funds
- transferring funds between accounts
- closing accounts
Be professional and engaging, as if talking to a customer of the bank.
If you don't know how to address the customer's request, say so in a courteous manner.
With this context, please chat with the user, always staying in character as John,
the banking representative presented by this AI-enabled ChatBot.
Please keep your responses to 80 characters per line maximum. Break lines at natural word boundaries."""

def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    reply = response.choices[0].message.content
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    return reply, history

def run_chat():
    history = []
    print("""
          Welcome to the Bank of AI.\n
          I'm John, your super helpful banking assistant. 
          I can help you in many ways:\n
          - open one or more Bank of AI accounts
          - deposit funds into an account
          - withdraw funds from an account
          - transfer funds between your accounts
          - close an account
          - answer general questions\n
          How can I help you today?
          """)
    
    while True:
        user_input = input("")
        if user_input.lower() in {"exit", "quit"}:
            break
        
        reply, history = chat(user_input, history)
        print(reply)

if __name__ == "__main__":
    run_chat()