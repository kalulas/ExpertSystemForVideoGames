class VideoGame:
    games = []
    Platform = set()
    Genre = set()
    Rating = set()
    
    def __init__(self, data):
        # 初始化对象
        self.name = data.Name
        self.platform = data.Platform
        self.year_of_release = data.Year_of_Release
        self.genre = data.Genre
        self.publisher = data.Publisher
        self.global_sales = data.Global_Sales
        self.critic_score = data.Critic_Score
        self.user_score = data.User_Score
        self.developer = data.Developer
        self.rating = data.Rating
        # 记录类型
        VideoGame.Platform.add(self.platform)
        VideoGame.Genre.add(self.genre)
        VideoGame.Rating.add(self.rating)
        VideoGame.games.append(self)

    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
    
    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)

    @ classmethod
    def show_rating(cls):
        print(len(cls.Rating), ' ratings in total: ', cls.Rating)
        