import time
start = time.time()
print('我是形，')
target = input('一句话说明，你要做什么？')
todo = input('你打算怎么做？')
over = False
while not over:
    tag_start = input('开始计时？(y/n)')
    if tag_start == ('y' or 'yes'):
        start = time.time()
        tag_end = input('结束计时？(y/n)？')
        while tag_end != ('y' or 'yes'):
            tag_end = input('结束计时？(y/n)？')
        end = time.time()
        cost = end - start
        print('你消耗了%.2f秒。' % cost)
        over = True
