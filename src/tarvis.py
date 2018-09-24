import time
import tweepy
from .settings import (
        API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, SEARCH_TERMS)


class ResultType(object):
    MIXED = 'mixed'
    RECENT = 'recent'
    POPULAR = 'popular'


class Tarvis(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def get_api_user(self):
        user = self.api.me()
        return user.name

    def search(self, terms=SEARCH_TERMS):
        data = []
        for term in terms:
            term = '#{} {}'.format(term, '-filter:retweets')
            for tweet in tweepy.Cursor(
                    self.api.search, q=term, lang='en',
                    result_type=ResultType.POPULAR).items(5):
                data.append(tweet)
        return data

    def favourite(self, tweets):
        fav_count = 0
        for tweet in tweets:
            if not tweet.favorited:
                try:
                    tweet.favorite()
                    fav_count += 1
                except:
                    pass
        print('\nFavorited {} tweets!\n'.format(fav_count))


if __name__ == '__main__':
    print('T A R V I S')
    print('-----------')
    print('RUNNING... ')
    print('-----------')
    tarvis = Tarvis()
    while True:
        tweets = tarvis.search()
        tarvis.favourite(tweets)
        time.sleep(900)
