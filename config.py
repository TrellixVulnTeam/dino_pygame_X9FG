IMMORTAL = False

COLOR_SKY = (52, 183, 235)
COLOR_EARTH = (68, 207, 98)
SIZE_SKY = 0.7
SIZE_EARTH = 0.3

SPEED_CACTUS = 4
SPEED_BIRD = 4.5
SPEED_TORNADO = 6

DISTANCE_BETWEEN_ENEMY_MAX = 500

DINO_JUMP_SPEED = 17
DINO_JUMP_HEIGNT = 170
DINO_FALL_SPEED = 12

MAX_GAME_SPEED = 200
BROKE_ENEMY_SPEED = 10

TORNADO_SCORE_START = 40
BIRD_SCORE_START = 20

BONUS_CHANCE_SPAWN = 200
BONUS_DURATION = 5
BONUS_SPEED_BUST = 3
MIN_BONUS_FREQUENCY = 10

animate_sprites = {
    'bird.png': (7, 1),
    'tornado.png': (2, 1)
}

WARNING_RADIUS = 20

effects = {
    'wine.png': ["Опьянение", "speed_up", 3],
    'mushroom.png': ["Галлюцинация", "jump_speed_down", 0.2],
}