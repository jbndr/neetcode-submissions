class Twitter:

    def __init__(self):
        self.posts = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        following = {userId}
        following.update(self.follows.get(userId, []))

        feed = [post for user, post in reversed(self.posts) if user in following]
        return feed[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = [followeeId]
        else:
            self.follows[followerId] += [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = [f for f in self.follows if f != followeeId]
        
