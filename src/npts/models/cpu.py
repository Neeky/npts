# -*- coding: utf8 -*-


import logging
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CpuTimes(object):
    """反应 CPU 的时间消耗分布的指标
    """
    cores: int = 0
    user: float = 0
    system: float = 0
    idle: float  = 0
    iowait: float = 0
    softirq: float = 0
    clt_at: datetime = None

    def save():
        logging.debug(f"save CpuTimes to sqlite .")

    
