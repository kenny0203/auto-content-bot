import os
import openai
import tweepy
from datetime import datetime

# Load secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

# OpenAI
openai.api_key = OPENAI_API_KEY

def generate_post():
    prompt = """
    Write a short, high-engagement post about AI automation for small businesses.
    Under 200 characters.
    Include a hook and insight.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# X Auth
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET,
    ACCESS_TOKEN, ACCESS_SECRET
)

api = tweepy.API(auth)

post = generate_post()
api.update_status(post)

print("Posted:", post)
