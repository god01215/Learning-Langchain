from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import os
#

def main():
    # 1. Initialize the local model
    # Ensure Ollama is running in your system tray!
    llm = ChatOllama(
        model="gemma3:1b", # Or "gemma:2b" depending on what you downloaded
        temperature=0.7,
        max_tokens=2048,
    )


    output_file = "output.md"
    if os.path.exists(output_file):
        print(f"{output_file} exists and will be overwritten.")
    else:
        print(f"{output_file} does not exist. It will be created.")

    # Open output file for writing (erases old content)
    with open(output_file, "w") as f:
        # 2. Simple invocation
        f.write("--- Basic Query ---\n")
        response = llm.invoke("What is the difference between a Chain and an Agent in LangChain?(In brief and in .md format)\n")
        f.write(response.content + "\n")

        # 3. Chat-style invocation (Recommended for Gemma)
        f.write("\n--- Chat Query ---\n")
        messages = [
            HumanMessage(content="Give me a 3-step plan to learn Deep Learning as a CS student.(In brief and in .md format)"),
        ]
        chat_response = llm.invoke(messages)
        f.write(chat_response.content)
    
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    main()