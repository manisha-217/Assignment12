#Q.1.write short note on access token and generate access token.
#Answer-1. An access token is an object encapsulating the security identity of a process or thread.
           #While a token is generally used to represent only security information,
           #it is capable of holding additional free-form data that can be attached while the token is being created.
           #power for perform action in any thing which we access.
           #for example to create a new token with lower levels of access rights to restrict the access of a launched application.
           #The authentication database contains credential information required to construct the initial token for the logon session.
#Q.2. Get the ip of some common site like facebook,google by using DNS lookup
#nslookup facebook.com
#nslookup google.com
#$ nslookup google.com
#Non-authoritative answer:
#Server:  google-public-dns-a.google.com
#Address:  8.8.8.8
#
#Name:    google.com
#Addresses:  2404:6800:4002:803::200e
 #         172.217.24.238


#student@LAB5-137 MINGW32 ~/Desktop
#$ nslookup facebook.com
#Non-authoritative answer:
#Server:  google-public-dns-a.google.com
#Address:  8.8.8.8

#Name:    facebook.com
#Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
 #         157.240.13.35

#Q.3.using tweepy library to extract tweets from tweeter.
#import tweepy
#consumer_key=''
#consumer_secret=''
#access_token=''
#access_token_secret=''
#auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
#auth.set_access_token(access_token,access_token_secret)
#api=tweepy.API(auth)
#tweets=api.search('#love',lang="en",count=2,tweet_mode="extended")
#for tweet in tweets:
 #   print("consumer key sucess")
  #  print(tweet.full_text)
   # print("consumer secret is sucess")
#Q.4. diffrence between library and api.


   # Library
#
# As per simple English terminology – A library is a collection of sources of information and similar resources, made accessible to a defined community for reference or borrowing.
#
# Now put that definition in the Custom Software Development context – What will be the collection of information? And why will a developer use it for reference? The basic building block of any application is its “Code”, and there are certain functionalities that any programmer needs to use repeatedly – then why to code it every time for different applications? That’s where a ‘Library’ comes to a rescue – a chunk of pre-defined code (a collection) that you can call (use for reference) from your own code, to help you do things (similar functionality) more quickly/easily.
#
# example= NumPy , Scrapy-If you are involved in webscraping then this is a must have library for you. ,
#  wxPython- A gui toolkit for python
#
#
#
#
#
# API
#
# Unlike English, not everything in this ‘Library’ is accessible directly. There will be back-end code to support the front-end code which needs to be accessible to programmers for Custom Software Development. Now how do a programmer access this front-end code? Yeah, the API – the Interface to Library.
#
#
# An API (Application Programming Interface) are the functions/methods (the front-end code) in a library that you can call to ask it to do things for you – the interface to the library.
#
# In general terms, it is a set of clearly defined methods of communication between various software components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer.
#
# example= When used in the context of web development, an API is typically defined a set of specifications , such as Hypertext Transfer Protocol (HTTP) request messages, along with a definition of the structure of response messages, which is usually in an Extensible Markup Language (XML) or JavaScript Object Notation (JSON) format

