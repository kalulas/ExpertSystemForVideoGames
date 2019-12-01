from pandas import read_csv
from VideoGame import VideoGame
NORECORD = 'NORECORD'

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
        display_message = '\n为您找到 {} 款游戏，当前显示第 {} 项\n\n游戏名称：{}\n游戏类型：{}\n发售时间：{}\n发售平台：{}\n开发者：{}\n媒体评分：{}\n大众评分：{}\n游戏销量（百万）：{}\n游戏评级：{}\n'.format(
                                len(properties), selection+1,
                                properties[selection].name, properties[selection].genre,properties[selection].year_of_release, properties[selection].platform,
                                properties[selection].developer, properties[selection].critic_score,properties[selection].user_score, properties[selection].global_sales,
                                properties[selection].rating)
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