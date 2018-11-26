import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")
walkRight = [pygame.image.load('right_stand.png'),pygame.image.load('right_walk1.png'), pygame.image.load('right_walk2.png')]
walkLeft = [pygame.image.load('left_stand.png'),pygame.image.load('left_walk1.png'), pygame.image.load('left_walk2.png')]
bg = pygame.image.load('bg.png')
walkDown = [pygame.image.load('down_stand.png'), pygame.image.load('down_walk1.png'), pygame.image.load('down_walk2.png')]
walkUp = [pygame.image.load('up_stand.png'), pygame.image.load('up_walk1.png'), pygame.image.load('up_walk2.png')]
char = pygame.image.load('down_stand.png')
clock = pygame.time.Clock()

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0
        self.up = False
        self.down = False

    def draw(self, win):
        #global walkCount
        #win.blit(bg, (0,0))

        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            win.blit(walkDown[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            win.blit(walkUp[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))

class Enemy():
    walkRight = [pygame.image.load('enemy_right_walk1.png'), pygame.image.load('enemy_right_walk2.png')]
    walkLeft = [pygame.image.load('enemy_left_walk1.png'), pygame.image.load('enemy_left_walk2.png'), pygame.image.load('enemy_left_walk1.png')]
    walkDown = [pygame.image.load('enemy_down_walk1.png'), pygame.image.load('enemy_down_walk2.png'), pygame.image.load('enemy_down_walk2.png')]
    walkUp = [pygame.image.load('enemy_up_walk1.png'), pygame.image.load('enemy_up_walk2.png')] 

    def __init__(self, x, y, width, height, xend, yend):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xend  = xend
        self.yend = yend
        self.path = [self.x, self.y, self.xend, self.yend]
        self.walkCount = 0
        self.vel = 3
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        

    def draw(self, win):

        if self.walkCount + 1 >= 6:
            self.walkCount = 0
        if self.right == True:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if self.up == True :
            win.blit(self.walkUp[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if self.left == True:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if self.down == True:
            win.blit(self.walkDown[self.walkCount// 3], (self.x, self.y))
            self.walkCount +=1

        pass
    #----Rewrote this segment for enemy movement path.     ----
    #----Enemy movement capped at self.path[#] based on    ----
    #----constructor.                                      ----
    #----Else statement helps changes the enemy direction  ----
    #----                 mD 11-26-18                      ----
    def enemyRight(self):
        if self.x < self.path[2]:
            self.x += self.vel
        else:
            self.right = False
            self.up = True
    def enemyUp(self):
        if self.y > self.path[3]:
            self.y -= self.vel
        else:
            self.up = False
            self.left = True
    def enemyLeft(self):
        if self.x > self.path[0]:
            self.x -= self.vel
        else:
            self.left = False
            self.down = True
    def enemyDown(self):
        if self.y < self.path[1]:
            self.y += self.vel
        else:
            self.down = False
            self.right = True



        # elif self.y < 0:
        #         if self.x < 400:
        #             self.left = True
        #             self.x -= self.vel
        #         else:
        #             self.left = False

            # else:
            #     if self.x - self.vel > self.path[0]:
            #         self.x += self.vel
            #     else: 
            #         self.vel = self.vel * -1
            #         self.walkCount = 0
            
#----win.blit:              background                     ----
#----goblin.draw:           enemy image                    ----
#----hero.draw:             hero image                     ----
#----pygame.display.update: refreshes screen               ----
def redrawGameWindow():
    win.blit(bg, (0,0))
    goblin.draw(win)
    hero.draw(win)
    pygame.display.update()
    

hero = Player(100,410, 64,64)
goblin = Enemy(100,400,64,64,300,300)
runMonster = True



    
#----mainloop                                              ----
run = True
#----trigger point to start the monster path               ----
#----set to false if you want to start with no monster     ----
#----                mD 11-26-18                           ----
goblin.right = True
while run == True:
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#----user input for hero movement                          ----
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and  hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False
        hero.down = False
        hero.up = False

    elif keys[pygame.K_RIGHT] and hero.x < 500 - hero.width - hero.vel:
        hero.x+= hero.vel
        hero.right = True
        hero.left = False
        hero.down = False
        hero.up = False

    elif keys[pygame.K_UP] and hero.y > hero.vel:
        hero.y -= hero.vel
        hero.right = False
        hero.left = False
        hero.down = False
        hero.up = True

    elif keys[pygame.K_DOWN] and hero.y < 500 - hero.height - hero.vel:
        hero.y += hero.vel
        hero.right = False
        hero.left = False
        hero.down = True
        hero.up = False

    else:
        hero.right = False
        hero.left = False
        hero.up = False
        hero.down = False
        hero.walkCount = 0
    #----enemy movement                                    ----
    #----shift enemy movement in hero while loop           ----
    #----            mD 11-26-18                           ----
    if goblin.right == True:
        goblin.enemyRight()      
    elif goblin.left == True:
        goblin.enemyLeft()
    elif goblin.up ==  True:
        goblin.enemyUp()
    elif goblin.down == True:
        goblin.enemyDown()
    else:
        goblin.down = False
        goblin.up = False
        goblin.left = False
        goblin.right = False
        runMonster = False
    #----telling program to update all the images          ----
    redrawGameWindow()

    # if hero.isJump == False:
    #     # not used for platforms
    #     if keys[pygame.K_UP] and hero.y > hero.vel:
    #         hero.y -= hero.vel

    #     if keys[pygame.K_DOWN] and hero.y < 500 - hero.height - vel:
    #         hero.y += hero.vel
        # if keys[pygame.K_SPACE]:
        #     hero.isJump = True
        #     hero.right = False
        #     hero.left = False
        #     hero.walkCount = 0
    # else:
    #     if hero.jumpCount >= -10:
    #         neg = 1
    #         if hero.jumpCount < 0:
    #             neg = -1
    #         hero.y -= (hero.jumpCount ** 2) * 0.5 * neg
    #         jumpCount -= 1
    #     else:
    #         hero.isJump = False
    #         hero.jumpCount = 10    




# runMonster = True
# while runMonster == True:
#     if goblin.right == True:
#         goblin.move()

#     elif goblin.left == True:
#         goblin.enemyLeft()
#     elif goblin.up ==  True:
#         goblin.enemyUp()
#     elif goblin.down == True:
#         goblin.enemyDown()
#     else:
#         goblin.down = False
#         goblin.up = False
#         goblin.left = False
#         goblin.right = False

        

pygame.quit()
