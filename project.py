import pygame, sys, random
pygame.font.init()
textfont = pygame.font.SysFont('monospace',50)

def ball_animation():
    global bspeed_x,bspeed_y
    ball.x += bspeed_x
    ball.y += bspeed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        bspeed_y *=-1
    if ball.left <=0 or ball.right >= screen_width:
        ball_restart() 
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        bspeed_x *= -1
    
def player_animation():
    player.y += pspeed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    opponent.y += ospeed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global bspeed_x,bspeed_y
    ball.center = (screen_width/2,screen_height/2)
    bspeed_y *= random.choice((1,-1))
    bspeed_x *= random.choice((1,-1))
    
pygame.init()
clock = pygame.time.Clock();

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Graphics Project: Pong game')
run = True


ball = pygame.Rect(screen_width/2-17.5,screen_height/2-17.5,35,35)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)

bg_color = pygame.Color('white')
elements = (0,0,0)

bspeed_x = 8 *random.choice((1,-1))
bspeed_y = 8 *random.choice((1,-1))
pspeed = 0
ospeed = 0


while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pspeed += 10
                if event.key == pygame.K_UP:
                    pspeed -= 10  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pspeed -= 10
                if event.key == pygame.K_UP:
                    pspeed += 10 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    ospeed += 10
                if event.key == pygame.K_w:
                    ospeed -= 10  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    ospeed -= 10
                if event.key == pygame.K_w:
                    ospeed += 10 
                
        ball_animation()
        player_animation()
        opponent_animation()
        
        
        screen.fill(bg_color)    
        pygame.draw.rect(screen,elements, player) 
        pygame.draw.rect(screen,elements, opponent)
        pygame.draw.ellipse(screen,elements, ball)
        pygame.draw.aaline(screen,elements,(screen_width/2,0),(screen_width/2,screen_height))    
        pygame.display.flip()
        clock.tick(60)
        