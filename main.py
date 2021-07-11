from datetime        import date, timedelta
from dateutil.easter import *
import tweepy

d = timedelta(days=1)

today = date.today()
print(f"Running bot script with day = {today}")

tweet = f"Het is vandaag, {today}, geen paasmaandag."

if (easter(today.year) + d == today):
    tweet = f"Het is vandaag, {today}, paasmaandag! LETS GOOOOO"

print(tweet)

api_key = "lJXLwZlrD9aWJO6QQypOSUQZ1"
api_key_secret = "F8UWIXwcjU7m7eX2HXvVjfL6v2FvQAntK2EXIrOmETDwImxu6m"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAMHiRAEAAAAASvtiY%2BsEWVIu%2BlNEGXOsAJIddBM%3DSto4owj4G5LzC89RIh4vep6hAGMjEP97OijN0sDk87EgLWnbFi"

access_token_key = "1409815419377049600-M8vra0PibWo8GiTdeT64yv8amMZ4hU"
access_token_secret = "aLpitRdDxh2ICrtCa99njSRsQycXOtjlvi7JJNywq1dlr"


auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

print(api.me().screen_name)

status = api.update_status(status = tweet)
