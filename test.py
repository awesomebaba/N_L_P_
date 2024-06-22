#export HF_TOKEN="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"

from huggingface_hub import InferenceClient
import json

repo_id = "SoyGema/english-hindi"

llm_client = InferenceClient(
    model = repo_id,
    timeout=120,
)

def call_llm(inference_client: InferenceClient,prompt:str ):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "text-generation",
        
        },
    )
    return json.loads(response.decode())[0]["generated_text"]

response=call_llm(llm_client, "jai hind, how are you dear?")
print (response)