# -*- coding: utf8 -*-

import time
import logging
import argparse
from logging.handlers import RotatingFileHandler

from npts.cores.daemon import start_daemon, stop_daemon
from npts.version import VERSION


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
        print(f"npts-{VERSION} \npowered by neeky \nblogs https://www.sqlpy.com .")
        return 0
    elif args.action == 'start':
        start_daemon("/tmp/npts-daemon.pid")
    elif args.action == 'stop':
        stop_daemon('/tmp/npts-daemon.pid')
    
    # 配置日志
    logfile="/tmp/npts-daemon.log"
    levels = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'error': logging.ERROR,
        'warn': logging.WARN
        }
    handler = RotatingFileHandler(filename=logfile, maxBytes=128 * 1024 * 1024, backupCount=8, encoding="utf8")
    logging.basicConfig(handlers=[handler], level=levels[args.log_level], format="[%(asctime)s %(levelname)s] - [%(threadName)s] - [%(pathname)s %(lineno)d line]  ~  %(message)s")
    logging.info(f"logging config completed using log file '{logfile}' .")

    # 主线程永远在后台运行下去
    while True:
        logging.info(f"npts-daemon is running .")
        time.sleep(11)
