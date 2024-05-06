import pygame
from ai import agent
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("SMART AI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

class player:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.surf = pygame.Surface((25,25))
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x,self.y)
        self.color = (255,255,255)

    def keypress(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.y -= 5
        if key[pygame.K_DOWN]:
            self.y += 5
        if key[pygame.K_RIGHT]:
            self.x += 5
        if key[pygame.K_LEFT]:
            self.x -= 5

    def draw(self):
        self.rect.center = (self.x,self.y)
        self.surf.fill(self.color)
        screen.blit(self.surf,self.rect)

run = True
Player = player()
class fullai:
    def __init__(self):
        #Forms a tuple with The ai object, ai surface, and ai rect
        self.allai = []
        for i in range(0,3):
            ai = agent(0,0,1,Player,100)
            aisurf = pygame.Surface((25,25))
            airect = aisurf.get_rect()
            airect.center = (ai.x,ai.y)
            self.allai.append((ai,aisurf,airect))

    def draw(self):
        global run
        for i in self.allai:
            i[2].center = (i[0].x,i[0].y)
            i[0].checkinradius()
            i[1].fill((255,0,0))
            screen.blit(i[1],i[2])
            if Player.rect.colliderect(i[2]):
                run = False
Fullai = fullai()
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    screen.fill((0,0,0))
    Player.keypress()
    Fullai.draw()
    Player.draw()
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
pygame.quit()