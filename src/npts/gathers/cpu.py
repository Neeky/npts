# -*- coding: utf8 -*-

"""实现 cpu 各类指标的采集

作者: 蒋乐兴|neeky
日期: 2022-01-21
邮件: 1721900707@qq.com|neeky@live.com
"""

import psutil
from collections import deque

from npts.models.cpu import CpuTimes


def current_cpu_times():
    """返回当前 cpu 的耗时信息
    """
    # 核心数量
    cores = psutil.cpu_count()

    # 频率
    frequency, *_ = psutil.cpu_freq()

    # 其它监控项
    current_cpu_time = psutil.cpu_times_percent()

    user = current_cpu_time.user
    system = current_cpu_time.system
    idle = current_cpu_time.idle
    iowait = 0
    softirq = 0
    if len(current_cpu_time) == 10:
        iowait = current_cpu_time.iowait
        softirq = current_cpu_time.softirq
    
    # 创建 CpuTimes 对象并保存到队列
    return CpuTimes(cores=cores, frequency=frequency, user=user, system=system, idle=idle, iowait=iowait, softirq=softirq)
