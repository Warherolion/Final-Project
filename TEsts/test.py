"""
import pygame as pg



def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 60))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
"""

import os
import sys
import pygame as pg

import 


KEY_REPEAT_SETTING = (200,70)


class Control(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Input Box")
        self.screen = pg.display.set_mode((500,500))
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.input = TextBox((100,100,150,30),command=self.change_color,
                              clear_on_enter=True,inactive_on_enter=False)
        self.color = (100,100,100)
        self.prompt = self.make_prompt()
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

    def make_prompt(self):
        font = pg.font.SysFont("arial", 20)
        message = 'Please type a color name for background (ex. "red"):'
        rend = font.render(message, True, pg.Color("white"))
        return (rend, rend.get_rect(topleft=(10,35)))

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.input.get_event(event)

    def change_color(self,id,color):
        try:
            self.color = pg.Color(str(color))
        except ValueError:
            print("Please input a valid color name.")

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.input.update()
            self.screen.fill(self.color)
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()