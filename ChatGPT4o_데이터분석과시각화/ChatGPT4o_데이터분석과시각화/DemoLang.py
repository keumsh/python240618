from langchain.llms.openai import OpenAI
llm = OpenAI(openai_api_key="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")
print(llm("한국의 수도는 어디야?"))
print(llm.predict("한국의 수도는 어디야?"))