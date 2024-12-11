import os
add_library('minim')
import random
RESX=1000
RESY=1000
player=Minim(this)

PATH=os.getcwd()
volume=0.5 #initialise volume
#Images
momduck=loadImage(PATH+'/images/duck/MomDuck.png')
duckback=loadImage(PATH+'/images/duck/DuckBackward.png')
duckforward=loadImage(PATH+'/images/duck/DuckForward.png')
duckside=loadImage(PATH+'/images/duck/DuckSide.png')
duckbackeat=loadImage(PATH+'/images/duck/EatBack.png')
duckfronteat=loadImage(PATH+'/images/duck/EatFront.png')
ducksideeat=loadImage(PATH+'/images/duck/EatSide.png')
duckswimfly=loadImage(PATH+'/images/duck/SwimFly.png')
duckfly=loadImage(PATH+'/images/duck/Fly.png')
water=loadImage(PATH+'/images/WaterParralax.png')
berry1=loadImage(PATH+'/images/food/berry1.png')
berry2=loadImage(PATH+'/images/food/berry2.png')
croc=loadImage(PATH+'/images/predator/crocoswim.png')
cat1=loadImage(PATH+'/images/predator/cat1.png')
cat3=loadImage(PATH+'/images/predator/cat3.png')
cat2=loadImage(PATH+'/images/predator/cat2.png')
land=loadImage(PATH+'/images/Land.png')
plant1=loadImage(PATH+'/images/Obstacle/plant1.png')
plant2=loadImage(PATH+'/images/Obstacle/plant2.png')
plant3=loadImage(PATH+'/images/Obstacle/plant3.png')
stamina=loadImage(PATH+'/images/StaminaBar.png')
gameover=loadImage(PATH+'/images/GameOver.PNG')
home=loadImage(PATH+'/images/MomHome.PNG')
bgimage=loadImage(PATH+'/images/StartScreen/Bg.PNG')
settingsb=loadImage(PATH+'/images/StartScreen/Settings.PNG')
levels=loadImage(PATH+'/images/StartScreen/Levels.PNG')
start=loadImage(PATH+'/images/StartScreen/Start.PNG')
tutorial=loadImage(PATH+'/images/StartScreen/Tutorial.PNG')
levelsbg=loadImage(PATH+'/images/StartScreen/LevelsPg.PNG')
complete=loadImage(PATH+'/images/StartScreen/LevelCleared.PNG')
tutorialscreen=loadImage(PATH+'/images/StartScreen/TutorialBG.PNG')
soundset=loadImage(PATH+'/images/StartScreen/Soundbg.PNG')
audiobar=loadImage(PATH+'/images/StartScreen/bar.png')
class game:
    def __init__(self):
        
        self.length=280*7
        self.duck=duck(duckforward,112,136,500,900,5,10,10,11) 

        self.mamay=-self.length 
        self.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(7)]+[landstrips(water,RESY-280*(j+1)) for j in range(6)]
        
        self.slice=0
        
        #Screens
        self.start=True
        self.levelscreen=False
        self.tutorial=False
        self.setting=False
        
         # Load background music and sound effects
        self.bg_music = player.loadFile(PATH + "/sounds/bgm2.mp3")
        self.startmusic=player.loadFile(PATH + "/sounds/bgm1.mp3")
        self.winsound=player.loadFile(PATH + "/sounds/win.mp3")
        self.losesound=player.loadFile(PATH + "/sounds/lose.mp3")
        self.eat=player.loadFile(PATH + "/sounds/eat.mp3")
        self.bg_music.setGain(volume)
        self.startmusic.setGain(volume)
        self.losesound.setGain(volume) 
        self.winsound.setGain(volume) 
        self.eat.setGain(volume)
        self.bg_music.loop()
    def display(self):
        image(home,0,self.mamay-40,RESX,RESY/2) #final house img
        if self.start:
            self.startscreen()
            
        elif self.levelscreen:
            image(levelsbg,0,0,RESX,RESY,370,0,1350,980)
            fill(0) 
            textAlign(CENTER)
            textSize(50)
            text('Use SHIFT key to go back to start screen',RESX/2,RESY-50)
        elif self.tutorial:
            image(tutorialscreen,0,0,RESX,RESY)
            fill(0) 
            textAlign(CENTER)
            textSize(30)
            text('Use SHIFT key to go back to start screen',RESX/2,50)   
        elif self.setting:
            image(soundset,0,0,RESX,RESY) 
            image(audiobar,RESX/2-275,RESY/2-40,500,80,int((volume//0.25))*217,0,int(((volume/0.25)+1))*217,77)
            textSize(30)
            fill(0) 
            textAlign(CENTER)
            text('Use LEFT and RIGHT arrow keys to adjust volume',RESX/2,RESY*2/5)
            text('Use SHIFT key to go back to start screen',RESX/2,RESY*3/5)
        elif self.duck.distance==self.length: #win condition
            
            self.duck.alive=False
            image(complete,0,0,RESX,RESY,347,0,1488,1141)
            textSize(50)
            fill(255,255,255)
            textAlign(CENTER)
            self.winsound.play()
            self.winsound.rewind() 
            if frameCount%20 in [0,1,2,3,4,5]:
                text("SHIFT to Start Screen", RESX / 2, RESY -50)
            self.winsound.play() #winning jingle
            self.winsound.rewind()
        elif self.duck.alive:
            #move static elements up and down the screen when duck is moving
            if self.duck.y<RESY/2 and self.duck.distance<self.length-RESY/2+140:
                self.duck.y+=10
                self.mamay+=10
                for i in self.landstrips:
                    i.y+=10
                    i.predator.y+=10
                    for j in i.food:
                        j.y+=10
                    for x in i.obstacles:
                        x.y+=10
                    # i.obstacle.y+=10
            if self.duck.y>RESY/2 and self.duck.distance>RESY/2-140:
                self.duck.y-=10
                self.mamay-=10
                for i in self.landstrips:
                    i.y-=10
                    i.predator.y-=10
                    for j in i.food:
                        j.y-=10
                    for x in i.obstacles:
                        x.y-=10
                
                                                                 
                
                    
            self.collisions()
            for i in self.landstrips:
                i.display()#display all landstrips(water and land)
                                                   
            self.duck.display()#display duck
            if frameCount%15==0:
                self.slice=(self.slice+1)%20
            print(self.mamay,self.duck.y)
            
            image(momduck,RESX/2,self.mamay,168,205,276, 0, 0, 310)#show mother duck
            image(stamina,10,10,400,67,0,(19-(self.duck.stamina//52))*98,776,(20-(self.duck.stamina//52))*98)#display stamina bar
        else:
            #gameover screen
            image(gameover,0,0,RESX,RESY)
            textSize(50)
            fill(0) 
            textAlign(CENTER) 
            if frameCount%20 in [0,1,2,3,4,5]:
                text("SHIFT TO START SCREEN", RESX / 2, RESY / 2)
    
    def startscreen(self):
          #display startscreen with buttons
          image(bgimage,0,0,RESX,RESY,99,0,466,367)
          
          image(levels,RESX*2/3,RESY*2/3-100,220,170)
          image(tutorial,RESX*2/3,RESY*2/3,220,170)
          image(settingsb,RESX*2/3,RESY*2/3+100,220,170)
            
    def collisions(self):
        #collisons with food, predators and obstacles
        for i in self.landstrips[len(self.landstrips)//2:]:
            if abs(i.y-self.duck.y)<i.img_h/2 and i.img==water:
                self.duck.swim=True
                break
            else:
                self.duck.swim=False
            
        for i in self.landstrips:
            if self.duck.collision(i.predator) and not self.duck.fly:
                self.duck.alive=False
                
                self.losesound.play()
                self.losesound.rewind()
            for j in i.food:
                if self.duck.collision(j):
                    self.duck.eat()
                    
                    self.eat.play()#eating sound
                    self.eat.rewind()
                    
                    i.food=[]
            for x in i.obstacles:
                if 0<(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w and abs(self.duck.y+self.duck.img_h-x.y-x.img_h)<x.img_h/2:
                    self.duck.key_handler[LEFT]=False
                if 0<-(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w/2 and abs(self.duck.y+self.duck.img_h-x.y-x.img_h)<x.img_h/2:
                    self.duck.key_handler[RIGHT]=False
                if 0<-(self.duck.y+self.duck.img_h-x.y-x.img_h)<x.img_h and (0<(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w or 0<-(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w/2):
                    self.duck.key_handler[DOWN]=False
                if 0<(self.duck.y+self.duck.img_h-x.y-x.img_h)<x.img_h and (0<(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w or 0<-(self.duck.x+self.duck.img_w-x.x-x.img_w)<x.img_w/2):
                    self.duck.key_handler[UP]=False
                if i.predator.y==x.y and 0<x.x-i.predator.x<x.img_w:
                    i.predator.v=-i.predator.v
                    
                    
                    
            
class animal:
    def __init__(self,img,w,h,x,y,v,rh,rw,num_slices):
        self.img=img
        self.img_w = w
        self.img_h = h
        self.x=x
        self.y=y
        self.realw=rw
        self.realh=rh
        self.v=v #velocity
        self.dir='forward'
        self.slice=0
        self.num_slices=num_slices
    def move(self):
        if self.x <-self.img_w or self.x>RESX-self.v: #prevent animals from leaving screen
            self.v=-self.v
        self.x=self.x+self.v
        if frameCount%5 == 0:
            self.slice = (self.slice + 1) % self.num_slices
        
    def display(self):
        self.move()
        #animals turn around when they reach the border
        if self.v>0:
            image(self.img, self.x , self.y, self.img_w, self.img_h, (self.slice + 1) * self.realw, 0, self.slice * self.realw, self.realh)        
        else:
            
            image(self.img, self.x, self.y , self.img_w, self.img_h, (self.slice) * self.realw, 0, (self.slice+1) * self.realw, self.realh)        
            
        
class duck(animal): #inherits from animal class
    def __init__(self,img,w,h,x,y,v,rw,rh,num_slices):
        animal.__init__(self,img,w,h,x,y,v,rw,rh,num_slices)
        self.fly=False
        self.alive=True
        self.key_handler = {LEFT:False, RIGHT:False, UP:False, DOWN: False, ' ':False}
        self.stamina=1000
        self.flytime=0
        self.maxflytime=600000
        self.distance=0
        self.swim=False
    

    def move(self):
        #keyboard inputs and movement
        if self.alive:
            if self.key_handler[LEFT] and self.x>0:
                self.dir='left'
                self.x-=10
                if self.stamina>0:
                    self.stamina-=1
            elif self.key_handler[RIGHT] and self.x<RESX-self.img_w:
                self.dir='right'
                self.x+=10
                if self.stamina>0:
                    self.stamina-=1
                
            elif self.key_handler[UP] and self.y>0:
                self.dir='forward'
                self.y-=10
                self.distance+=10
                if self.stamina>0:
                    self.stamina-=1
            elif self.key_handler[DOWN] and self.y<RESY-self.img_h/2:
                self.dir='back'
                self.y+=10
                self.distance-=10
                if self.stamina>0:
                    self.stamina-=1
            if self.key_handler[' '] and self.stamina>=5:
                self.fly=True
                self.stamina-=5   #Flying uses 3 stamina
            else:
                self.fly=False
            if frameCount%10 == 0:
                self.slice = (self.slice + 1) % self.num_slices
            
    def collision(self,other):
        if abs(self.x+self.img_w-other.x-other.img_w)<max(other.img_w,self.img_w)/2 and abs(self.y+self.img_h-other.y-other.img_h)<max(other.img_h,self.img_h)/2:   #This will be used for collisons with obstacles, food and predators
            return True
        return False
    def eat(self):
    
        self.stamina+=100
        if self.stamina>1000:
            self.stamina=1000
         
    def display(self):
        self.move()
        print(self.stamina)
        
        #animaions   
        if self.fly:
            
            self.img=duckfly
            if frameCount%5 == 0 :
                
                self.slice = (self.slice + 1) % 5
        
            image(self.img, self.x - self.img_w//2*0.5, self.y, self.img_w*1.5, self.img_h, 0,self.slice * 595, 748,(self.slice + 1) * 595)
        elif self.swim:
            self.slice = (self.slice + 1) % 3
            self.img=duckswimfly
            image(self.img, self.x, self.y, self.img_w, self.img_h, self.slice * 274, 0, (self.slice + 1) * 274, 262)   
        elif self.dir == 'forward':
            self.img=duckforward
            image(self.img, self.x, self.y , self.img_w, self.img_h, self.slice * 278, 0, (self.slice + 1) * 278, 332)
        elif self.dir == 'back':
            self.img=duckback
            image(self.img, self.x, self.y, self.img_w, self.img_h, (self.slice + 1) * 276, 0, self.slice * 276, 332)        
        elif self.dir == 'right':
            self.img=duckside
            image(self.img, self.x, self.y, self.img_w, self.img_h, self.slice * 296, 0, (self.slice + 1) * 296, 332)        
        elif self.dir == 'left':
            self.img=duckside
            image(self.img, self.x, self.y , self.img_w, self.img_h, (self.slice + 1) * 296, 0, self.slice * 296, 332)        
            
        
        
class obstacle:
    def __init__(self,img,x,y,w,h):
        self.img=img
        self.x=x
        self.y=y
        self.img_w=w
        self.img_h=h
    def display(self):
        
                
        image(self.img,self.x,self.y,self.img_w,self.img_h)
        
class landstrips:
    def __init__(self,img,y):
        self.img=img
        self.x=0
        self.y=y
        self.food=[]
        self.obstacles=[]
        self.img_h=140
        self.slice=0
        #randomly generates predators, obstacles and berries
        if self.img==water:
            self.predator=animal(croc,200,125,random.randint(30,RESX-30),self.y,5,500,830,3)
        elif self.img==land:
            x=random.randint(1,3)
            if x==1:
                self.predator=animal(cat1,120,96,random.randint(60,RESX-60),self.y,5,32,39,9)
                
            elif x==2:
                self.predator=animal(cat2,120,96,random.randint(60,RESX-60),self.y,8,32,39,9)
            else:
                self.predator=animal(cat3,120,96,random.randint(60,RESX-60),self.y,7,32,39,9)
            y=random.randint(1,2)
            if y==1:
                self.food=[food(berry1,random.randint(30,RESX-120),self.y)] 
                
            elif y==2:
                self.food=[food(berry2,random.randint(30,RESX-120),self.y)]  
            else:
                self.food=[] 
            for h in range(0,2):
                z=random.randint(0,3)
                if z==1:
                    self.obstacles+=[obstacle(plant1,random.randint(h*RESX/2+30,RESX/2+h*RESX/2-30),self.y,64,98)]
                    if abs(self.obstacles[-1].x-self.predator.x)<50:
                        del self.obstacles[-1]
                elif z==2:
                    self.obstacles+=[obstacle(plant2,random.randint(h*RESX/2+30,RESX/2+h*RESX/2-30),self.y,66,76)]
                    if abs(self.obstacles[-1].x-self.predator.x)<50:
                        del self.obstacles[-1]
                elif z==3:
                    self.obstacles+=[obstacle(plant3,random.randint(h*RESX/2+30,RESX/2+h*RESX/2-30),self.y,64,92)]
                    if abs(self.obstacles[-1].x-self.predator.x)<50:
                        del self.obstacles[-1]
                else:
                    self.obstacles+=[] 
    def display(self):
        
        if frameCount%11==0:
            self.slice=(self.slice+1)%4
        if self.img==water:
            image(self.img,0,self.y,RESX, self.img_h, (self.slice + 1) * 700, 0, self.slice * 700, 606)
        else:
            image(self.img,0,self.y,RESX,self.img_h)
        self.predator.display()
        for i in self.food:
            i.display()
        for j in self.obstacles:
            j.display()

class food:
    def __init__(self,img,x,y):
        self.img=img
        self.x=x
        self.y=y
        self.slice=0
        self.img_w=75
        self.img_h=68
    def display(self):
        #fruit animation
        if frameCount%10 == 0:
                self.slice = (self.slice + 1) % 7
        image(self.img,self.x,self.y+10,75,68,(self.slice + 1) * 100, 0, self.slice * 100, 90)

game=game()
def setup():
    size(RESX,RESY)
def draw():
    background(255, 255, 255)
    game.display()
    
def keyPressed():
    global volume
    #keyboard controlled movements
    if game.duck.alive:
        if keyCode == LEFT:
            game.duck.key_handler[LEFT] = True
        elif keyCode == RIGHT:
            game.duck.key_handler[RIGHT] = True
        elif keyCode == UP:
            game.duck.key_handler[UP] = True
        elif keyCode == DOWN:
            game.duck.key_handler[DOWN] = True
        elif key == ' ':
            game.duck.key_handler[' '] = True
    if game.setting:
        #control volume with keyboard input
        if keyCode == RIGHT:
            print(keyCode)
            volume=min(1,volume+0.25)
            game.bg_music.setGain(volume)
            game.losesound.setGain(volume)
            game.winsound.setGain(volume)
            game.eat.setGain(volume)
            if volume==0:
                game.bg_music.pause()
                game.bg_music=player.loadFile(PATH + "/sounds/silence.mp3")
                game.losesound=player.loadFile(PATH + "/sounds/silence.mp3")
                game.winsound=player.loadFile(PATH + "/sounds/silence.mp3")
                game.eat=player.loadFile(PATH + "/sounds/silence.mp3")
                
                game.bg_music.loop()
            else:
                game.bg_music.pause()
                game.winsound=player.loadFile(PATH + "/sounds/win.mp3")
                game.losesound=player.loadFile(PATH + "/sounds/lose.mp3")
                game.eat=player.loadFile(PATH + "/sounds/eat.mp3")
                game.bg_music = player.loadFile(PATH + "/sounds/bgm2.mp3")
                
                game.bg_music.loop()
                
        elif keyCode == LEFT:
            print(keyCode)
            volume=max(0,volume-0.25)
            game.bg_music.setGain(volume)
            game.losesound.setGain(volume)
            game.winsound.setGain(volume)
            game.eat.setGain(volume)
            if volume==0:
                game.bg_music.pause()
                game.bg_music=player.loadFile(PATH + "/sounds/silence.mp3")
                game.losesound=player.loadFile(PATH + "/sounds/silence.mp3")
                game.winsound=player.loadFile(PATH + "/sounds/silence.mp3")
                game.eat=player.loadFile(PATH + "/sounds/silence.mp3")
                
                game.bg_music.loop()
            else:
                game.bg_music.pause()
                game.winsound=player.loadFile(PATH + "/sounds/win.mp3")
                game.losesound=player.loadFile(PATH + "/sounds/lose.mp3")
                game.eat=player.loadFile(PATH + "/sounds/eat.mp3")
                game.bg_music = player.loadFile(PATH + "/sounds/bgm2.mp3")
               
                game.bg_music.loop()
        
    if keyCode==SHIFT: #navigate through screens with shift key
        
        if game.tutorial:
            game.tutorial=False
            game.start=True
        elif game.setting:
            game.setting=False
            game.start=True
        elif game.levelscreen:
            game.levelscreen=False
            game.start=True
            
            
        if not game.duck.alive:
            game.start=True
    
    

def keyReleased():
    if game.duck.alive:
        if keyCode == LEFT:
            game.duck.key_handler[LEFT] = False
        elif keyCode == RIGHT:
            game.duck.key_handler[RIGHT] = False
        elif keyCode == UP:
            game.duck.key_handler[UP] = False
        elif keyCode == DOWN:
            game.duck.key_handler[DOWN] = False
        elif key == ' ':
            game.duck.key_handler[' '] = False
def mouseClicked():
    
    print(volume)
    print(game.bg_music.getVolume())
    #click on buttons from start screen
    if game.start:
        if RESX*2/3<mouseX<RESX*2/3+220 and RESY*2/3-100+50<mouseY<RESY*2/3-100+100:
            game.levelscreen=True
            game.start=False
            game.setting=False
            game.tutorial=False
            
            
        elif RESX*2/3<mouseX<RESX*2/3+220 and RESY*2/3+50<mouseY<RESY*2/3+100:
            game.tutorial=True
            game.start=False
            game.levelscreen=False
            game.setting=False
            
        elif RESX*2/3<mouseX<RESX*2/3+220 and RESY*2/3+100+50<mouseY<RESY*2/3+100+100:
            game.setting=True
            game.start=False
            game.levelscreen=False
            game.tutorial=False
    if game.levelscreen:
        #level selection with dynamic difficultys
        if 0.34*RESX<mouseX<0.65*RESX and RESY*0.27<mouseY<RESY*0.37:
            game.duck=duck(duckforward,112,136,RESX/2,RESY-150,5,10,10,11)
            game.length=280*7
            game.mamay=-game.length+RESY -280       
            game.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(7)]+[landstrips(water,RESY-280*(j+1)) for j in range(6)]
            game.landstrips[0].predator.x=-56789
            for i in range(10):
                game.landstrips[random.randint(0,12)].predator.x=-56789
            
                
            for i in game.landstrips[0].obstacles:
                i.x=456789
            game.start=False
            game.levelscreen=False

            
            
        elif 0.34*RESX<mouseX<0.65*RESX and RESY*0.4<mouseY<RESY*0.5:
            game.duck=duck(duckforward,112,136,RESX/2,RESY-150,5,10,10,11)
            game.length=280*10
            game.mamay=-game.length+RESY -280   
            game.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(10)]+[landstrips(water,RESY-280*(j+1)) for j in range(9)]
            game.landstrips[0].predator.x=-56789
            for i in range(10):
                game.landstrips[random.randint(0,18)].predator.x=-56789
            for i in game.landstrips[0].obstacles:
                i.x=456789
            game.start=False
            game.levelscreen=False
        elif 0.34*RESX<mouseX<0.65*RESX and RESY*0.53<mouseY<RESY*0.63:
            game.duck=duck(duckforward,112,136,RESX/2,RESY-150,5,10,10,11)
            game.length=280*17
            game.mamay=-game.length+RESY -280   
            game.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(17)]+[landstrips(water,RESY-280*(j+1)) for j in range(16)]
            game.landstrips[0].predator.x=-56789
            for i in range(3):
                game.landstrips[17+random.randint(0,16)].predator.x=-56789
            for i in game.landstrips[0].obstacles:
                i.x=456789
            game.start=False
            game.levelscreen=False
        elif 0.34*RESX<mouseX<0.65*RESX and RESY*0.67<mouseY<RESY*0.77:
            game.duck=duck(duckforward,112,136,RESX/2,RESY-150,5,10,10,11)
            game.length=280*22
            game.mamay=-game.length+RESY -280   
            game.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(22)]+[landstrips(water,RESY-280*(j+1)) for j in range(21)]
            game.landstrips[0].predator.x=-56789
            for i in game.landstrips[0].obstacles:
                i.x=456789
            game.start=False
            game.levelscreen=False
        elif 0.34*RESX<mouseX<0.65*RESX and RESY*0.79<mouseY<RESY*0.89:
            game.duck=duck(duckforward,112,136,RESX/2,RESY-150,5,10,10,11)
            game.length=280*32
            game.mamay=-game.length+RESY -280   
            game.landstrips=[landstrips(land,RESY-(140+280*i)) for i in range(32)]+[landstrips(water,RESY-280*(j+1)) for j in range(31)]
            game.landstrips[0].predator.x=-56789
            for i in game.landstrips[0].obstacles:
                i.x=456789
            game.start=False
            game.levelscreen=False
