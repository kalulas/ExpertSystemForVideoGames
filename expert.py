import os
import copy
import time
from time import sleep
from pandas import read_csv
from tkinter import Label, Frame, Button, Checkbutton, Tk, IntVar, HORIZONTAL, Scale, filedialog
import tkinter.font as tkFont
from tkinter import ttk, scrolledtext
from VideoGame import VideoGame
from ActionData import ActionData
from Evaluation import Evaluation

NORECORD = 'NORECORD'
# 关联九种不同rating的intVar列表，为1时表示被选中
intVar = []
# 当前显示第n条记录，通过按钮进行切换
selection = 0
# 保存数据库中所有的游戏记录
game_list = []
# 满足用户搜索条件的游戏
rating_list =  ['E10+', 'T', 'K-A', 'RP', 'E', 'EC', 'AO', 'M']

# 【调用ActionData类方法】根据用户交互改变UI显示内容
# 激发goto_prev_property和goto_next_property的WHEN CHANGED方法
def switch_property(direction):
    if direction == 'prev':
        message = action_data_agent.goto_prev_property()
    else:
        message = action_data_agent.goto_next_property()
    result_message['text'] = message


# 【守护程序】根据用户的检索条件从game_list队列中遍历查找符合条件的实例
# 把界面的组件和守护程序链接起来，去掉不合适的实例
# 将符合条件的实例存储在ActionData.properties中
def properties_filter():
    # 从各个组件中得到界面中用户选择的查询条件 
    ActionData.properties.clear()
    
    args = {'pf': platform_select.get(),
            'ge': genre_select.get(),
            'lb': int(from_year_select.get()),
            'rb': int(to_year_select.get()),
            'cs': int(critical_score_scale.get()),
            'us': round((user_score_scale.get()),1)}
    allowed_rating = []
    for idx in range(len(intVar)):
        if intVar[idx].get():
            allowed_rating.append(rating_list[idx])
    args['ar'] = allowed_rating
    evaluate = Evaluation(args)
    evaluate.print_rule()

    for game in game_list:
        if evaluate.qualified(game):
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


if __name__ == '__main__':

    window = Tk()
    window.title("Play-Smart.expertsystem")
    window.geometry('1024x640')
    window.iconbitmap('./game_128px_1234884_easyicon.net.ico')
    window.resizable(width=False, height=False)

    # 第0行与第一行放置给用户的推荐游戏信息
    message = Label(window, text='[EXPERT SYSTEM]', font=('Microsoft YaHei', 18))
    result_window = Frame(window, width=1024, height=180)
    # 保证窗口大小不变
    result_window.propagate(0)
    message.grid(row=0, columnspan=5)
    result_message = Label(result_window, text='还没有推荐内容')
    result_message.pack()
    result_window.grid(row=1, columnspan=5)

    # 第二行设置按钮，有多条推荐信息时用按钮进行切换
    prev_btn = Button(window, text='上一条', command=lambda:switch_property('prev'))
    next_btn = Button(window, text='下一条', command=lambda:switch_property('next'))
    prev_btn.grid(row=2, column=3, sticky='e', ipadx=20, pady=30)
    next_btn.grid(row=2, column=4, ipadx=20)

    # 第三行用于选择游戏所在平台以及游戏类型
    platform_label = Label(window, text='主机平台', font=('tMicrosoft YaHei',12,'bold'))
    genre_label = Label(window, text='游戏类型', font=('tMicrosoft YaHei',12,'bold'))
    platform_select = ttk.Combobox(window)
    genre_select = ttk.Combobox(window)
    platform_label.grid(row=3, column=0)
    platform_select.grid(row=3, column=1)
    genre_label.grid(row=3, column=2)
    genre_select.grid(row=3, column=3)

    # 第四行，选择游戏发售时间段
    time_range_labelA = Label(window, text='发售时间自', font=('tMicrosoft YaHei',12,'bold'))
    time_range_labelB = Label(window, text='年起至', font=('tMicrosoft YaHei',12,'bold'))
    from_year_select = ttk.Combobox(window)
    to_year_select = ttk.Combobox(window)
    time_range_labelA.grid(row=4, column=0)
    time_range_labelB.grid(row=4, column=2)
    from_year_select.grid(row=4, column=1)
    to_year_select.grid(row=4, column=3)

    # 第五行，对游戏评分做出要求
    critical_score_scale = Scale(window, label='媒体评分高于', from_=0, to=100, orient=HORIZONTAL,
             length=400, showvalue=1, tickinterval=10, resolution=1)
    critical_score_scale.grid(row=5, column=0, columnspan=2)
    user_score_scale = Scale(window, label='大众评分高于', from_=0, to=10, orient=HORIZONTAL,
             length=400, showvalue=1, tickinterval=1, resolution=0.1)
    user_score_scale.grid(row=5, column=2, columnspan=2)

    # 第六行，确认提交所选游戏指标要求
    submit_btn = Button(window, text='提交', font=('Microsoft YaHei', 15), command=properties_filter)
    submit_btn.grid(row=6, column=2, ipadx=70, ipady=10, pady=10)

    # 最右列放置一个用于选择游戏分级的listGroup
    rating_frame = Frame(window)
    rating_frame.grid(row=3, column=4, rowspan=3)
    rating_note_label = Label(rating_frame, text='游戏评级选择', font=('tMicrosoft YaHei',12,'bold'))
    rating_note_label.pack()
    for idx in range(len(rating_list)):
        intVar.append(IntVar(value=1))
        check = Checkbutton(rating_frame, text=rating_list[idx], variable=intVar[idx], onvalue=1, offvalue=0)
        check.pack(side='top', expand='yes', fill='both')
    
    # 【Load Properties】UI界面加载完毕后加载csv文件
    # 创建ActionData对象action_data_agent
    # 激发WHEN CHANGED对数据库中的所有记录进行实例化
    print('SYSTEM: 专家正在选择加载CSV文件')
    print('SYSTEM: 当前目录', os.getcwd())
    try:
        result_message['text'] = '正在加载数据...'
        csv_filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title='选择csv文件')
        start = time.time()
        print('SYSTEM: csv文件加载中...')
        action_data_agent = ActionData()
        game_list = action_data_agent.load_properties(csv_filepath)
        counter = round(time.time() - start, 2)
        result_message['text'] = '数据加载完毕，耗时{}s，目前还没有推荐内容'.format(counter)
        print('SYSTEM: csv文件加载完毕,耗时{}s'.format(counter))
    except Exception:
        print('ERROR: 加载 CSV 文件失败')
        window.destroy()
        sleep(1)
        exit()

    # 根据数据加载首页下拉菜单内容
    platform_select['value'] = sorted(list(VideoGame.Platform))
    genre_select['value'] = sorted(list(VideoGame.Genre))
    from_year_select['value'] = list(VideoGame.YearOfRelease)
    to_year_select['value'] = list(VideoGame.YearOfRelease)
    platform_select.current(0)
    genre_select.current(0)
    from_year_select.current(0)
    to_year_select.current(len(VideoGame.YearOfRelease)-1)

    # 用于早期输出表中的特定属性种类以及具体内容
    VideoGame.show_genre()
    VideoGame.show_platform()

    window.mainloop()