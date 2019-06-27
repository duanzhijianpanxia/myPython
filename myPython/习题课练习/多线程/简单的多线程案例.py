import _thread as thread
import time

movie_list = ['斗破苍穹.mp4', '复仇者联盟.mp4', '九层妖塔.rmvb', '色戒.avi']
music_list = ['七里香.mp3', '新贵妃醉酒.mp3']
movie_format = ['mp4', 'avi']
music_format = ['mp3']


def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print('你现在收看的是{0}'.format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print('你现在收听的是{0}'.format(i))
            time.sleep(2)
        else:
            print("没有能播放的格式")


def thread_run():
    thread.start_new_thread(play, (movie_list,))
    thread.start_new_thread(play, (music_list,))
    # 没有西面的代码压根就不会打印
    while True:
        time.sleep(15)

if __name__ == '__main__':
    thread_run()