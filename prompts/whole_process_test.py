from prompts.prompter import produce_prompt
from prompts.parser import extract_code_from_completion
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

directories = [
    "fizz-buzz",
    "move-zeroes",
    "n-stacks",
    "print-binary",
    "quick-sort",
    "search-sorted-matrix",
    "two-sum",
]


def generate_ai_skeleton(directory):

    prompt = produce_prompt(directory)

    client = OpenAI(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": prompt}],
    )

    extract_code_from_completion(chat_completion, path=directory)


for dir in directories:
    directory = """problems/""" + dir + """/"""
    generate_ai_skeleton(directory)
