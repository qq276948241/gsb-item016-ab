#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一段时分秒收成总秒数。认字、判断、换算三步分开，各管各的。"""

import sys


单位表 = (
    ("时", 3600),
    ("分", 60),
    ("秒", 1),
)


def 认字(文):
    """把一段文字从左到右认成（数字, 单位）小段；认不出就返回 None。"""
    小段 = []
    位置 = 0
    while 位置 < len(文):
        数字起点 = 位置
        while 位置 < len(文) and "0" <= 文[位置] <= "9":
            位置 = 位置 + 1
        if 位置 == 数字起点 or 位置 >= len(文):
            return None
        单位 = 文[位置]
        if 单位 not in ("时", "分", "秒"):
            return None
        小段.append((int(文[数字起点:位置]), 单位))
        位置 = 位置 + 1
    return 小段


def 检查(小段):
    """决定过不过：至少一段，单位只按时、分、秒顺序出现且不重复。"""
    if not 小段:
        return False
    已见单位 = set()
    上次次序 = -1
    for 数值, 单位 in 小段:
        次序 = next((i for i, (名, 倍率) in enumerate(单位表) if 名 == 单位), -1)
        if 次序 <= 上次次序 or 单位 in 已见单位:
            return False
        已见单位.add(单位)
        上次次序 = 次序
    return True


def 换算(小段):
    """把认好的小段按时、分、秒加成总秒数。"""
    倍率表 = dict(单位表)
    return sum(数值 * 倍率表[单位] for 数值, 单位 in 小段)


def 主程序(参数):
    失败话 = "没法收秒：请给出一段时分秒，顺序不能乱，也不能重复\n"
    if len(参数) != 1 or 参数[0] == "":
        sys.stderr.write(失败话)
        return 2

    小段 = 认字(参数[0])
    if 小段 is None or not 检查(小段):
        sys.stderr.write(失败话)
        return 2

    sys.stdout.write(str(换算(小段)) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
