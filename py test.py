import pygame, sys, random

#Tạo hàm cho trò chơi

def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def draw_bg():
    screen.blit(bg,(bg_x_pos,0))
    screen.blit(bg,(bg_x_pos+432,0))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-800))
    return bottom_pipe, top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=2
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600: 
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()  
            return False
    if bird_rect.top <= -250 or bird_rect.bottom >= 650:
            hit_sound.play()
            return False 
    return True  
def check_collision_1(pipes):
    for pipe in pipes:
        if bird1_rect.colliderect(pipe):
            hit_sound.play()  
            return False
    if bird1_rect.top <= -250 or bird1_rect.bottom >= 650:
            hit_sound.play()
            return False 
    return True 
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*4,1)
    return new_bird
def rotate_bird_1(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement_1*4,1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect
def bird1_animation():
    new_bird = bird1_list[bird1_index]
    new_bird_rect = new_bird.get_rect(center = (200,bird1_rect.centery))
    return new_bird, new_bird_rect
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = score_surface.get_rect(center = (216,630))
        screen.blit(high_score_surface,high_score_rect)
def update_score(score,high_score):
    if score >high_score:
        high_score=score
    return high_score
def screen_heloo():
    screen.blit(screen_helloing,(0,0))
    screen.blit(bird_mid,(170,250))
    flappy_surface=pygame.image.load('assets/flappybird2.png').convert_alpha()
    flappy_surface = pygame.transform.scale2x(flappy_surface)
    screen.blit(flappy_surface,(125,100))
    #flappy_surface = game_font.render(f'FLAPPY BIRD',True,(180,255,180))
    #flappy_surface_rect = flappy_surface.get_rect(center = (216,100))
    #screen.blit(flappy_surface,flappy_surface_rect)
    play_surface = game_font.render(f'< Play >',True,(255,200,180))
    play_surface_rect = play_surface.get_rect(center = (216,450))
    screen.blit(play_surface,play_surface_rect)


    
def screen_wait():
    hello_surface = game_font.render(f'Click to pick Music',True,(255,255,255))
    hello_rect = hello_surface.get_rect(center =(216,100))
    hello1_surface = game_font.render(f'Space to Play :>',True,(255,255,255))
    hello1_rect = hello1_surface.get_rect(center =(216,700))
    hello2_surface = game_font.render(f'Solo',True,(255,255,255))
    hello2_rect = hello2_surface.get_rect(center =(216,500))
    hello3_surface = game_font.render(f'Cu Pit',True,(255,255,255))
    hello3_rect = hello3_surface.get_rect(center =(216,600))
    screen.blit(screen_waitting,(0,0))
    screen.blit(hello_surface,hello_rect)
    screen.blit(hello1_surface,hello1_rect) 
    screen.blit(hello2_surface,hello2_rect) 
    screen.blit(hello3_surface,hello3_rect) 

    #screen.blit(bird_mid,bird_rect)
    
    music_1=pygame.image.load('assets/MCK1.jpg').convert_alpha()
    music_1 = pygame.transform.scale2x(music_1)
    music_2=pygame.image.load('assets/Son_Tung1.jpg').convert_alpha()
    music_2 = pygame.transform.scale2x(music_2)
    music_3=pygame.image.load('assets/K391.jpg').convert_alpha()
    music_3 = pygame.transform.scale2x(music_3)
    music_4=pygame.image.load('assets/no_music.png').convert_alpha()
    music_4 = pygame.transform.scale2x(music_4)
    #back_music_1=pygame.image.load('assets/1.png').convert_alpha()
    #back_music_1= pygame.transform.scale2x(back_music_1)
    #screen.blit(back_music_1,(10,300))
    screen.blit(music_1,(10,200))
    screen.blit(music_2,(150,200))
    screen.blit(music_3,(300,200))
    screen.blit(music_4,(150,350))
  
pygame.mixer.pre_init(frequency= 44100, size=-16, channels=2, buffer=512)
pygame.init()        
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

#Tạo các biến cho trò chơi
gravity = 0.25
bird_movement=0
bird_movement_1 =0
game_active = False
score = 0
high_score = 0

#Màn hình chờ
screen_waitting = pygame.image.load('assets/background-night.png').convert()
screen_waitting = pygame.transform.scale2x(screen_waitting)
screen_waitting_countdown = 3
screen_helloing = pygame.image.load('assets/background-day.png').convert()
screen_helloing = pygame.transform.scale2x(screen_helloing)
screen_waitting_countdown_time = 30000
hello_countdown =1
#chèn background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
bg_x_pos = 0

#chèn sàn
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#tạo chim1
#bird_down = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
#bird = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
#bird = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()

bird_down= pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png')).convert_alpha()
bird_mid= pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png')).convert_alpha()
bird_up= pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png')).convert_alpha()
bird_list= [bird_down,bird_mid,bird_up]
bird_index=0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))

