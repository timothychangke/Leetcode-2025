from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.followList = defaultdict(list)
        self.tweetList = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetList[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followList: self.followList[userId].append(userId)
        tweets = [tweet for tweet in self.tweetList[id] for id in self.followList[userId]]
        return heapq.nsmallest(10, tweets)
        

    def follow(self, followerId: int, followeeId: int) -> None:
       self.followList[followerId].append(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)