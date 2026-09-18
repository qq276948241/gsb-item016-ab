#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一段时分秒收成总秒数。认字、换算、判定三段分开，各管各的。"""

import sys


单位表 = {"时": 60 * 60, "分": 60, "秒": 1}
单位次序 = {"时": 1, "分": 2, "秒": 3}
失败话 = "没法收秒：请给出一段时分秒，顺序不能乱，也不能重复\n"
退出成功 = 0
退出失败 = 2


class 不认字(ValueError):
    """认字段看不懂原文时抛出。"""


def 认字(文):
    """把原文认成一串 (数字, 单位) 段。只认字，不判顺序，不算秒。"""
    if 文 == "":
        raise 不认字
    段 = []
    位置 = 0
    长度 = len(文)
    while 位置 < 长度:
        数字起点 = 位置
        while 位置 < 长度 and "0" <= 文[位置] <= "9":
            位置 = 位置 + 1
        if 位置 == 数字起点 or 位置 >= 长度:
            raise 不认字
        单位 = 文[位置]
        if 单位 not in 单位表:
            raise 不认字
        段.append((int(文[数字起点:位置]), 单位))
        位置 = 位置 + 1
    return 段


def 换算(段):
    """把认好的段加总成总秒数。"""
    总秒 = 0
    for 数值, 单位 in 段:
        总秒 = 总秒 + 数值 * 单位表[单位]
    return 总秒


def 判定(段):
    """单位必须按时、分、秒往前走，同一段不能出现两次。"""
    上次序 = 0
    for _, 单位 in 段:
        次序 = 单位次序[单位]
        if 次序 <= 上次序:
            return False
        上次序 = 次序
    return True


def 主程序(参数):
    if len(参数) != 1:
        sys.stderr.write(失败话)
        return 退出失败
    try:
        段 = 认字(参数[0])
    except 不认字:
        sys.stderr.write(失败话)
        return 退出失败
    if not 判定(段):
        sys.stderr.write(失败话)
        return 退出失败

    sys.stdout.write(str(换算(段)) + "\n")
    return 退出成功


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
