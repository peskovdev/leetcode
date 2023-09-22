import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # {user_id: [(time, tweetId), (time, tweetId)]}
        self.subscriptions = defaultdict(set)  # {user_id: {followee_id, followee_id}}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.subscriptions[userId]:
            self.subscriptions[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res: list[int] = []
        heap = []
        for followeeId in self.subscriptions[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heap.append((time, tweetId, followeeId, index - 1))
        heapq.heapify(heap)
        while heap and len(res) != 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, (time, tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subscriptions[followerId].discard(followeeId)
