from pico2d import *
import random

# Game object class here
class Grass:
    #생성자 함수 초기화
    def __init__(self): #객체의 속성을 정의하고 초기값을 알려주는 역할 -> python의 constructor
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100,700)
        self.frame = random.randint(0,8)

    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,90)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x +=5
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    global world #모든 객체들을 갖고 있는 list

    running = True
    world = [] #객체가 하나도 없는 월드

    #땅을 만들고 월드에 추가
    grass = Grass()
    world.append(grass)
    #소년 11명을 만들고 월드에 추가
    team = [Boy() for _ in range(11)]
    world += team

    pass

#객체들의 상호작용을 simulation
def update_world():
    for game_object in world:
        game_object.update()

    pass

def render_world():
    #월드에 객체들을 그린다
    clear_canvas()
    for game_object in world:
        game_object.draw()

    update_canvas()
    pass

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
