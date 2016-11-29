import praw
import time

user_agent = ("PyGet Engine 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("powerlifting")

for submission in subreddit.get_new(limit = 5):
    if(submission.url == ""):
        print "Subreddit: ", submission.subreddit
        print "Title: ", submission.title
        print "Text: ", submission.selftext
        print "Score: ", submission.score
        print "------------------------------------------------------"
    else:
        print "Subreddit: ", submission.subreddit
        print "Title: ", submission.title
        print "Link: ", submission.url
        print "Score: ", submission.score
        print "------------------------------------------------------"