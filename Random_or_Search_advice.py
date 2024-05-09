import requests
import random
from Speak import Say
from Listen import Listen

def get_random_advice():
    url = 'https://api.adviceslip.com/advice'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice_data = response.json()
            advice = advice_data['slip']['advice']
            return advice
        else:
            print(f"Error: Unable to fetch advice. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def search_advice(query, num_advice):
    url = f'https://api.adviceslip.com/advice/search/{query}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice_data = response.json()
            advice_slips = advice_data['slips']
            count = 0
            for slip in advice_slips:
                if count < num_advice:
                    advice = slip['advice']
                    print('Advice:', advice)
                    count += 1
                else:
                    break
        else:
            print(f"Error: Unable to fetch advice. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# def handle_advice():
#     try:
#         Say("Do you want to get random advice or search for advice?")
#         Say("Please specify.")
#         option = Listen()
#
#         if "random advice" in option:
#             random_advice = get_random_advice()
#             if random_advice:
#                 Say("Random Advice: " + random_advice)
#         else:
#             Say("Please specify the advice category you want: Money, Health, Environment, or anything else")
#             word_in_advice = Listen()
#             num_advice = 3
#             search_advice(word_in_advice, num_advice)
#     except requests.exceptions.RequestException as e:
#         Say("Sorry, I encountered an error while handling your request. Please try again later.")
#         print(f"Error: {e}")

# handle_advice()
# Example usage
# random_advice = get_random_advice()
# if random_advice:
#     print("Random Advice:", random_advice)

# Example usage: Search for advice containing the word "love"
# search_advice('finance', 3)