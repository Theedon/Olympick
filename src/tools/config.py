from langchain_groq import ChatGroq

llm_model = "llama-3.1-70b-versatile"

model = ChatGroq(model=llm_model, stop_sequences=None)
