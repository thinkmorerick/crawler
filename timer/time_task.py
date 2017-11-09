# coding:utf-8

import datetime,os,platform

# 需要执行的任务
def run_Task():
    os_platform=platform.platform()
    if os_platform.startswith('Darwin'):
        print('this is mac os system')
        os.system('ls')
    elif os_platform.startswith('Window'):
        print('this is win system')
        os.system('dir')

# 定时器 周期和修改
def timerFun(sched_Timer):
    flag=0
    while True:
        now = datetime.datetime.now()
        if now == sched_Timer:
            run_Task()
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer + datetime.timedelta(minutes=1)
                flag = 0

# 主程序
if __name__ == '__main__':
    sched_Timer = datetime.datetime(2017,11,9,9,30,10)
    print('run the timer task at {0}'.format(sched_Timer))
    timerFun(sched_Timer)