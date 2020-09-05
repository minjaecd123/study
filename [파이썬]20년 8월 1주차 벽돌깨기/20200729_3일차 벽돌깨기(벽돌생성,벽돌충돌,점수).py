import pygame as p

p.init() #라이브러리 초기화
w = (255,255,255)
size = (600,800) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing = True
#판 이미지
pan = p.image.load("pan.png")
p_rect = pan.get_rect(left = 300 , top = 700)
x = 0
y = 0
#배경
bg = p.image.load("bg.png")
#공
ball = p.image.load("ball.png")
b_rect = ball.get_rect(left = 270,top = 300)
#공속도 관련 변수 
b_x = 1
b_y = 1
#game over 문구
font = p.font.SysFont('malgungothic',50)
#벽돌 생성
block = p.image.load("block.png")
bl_list = []
#2중포문 벽돌생성 가로 10 세로 5
for x in range(10):
      for y in range(5):
            bl_rect = block.get_rect(left = x*60, top = y*40)
            bl_list.append(bl_rect) 
      

while playing: #while true - 계속반복

      for event in p.event.get(): #사용자가 무엇을 누르는지 검사
            if event.type == p.QUIT: #게임창 x버튼을 누르면
                  playing = False #게속반복을 종료
                  p.quit() #게임창 종료
                  quit() #sell창 종료

            if event.type == p.KEYDOWN:
                  if event.key == p.K_LEFT:
                        x = -1
                  if event.key == p.K_RIGHT:
                        x = 1
            if event.type == p.KEYUP:
                  if event.key == p.K_LEFT:
                        x = 0
                  if event.key == p.K_RIGHT:
                        x = 0
                  
      p_rect.left += x
      sc.fill(w)
      sc.blit(bg,(0,0))
      sc.blit(pan,p_rect)
      if p_rect.left >= 500:
            p_rect.left = 500
      if p_rect.left <= 0:
            p_rect.left = 0
      #공 화면 업로드
      sc.blit(ball,b_rect)
      b_rect.top += b_y
      b_rect.left += b_x
      if b_rect.top >= 780:
            sc.blit(text,(200,350))
            playing = False
      if b_rect.top <= 0:
            b_y = -b_y
      if b_rect.left >= 570:
            b_x = -b_x
      if b_rect.left <= 0:
            b_x = -b_x 
      text = font.render("Game Over",True,(255,0,0))
      #판과 공 충돌 
      if p_rect.colliderect(b_rect):
            b_y = -b_y 
            if b_rect.centerx <= p_rect.left or b_rect.centerx > p_rect.right:
                  b_x = b_x * -1
      #벽돌 출력
      for bl_rect in bl_list:
            sc.blit(block,bl_rect)
      #벽돌 공 충돌
      for bl_rect in bl_list:
            if b_rect.colliderect(bl_rect):
                  bl_list.remove(bl_rect)
                  b_y = -b_y
                  
            
      p.display.flip() # 화면 업데이트









      
      

