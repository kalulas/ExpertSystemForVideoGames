import pandas as pd
import tkinter as tk
from tkinter import ttk, scrolledtext
# from tkinter import scrolledtext
from VideoGame import VideoGame

# game_list = []
# printMaximum = 1
csv_filepath = '../video-game-sales-with-ratings/Video_Games_Sales.csv'

if __name__ == '__main__':
    # TODO: 初始化，考虑封装为函数
    # dataFrame = pd.read_csv(csv_filepath)
    # for index, row in dataFrame.iterrows():
    #     VideoGame(row)
    # game_list = VideoGame.games

    # 用于查看表中的特定属性种类以及具体内容
    # VideoGame.show_genre()
    # VideoGame.show_platform()
    # VideoGame.show_rating()

    window = tk.Tk()
    window.title("Play Smart")
    window.geometry('1024x768')
    window.resizable(width=False, height=False)

    # 第0行与第一行放置给用户的推荐游戏信息
    message = tk.Label(window, text='根据您的要求为您推荐适合的主机游戏')
    result_window = tk.Frame(window, width=1024, height=250)
    # 保证窗口大小不变
    result_window.propagate(0)
    # result_window.insert(tk.INSERT, '还没有推荐内容')
    message.grid(row=0, columnspan=5)
    result_message = tk.Label(result_window, text='还没有推荐内容')
    result_message.pack()
    result_window.grid(row=1, columnspan=5)

    # 第二行设置按钮，有多条推荐信息时用按钮进行切换
    prev_btn = tk.Button(window, text='上一条')
    next_btn = tk.Button(window, text='下一条')
    prev_btn.grid(row=2, column=3)
    next_btn.grid(row=2, column=4)

    # 第三行用于选择游戏所在平台以及游戏类型
    platform_select = ttk.Combobox(window)
    genre_select = ttk.Combobox(window)
    platform_select.grid(row=3, column=0, columnspan=2)
    genre_select.grid(row=3, column=2, columnspan=2)

    # 第四行，选择游戏发售时间段
    # TODO: 日期选择错误时报错
    time_range_labelA = tk.Label(window, text='发售年份从')
    time_range_labelB = tk.Label(window, text='至')
    from_year_select = ttk.Combobox(window)
    to_year_select = ttk.Combobox(window)
    time_range_labelA.grid(row=4, column=0)
    time_range_labelB.grid(row=4, column=2)
    from_year_select.grid(row=4, column=1)
    to_year_select.grid(row=4, column=3)

    # 第五行，对游戏评分做出要求
    

    window.mainloop()