
import requests
from requests.auth import HTTPDigestAuth
from requests.oauthlib import OAuth1
import json

# Replace with the correct URL
url = 'https://api.twitter.com/1.1/search/tweets.json'
auth = OAuth1('fntDSfJzlUAutiPheEKeP1AQl', '45EKtyijar5S6CLbqmYDBh3sWqyepqBi3r2WfYIPPsFuWQ7RFH',
               '207452277-bHesmJ9WmIpOMraoJT0Rwv30kDlSVcHLlTGW5l3Z', 'BfNzNEez0sSBxLErvqWXUP7sqBxJQUYS3iUm6GSEtpdGC')

f=requests.get(url, auth=auth)
print(f)
