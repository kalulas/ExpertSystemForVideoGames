## 基于框架的电子游戏推荐专家系统



### 内容摘要 Abstract

> *在电子游戏行业迅猛发展的今天，每年都有大量的电子游戏发行，如此大量的资讯造成了玩家的选择困难。本文设计了一个以框架为主体，以方法和守护程序为设计思路的专家系统，可以根据用户对游戏属性的偏好，在1980-2016年间发行的一万三千多款不同平台上的电子游戏中挑选出最适合用户的结果，帮助用户做出选择。*
>
> *关键词：框架 方法 守护程序*



![](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/start&load.gif?raw=true)

![](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/select.gif?raw=true)



项目GitHub地址：<https://github.com/KaLuLas/ExpertSystemForVideoGames>

数据来源：<https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings>

#### 项目文件组织

/video–game-sales-with-ratings

​	/Video_Games_Sales.csv 存放VGChartz网站爬取的电子游戏信息

/ActionData.py ActionData类实现

/VideoGame.py VideoGame类实现

/expert.py 专家系统主入口

/expert.exe 可执行文件



### 一、指定问题、系统范围定义以及实现

#### 问题指定

Play Smart专家系统旨在解决玩家面对海量游戏时的选择困难问题，为了能够帮玩家做出全面周到的选择，Play Smart专家系统选择了kaggle网站上的可靠数据源《Video Game Sales with Ratings》：该数据集来源于作者Gregory Smith编写的VGChartz网站爬虫，爬取了1980-2016年各个平台上的游戏记录，每条记录包括以下内容：

1. Name: 游戏名称
2. Platform: 游戏发售平台
3. Year_of_Release: 发售年份
4. Genre: 游戏类型
5. Publisher: 游戏发行商
6. NA_Sales/EU_Sales/JP_Sales/Other_Sales: 各地区游戏销量
7. Global_Sales: 全球销量
8. Critic_score:  Metacritic网站员工对游戏的评分
9. Critic_count:  获得的员工评分数
10. User_score: Metacritic网站用户对游戏的评分
11. User_count: 获得的用户评分数
12. Developer: 游戏开发者
13. Rating: 游戏评级

在这里给出部分数据记录（10/16317）：

| Name                      | Platform | YoR  | Genre        | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales | Global_Sales | Critic_Score | Critic_Count | User_Score | User_Count | Developer | Rating |
| ------------------------- | -------- | ---- | ------------ | --------- | -------- | -------- | -------- | ----------- | ------------ | ------------ | ------------ | ---------- | ---------- | --------- | ------ |
| Wii Sports                | Wii      | 2006 | Sports       | Nintendo  | 41.36    | 28.96    | 3.77     | 8.45        | 82.53        | 76           | 51           | 8          | 322        | Nintendo  | E      |
| Super Mario Bros.         | NES      | 1985 | Platform     | Nintendo  | 29.08    | 3.58     | 6.81     | 0.77        | 40.24        |              |              |            |            |           |        |
| Mario Kart Wii            | Wii      | 2008 | Racing       | Nintendo  | 15.68    | 12.76    | 3.79     | 3.29        | 35.52        | 82           | 73           | 8.3        | 709        | Nintendo  | E      |
| Wii Sports Resort         | Wii      | 2009 | Sports       | Nintendo  | 15.61    | 10.93    | 3.28     | 2.95        | 32.77        | 80           | 73           | 8          | 192        | Nintendo  | E      |
| Pokemon Red/Pokemon Blue  | GB       | 1996 | Role-Playing | Nintendo  | 11.27    | 8.89     | 10.22    | 1           | 31.37        |              |              |            |            |           |        |
| Tetris                    | GB       | 1989 | Puzzle       | Nintendo  | 23.2     | 2.26     | 4.22     | 0.58        | 30.26        |              |              |            |            |           |        |
| New Super Mario Bros.     | DS       | 2006 | Platform     | Nintendo  | 11.28    | 9.14     | 6.5      | 2.88        | 29.8         | 89           | 65           | 8.5        | 431        | Nintendo  | E      |
| Wii Play                  | Wii      | 2006 | Misc         | Nintendo  | 13.96    | 9.18     | 2.93     | 2.84        | 28.92        | 58           | 41           | 6.6        | 129        | Nintendo  | E      |
| New Super Mario Bros. Wii | Wii      | 2009 | Platform     | Nintendo  | 14.44    | 6.94     | 4.7      | 2.24        | 28.32        | 87           | 80           | 8.4        | 594        | Nintendo  | E      |

