class Color:
    """
    color theme type
    """
    COLOR_TYPE_PROGRESSBAR = 0
    
    """
    default color
    """
    PROGRESS_COLOR = "#e6e6e6"
    
    
    theme_map = {
        COLOR_TYPE_PROGRESSBAR: "normal",
    }

    theme = {
        "normal": ["#00b300", " #00cc00", "#00e600", "#d4ff80", "#ffff80", " #ffd633", "#ffd11a", "#ff9933", "#ff5c33", "#e62e00"]
    }
    
    def __cal(self, value, max_value):
        unit = max_value // 10
        for i in range(10, -1, -1):
            MAX = unit * i
            MIN = unit * (i - 1)
            if value > MAX and value - MAX < unit:
                return (-1, i)
            if value > MIN and value < MAX:
                return (i-1, i)
        # error
        return (-2, 0)
    
    def __progressBar(self, index):
        pass
    
    def __call__(self, value, max_value, theme=None, custom=None, theme_type=None, **kwargs):
        if theme is None:
            color_theme = self.theme['normal']
        else:
            color_theme = self.theme[theme]
        if custom is not None:
            color_theme = custom
        if theme_type is not None and theme is not None:
            color_theme = self.theme[theme]
            return color_theme[kwargs["index"] // 2]
        ret = self.__cal(value, max_value)
        if ret[0] >= -1:
            return color_theme[ret[1] - 1]
        return None