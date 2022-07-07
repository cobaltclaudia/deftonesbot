import os
import random

import twitter

api = twitter.Api(os.environ['CONSUMER_KEY'],
                  os.environ['CONSUMER_SECRET'],
                  os.environ['ACCESS_TOKEN_KEY'],
                  os.environ['ACCESS_TOKEN_SECRET'])

videoList = list()
videoList.append("I watched a change in you... https://www.youtube.com/watch?v=WPpDyIJdasg")
videoList.append("Its an illusion... https://www.youtube.com/watch?v=Kbl0aSRzvKg")
videoList.append("Take me for one last ride... https://www.youtube.com/watch?v=f0pdwd0miqs")
videoList.append("I get bored... https://www.youtube.com/watch?v=-WdYo3WlETY")
videoList.append("See, I try and look up to the sky, but my eyes burn... https://www.youtube.com/watch?v=XOzs1FehYOA")
videoList.append("I don't care where just far... https://www.youtube.com/watch?v=KvknOXGPzCQ")
videoList.append("Well here's my new address... https://www.youtube.com/watch?v=hbknq6azohw")
videoList.append("And God bless you all for the song you sang us... https://www.youtube.com/watch?v=mLa0-sQg1YM")
videoList.append("There's a hole in the earth...   https://www.youtube.com/watch?v=LnI_QIXU058")
videoList.append("Time will see us realign... https://www.youtube.com/watch?v=qksTlo_1Tpw")
videoList.append("That way I'll always stay away from you... https://www.youtube.com/watch?v=WhstBxChY18")
videoList.append("I wanna watch the way you creep across my skull... https://www.youtube.com/watch?v=woAcXSMyCEw")
videoList.append("You're shooting stars from the barrel of your eyes... https://www.youtube.com/watch?v=2bK4aeahcXc")
videoList.append("Guns! razors! knives! https://www.youtube.com/watch?v=woR6ohiFeYE")
videoList.append("And tonight I feel like more... https://www.youtube.com/watch?v=O_IIAYZL1R4")
videoList.append("Cause back in school we are the leaders of it all... https://www.youtube.com/watch?v=1gxZIL4zpIQ")

randomVideo = random.choice(videoList)
api.PostUpdate(randomVideo)
