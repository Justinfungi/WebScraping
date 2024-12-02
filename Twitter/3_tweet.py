from twitter.account import Account

## sign-in with credentials
email, username, password = "fhj1371201288@gmail.com", "fish_ung", "Fhj12371201288"
#account = Account(email, username, password)
account = Account(cookies='twitter_cookies.cookies')

"""account.tweet('Damnnnn', media=[
  {'media': '/home/fish/Pictures/Screenshots/1.png', 'alt': 'some alt text', 'tagged_users': [123]},
])"""

account.quote('Quite Interesting', tweet_id=1863644451987468767)
#account.save_cookies(fname="twitter_cookies")
