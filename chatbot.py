import re
import os
import webbrowser
from datetime import datetime
import requests
import subprocess
import json
import random
import webbrowser

# Replace with your actual API keys
openai_api_key = 'your_openai_api_key'
news_api_key = 'your_news_api_key'

# Function to get the current date
def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

# Function to handle arithmetic
def simple_arithmetic(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."
    except:
        return "I couldn't understand the arithmetic expression."

# Function to return a random joke
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kats!"
    ]
    return random.choice(jokes)

# Function to return a random motivational quote
def motivation_quote():
    quotes = [
        "Believe in yourself and all that you are.",
        "The only way to do great work is to love what you do.",
        "Success is not how high you have climbed, but how you make a positive difference to the world."
    ]
    return random.choice(quotes)



# Function to search the web using Google Chrome
def search_web(query):
    try:
        search_url = f"https://www.google.co.in/search?q={query}"
        webbrowser.open_new_tab(search_url)
        return f"Opening Google search for '{query}' in your default web browser."
    except Exception as e:
        return f"Error occurred while trying to search: {str(e)}"


# Function to get the latest news using NewsAPI
import requests

# Function to get the latest news based on country
def get_latest_news(country_code='in'):  # Default country code is 'in' (India)
    try:
        news_url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_api_key}'
        response = requests.get(news_url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        if not articles:
            return f"No news available for country with code '{country_code}'."
        news_list = [f"{article['title']} - {article['source']['name']}" for article in articles[:5]]
        return "\n".join(news_list)
    except requests.exceptions.RequestException as e:
        return f"Error occurred while fetching news: {str(e)}"
    except KeyError:
        return "Unexpected response from the news API."


# Function to play music from YouTube
def play_music_on_youtube(song_name):
    try:
        search_query = "+".join(song_name.split())
        search_url = f"https://www.youtube.com/results?search_query={search_query}"
        webbrowser.open(search_url)
        return f"Searching for {song_name} on YouTube."
    except Exception as e:
        return f"Couldn't play music. Error: {str(e)}"
    
# Function to get user feedback
def get_feedback():
    return "Thank you for your feedback! It helps me improve."

# Function to echo user's input
def echo_input(user_input):
    return f"You said: {user_input}"    

# Main chatbot function
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined responses
    responses = {
    r"^(hello|hi|hey)\b": "Hello! How can I assist you today?",
    r"\bbye\b|\bgoodbye\b": "Goodbye! Have a wonderful day!",
    r"\bhelp\b": "I'm here to help. Please specify your query.",
    r"\bweather\b": "I currently don't provide real-time weather updates. Please check your local weather online.",
    r"\btime\b": f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
    r"\bdate\b": f"Today's date is {get_current_date()}.",
    r"\barithmetic\b (.+)": lambda m: simple_arithmetic(m.group(1)),
    r"\bjoke\b": lambda _: tell_joke(),
    r"\bcompliment\b": "You're amazing just the way you are!",
    r"\babout you\b|\byour name\b": "I'm a simple chatbot here to assist you with basic tasks and provide information.",
    r"\bquote\b|\bmotivation\b": lambda _: motivation_quote(),
    r"\bfavorite color\b": "I don't have a favorite color, but I love the way you interact with me!",
    r"\bfavorite food\b": "As a bot, I don't eat, but I hear pizza is quite popular!",
    r"\bfeedback\b": get_feedback,
    r"\becho\b (.+)": lambda m: echo_input(m.group(1)),
    r"\bsearch for\b (.+)": lambda m: search_web(m.group(1)),
    r"\bnews in ([a-zA-Z]{2})\b": lambda m: get_latest_news(m.group(1).lower()),
    r"\bplay music\b (.+)": lambda m: play_music_on_youtube(m.group(1))
}


    # Check user input against patterns
    for pattern, response in responses.items():
        match = re.search(pattern, user_input)
        if match:
            if callable(response):
                return response(match)
            return response

    # Custom handling for unrecognized inputs
    return "Sorry, I didn't understand that. Can you rephrase or ask something else?"

# Interactive chat loop
def run_chatbot():
    print("Welcome to the chatbot! Type 'q' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'q':
            print("Chatbot: Goodbye! Have a wonderful day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        print("Chatbot: Is there anything else I can help you with today?")

# Running the chatbot
if __name__ == "__main__":
    run_chatbot()
