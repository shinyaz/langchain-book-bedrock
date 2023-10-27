from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import BedrockChat
from langchain.schema import HumanMessage

chat = BedrockChat(
    model_id="anthropic.claude-v2",
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler()
    ],
    model_kwargs={"max_tokens_to_sample": 500},
)
resp = chat([
    HumanMessage(content="おいしいステーキの焼き方を教えて")
])
