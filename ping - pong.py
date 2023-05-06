from pygame import*

window = display.set_mode((900,700))
display.set_caption("Пінг-понг")
background = transform.scale(image.load("bg2.jpg"),(900,700))

class Player(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(100,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()# створити рамку навколо картинки  спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):# фнукція для того щоб намалювати спрайт на екрані
        window.blit(self.image,(self.rect.x, self.rect.y))

class Hero(Player):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 695:
            self.rect.y += self.speed
    def update_f(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 695:
            self.rect.y += self.speed

game = True
finish = False
clock = time.Clock()
FPS = 50
racket1 = Hero('',5,50,10)
racket2 = Hero('',880,50,10)
ball = ('',500,500,0)

speed_x = 10
speed_y = 10 
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit()
        racket1.update_r()
        racket2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide.rect()
        






display.update()
clock.tick(FPS)




