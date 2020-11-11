import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 화면 가로 크기
screen_height = 640 # 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("First Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("D:\\Python_git\\Class_Python\\pygame\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생 하였는가?
            running = False # 게임이 진행중이 아니다

    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()

