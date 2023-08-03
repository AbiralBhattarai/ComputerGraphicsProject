import pygame, sys, random, button
pygame.font.init()
textfont = pygame.font.SysFont('monospace',50)
global intro, run, ending
global player_score,opponent_score
opponent_score = 0
player_score = 0



def ball_animation():
    global bspeed_x,bspeed_y,player_score,opponent_score
    ball.x += bspeed_x
    ball.y += bspeed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        bspeed_y *=-1
    if ball.left <=0 :
        ball_restart()
        player_score += 1
    if ball.right >= screen_width:
        ball_restart()
        opponent_score +=1
        
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
    
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))

def introf():
    global intro
    while intro:
        screen.fill(bg_color)
        draw_text("Welcome to Pong Game!",text_font,(0,0,0,0),450,300)
        draw_text("Press Space To START",text_font,(0,0,0,0),450,400)
        draw_text("Press Q to Quit",text_font,(0,0,0,0),450,500)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update();
        clock.tick(15)
    
def game():
    global run,pspeed,ospeed   
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
            ball_animation()
            player_animation()
            opponent_animation()
            
            
            screen.fill(bg_color)
            
            draw_text('Player 1 score: '+ str(opponent_score),text_font,(0,0,0),220,150)
            draw_text('Player 2 score: '+ str(player_score),text_font,(0,0,0),840,150)
            draw_text('Press SPACE To End Game',text_font,(0,0,0),450,650)   
            pygame.draw.rect(screen,elements, player) 
            pygame.draw.rect(screen,elements, opponent)
            pygame.draw.ellipse(screen,elements, ball)
            pygame.draw.aaline(screen,elements,(screen_width/2,0),(screen_width/2,screen_height))
            pygame.display.flip()
            clock.tick(60)
def endingf():
    global ending                   
    while ending:
                screen.fill(bg_color)
                if player_score > opponent_score:
                    draw_text("Player 1 Wins!!!",text_font,(0,0,0,0),500,300)
                elif player_score < opponent_score:
                    draw_text("Player 1 Wins!!!",text_font,(0,0,0,0),500,300)
                else :
                    draw_text("DRAW!!!",text_font,(0,0,0,0),600,300)
                draw_text("Press Q to Quit",text_font,(0,0,0,0),500,400)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

                pygame.display.update();
                clock.tick(15)
        
def start_game():
    introf()
    game()
    endingf()
        
pygame.init()
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("monospace", 30)  

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Graphics Project: Pong game')
run = True
intro = True
ending = True
resume_image = pygame.image.load("images/resume.png").convert_alpha()
quit_image = pygame.image.load("images/quit.png").convert_alpha()
resume_button = button.Button(500,125,resume_image,1)
quit_button = button.Button(500,200,quit_image,1) 


ball = pygame.Rect(screen_width/2-17.5,screen_height/2-17.5,35,35)
player = pygame.Rect(screen_width-20,screen_height/2-70,10,140)
opponent = pygame.Rect(10,screen_height/2-70,10,140)

bg_color = pygame.Color('white')
elements = (0,0,0)
bspeed_x = 9*random.choice((1,-1))
bspeed_y = 9*random.choice((1,-1))
pspeed = 0
ospeed = 0 
start_game()

        