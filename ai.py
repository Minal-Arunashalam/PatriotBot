import openai
import config

openai.api_key = config.ai_apikey

messages = [{"role": "system", "content": "You are a bot created to help George Mason University students learn more about the university and navigate college life. The next message you will receive is the information scraped from the GMU website. You need to learn this information. The subsequent messages you will get after this are questions that students ask you. Don't reply to this first message."}]

def primeAI(data):
    messages.append({"role": "user", "content": "GMU information from website. Just learn this information for when students ask you questions, don't reply to this message. " + data})

def AI(user_input):
    messages.append({"role": "user", "content": "Student question: " + user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    AI_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": AI_reply})
    return AI_reply
