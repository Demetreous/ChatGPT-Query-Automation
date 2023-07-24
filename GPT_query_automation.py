#Script to send queries to chatGPT and store responses in a file.
#Currently does not work, as OpenAI's API needs payment to use
import openai
import time

# Set your OpenAI API key here
openai.api_key = OPENAI_API_KEY

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()

def main():
    query_list = [
        "When were you released?",
        "What is the smallest city in the world?"
        # Add more queries to the list as needed
    ]

    output_file = "chatgpt_responses.txt"

    with open(output_file, "w") as file:
        for query in query_list:
            chatgpt_response = get_chatgpt_response(query)
            print("User Query:", query)
            print("ChatGPT Response:", chatgpt_response)
            file.write(f"User Query: {query}\n")
            file.write(f"ChatGPT Response: {chatgpt_response}\n")
            file.write("=" * 30 + "\n")

            # To avoid rate-limiting, sleep for a few seconds between API calls
            time.sleep(10)

if __name__ == "__main__":
    main()
