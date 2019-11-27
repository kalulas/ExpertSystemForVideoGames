## 专家系统设计文档

#### 运行环境

python3.7 非必须

pandas

#### 数据情况

来源 https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings  

#### Context
Motivated by Gregory Smith's web scrape of VGChartz Video Games Sales, this data set simply extends the number of variables with another web scrape from Metacritic. Unfortunately, there are missing observations as Metacritic only covers a subset of the platforms. Also, a game may not have all the observations of the additional variables discussed below. Complete cases are ~ 6,900

#### Content
Alongside the fields: Name, Platform, Year_of_Release, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales, we have:-

Critic_score - Aggregate score compiled by Metacritic staff  
Critic_count - The number of critics used in coming up with the Critic_score  
User_score - Score by Metacritic's subscribers  
User_count - Number of users who gave the user_score  
Developer - Party responsible for creating the game  
Rating - The ESRB ratings  
#### Acknowledgements
This repository, https://github.com/wtamu-cisresearch/scraper, after a few adjustments worked extremely well!


#### VideoGame类的属性

```python
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
```

#### 列入筛选条件

类型（13种单选）、平台（31种单选）、分级（9种多选）、发布年代（1980-2017）、专业评价（0-100）、大众评价（0-10）

不选默认全选

**13**  genres in total:  {'Sports', 'Adventure', 'Puzzle', nan, 'Strategy', 'Simulation', 'Role-Playing', 'Fighting', 'Platform', 'Shooter', 'Racing', 'Misc', 'Action'}  
**31**  platforms in total:  {'SNES', 'GEN', '3DO', 'SCD', 'DS', 'DC', 'N64', 'PSP', 'Wii', 'PS4', 'NES', 'PS', '2600', 'XOne', 'TG16', 'XB', 'NG', 'PC', 'WiiU', 'GBA', 'GC', 'WS', 'GG', '3DS', 'GB', 'SAT', 'X360', 'PSV', 'PCFX', 'PS2', 'PS3'}  
**9**  ratings in total:  {nan, 'E10+', 'T', 'K-A', 'RP', 'E', 'EC', 'AO', 'M'}