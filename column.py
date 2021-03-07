import math
import os
import sys
import time
import random
from character import Symbol
from color import Color
from rich.text import Text
from rich import print

class ColumnChart:
    color = Color()
    
    @classmethod
    def create(cls, data, width, height, max_value=100, shape=None):
        output = Text()
        result = ""
        if len(data) < width:
            data.extend([0] * (width - len(data)))
        if len(data) > width:
            data = data[:width]
        unit = max_value // height
        for row in range(height, 0, -1):
            row_ret = Text()
            for col in range(width):
                # check the value size whether between (row-1)*unit and row*unit
                value = data[col]
                if value > row * unit:
                    if shape is None:
                        row_ret.append('▋', style=cls.color(value, max_value))
                    else:
                        row_ret.append(cls.symbol[shape])
                else:
                    row_ret.append(' ')
            output.append(row_ret.append('\n'))
        return output