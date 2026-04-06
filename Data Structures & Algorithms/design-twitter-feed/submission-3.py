class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set)  
        self.user_tweet_map =defaultdict(list)  
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map[userId].append([self.time, tweetId])
        if len(self.user_tweet_map[userId]) > 10:
            self.user_tweet_map[userId].pop(0)
        self.time -= 1 


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Include user's own tweets
        followees = self.follower_map[userId] | {userId}
       
        # Initialize heap with most recent tweet from each followee
        for followeeId in followees:
            if followeeId in self.user_tweet_map and self.user_tweet_map[followeeId]:
                index = len(self.user_tweet_map[followeeId]) - 1
                count, tweetId = self.user_tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        # Extract top 10 tweets using merge k sorted lists approach
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # Add next tweet from same followee if exists
            if index >= 0:
                count, tweetId = self.user_tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        


        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.follower_map:
            self.follower_map[followerId].discard(followeeId)
        
