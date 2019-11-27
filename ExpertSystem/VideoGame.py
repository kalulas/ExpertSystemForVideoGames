import math


class VideoGame:
    games = []
    Platform = set()
    Genre = set()
    YearOfRelease = set()
    
    def __init__(self, data):
        # 初始化对象
        self.name = data.Name
        self.platform = data.Platform

        if not math.isnan(float(data.Year_of_Release)):
            self.year_of_release = int(data.Year_of_Release) 
        else:
            self.year_of_release = -1
        
        self.genre = data.Genre
        self.publisher = data.Publisher
        self.global_sales = data.Global_Sales
        self.critic_score = data.Critic_Score
        self.user_score = data.User_Score
        self.developer = data.Developer
        self.rating = data.Rating
        # 记录类型
        VideoGame.Platform.add(self.platform)
        # 避免出现NaN游戏类型
        if type(self.genre) != float:
            VideoGame.Genre.add(self.genre)
        if self.year_of_release != -1:
            VideoGame.YearOfRelease.add(int(self.year_of_release))
        VideoGame.games.append(self)

    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
    
    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)
