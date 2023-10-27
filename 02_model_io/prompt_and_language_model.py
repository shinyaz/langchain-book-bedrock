from langchain.prompts import PromptTemplate
from langchain.chat_models import BedrockChat
from langchain.schema import HumanMessage

chat = BedrockChat(
    model_id="anthropic.claude-v2"
)

prompt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか？",
    input_variables=["product"],
)

result = chat([
    HumanMessage(content=prompt.format(product="iPhone")),
])

print(result.content)
