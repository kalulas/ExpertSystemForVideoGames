import math
NORECORD = 'NORECORD'

class VideoGame:
    games = []
    Platform = set()
    Genre = set()
    YearOfRelease = set()
    
    def __init__(self, data):
        # 初始化对象
        # 数据缺失替换为字符串no_record
        self.name = data.Name
        self.platform = data.Platform
        try:
            self.year_of_release = int(data.Year_of_Release) 
        except ValueError:
            self.year_of_release = NORECORD
        
        self.genre = data.Genre
        self.publisher = data.Publisher
        self.global_sales = data.Global_Sales

        try:
            self.critic_score = int(data.Critic_Score)
        except ValueError:
            self.critic_score = NORECORD
        try:
            self.user_score = round(float(data.User_Score), 1)
        except ValueError:
            self.user_score = NORECORD
        self.developer = data.Developer
        self.rating = data.Rating
        # 记录游戏类型
        VideoGame.Platform.add(self.platform)
        # 避免在下拉菜单中出现NaN游戏类型
        if self.genre != NORECORD:
            VideoGame.Genre.add(self.genre)
        if self.year_of_release != NORECORD:
            VideoGame.YearOfRelease.add(int(self.year_of_release))
        VideoGame.games.append(self)

    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
    
    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)
