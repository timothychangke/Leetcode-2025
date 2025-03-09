from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.followList = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followList[userId].add(userId)
        user_feed = [tweet for follower in self.followList[userId] for tweet in self.tweets[follower]]
        return [tweetId for _, tweetId in heapq.nsmallest(10, user_feed)]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

""" 
with a hash set, items can be added and removed in O(1), this will work for the follow and unfollow functions
need to map a userid to the list of their tweets, can be achieved in O(1)
to get news feed, you merge k sorted lists

"""