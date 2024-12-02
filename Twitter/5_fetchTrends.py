from twitter.account import Account
from twitter.search import Search

## sign-in with credentials
email, username, password = "fhj1371201288@gmail.com", "fish_ung", "Fhj12371201288"
account = Account(cookies='twitter_cookies.cookies')

search = Search(email, username, password, save=True, debug=1)

res = search.run(
    limit=37,
    retries=5,
    queries=[
        {
            'category': 'Top',
            'query': 'crypto'
        },
        {
            'category': 'Latest',
            'query': 'crypto'
        }
    ],
)

