import os
import openai
from datetime import datetime
import ReadLastTotalTokens

openai.api_key = os.getenv("OPENAI_API_KEY")  # Windows 환경변수에 저장된 API key 불러오는 방식
#openai.api_key = "{MY_OPENAI_API_KEY}"       # OPENAI_API_KEY 문자열 직접 입력 방식

messages = []
tokens = []

### Save Converation History bewteen the user and ChatGPT in a variable, "messages" ###
while True:
    user_content = input("user : ")

    if user_content == "-1":
        print(f"total tokens in this conversation: {token}")
        print("End of program. Goodbye!")
        break
    else:
        messages.append({"role" : "user", "content" :  f"{user_content}" })
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        assistant_content = completion.choices[0].message["content"].strip()
        messages.append({"role": "assistant", "content": f"{assistant_content}"})
        token = completion.usage.total_tokens
        tokens.append(token)

        #print(f"ChatGPT: {assistant_content}")
        #print(f"total_tokens: {token}")

### print the conversation history ###        
now = datetime.now()
now_string=now.strftime("%Y-%m-%d %H:%M:%S")
print(now_string)

conversation_count = len(messages)

for i in range(conversation_count):
    role =  "ChatGPT" if messages[i]["role"] == "assistant" else messages[i]["role"]
    print(role, ": ")
    print(messages[i]["content"]) 
    
print(tokens)

### Save the conversation history to a file ###
log_file = os.path.join(os.getcwd(), "conversation_history.txt")
total_tokens = tokens[-1]
last_total_tokens = ReadLastTotalTokens(log_file)
total_tokens_accumulated = last_total_tokens + total_tokens

with open(log_file, 'a') as f:
    f.write("\n" + now_string)
    for i in range(conversation_count):
        role = "ChatGPT" if messages[i]["role"] == "assistant" else messages[i]["role"]
        f.write("\n" + role + ": " + messages[i]['content'] + "\n" )

    f.write('\n')
    f.write('accumulated_total_tokens: ' + str(total_tokens_accumulated) + '\n')
    f.write('='*80)
