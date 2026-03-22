import os
import warnings
warnings.simplefilter("ignore")
from dotenv import load_dotenv
from transcript import get_transcript
from rag import build_vectorstore, ask_video, summarize_video

load_dotenv()

def main():
    print("\n=== YouTube Video Q&A Bot ===")
    url = input("\nPaste YouTube URL: ").strip()
    print("\nFetching transcript...")
    try:
        data = get_transcript(url)
        print(f"Loaded! {data['word_count']} words transcribed.")
    except Exception as e:
        print(f"Error: {e}")
        return
    print("\nBuilding knowledge base...")
    vectorstore = build_vectorstore(data["full_text"], data["video_id"])
    print("\nGenerating summary...")
    summary = summarize_video(data["full_text"])
    print("\n--- VIDEO SUMMARY ---")
    print(summary)
    print("---------------------")
    print("\nNow ask questions! Type quit to exit.\n")
    while True:
        question = input("Your question: ").strip()
        if question.lower() == "quit":
            break
        if not question:
            continue
        print("\nSearching transcript...")
        result = ask_video(question, vectorstore)
        print("\n--- ANSWER ---")
        print(result["answer"])
        print("\n--- SOURCES ---")
        for i, chunk in enumerate(result["chunks"]):
            print(f"Chunk {i+1} score {chunk['score']}: {chunk['text']}")
        print("--------------\n")

if __name__ == "__main__":
    main()
