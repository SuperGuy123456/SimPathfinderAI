import time,math
from random import randint
class agent:
    def __init__(self,x,y,speed,target,view):
        self.x = x
        self.y = y
        self.speed = speed
        self.target = target
        self.target_last_pos = (0,0)
        self.view = view
        self.mode = 0
        self.lost = False
        self.stime = time.time()
        self.findnewspot = True

    def checkinradius(self):
        #pygame.draw.circle(screen,(150,150,150),(self.x,self.y),self.view)
        #pygame.draw.line(screen,(0,0,155),(self.x,self.y),self.target_last_pos)
        if self.mode == 0:
            self.search()
        if self.mode == 1:
            self.lost = False
            self.update()

    def chooserandom(self):
        self.target_last_pos = (randint(int(self.x-self.view),int(self.x+self.view)),
                                randint(int(self.y-self.view),int(self.y+self.view)))
        self.findnewspot = False
        self.patrol()

    def gotospot(self):
        target_x = self.target_last_pos[0]
        target_y = self.target_last_pos[1]
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            ratio = self.speed / distance
            self.x += dx * ratio
            self.y += dy * ratio

    def gotospottimer(self):
        if time.time()-self.stime >= 2:
            self.stime = time.time()
            self.findnewspot = True

    def patrol(self):
        self.gotospot()
        self.gotospottimer()

    def search(self):
        if self.lost != True:
            target_x = self.target_last_pos[0]
            target_y = self.target_last_pos[1]

            dx = target_x - self.x
            dy = target_y - self.y

            distance = math.sqrt(dx**2 + dy**2)

            if distance > 0:
                ratio = self.speed / distance
                self.x += dx * ratio
                self.y += dy * ratio
        else:
            if self.findnewspot:
                self.chooserandom()
            else:
                self.patrol()

        if abs(self.x - self.target_last_pos[0]) <= 2 and abs(self.y - self.target_last_pos[1]) <= 2:
            #print("lost")
            self.lost = True
        if abs(self.x - self.target.x) <= self.view and abs(self.y - self.target.y) <= self.view:
            self.mode = 1

    def checkifstillvis(self):
        if abs(self.x - self.target.x) <= self.view and abs(self.y - self.target.y) <= self.view:
            self.target_last_pos = (self.target.x,self.target.y)
            self.mode = 0
            

    def update(self):
        self.checkifstillvis()
        target_x = self.target.x
        target_y = self.target.y

        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            ratio = self.speed / distance
            self.x += dx * ratio
            self.y += dy * ratio