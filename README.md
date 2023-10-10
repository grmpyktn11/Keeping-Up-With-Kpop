# Keeping-Up-With-Kpop
 This is an ai-powered app that posts autoamatic tweets about the latest news in K-pop!

    This was the first personal project I decided to work on from start to finish. At the time of writing, I am in my 6th week of college

    WHAT THIS APP USES:
    
        This app uses Twitter API, ChatGPT API (using gpt 3.5 turbo), dateTime, and HTMLparser. It is also hosted in AWS Lambda for automation. 

            DateTime and HTML Parser
                >Pulls the headlines from the trending page of soompi's website depending on the day of the week and feeds them to

            ChatGPT
                >Takes the article given and provides a response in the form of a tweet. If it is Wednesday, the tweets are all questions
        
            Twitter API:
                >Posts the tweets using the v2 api 
            
            AWS Lambda:
                >Runs the script every few hours, hosted on lambda because it is free and easy lol
                
            
            