在项目中，内容被以外部文件的形式选择加载，并初始化为一个个具体实例，因此只要维持对网站的数据爬取获得新数据，就能够访问、修改、删除系统中的数据并执行一些其他动作。

#### 定义系统范围

Play Smart专家系统中为用户提供了以下查询条件：游戏平台、游戏类型、游戏发售年份（一个[年份A，年份B]的闭区间）、媒体评分（>=Score）、大众评分（>=Score）、游戏评级（8个可选的等级：['E10+', 'T', 'K-A', 'RP', 'E', 'EC', 'AO', 'M']，可多选）。

在用户对这些条件做出限定后，专家系统就能够为用户提供合适的游戏。

#### 系统实现

由于该专家系统需要读取csv文件，而python的pandas模块提供了简单上手的读取修改支持，并且python还拥有着较为易用的GUI设计模块tkinter，所以本次专家系统使用了python进行编写，框架使用了python的类来设计，框架中的槽对应类的成员变量，填槽的过程对应类的成员函数，开发工具使用了编辑器Visual Studio Code，并使用模块pyinstaller进行脚本打包形成可执行文件。



### 二、定义类及属性

此专家系统共有两个类：一个为VideoGame类，包含了对电子游戏适用的通用特征，一个为ActionData类，执行加载实例，切换实例显示的工作，具体设计以及代码实现如下：

| Class: VideoGame     |
| -------------------- |
| [Str] Name:          |
| [Str] Platform:      |
| [N] Year_of_Release: |
| [Str] Genre:         |
| [Str] Publisher:     |
| [N] Global_Sales:    |
| [N] Critic_Score:    |
| [N] User_Score:      |
| [Str] Developer:     |
| [Str] Rating:        |

```python
# VideoGame.py
class VideoGame:
    games = []
    Platform = set()
    Genre = set()
    YearOfRelease = set()
    
    def __init__(self, data):
        '...此处省略，见实例化'
        
	# 打印出爬取的数据文件有哪些游戏类型
    @ classmethod
    def show_genre(cls):
        print(len(cls.Genre), ' genres in total: ', cls.Genre)
        
    # 打印出爬取的数据文件有哪些游戏平台
    @ classmethod
    def show_platform(cls):
        print(len(cls.Platform), ' platforms in total: ', cls.Platform)
```

ActionData类设计以及代码实现：

| Class: ActionData                  |
| ---------------------------------- |
| [S] Load Properties:[WHEN CHANGED] |
| [S] Change Display:[WHEN CHANGED]  |
| [S] Year_of_Release:[WHEN CHANGED] |
| [N] selection:                     |
| [C] properties: VideoGame type     |

```python
class ActionData:
    properties = []
    selection = 0
    # 主界面UI加载结束事件与load_properties()的WHEN CHANGED属性链接起来
    # 加载指定目录下的csv文件创建所有实例
    def load_properties(self, csv_filepath):
        # WHEN CHANGED
        dataFrame = read_csv(csv_filepath)
        # 在这里对nan数据进行处理
        dataFrame.fillna(NORECORD,inplace=True)
        for _, row in dataFrame.iterrows():
            VideoGame(row)
        game_list = VideoGame.games
        return game_list
    
    # 以指定格式更改推荐游戏的内容
    def change_display(self):
        properties = ActionData.properties
        selection = ActionData.selection
        display_message = '...省略'
        return display_message

    def goto_next_property(self):
        # WHEN CHANGED
        if ActionData.selection < len(ActionData.properties)-1:
            ActionData.selection += 1
        return self.change_display()

    def goto_prev_property(self):
        # WHEN CHANGED
        if ActionData.selection > 0:
            ActionData.selection -= 1
        return self.change_display()
```



### 三、定义实例

