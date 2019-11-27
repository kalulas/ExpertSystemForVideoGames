import os
import pandas as pd
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, scrolledtext
# from tkinter import scrolledtext
from VideoGame import VideoGame

# 关联九种不同rating的intVar列表，为1时表示被选中
intVar = []
# game_list = []
# printMaximum = 1
rating_list =  ['nan', 'E10+', 'T', 'K-A', 'RP', 'E', 'EC', 'AO', 'M']
# os.chdir('../video-game-sales-with-ratings/')
csv_filepath = './video-game-sales-with-ratings/Video_Games_Sales.csv'

if __name__ == '__main__':
    # TODO: 初始化，考虑封装为函数
    dataFrame = pd.read_csv(csv_filepath)
    for index, row in dataFrame.iterrows():
        VideoGame(row)
    game_list = VideoGame.games

    # 用于早期输出表中的特定属性种类以及具体内容
    # VideoGame.show_genre()
    # VideoGame.show_platform()
    # VideoGame.show_rating()

    window = tk.Tk()
    window.title("Play-Smart.expertsystem")
    window.geometry('1024x768')
    window.resizable(width=False, height=False)

    # 第0行与第一行放置给用户的推荐游戏信息
    message = tk.Label(window, text='[EXPERT SYSTEM]根据您给出的要求，为您推荐以下游戏', font=('Microsoft YaHei', 18))
    result_window = tk.Frame(window, width=1024, height=250)
    # 保证窗口大小不变
    result_window.propagate(0)
    message.grid(row=0, columnspan=5)
    result_message = tk.Label(result_window, text='还没有推荐内容')
    result_message.pack()
    result_window.grid(row=1, columnspan=5)

    # 第二行设置按钮，有多条推荐信息时用按钮进行切换
    prev_btn = tk.Button(window, text='上一条')
    next_btn = tk.Button(window, text='下一条')
    prev_btn.grid(row=2, column=3, sticky='e', ipadx=20, pady=30)
    next_btn.grid(row=2, column=4, ipadx=20)

    # 第三行用于选择游戏所在平台以及游戏类型
    platform_label = tk.Label(window, text='主机平台', font=('tMicrosoft YaHei',12,'bold'))
    genre_label = tk.Label(window, text='游戏类型', font=('tMicrosoft YaHei',12,'bold'))
    platform_select = ttk.Combobox(window, value=list(VideoGame.Platform))
    platform_select.current(0)
    genre_select = ttk.Combobox(window, value=list(VideoGame.Genre))
    genre_select.current(0)
    platform_label.grid(row=3, column=0)
    platform_select.grid(row=3, column=1)
    genre_label.grid(row=3, column=2)
    genre_select.grid(row=3, column=3)

    # 第四行，选择游戏发售时间段
    # TODO: 日期选择错误时报错
    time_range_labelA = tk.Label(window, text='发售时间自', font=('tMicrosoft YaHei',12,'bold'))
    time_range_labelB = tk.Label(window, text='年起至', font=('tMicrosoft YaHei',12,'bold'))
    from_year_select = ttk.Combobox(window, value=list(VideoGame.YearOfRelease))
    from_year_select.current(0)
    to_year_select = ttk.Combobox(window, value=list(VideoGame.YearOfRelease))
    to_year_select.current(0)
    time_range_labelA.grid(row=4, column=0)
    time_range_labelB.grid(row=4, column=2)
    from_year_select.grid(row=4, column=1)
    to_year_select.grid(row=4, column=3)

    # 第五行，对游戏评分做出要求
    critical_score_scale = tk.Scale(window, label='媒体评分高于', from_=0, to=100, orient=tk.HORIZONTAL,
             length=400, showvalue=1, tickinterval=10, resolution=1)
    critical_score_scale.grid(row=5, column=0, columnspan=2)
    user_score_scale = tk.Scale(window, label='大众评分高于', from_=0, to=10, orient=tk.HORIZONTAL,
             length=400, showvalue=1, tickinterval=1, resolution=0.1)
    user_score_scale.grid(row=5, column=2, columnspan=2)

    # 第六行，确认提交所选游戏指标要求
    submit_btn = tk.Button(window, text='提交', font=('Microsoft YaHei', 15))
    submit_btn.grid(row=6, column=2, ipadx=70, ipady=10, pady=10)

    # 最右列放置一个用于选择游戏分级的listGroup
    rating_frame = tk.Frame(window)
    rating_frame.grid(row=3, column=4, rowspan=3)
    rating_note_label = tk.Label(rating_frame, text='游戏评级选择', font=('tMicrosoft YaHei',12,'bold'))
    rating_note_label.pack()
    for i in range(9):
        intVar.append(tk.IntVar)
        check = tk.Checkbutton(rating_frame, text=rating_list[i], variable=intVar[i], onvalue=1, offvalue=0)
        check.pack(side='top', expand='yes', fill='both')

    window.mainloop()