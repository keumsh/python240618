import pygame
import random

# 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# 공 설정
ball_size = 10
ball_speed = [4, -4]
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_size, ball_size)

# 패들 설정
paddle_width = 400
paddle_height = 10
paddle_speed = 6
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 40, paddle_width, paddle_height)

# 블럭 설정
block_rows = 5
block_cols = 8
block_width = screen_width // block_cols
block_height = 30
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # 공 이동
    ball.left += ball_speed[0]
    ball.top += ball_speed[1]

    # 공 충돌 처리
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # 공이 바닥에 닿았을 때
    if ball.top >= screen_height:
        running = False

    # 공과 블럭 충돌 처리
    for block in blocks[:]:
        if ball.colliderect(block):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)
            break

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.ellipse(screen, white, ball)
    for block in blocks:
        pygame.draw.rect(screen, green, block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
