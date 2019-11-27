## 专家系统设计文档

#### 运行环境

python3.7 非必须

pandas

#### 数据情况

总记录条数16719

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