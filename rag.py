import os
from groq import Groq
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_vectorstore(text, video_id):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk, metadata={"video_id": video_id, "chunk": i}) for i, chunk in enumerate(chunks)]
    return Chroma.from_documents(documents=docs, embedding=get_embeddings())

def ask_video(question, vectorstore):
    results = vectorstore.similarity_search_with_score(question, k=3)
    context = "\n\n".join([doc.page_content for doc, _ in results])
    prompt = f"""You are a helpful assistant answering questions about a YouTube video.
Answer using ONLY the transcript context below.
If the answer is not in the transcript, say This topic was not covered in the video.

Transcript context:
{context}

Question: {question}"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    return {
        "answer": res.choices[0].message.content,
        "chunks": [{"text": doc.page_content[:150], "score": round(float(s), 3)} for doc, s in results]
    }

def summarize_video(text):
    prompt = f"""Summarize this YouTube video transcript in 5 bullet points.
Be specific and include the key insights.
Transcript (first 3000 chars): {text[:3000]}"""
    res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )
    return res.choices[0].message.content
