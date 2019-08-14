import pygame
pygame.init()
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Trex Game")
bg = pygame.image.load('mountains.png')
char = pygame.image.load('standing.png')
dino_pics = [ pygame.image.load('pics/0.png'),pygame.image.load('pics/1.png'), pygame.image.load('pics/2.png'), pygame.image.load('pics/3.png')]
print(char.get_height(),char.get_width())
print(dino_pics[0].get_width(),dino_pics[0].get_height())
dem = [0,0]
fire = pygame.image.load('fire_1.jpg')
class player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.isjump = False
        self.neg = 1
        self.hitbox = ((self.x + self.width //2+20), (self.y + self.height//2)+10, (self.width) //2-8 )

    def draw(self,win):
        self.hitbox = ((self.x + self.width //2+18), (self.y + self.height//2)+10, (self.width) //2 -15)
        #pygame.draw.circle(win,(0,255,0),(int(self.hitbox[0]),int(self.hitbox[1])),int(self.hitbox[2]))
        if gameover:
            win.blit(dino_pics[2],(self.x,self.y))
        elif self.isjump:
            win.blit(dino_pics[2],(self.x,self.y))
        else:
            win.blit(dino_pics[num%4],(self.x,self.y))

class obstacle(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = -10
        self.passed = False
    def draw(self,win):
        self.move()
        #pygame.draw.rect(win,(255,0,0),(self.x,self.y,self.height+100,self.width+100),2)
        win.blit(fire,(self.x,self.y))

    def move(self):
        if self.x + self.vel > -20:
            self.x += self.vel
        else:
            self.passed = True



run = True
clock = pygame.time.Clock()
dino = player(50,380,64,68)
stone = obstacle(200,400,30,40)
obstacles=[]
#obstacles.append(stone)

def draw_window(dem,stone):
    # if dem[0] <= -(bg.get_width()):
    #     dem[0] = 0
    # else:
    #     dem[0] -= 15
    # if dem[0] <= -(bg.get_width() - 480):
    #     win.blit(bg,(bg.get_width()+dem[0],-100))

    # win.blit(bg,(dem[0],-100))
    if stone.vel!=0:
        if(dem[0]<= -(bg.get_width())):
            #win.fill()
            dem[0] = 0

        elif dem[0] + stone.vel < -(bg.get_width()):
            dem[0] -= (dem[0] +bg.get_width())
        else:
            dem[0] += stone.vel
        
        if(dem[0] <= -(bg.get_width()-480)):
            win.blit(bg,(bg.get_width()+dem[0],-400))
        print(dem[0],bg.get_width())
    
    win.blit(bg,(dem[0],-400))
   
    dino.draw(win)
    for stone in obstacles:
        stone.draw(win)
    pygame.display.update()


count = 12.5
num = 0
gameover = False

while run:
    clock.tick(27)
    if num%50 == 0 and not gameover:
        stone = obstacle(500,370,30,40)
        obstacles.append(stone)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_SPACE]):
        dino.isjump = True
    if dino.hitbox[0] + dino.hitbox[2] > stone.x and dino.hitbox[0] - dino.hitbox[2] < stone.x + stone.height:
        if dino.hitbox[1] + dino.hitbox[2] > stone.y and dino.hitbox[1] - dino.hitbox[2] < stone.y + stone.width:
            stone.vel = 0
            dino.isjump = False
            count = 12.5
            gameover = True


    
    for stone in obstacles:
        if stone.passed:
            obstacles.pop(obstacles.index(stone))
    
    if dino.isjump:
        if count > 0:
            dino.y -= (count**2)*dino.neg*0.3
            count -= 2.5
        elif count == 0:
            dino.neg = -1
            count -= 2.5
        elif count >= -12.5:
            dino.y -= (count**2)*dino.neg*0.3
            count -= 2.5
        else:
            count = 12.5
            dino.neg = 1
            dino.isjump = False
        
        

    num += 1
    print(num)   
    draw_window(dem,stone)
    
    
    

pygame.quit()



