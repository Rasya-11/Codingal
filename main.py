import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
from generator import generate_answer
from verifier import verify_answer


def main():
    print("=" * 40)
    print("AI GENERATION WITH VERIFICATION")
    print("=" * 40)

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a question.")
        return
    
    try:
        print("\nGenerating answe...")

        answer = generate_answer(question)

        print("\nAI Generated Answer:")
        print(answer)

        print("\nVerifying answer...")

        is_valid, message = verify_answer(answer)

        print("\nVerification Result:", message)

        if is_valid:
            print("\nFinal Verified Output:")
            print(answer)
        else:
            print("\nAnswer rejected.")
            print("Please try again.")

    except Exception as error:
        print("\nAn error occurred:")



if __name__=="__main__":
    main()