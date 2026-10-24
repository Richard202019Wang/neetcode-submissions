class Twitter:

    def __init__(self):
        self.followM = defaultdict(set) # Store followerId : [followeeId]
        self.tweetM = defaultdict(list) # Store userID : [tweetId]
        self.creattime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetM[userId].append((-self.creattime, tweetId))
        self.creattime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minH = []

        self.followM[userId].add(userId)
        for followeeId in self.followM[userId]:
            if followeeId in self.tweetM and self.tweetM[followeeId]:
                idx = len(self.tweetM[followeeId]) - 1
                time, tweetId = self.tweetM[followeeId][idx]
                heapq.heappush(minH, [time, tweetId, followeeId, idx - 1])
        while minH and len(result) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minH)
            result.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetM[followeeId][idx]
                heapq.heappush(minH, [time, tweetId, followeeId, idx - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.followM[followerId].discard(followeeId)
