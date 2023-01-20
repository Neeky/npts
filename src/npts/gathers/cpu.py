# -*- coding: utf8 -*-

"""实现 cpu 各类指标的采集
"""

import psutil
"""
    def __post_init__(self):
        self.clt_at = datetime.now()
        psutil_cpu_times = psutil.cpu_times()
        if len(psutil_cpu_times) == 4:
            logging.info("len of psutil.cpu_times() equals 4 mac os .")
            self.user = psutil_cpu_times.user
            self.system = psutil_cpu_times.system
            self.idle = psutil_cpu_times.idle
        elif len(psutil_cpu_times) == 10:
            logging.info("len of psutil.cpu_times() equals 10 linux .")
"""
