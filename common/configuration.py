class Configuration:
    def __init__(self, bullet_config):
        self.bullet = bullet_config


class BulletConfiguration:
    def __init__(
        self,
        align,
        background_color,
        background_color_on_switch,
        bullet,
        bullet_color,
        indent,
        margin,
        pad_right,
        shift,
        word_color,
        word_color_on_switch
    ):
        self.align = align
        self.background_color = background_color
        self.background_color_on_switch = background_color_on_switch
        self.bullet = bullet
        self.bullet_color = bullet_color
        self.indent = indent
        self.margin = margin
        self.pad_right = pad_right
        self.shift = shift
        self.word_color = word_color
        self.word_color_on_switch = word_color_on_switch