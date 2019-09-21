import time


def subprocess(sublist):
    print('-'*50, '\n你已进入子进程，')
    target = input('一句话说明，你要做什么？')
    todo = input('你打算怎么做？')
    over = False
    cost = 0
    while not over:
        tag_start = input('开始计时？(y/n)')
        if tag_start == 'y':
            start = time.time()
            tag_end = input('结束计时？(y/n)')
            while tag_end != 'y':
                tag_end = input('结束计时？(y/n)')
            end = time.time()
            cost = end - start
            print('你在该子进程上消耗了%.2f秒。' % cost)
            print('-'*50)
            over = True
    sublist.append([target, todo, cost])


def main_process():
    main_target = input('我是形，下午好，主进程决定是什么？')  # 智能化、多级子进程（子进程开启子子进程）
    main_todo = input('你打算怎么做？')
    main_over = False
    main_cost = 0
    sublist = []
    while not main_over:
        tag_start = input('开始计时？(y/n)')
        if tag_start == 'y':
            start = time.time()
            tag_sub_or_end = input('开启子进程(s)？结束计时(e)？')
            while tag_sub_or_end != 'e':
                if tag_sub_or_end == 's':
                    subprocess(sublist)
                    tag_sub_or_end = input('你已回归主进程，开启子进程(s)？结束计时(e)？')
                else:
                    tag_sub_or_end = input('开启子进程(s)？结束计时(e)？')
            end = time.time()
            main_cost = end - start
            print('你在该主进程上消耗了%.2f秒。' % main_cost)
            main_over = True
    sublist.append([main_target, main_todo, main_cost])
    return sublist


if __name__ == '__main__':
    processlist = main_process()
    print('*'*50, '\n你完成的主进程(%.2f秒)：' % processlist[-1][-1], processlist[-1][0])
    print('你依次完成的子进程：')
    for i, sub in enumerate(processlist[0:-1]):
        print('[%d](%.2f秒)' % (i+1, sub[-1]), sub[0])