在确定了VideoGame类框架和ActionData类框架之后，就可以通过爬取的数据在启动专家系统时进行对象实例化。由于数据较多，涉及数量一万以上的对象实例化，实例化这一过程被规定在主界面GUI加载完成之后，实际测试需要大约3.7秒的时间。在实例化完成后，专家系统将根据数据中的“游戏平台、游戏类型、发行年份”这几个属性对GUI中的相应下拉菜单赋值，这样即使数据出现改动系统仍然有较好的鲁棒性。

专家系统使用下面的代码来创建新实例：

<span id="jump"></span>

```python
# expert.py
csv_filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title='选择csv文件')
action_data_agent = ActionData()
game_list = action_data_agent.load_properties(csv_filepath)

# ActionData.py
# Class ActionData:
# 主界面UI加载结束事件与load_properties()的WHEN CHANGED属性链接起来
# 加载指定目录下的csv文件创建所有实例
def load_properties(self, csv_filepath):
    # WHEN CHANGED
    dataFrame = read_csv(csv_filepath)
    # 在这里对nan数据进行处理
    dataFrame.fillna(NORECORD,inplace=True)
    for _, row in dataFrame.iterrows():
        VideoGame(row)
    game_list = VideoGame.games
    return game_list

# VideoGame.py 
# Class VideoGame:
# NORECORD表示数据中该记录没有对应属性，为了防止显示错误或者类型错误需要特殊处理
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
```

由于在整个系统执行过程中用户可能进行多次查询，将实例不断的析构又重新构造开销是很大的，因此在整个系统的生命周期中game_list始终是所有游戏实例的列表，当用户进行条件限定时新建一个列表存放满足用户要求的实例，具体代码实现会在下文给出。



### 四、设计显示

专家系统的显示界面设计如下：

1. 在系统启动并加载完主要组件后，弹出窗口令用户选择数据文件：

![select_csv](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/select_csv.jpg?raw=true)

2. 第二个显示的界面是查询显示界面。这个界面允许用户通过回答专家系统的问题来表明自身的要求，基于这些选择，专家系统接下来给出合适的游戏的完整列表。

![csv_loaded](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/csv_loaded.jpg?raw=true)

3. 最后是游戏信息显示界面，这个界面提供一系列合适的游戏，并可以显示前一个条目，后一个条目，以及实例的详尽信息。

![process](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/process.jpg?raw=true)



### 五、定义WHEN CHANGED方法和守护程序

在本次实现的基于框架的系统中，定义了以下方法和守护程序：

