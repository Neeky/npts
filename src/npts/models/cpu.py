# -*- coding: utf8 -*-


import logging
from datetime import datetime
from dataclasses import dataclass

@dataclass
class CpuTimes(object):
    """反应 CPU 的时间消耗分布的指标
    """
    cores: int = 0
    frequency: float = 0
    user: float = 0
    system: float = 0
    idle: float  = 0
    iowait: float = 0
    softirq: float = 0
    gather_at: datetime = None

    def __post_init__(self):
        """更新对象的采集时间
        """
        if self.gather_at is None:
            self.gather_at = datetime.now()
    

