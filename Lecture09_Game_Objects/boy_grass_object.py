
from pico2d import *

import random
# Game object class here
class Grass:
    # 생성자를 이용해 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
    pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,400), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:

    def __init__(self):
        self.x1, self.y1 = random.randint(0,800), 599
        self.x2, self.y2 = random.randint(0,800), 599
        self.image1 = load_image('ball21x21.png')
        self.image2 = load_image('ball41x41.png')

    def update(self):
        if self.y1<=30:
            self.y1 = 30
        else:
            self.y1 -= random.randint(0, 10)
        if self.y2<=30:
            self.y2 = 30
        else:
            self.y2 -= random.randint(0,10)



    def draw(self):
        self.image1.draw(self.x1, self.y1)
        self.image2.draw(self.x2, self.y2)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()

    update_canvas()



def reset_world(): # 초기화하는 함수
    global running
    global grass
    global team
    global world
    global ball1
    global ball2

    running = True
    world = []

    grass = Grass() # Grass하는 클래스를 이용해서 grass라는 객체 생성
    world.append(grass)

    team = [ Boy() for i in range(11)] # 11명 소년의 팀 생성
    ball1 = [Ball() for i in range(9)]
    ball2 = [Ball() for i in range(9)]
    world += team
    world += ball1
    world += ball2


open_canvas()

# initialization code
reset_world()


# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
