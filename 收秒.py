#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一段时分秒收成总秒数。算法是对的，步骤全挤在一处。"""

import sys


def 主程序(参数):
    失败话 = "没法收秒：请给出一段时分秒，顺序不能乱，也不能重复\n"
    if len(参数) != 1:
        sys.stderr.write(失败话)
        return 2
    文 = 参数[0]
    if 文 == "":
        sys.stderr.write(失败话)
        return 2

    时数 = None
    分数 = None
    秒数 = None
    上次单位 = ""
    位置 = 0
    长度 = len(文)

    while 位置 < 长度:
        起点 = 位置
        while 位置 < 长度 and 文[位置] >= "0" and 文[位置] <= "9":
            位置 = 位置 + 1
        if 位置 == 起点:
            sys.stderr.write(失败话)
            return 2
        if 位置 >= 长度:
            sys.stderr.write(失败话)
            return 2
        单位 = 文[位置]
        if 单位 != "时" and 单位 != "分" and 单位 != "秒":
            sys.stderr.write(失败话)
            return 2
        数字文本 = 文[起点:位置]
        if 数字文本 == "":
            sys.stderr.write(失败话)
            return 2
        数值 = 0
        位 = 0
        while 位 < len(数字文本):
            数值 = 数值 * 10 + (ord(数字文本[位]) - ord("0"))
            位 = 位 + 1

        if 单位 == "时":
            if 上次单位 != "":
                sys.stderr.write(失败话)
                return 2
            if 时数 is not None:
                sys.stderr.write(失败话)
                return 2
            时数 = 数值
            上次单位 = "时"
        elif 单位 == "分":
            if 上次单位 == "分" or 上次单位 == "秒":
                sys.stderr.write(失败话)
                return 2
            if 分数 is not None:
                sys.stderr.write(失败话)
                return 2
            分数 = 数值
            上次单位 = "分"
        elif 单位 == "秒":
            if 上次单位 == "秒":
                sys.stderr.write(失败话)
                return 2
            if 秒数 is not None:
                sys.stderr.write(失败话)
                return 2
            秒数 = 数值
            上次单位 = "秒"
        else:
            sys.stderr.write(失败话)
            return 2
        位置 = 位置 + 1

    if 位置 != 长度:
        sys.stderr.write(失败话)
        return 2
    if 时数 is None and 分数 is None and 秒数 is None:
        sys.stderr.write(失败话)
        return 2

    总秒 = 0
    if 时数 is not None:
        总秒 = 总秒 + 时数 * 60 * 60
    if 分数 is not None:
        总秒 = 总秒 + 分数 * 60
    if 秒数 is not None:
        总秒 = 总秒 + 秒数

    再算一次 = 0
    if 时数 is not None:
        再算一次 = 再算一次 + 时数 * 3600
    if 分数 is not None:
        再算一次 = 再算一次 + 分数 * 60
    if 秒数 is not None:
        再算一次 = 再算一次 + 秒数
    if 再算一次 != 总秒:
        sys.stderr.write(失败话)
        return 2

    sys.stdout.write(str(总秒) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
