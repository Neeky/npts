# -*- coding: utf8 -*-

"""npt 服务入口点

作者: 蒋乐兴|neeky
日期: 2022-01-24
邮件: 1721900707@qq.com|neeky@live.com
"""

import time
import logging
import argparse
from logging.handlers import RotatingFileHandler

from npts.cores.daemon import start_daemon, stop_daemon
from npts.version import VERSION
from npts.cores import defaults


def parser_args():
    """
    """
    parser = argparse.ArgumentParser("npts-daemon")
    parser.add_argument('--log-level', default='info', choices=['debug', 'info', 'warn','error'], type=str)
    parser.add_argument("action", choices=("start", "stop", "version"))
    return parser.parse_args()

def main():
    """配置日志，处理参数
    """
    # 参数处理
    args = parser_args()

    # 确认运行模式
    if args.action == 'version':
        print(defaults.MSG_FULL_VERSION.format(VERSION))
        return 0
    elif args.action == 'start':
        start_daemon(defaults.PID)
    elif args.action == 'stop':
        stop_daemon(defaults.PID)
    else:
        return 0
    
    # 配置日志
    levels = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'error': logging.ERROR,
        'warn': logging.WARN
        }
    handler = RotatingFileHandler(filename=defaults.LOG_FILE_FULL_PATH, maxBytes=128 * 1024 * 1024, backupCount=8, encoding="utf8")
    logging.basicConfig(handlers=[handler], level=levels[args.log_level], format="[%(asctime)s %(levelname)s] - [%(threadName)s] - [%(pathname)s %(lineno)d line]  ~  %(message)s")
    logging.info(defaults.MSG_LOG_CONFIG_COMPLETED.format(defaults.LOG_FILE_FULL_PATH))

    # 主线程永远在后台运行下去
    while True:
        logging.info(defaults.MSG_DAEMON_IS_RUNNING.format(VERSION))
        time.sleep(defaults.MAIN_THREAD_SLEEP_TIME)
