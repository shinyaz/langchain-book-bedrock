import json
import boto3

bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

prompt = """
Human: 大谷翔平について教えて

Assistant:
"""

body = json.dumps(
    {
        "prompt": prompt,
        "max_tokens_to_sample": 500,
    }
)

resp = bedrock_runtime.invoke_model(
    modelId="anthropic.claude-v2",
    body=body,
    contentType="application/json",
    accept="application/json",
)

answer = resp["body"].read().decode()
print(json.loads(answer)["completion"])
