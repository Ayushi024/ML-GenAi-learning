from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()
                              #chunking
#Define the PDF path
pdf_path = Path(__file__).parent / "LangChain.pdf"  # __file__ instead of _file_

#PyPDFLoader will later read the PDF and split it into document chunks (usually one chunk per page).
loader = PyPDFLoader(file_path=pdf_path)

#loader.load() reads the PDF file and returns a list of Document objects. Each Document object contains the text content of a chunk and its metadata (like page number).loader is a PyPDFLoader object, which knows how to read a PDF.When you call .load(), PyPDFLoader: Reads the PDF pages.Splits each page (or part of a page) into a Document object, which is considered a “chunk” in LangChain.Returns a list of Document objects
docs = loader.load()


#split the docs into smaller chunks. This is useful for better handling by language models, which often have token limits. The RecursiveCharacterTextSplitter will split the text into chunks of a specified size (chunk_size) with some overlap (chunk_overlap) to maintain context between chunks.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(docs)
# to access  the 13th chunk of your PDF
print(chunks[12])


                      #vector embeddings of these chunks
#model used to convert text into vector embeddings.
embedding_model = OpenAIEmbeddings( 
    model="text-embedding-3-large"
)

#creating vectore embeddings of the chunks and storing them in vector database (qdrant is used in this case)
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    collection_name="learning_rag",
    host="localhost",
    port=6333
)

print("Indexing of documents done...")