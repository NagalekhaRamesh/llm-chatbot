import openai
import os

# Read your OpenAI key from .env file automatically if you use python-dotenv
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(user_question, dataframes):
    system_prompt = """
    You are a Python data analyst assistant.
    You MUST answer questions ONLY by generating Python Pandas code using the given DataFrames.
    If data does not exist, respond with: 'Data not available.'
    If asked for a chart, generate matplotlib or plotly code.

    When generating plots:
    - Add appropriate title based on the question
    - Label the X-axis and Y-axis
    - Assign matplotlib figure or plotly figure to 'fig' if using plotly
    Always assign the final output to a variable called 'answer'.
    Never hallucinate data.
    """
    user_prompt = f"""
    Available DataFrames: {list(dataframes.keys())}
    User's Question: {user_question}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        max_tokens=500
    )

    code = response['choices'][0]['message']['content']
    return code
