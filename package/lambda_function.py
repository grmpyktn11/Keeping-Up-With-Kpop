import requests 
from bs4 import BeautifulSoup 
import openai
from datetime import date
import config 
import random
import tweepy


def lambda_handler(event, context):

    ##getting keys 
    openai.api_key = config.gptToken

    ##this is where the news is pulled from
    url = 'https://www.soompi.com/trending'
    response = requests.get(url) 

    randomNum = random.randint(1,14)
    soup = BeautifulSoup(response.text, 'html.parser') 
    headlines = soup.find('body').find_all('h4') 

    ##this is the top headline on soompi! 
    mainHeadline = list(dict.fromkeys(headlines))[randomNum].text.strip()



    ##chatGPT shenanigans
    #gets the day to check what type of content to post

    today = date.today()

    day = today.weekday()

    
    ## on wednesday, ask a question! 
    if(day == 2): 
        completion = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [{'role':'user', "content":("write a twitter tweet for my kpop news account, today is question wednesday where i ask a question to my fans")}]
        )
        
    else:     
        completion = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = [{'role':'user', "content":("reminder: it is extremely important that the response is less than 280 characters (including spaces) write a twitter tweet and add some background information about the following headline: " + mainHeadline + " make sure to not seperate the background, it should be one comprehensive text. also remember you can only have 250 characters spaces included.")}]
        )


    replyContent = str(completion.choices[0].message.content)

    while(len(replyContent) >= 280):
        completion = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{'role':'user', "content":("write a twitter tweet and add some background information about the following headline: " + mainHeadline + " make sure to not seperate the background, it should be one comprehensive text. also remember you can only have 250 characters. ")}]
        )
        replyContent = str(completion.choices[0].message.content)



    client = tweepy.Client(consumer_key=config.twtApiKey,
                            consumer_secret=config.twtApiKeySecret,
                            access_token=config.accessToken,
                            access_token_secret=config.acessTokenSecret)

    response = client.create_tweet(text=str(replyContent))
    print(response)