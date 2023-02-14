# -*- coding: utf-8 -*-
"""
# @Time: 2023/1/4 11:10
# @Author: supermap.lln
# @File: Rain.py
"""
import random

import pygame

# 初始化参数设计
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
# 文字间隔，调整代码雨的疏密
font_px = 18

# 创建窗口
pygame.init()
winsur = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 文字大小
font = pygame.font.SysFont('', 28)
bg_suface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 28))
winsur.fill((0, 0, 0))
# 文本内容
letter = '1234567890!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
texts = [font.render(letter[i], True, (0, 255, 0)) for i in range(44)]

# 显示设计 计算可以放几列
column = int(WINDOW_WIDTH / font_px)
drops = [0 for i in range(column)]
# 不让一闪而过
while True:
    # 从队列中获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[32]:
                exit()
    # 毫秒数 60 下落速度
    pygame.time.delay(60)

    # 重新编辑图像第二个参数是坐上角坐标
    winsur.blit(bg_suface, (0, 0))
    for i in range(len(drops)):
        text = random.choice(texts)
        # 重排每个坐标点
        winsur.blit(text, (i * font_px, drops[i] * font_px))
        drops[i] += 1
        if drops[i] * 10 > WINDOW_HEIGHT or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()
