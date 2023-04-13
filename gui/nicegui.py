# -*- coding: utf-8 -*-
"""
# @Time: 2023/4/11 17:02
# @Author: supermap.lln
# @File: __init__.py.py
"""
from nicegui import ui

ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
result = ui.label()

ui.run()
