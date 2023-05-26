#!/usr/bin/env python

import openai
import sys
def chatBot(text):
    openai.api_key = "your key openAI"
    response = openai.Completion.create(
        
        engine = "text-davinci-003",
        #engine = "gpt-3.5-turbo",
        
        prompt = text,
        temperature = 0.3,
        max_tokens = 4000,
    )
    return print(response.choices[0].text)
def main():
    domanda = sys.argv[1] 
    chatBot(domanda)
    print('\n')
main()
