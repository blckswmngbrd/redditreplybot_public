#!/usr/bin/python

import praw
import config


search_term = input("What is your search term?: ")
sub_search = input("Preferred subreddit: ")
comment_reply = input("How would you like to reply?: ")
def bot_login():
	print("Logging in..")
	reddit =praw.Reddit(username= config.username, 
			password= config.password,
			client_id = config.client_id, 
			client_secret = config.client_secret, 
			user_agent = "") #Enter YOUR user agent
	print("Logged in!")

	return reddit

def run_bot(reddit,search_term,sub_search):
	for comment in reddit.subreddit(sub_search).comments(limit=50):
		if search_term in comment.body: #search term in reddit
			print("String with search term found at" + comment.id)
			comment.reply(comment_reply)
			print("Replied to comment"+comment.id)

reddit = bot_login()
run_bot(reddit,search_term,sub_search)