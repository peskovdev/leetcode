from collections import defaultdict


class Twitter:
    def __init__(self):
        self.tweets = []  # [(userId, tweetId), (userId, tweetId)]
        self.subscriptions = defaultdict(set)  # {user_id: {followee_id, followee_id}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.subscriptions[userId]:
            self.subscriptions[userId].add(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        news_feed = []
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][0] in self.subscriptions[userId]:
                news_feed.append(self.tweets[i][1])
            if len(news_feed) == 10:
                break
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].discard(followeeId)
