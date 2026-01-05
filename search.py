import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("rag-project")

query = "how can I make a Margarita?"

# Retrieve relevant chunks from vector DB:
results =  dense_index.search(
    namespace= "flamehamster",
    query = {
        "top_k": 3,
        "inputs": {
            "text": query
        }
    }
)

print('Raw results:')
print(results)
print("\n" + "="*50 + "\n")

#Convert chunks into one log string of documentation
documentation = ""

for hit in results['result']['hits']:
    fields = hit.get('fields')
    chunk_text = fields.get('chunk_text')
    score = hit.get('score')
    print(f"Score: {score}")
    print(f"Preview: {chunk_text[:200]}...")
    print("-" * 30)
    documentation += chunk_text

print("\n" + "="*50)
print("Combined documentation:")
print(documentation[:500] + "...")
