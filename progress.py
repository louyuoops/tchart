import math
import os
import sys
import time
import random
from character import Symbol
from color import Color
from rich.text import Text
from rich import print

class ProgressBar:
    symbol = Symbol.progress_bar
    color = Color()
    
    @classmethod
    def create(cls, data, size = 10, max_value=100, shape=None):
        output = Text()
        unit = max_value // size
        count = data // unit
        rest = 1 if data % unit > 0 else 0
        count += rest
        for i in range(size):
            if i <= count:
                if shape is None:
                    output.append("▇", style=cls.color(unit * i, max_value, theme="normal", theme_type=cls.color.COLOR_TYPE_PROGRESSBAR, index=i))
                else:
                    output.append(cls.symbol[shape], style=cls.color(unit * i, max_value, theme="normal", theme_type=cls.color.COLOR_TYPE_PROGRESSBAR, index=i))
            else:
                if shape is None:
                    output.append("▇", style=cls.color.PROGRESS_COLOR)
                else:
                    output.append(cls.symbol[shape], style=cls.color.PROGRESS_COLOR)
        output.append(" " + str(data) + "%")
        return output