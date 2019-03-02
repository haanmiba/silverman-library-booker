import click
import helper_functions as hf
from bullet import Bullet
from common.prompts import Prompt 

@click.command('silverman-booker')
def main():
    click.echo(Prompt.WELCOME)
    config = hf.parse_settings_ini()
    study_rooms = hf.get_study_rooms()

    running = True
    while running:
        study_room_choice = Bullet(
            prompt=Prompt.CHOOSE_ROOM,
            choices=list(map(str, study_rooms)),
            bullet=config.bullet.bullet,
            bullet_color=config.bullet.bullet_color,
            word_color=config.bullet.word_color,
            word_on_switch=config.bullet.word_color_on_switch,
            background_color=config.bullet.background_color,
            background_on_switch=config.bullet.background_color_on_switch,
            pad_right=config.bullet.pad_right,
            indent=config.bullet.indent,
            align=config.bullet.align,
            margin=config.bullet.margin,
            shift=config.bullet.shift
        )
        study_room_choice.launch()
        running = click.confirm(Prompt.CONTINUE)
    click.echo(Prompt.GOODBYE)

if __name__ == '__main__':
    main()