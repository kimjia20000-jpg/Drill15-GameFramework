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
    # 아이템 창이 열려 있어도 게임은 계속 진행한다.
    play_mode.update()


def render():
    clear_canvas()

    # 게임 화면을 먼저 그린다.
    game_world.render()

    # 게임 화면 위에 아이템 선택 창을 그린다.
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

        if event.type == SDL_KEYDOWN:
            if event.key in (SDLK_0, SDLK_1, SDLK_2, SDLK_i):
                if getattr(event, 'repeat', 0):
                    continue

                if event.key == SDLK_0:
                    play_mode.boy.select_ball(0)

                elif event.key == SDLK_1:
                    play_mode.boy.select_ball(1)

                elif event.key == SDLK_2:
                    play_mode.boy.select_ball(2)

                # 숫자키로 선택하거나 I를 다시 누르면 창을 닫는다.
                game_framework.pop_mode()
                return

        # 이동과 발사 입력은 소년에게 전달한다.
        play_mode.boy.handle_event(event)