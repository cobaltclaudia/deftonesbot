import os
import twitter

api = twitter.Api(os.environ['CONSUMER_KEY'],
                  os.environ['CONSUMER_SECRET'],
                  os.environ['ACCESS_TOKEN_KEY'],
                  os.environ['ACCESS_TOKEN_SECRET'])
status = api.VerifyCredentials()
print(status)
