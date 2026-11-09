from pico2d import *

import game_framework
import game_world
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
    # 창이 열려 있어도 소년과 공은 계속 업데이트한다.
    play_mode.update()


def render():
    clear_canvas()

    game_world.render()

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

        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if getattr(event, 'repeat', 0):
                continue

            game_framework.pop_mode()
            return

        else:
            # 이동 및 발사 입력은 계속 처리한다.
            play_mode.boy.handle_event(event)