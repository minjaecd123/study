import pygame as p

p.init()
w =(255,255,255)
size = (600,800)
sc = p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing = True
#판생성 
pan = p.image.load("pan.png")
p_rect = pan.get_rect(left = 245, top = 725)
px = 0
#배경생성
bg = p.image.load("bg3.png")
#공생성 
bl = p.image.load("ball.png")
bl_rect = bl.get_rect(left = 270, top = 370)
#공 스피드 
bx=2
by=2
#게임오버
font = p.font.SysFont("malgungothic",50)
#벽돌생성
block = p.image.load("block.png")
block_list = []
for x1 in range(10): #가로 
    for y1 in range(5): #세로
        blo_rect = block.get_rect(left = 60*x1, top = 50*y1)
        block_list.append(blo_rect)

score = 0

font1 = p.font.SysFont("malgungothic",30)

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                px = -5
            if event.key == p.K_RIGHT:
                px = 5
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                px = 0
            if event.key == p.K_RIGHT:
                px = 0
                
    p_rect.left += px

    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    
    if p_rect.left >= 500:
        p_rect.left = 500
    if p_rect.left <= 0:
        p_rect.left = 0
    sc.blit(bl,bl_rect)

    bl_rect.top += by
    bl_rect.left += bx
    if bl_rect.top >=770:
        by = -by  
    if bl_rect.top <=10:
        by = -by
    if bl_rect.left >=550:
        bx = -bx
    if bl_rect.left <=10:
        bx = -bx        
    if bl_rect.top >=770:
        sc.blit(text,(200,400))
        by = -by
        playing = False

    text = font.render("Game Over",True,(102,0,102))
    text1 = font1.render("점수".format(score),True,(255,255,0))
    text2 = font1.render("남은 갯수: {}".format(len(block_list)),True,(255,255,0))
    text3 = font.render("Clear",True,(0,255,0))
    if p_rect.colliderect(bl_rect):
        by = -2

    for blo_rect in block_list:
        sc.blit(block,blo_rect)
    
    for blo_rect in block_list:
        if bl_rect.colliderect(blo_rect):
            block_list.remove(blo_rect)
            
            
    sc.blit(text1,(0,750))
    sc.blit(text2,(300,750))
    
    #만일 블록갯수가 40개 이하면 클리어 문구 출력 
    if len(block_list) <= 40:
        sc.blit(text3,(200,400))
        playing = False
        

    
        
    p.display.flip()
