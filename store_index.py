from dotenv import load_dotenv
import os

from src.helper import pdf_loader, filter_to_minimal_docs, text_split, hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# Load env
load_dotenv()

os.environ["PINECONE_API_KEY"] =os.getenv("PINECONE_API_KEY")
os.environ["GROQ_API_KEY"] =os.getenv("GROQ_API_KEY")
    
# Pinecone client
pinecone = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# Load and process PDFs
extracted_data = pdf_loader(data="data")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)

# Embeddings
embeddings = hugging_face_embeddings()  # must use langchain_community.embeddings

# Create index if not exists
index_name = "medicalchatbot"

if not pinecone.has_index(index_name):
    pinecone.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Connect to index
index = pinecone.Index(index_name)

# Create LangChain Vector Store
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

print("✅ Pinecone Vector Store ready!")