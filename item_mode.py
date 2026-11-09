from pico2d import *

import game_framework
import play_mode


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def pause():
    pass


def resume():
    pass


def update():
    # 아이템 창이 열려 있어도 게임은 계속 진행한다.
    play_mode.update()


def render():
    clear_canvas()

    # 진행 중인 게임 화면을 먼저 그린다.
    play_mode.game_world.render()

    # 게임 화면 위에 아이템 선택 이미지를 그린다.
    image.draw(
        get_canvas_width() // 2,
        get_canvas_height() // 2
    )

    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return