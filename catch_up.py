from pygame import *
from random import choice
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size = (65, 65)):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speedx = player_speed
        self.speedy = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))   
    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speedy
        if keys[K_DOWN] and self.rect.y  < 320:
            self.rect.y += self.speedy
        
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speedy
        if keys[K_s] and self.rect.y < 320:
            self.rect.y += self.speedy

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speedx, player_speedy):
        super().__init__(player_image, player_x, player_y, player_speedx, player_speedy)
        self.direction = 'left'
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y >= 420 or self.rect.y <= 5:
            self.speedy *= -1
        
        
        
    
        
        
window = display.set_mode((700, 500))

display.set_caption('Ping-Pong')
ground = transform.scale(image.load('fon_blue.webp'), (700, 500))

player1 = Player('raketka.png', 45, 250, 10, (100, 180))
player2 = Player('raketka.png', 550, 250, 10, (100, 180))
ball = Ball("ball.png" , 315, 225,0, (80, 100))

finish = False
 
font.init()
font_1  = font.SysFont('Arial', 70)

clock = time.Clock()
FPS = 60

game = True
while game:
    window.blit(ground, (0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE and finish:
                finish = False
                ball.rect.x = 315
                ball.rect.y = 225
                ball.speedx = 0
                ball.speedy = 0
            if i.key == K_SPACE and finish == False:
                ball.speedx = choice([-4, 4])
                ball.speedy = choice([-4, 4])
        

    if finish == True:
        window.blit(winner_player, (65, 200))
        

    if finish != True:

        if player1.rect.colliderect(ball.rect):
            ball.speedx *= -1
        if player2.rect.colliderect(ball.rect):
            ball.speedx *= -1
        if ball.rect.x <= 0 :
            finish =True
            winner_player = font_1.render('☺Выиграл игрок 1!♣', True, (219, 112, 147)) 
        if ball.rect.right >= 700:
            finish = True
            winner_player = font_1.render('♣Выиграл игрок 2!♥', True, (219, 112, 147))

        player1.update_l()
        player2.update_r()
        ball.update()
        player1.reset() 
        player2.reset()
        ball.reset()

    
    
    
    
    
    
    clock.tick(FPS)
    display.update()



#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»