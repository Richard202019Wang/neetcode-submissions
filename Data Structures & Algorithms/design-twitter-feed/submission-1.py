class Twitter:

    def __init__(self):
        self.followM = defaultdict(set) # Store followerId : [followeeId]
        self.tweetM = defaultdict(list) # Store userID : [tweetId]
        self.creattime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetM[userId].append((-self.creattime, tweetId))
        self.creattime += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        totalT = self.tweetM[userId].copy()
        #print(totalT)
        for followerId in self.followM[userId]:
            totalT += self.tweetM[followerId].copy()
            # print(self.tweetM[followerId])
        heapq.heapify(totalT)
        result = []
        while len(result) < 10 and totalT:
            result.append(heapq.heappop(totalT)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followM[followerId].discard(followeeId)
