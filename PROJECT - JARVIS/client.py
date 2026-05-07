
# from openai import OpenAI
 
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="your API key",
#   )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
#   )

# print(completion.choices[0].message.content)





# from groq import Groq

# client = Groq(api_key="your API key")

# chat_completion = client.chat.completions.create(
#     messages=[
#         {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
#     ],
#     model="llama3-8b-8192"
# )

# print(chat_completion.choices[0].message.content)








from google import genai
from google.genai import types



client = genai.Client(
    api_key="your API key"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="what is jarvis?",
    config=types.GenerateContentConfig(
        system_instruction="You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please",
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)
print(response.text)