#Tạo chim 2
bird1_down= pygame.transform.scale2x(pygame.image.load('assets/red1.png')).convert_alpha()
bird1_mid= pygame.transform.scale2x(pygame.image.load('assets/red2.png')).convert_alpha()
bird1_up= pygame.transform.scale2x(pygame.image.load('assets/red3.png')).convert_alpha()
bird1_list= [bird1_down,bird1_mid,bird1_up]
bird1_index=0
bird1 = bird1_list[bird1_index]
bird1_rect = bird1.get_rect(center = (100,384))

#Tạo timer cho bird
birdflap = pygame.USEREVENT +1
pygame.time.set_timer(birdflap,200)
#Tạo timer cho bird 1
bird1flap = pygame.USEREVENT +2
pygame.time.set_timer(bird1flap,200)
#Tạo chở ngại
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]
#Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)
pipe_height = [200,300,400,500]
#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png')).convert_alpha()
game_over_rect = game_over_surface.get_rect(center = (216,384))
#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100
back_sound = pygame.mixer.Sound('sound/K391.mp3')
back_sound_countdown = 100
#Màn hình chờ 
check=1
dem=0 
check2=1
#Chuong trinh chinh
while True:
    #print(back_sound_countdown)
    #print(pipe.centerx)
    #print(check2)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(mouse_x,mouse_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                    flap_sound.play()
                    bird_movement = 0   
                    bird_movement = -7 
            if event.key == pygame.K_UP and game_active and check2 == 2:   
                    bird_movement_1 = 0   
                    bird_movement_1 = -7
            if event.key == pygame.K_SPACE and game_active == False:
                #score_sound.play()
                if check2==1:
                    game_active = True
                    pipe_list.clear()
                    dem=0
                    bird_rect.center = (100,384)
                    bird_movement = 0
                    score=0 
                else :
                    game_active = True
                    pipe_list.clear()
                    dem=0
                    bird_rect.center = (100,384)
                    bird_movement = 0
                    bird1_rect.center = (200,384)
                    bird_movement_1 = 0
                    score=0
        if event.type == pygame.MOUSEBUTTONDOWN and screen_waitting_countdown == 3 :
            if event.button ==1 and mouse_x>=130 and mouse_x<=300 and mouse_y>=430 and mouse_y<=470:
                    #play_surface = game_font.render(f'< Play >',True,(255,255,180))
                    #play_surface_rect = play_surface.get_rect(center = (216,450))
                    #screen.blit(play_surface,play_surface_rect)
                    
                    score_sound.play()
                    
                    screen_waitting_countdown=1
            
        if event.type == pygame.MOUSEBUTTONDOWN and screen_waitting_countdown == 0 :
            if event.button == 1 and check ==1:
                
                if mouse_x>=10 and mouse_x<=110 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/backs.mp3')
                    #screen.blit(bird_mid,(10,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=150 and mouse_x<=250 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/back2.mp3')
                    #screen.blit(bird_mid,(150,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=300 and mouse_x<=400 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/K391.mp3')
                    #screen.blit(bird_mid,(300,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=150 and mouse_x<=250 and mouse_y>=350 and mouse_y<=450:
                    back_sound_countdown-=3
                    score_sound.play()
                elif mouse_x>=175 and mouse_x<=250 and mouse_y>=480 and mouse_y<=515:
                    check2=1
                    score_sound.play()
                elif mouse_x>=155 and mouse_x<=270 and mouse_y>=580 and mouse_y<=615:
                    check2=2
                    score_sound.play()   
                check=0
            elif event.button == 1 and check ==0 :
                screen_wait()
                screen_waitting_countdown = 0
                check=1
                if mouse_x>=10 and mouse_x<=110 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/backs.mp3')
                    #screen.blit(bird_mid,(10,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=150 and mouse_x<=250 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/back2.mp3')
                    #screen.blit(bird_mid,(150,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=300 and mouse_x<=400 and mouse_y>=200 and mouse_y<=300:
                    back_sound = pygame.mixer.Sound('sound/K391.mp3')
                    #screen.blit(bird_mid,(300,430))
                    back_sound_countdown=100
                    score_sound.play()
                elif mouse_x>=150 and mouse_x<=250 and mouse_y>=350 and mouse_y<=450:
                    back_sound_countdown -= 3
                    score_sound.play()
                elif mouse_x>=175 and mouse_x<=250 and mouse_y>=480 and mouse_y<=515:
                    check2=1
                    score_sound.play()
                elif mouse_x>=155 and mouse_x<=270 and mouse_y>=580 and mouse_y<=615:
                    check2=2
                    score_sound.play()
                check=0
        if event.type == pygame.MOUSEBUTTONDOWN and screen_waitting_countdown == 2 :
            if event.button == 1:
                screen_wait()
                screen_waitting_countdown = 0
        if event.type == spawnpipe :
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index<2:
                bird_index+=1
            else :
                bird_index=0
        if event.type == bird1flap:
            if bird1_index<2:
                bird1_index+=1
            else :
                bird1_index=0
        if check2==1:
            bird, bird_rect =bird_animation()
        else:
            bird1,bird1_rect =bird1_animation()
            bird, bird_rect =bird_animation()
             
    if game_active:
        #chim
        bg_x_pos-=1
        draw_bg()
        if(bg_x_pos<= -432):
            bg_x_pos = 0
        
        if back_sound_countdown == 100:
            back_sound.play()
            back_sound_countdown-=1
        bird_movement += gravity
        bird_movement_1 +=gravity
        rotated_bird = rotate_bird(bird)
        rotate1_bird = rotate_bird_1(bird1)
        bird_rect.centery += bird_movement 
        bird1_rect.centery += bird_movement_1
        if check2==1:
            screen.blit(rotated_bird,bird_rect)
        else :
            screen.blit(rotated_bird,bird_rect)
            screen.blit(rotate1_bird,bird1_rect)
        if check2 == 2:
            if check_collision(pipe_list) and check_collision_1 (pipe_list):
                game_active=True
            else :
                game_active=False
        else :
            game_active = check_collision(pipe_list) 
        #pipe
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        if pipe_list.__len__()>0:
            if pipe_list[dem].centerx <= 10 and pipe_list[dem].centerx >= 0:
                score += 0.5
                score_sound_countdown -=50
                dem+=1  
        score_display('main game')
        
        if(score_sound_countdown==0):
            score_sound.play()
            score_sound_countdown =100 
        floor_x_pos-=1 
        draw_floor()
        if floor_x_pos <=-432:
            floor_x_pos = 0  
        screen_waitting_countdown = 2
    elif screen_waitting_countdown == 1 and game_active == False:
         screen_wait()
         screen_waitting_countdown = 0 
    elif screen_waitting_countdown == 2:
        draw_bg()
        draw_floor()
        high_score=update_score(score,high_score)
        score_display('game_over')
        screen.blit(game_over_surface,game_over_rect)
        back_sound.stop()
        back_sound_countdown=100
    elif screen_waitting_countdown == 3 :
        screen_heloo()
    #floor
    pygame.display.update()
    clock.tick(120)
