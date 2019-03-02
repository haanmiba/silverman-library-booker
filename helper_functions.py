import os
import re
import yaml
from bullet import colors
from common.bullet.defaults import BulletDefaults
from common.bullet.strings import BulletStrings
from common.client.study_room import StudyRoom
from common.configuration import BulletConfiguration, Configuration 
from common.ini.strings import INIStrings
from common.yaml.strings import YAMLStrings
from bullet import colors
from configparser import ConfigParser
from datetime import datetime
from common.paths import Path


def lookup_bullet_color(ini_color_value):
    ini_color_value = ini_color_value.lower()
    color = ini_color_value.split('.')[-1]
    
    lookup_color = colors.foreground[BulletStrings.Colors.DEFAULT]
    if BulletStrings.Colors.FOREGROUND in ini_color_value:
        lookup_color = colors.foreground[color]
    elif BulletStrings.Colors.BACKGROUND in ini_color_value:
        lookup_color = colors.background[color]
    elif BulletStrings.Colors.REVERSE in ini_color_value:
        lookup_color = colors.REVERSE
    elif BulletStrings.Colors.RESET_REVERSE in ini_color_value:
        lookup_color = colors.RESET_REVERSE
    elif BulletStrings.Colors.RESET in ini_color_value:
        lookup_color = colors.RESET
    
    for _ in range(ini_color_value.count(BulletStrings.Colors.BRIGHT)):
        lookup_color = colors.bright(lookup_color)
    
    return lookup_color


def create_bullet_config(bullet_config_dict):
    for key in [
        INIStrings.Keys.Bullet.ALIGN,
        INIStrings.Keys.Bullet.INDENT,
        INIStrings.Keys.Bullet.MARGIN,
        INIStrings.Keys.Bullet.PAD_RIGHT,
        INIStrings.Keys.Bullet.SHIFT
    ]:
        if key in bullet_config_dict:
            bullet_config_dict[key] = int(bullet_config_dict[key])
    
    for key in [
        INIStrings.Keys.Bullet.BACKGROUND_COLOR,
        INIStrings.Keys.Bullet.BACKGROUND_COLOR_ON_SWITCH,
        INIStrings.Keys.Bullet.BULLET_COLOR,
        INIStrings.Keys.Bullet.WORD_COLOR,
        INIStrings.Keys.Bullet.WORD_COLOR_ON_SWITCH
    ]:
        if key in bullet_config_dict:
            bullet_config_dict[key] = lookup_bullet_color(bullet_config_dict[key])

    return BulletConfiguration(
        align=bullet_config_dict.get(INIStrings.Keys.Bullet.ALIGN, BulletDefaults.Bullet.ALIGN),
        background_color=bullet_config_dict.get(INIStrings.Keys.Bullet.BACKGROUND_COLOR, BulletDefaults.Bullet.BACKGROUND_COLOR),
        background_color_on_switch=bullet_config_dict.get(INIStrings.Keys.Bullet.BACKGROUND_COLOR_ON_SWITCH, BulletDefaults.Bullet.BACKGROUND_COLOR_ON_SWITCH),
        bullet=bullet_config_dict.get(INIStrings.Keys.Bullet.BULLET, BulletDefaults.Bullet.BULLET),
        bullet_color=bullet_config_dict.get(INIStrings.Keys.Bullet.BULLET_COLOR, BulletDefaults.Bullet.BULLET_COLOR),
        indent=bullet_config_dict.get(INIStrings.Keys.Bullet.INDENT, BulletDefaults.Bullet.INDENT),
        margin=bullet_config_dict.get(INIStrings.Keys.Bullet.MARGIN, BulletDefaults.Bullet.MARGIN),
        pad_right=bullet_config_dict.get(INIStrings.Keys.Bullet.PAD_RIGHT, BulletDefaults.Bullet.PAD_RIGHT),
        shift=bullet_config_dict.get(INIStrings.Keys.Bullet.SHIFT, BulletDefaults.Bullet.SHIFT),
        word_color=bullet_config_dict.get(INIStrings.Keys.Bullet.WORD_COLOR, BulletDefaults.Bullet.WORD_COLOR),
        word_color_on_switch=bullet_config_dict.get(INIStrings.Keys.Bullet.WORD_COLOR_ON_SWITCH, BulletDefaults.Bullet.WORD_COLOR_ON_SWITCH)
    )


def parse_settings_ini(settings_ini_path=Path.CURRENT_DIRECTORY + '/settings.ini'):
    config = ConfigParser()
    config.optionxform = str
    config.read(settings_ini_path)
    bullet_config = create_bullet_config({key: config[INIStrings.Sections.BULLET][key] for key in config[INIStrings.Sections.BULLET]})
    return Configuration(bullet_config=bullet_config)

def get_study_rooms(study_rooms_yaml_path=Path.CURRENT_DIRECTORY + '/study_rooms.yml'):
    with open(study_rooms_yaml_path) as study_rooms_file:
        return [StudyRoom(room[YAMLStrings.ROOM_NUMBER], room[YAMLStrings.CAPACITY]) for room in yaml.load(study_rooms_file)]

def format_room_title(time_string, date_string, room_number, time_parse_template='%I%p', date_parse_template='%m/%d/%Y'):
    time_string = re.sub(r'[ +\.]', '', time_string)
    date_string = re.sub(r' +', '', date_string)
    time = datetime.strptime(time_string, time_parse_template)
    date = datetime.strptime(date_string, date_parse_template)

    time_format = '%-I:%M%p'
    date_format = '%A, %B %d, %Y'
    formatted_time = time.strftime(time_format).lower()
    formatted_date = date.strftime(date_format)

    if int(room_number) < 10:
        room_number = '0' + str(room_number)
    
    formatted_room_title_template = '{formatted_time} {formatted_date} - Room {room_number}'
    return formatted_room_title_template.format(formatted_time=formatted_time, formatted_date=formatted_date, room_number=room_number)