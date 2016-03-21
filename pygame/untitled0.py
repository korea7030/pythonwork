# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 23:39:51 2016

@author: Administrator
"""

import pygame, sys, random

skier_images = ["skier_down.png", "skier_right1.png", "skier_right2.png", "skier_left2.png", "skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
    def __init__(self):  # 스키선수 생성
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320,100]
        self.angle = 0
        
    def turn(self, direction):  # 스키선수 회전
        self.angle = self.angle+direction
        if self.angle < -2: 
            self.angle = -2
        if self.angle > 2: 
            self.angle=2
        
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6-abs(self.angle) * 2]
        return speed
    
    def move(self, speed):   # 스키선수 좌우 움직임
        self.rect.centerx = self.rect.centerx+speed[0]
        if self.rect.centerx < 20:
            self.rect.centerx = 20
        if self.rect.centerx > 620:
            self.rect.centerx = 620
    
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type): # 나무와 깃발 생성
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False
    def update(self):
        global speed
        self.rect.centery -= speed[1] # 배경을 위로 올림(내려갈때 같음)
        if self.rect.centery < -32: # 화면이 위로 올라갈 경우 장애물 삭제
            self.kill()
        

def create_map():  # 임의로 나무와 깃발이 채워진 화면 생성
    global obstacles
    locations = []
    for i in range(10):
        row = random.randint(0,9)
        col = random.randint(0,9)
        location = [col*64+20, row*64+20+640]
        
        if not (location in locations):
            locations.append(location)
            type =random.choice(["tree", "flag"])
            
            if type == "tree" :
                img = "skier_tree.png"
            elif type == "flag" :
                img = "skier_flag.png"
            
            obstacle = ObstacleClass(img,location,type)
            obstacles.add(obstacle)

def animate(): # 화면 재생성
    screen.fill([255,255,255])
    obstacles.draw(screen)
    screen.blit(skier.image, skier.rect)
    screen.blit(score_text, [10,10])
    pygame.display.flip()

## 게임준비 부분 
pygame.init()
screen = pygame.display.set_mode([640,640])
clock = pygame.time.Clock()
skier = SkierClass()
speed = [0,6]
obstacles = pygame.sprite.Group()
map_position = 0
points = 0
create_map()
font = pygame.font.Font(None, 50)

##

## 메인반복문 시작
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = skier.turn(-1)
            elif event.key == pygame.K_RIGHT:
                speed = skier.turn(1)
        
    skier.move(speed) ##  스키선수 움직이기
    
    map_position += speed[1] # 배경 움직이기 
    
    if map_position >= 640:
        create_map()
        map_position = 0
    
    hit = pygame.sprite.spritecollide(skier, obstacles, False)
    
    if hit: ## 나무와 깃발이 닿았는지
        if hit[0].type == "tree" and not hit[0].passed:
            points = points - 100
            skier.image = pygame.image.load("skier_crash.png")
            animate()
            pygame.time.delay(1000)
            skier.image = pygame.image.load("skier_down.png")
            skier.angle = 0
            speed = [0,6]
            hit[0].passed = True
        elif hit[0].type == "flag" and not hit[0].passed:
            points += 10
            hit[0].kill()
    
    obstacles.update()
    score_text = font.render("Score : "+str(points),1,(0,0,0))
    animate()

pygame.quit()