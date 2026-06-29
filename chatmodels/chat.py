from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
# from langchain.chat_models import init_chat_model

load_dotenv()

# #####    ----------for chat gpt model --------------

# model = ChatOpenAI(model = "gpt-4o-mini")
# response = model.invoke("what is Cricket ? ")
# print(response.content)

# ###### ------------ gemini model ------------------

# model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash-lite")
# response = model.invoke("what is Cricket ? ")
# print(response.content)

# ######----------- Groq model --------------- 

# model = ChatGroq(model = "openai/gpt-oss-120b")
# response = model.invoke("give me a paragraph on machin")
# print(response.content)

# ######----------- Mistral model --------------- 

model = ChatMistralAI(model = "mistral-small-2506", temperature=0)
response = model.invoke("write a poem on ai")
print(response.content)