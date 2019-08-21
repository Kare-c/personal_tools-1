'''import sys
import time
def progress_bar(total):
   """
   进度条效果
   """
   # 获取标准输出
   _output = sys.stdout
   # 通过参数决定你的进度条总量是多少
   for count in range(0, total + 1):
       # 这里的second只是作为工作量的一种代替
       # 这里应该是有你的主程序,main()
       _second = 0.1
       # 模拟业务的消耗时间
       time.sleep(_second)
       # 输出进度条
       _output.write(f'\rcomplete percent:{count:.0f}')
   # 将标准输出一次性刷新
   _output.flush()
progress_bar(100)'''


from time import sleep
from tqdm import tqdm
# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
for i in tqdm(range(1, 500)):
   # 模拟你的任务
   sleep(0.01)