当用户启动专家系统并且程序完成主界面组件的加载后，程序要求用户选择数据文件，当csv文件被成功读入时调用ActionData类Load Properties属性的WHEN CHANGED方法，根据csv文件数据创建Property类的所有实例。相应代码已经在[第三节](#jump)给出。

当出现查询显示界面时，用户通过选择设定一系列条件来找到心仪的游戏。由于用户与组件的交互顺序往往是随机的不可预测的，所以不能够将守护程序和页面选项组件链接起来，而是当用户完成了所有条件设置且与“提交”按钮交互时，才激活守护程序，在所有的游戏实例game_list中选取符合用户要求的实例properties。代码实现如下:

```python
# expert.py

# 【守护程序】根据用户的检索条件从game_list队列中遍历查找符合条件的实例
# 把界面的组件和守护程序链接起来，去掉不合适的实例
# 将符合条件的实例存储在ActionData.properties中
def properties_filter():
    # 从各个组件中得到界面中用户选择的查询条件 
    ActionData.properties.clear()
    platform = platform_select.get()
    genre = genre_select.get()
    l_bound = int(from_year_select.get())
    r_bound = int(to_year_select.get())
    critical_score_l = int(critical_score_scale.get())
    user_score_l = round((user_score_scale.get()),1)
    allowed_rating = []
    for idx in range(len(intVar)):
        if intVar[idx].get():
            allowed_rating.append(rating_list[idx])
    
    # 终端打印出用户的选取条件
    print('【RULE】',platform, genre, l_bound, r_bound, critical_score_l, user_score_l)
    for game in game_list:
        if game.platform == platform and game.genre == genre \
            and (game.year_of_release == NORECORD or game.year_of_release >= l_bound and game.year_of_release <= r_bound)\
                and (game.critic_score == NORECORD or game.critic_score >= critical_score_l) \
                    and(game.user_score == NORECORD or game.user_score >= user_score_l)\
                        and(game.rating == NORECORD or game.rating in allowed_rating):
            ActionData.properties.append(game)
    
    # 终端符合用户要求的选取结果
    print('【RESULT】', len(ActionData.properties))
    # 对搜索结果按照年份逆序排列
    ActionData.properties = sorted(ActionData.properties, key=lambda game: game.year_of_release if type(game.year_of_release) == int else -1, reverse=True)
    # 在窗口中显示符合用户要求的首条记录
    # 检测结果条数是否 > 0
    if len(ActionData.properties):
        ActionData.selection = 0
        result_message['text'] = action_data_agent.change_display()
    else:
        result_message['text'] = '数据库中没有符合要求的游戏'
```

同时为了能够实现移动，使用户查看前一条、后一条记录，创建了ActionData的Goto Next Property属性以及 Goto Prev Property属性；当用户与界面的“上一条”“下一条”按钮交互时，就会激活对应属性的WHEN CHANGED方法，代码实现如下：

```python
# ActionData.py
# Class ActionData:
    def goto_next_property(self):
        # WHEN CHANGED
        if ActionData.selection < len(ActionData.properties)-1:
            ActionData.selection += 1
        return self.change_display()

    def goto_prev_property(self):
        # WHEN CHANGED
        if ActionData.selection > 0:
            ActionData.selection -= 1
        return self.change_display()
```



### 六、评价系统

Play Smart专家系统的最初设计已经基本完成，现在给出一个测试用例，在项目目录下启动专家程序有两种方法：

```
# method 1
# 环境依赖: pandas 0.25.3
python expert.py

# method 2
双击执行expert.exe
```

1. 加载页面组件后初始化所有实例。
2. 出现查询显示界面后限定条件并提交，这里选择发售日期在1980-2020期间PS4平台上的Role-Playing类型游戏，满足条件的有52条结果。

![ps4-rpg-1980-2020](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/ps4-rpg-1980-2020.jpg?raw=true)

3. 可以通过“上一条/下一条”按钮切换显示信息，这里显示的游戏是发售于2016年的Dark Souls III黑暗之魂3，类型为Role-Playing角色扮演类。
4. 更改选择条件，这里将媒体评分下界限定在80分，大众评分下界限定在8.0，可以看到符合条件的游戏条目变少了，说明守护程序已将不符合选择的property实例去除，系统提供的游戏确实符合用户的要求。

![ps4-rpg-1980-2020-80](https://github.com/KaLuLas/ExpertSystemForVideoGames/blob/master/screenshots/ps4-rpg-1980-2020-80.jpg?raw=true)

5. 测试完成，现在可以将新的数据按照原有格式添加到数据库中了。



### 七、总结

本次专家系统的设计，模拟了一名人类专家在向玩家推荐电子游戏时的思维方式，用爬取的详尽数据建立了知识库，用框架进行知识的结构化表达，用可交互的UI让玩家能够向专家提供清晰的需求，除此之外还能及时地进行知识的修改以及更新。

而这个专家系统也存在着不足：由于爬取的数据来源单一，存在记录属性缺乏（如销量信息以及评分、评级信息存在着许多NaN记录）的现象，专家无法进行合理的判断；其次专家给出的都是比较武断的决策，对于无法进行量化表达的条件无能为力，而这样的条件在玩家选择游戏时又是时常出现的，这就要求使用模糊推理和模糊规则的方法对专家系统进行改进；再者就是专家系统没有学习的能力，不能通过大量用户的使用来学习用户的个人品味与理想游戏之间的映射关系，这就要求使用机器学习、神经网络的方法对专家系统进行改进。

综上，此专家系统有着一定的优势，同时也有着明显的不足。希望通过日后的学习，我能够更多地积累人工智能领域的知识和实践经验，让设计的应用能够更好地贴近用户需要，满足用户要求。