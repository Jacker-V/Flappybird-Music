import pygame, sys, random

#Tạo hàm cho trò chơi

def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+672,650))

def draw_bg():
    screen.blit(bg,(bg_x_pos,0))
    screen.blit(bg,(bg_x_pos+768,0))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (800,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (800,random_pipe_pos-800))
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
        score_rect = score_surface.get_rect(center = (384,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (384,100))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect = score_surface.get_rect(center = (384,630))
        screen.blit(high_score_surface,high_score_rect)
def update_score(score,high_score):
    if score >high_score:
        high_score=score
    return high_score
def screen_heloo():
    screen.blit(screen_helloing,(0,0))
    screen.blit(bird_mid,(350,250))
    music_surface_1 =pygame.image.load('assets/flappybird3.png').convert_alpha()
    screen.blit(music_surface_1,(170,100))
    #flappy_surface = game_font.render(f'FLAPPY BIRD',True,(180,255,180))
    #flappy_surface_rect = flappy_surface.get_rect(center = (216,100))
    #screen.blit(flappy_surface,flappy_surface_rect)
    play_surface = pygame.image.load('assets/22.png').convert_alpha()
    screen.blit(play_surface,(290,300))
    setting_surface_1 = pygame.image.load('assets/21.png').convert_alpha()
    screen.blit(setting_surface_1,(290,400))
    setting_surface_2 = pygame.image.load('assets/20.png').convert_alpha()
    screen.blit(setting_surface_2,(290,500))

def screen_setting():
    screen.blit(screen_waitting,(0,0))
    choice_2 =  pygame.image.load('assets/18.png').convert_alpha()
    screen.blit(choice_2,(290,100))
    choice_3 =  pygame.image.load('assets/17.png').convert_alpha()
    screen.blit(choice_3,(290,200))
    choice_4 =  pygame.image.load('assets/16.png').convert_alpha()
    screen.blit(choice_4,(290,300))
    choice_5 =  pygame.image.load('assets/15.png').convert_alpha()
    screen.blit(choice_5,(290,400))
    choice_6 =  pygame.image.load('assets/14.png').convert_alpha()
    screen.blit(choice_6,(290,500))

def screen_pick_music():    
    screen.blit(screen_waitting,(0,0))
    hello_surface = pygame.image.load('assets/19.png').convert_alpha()
    screen.blit(hello_surface,(280,0))
    exit_surface = pygame.image.load('assets/14.png').convert_alpha()
    screen.blit(exit_surface,(280,600))
    music_surface_1 =pygame.image.load('assets/1.png').convert_alpha()
    screen.blit(music_surface_1,(30,100))
    music_surface_2 =pygame.image.load('assets/2.png').convert_alpha()
    screen.blit(music_surface_2,(30,200))
    music_surface_3 =pygame.image.load('assets/3.png').convert_alpha()
    screen.blit(music_surface_3,(30,300))
    music_surface_4 =pygame.image.load('assets/130.png').convert_alpha()
    screen.blit(music_surface_4,(30,400))
    music_surface_5 =pygame.image.load('assets/5.png').convert_alpha()
    screen.blit(music_surface_5,(500,100))
    music_surface_6 =pygame.image.load('assets/140.png').convert_alpha()
    screen.blit(music_surface_6,(500,190))
    music_surface_7 =pygame.image.load('assets/150.png').convert_alpha()
    screen.blit(music_surface_7,(500,300))
    music_surface_8 =pygame.image.load('assets/8.png').convert_alpha()
    screen.blit(music_surface_8,(500,410))
    
def screen_pick_bird():
    screen.blit(screen_waitting,(0,0))
    flappy_surface_1=pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
    flappy_surface_1 = pygame.transform.scale2x(flappy_surface_1)
    screen.blit(flappy_surface_1,(350,200))
    flappy_surface_2=pygame.image.load('assets/red2.png').convert_alpha()
    flappy_surface_2 = pygame.transform.scale2x(flappy_surface_2)
    screen.blit(flappy_surface_2,(350,300))
    flappy_surface_3=pygame.image.load('assets/blue2.png').convert_alpha()
    flappy_surface_3 = pygame.transform.scale2x(flappy_surface_3)
    screen.blit(flappy_surface_3,(350,400))
    exit_surface = pygame.image.load('assets/14.png').convert_alpha()
    screen.blit(exit_surface,(280,600))

def screen_pick_mode():
    screen.blit(screen_waitting,(0,0))
    exit_surface = pygame.image.load('assets/14.png').convert_alpha()
    screen.blit(exit_surface,(280,600))
    mode_surface_1= pygame.image.load('assets/13.png').convert_alpha()
    screen.blit(mode_surface_1,(280,200))
    mode_surface_2= pygame.image.load('assets/12.png').convert_alpha()
    screen.blit(mode_surface_2,(280,300))
    mode_surface_3= pygame.image.load('assets/11.png').convert_alpha()
    screen.blit(mode_surface_3,(280,400))

def screen_pick_place():
    screen.blit(screen_waitting,(0,0))
    exit_surface = pygame.image.load('assets/14.png').convert_alpha()
    screen.blit(exit_surface,(280,600))   
    flappy_surface_3=pygame.image.load('assets/BACK.png').convert_alpha()
    #flappy_surface_3 = pygame.transform.scale2x(flappy_surface_3)
    screen.blit(flappy_surface_3,(350,400))
     
pygame.mixer.pre_init(frequency= 44100, size=-16, channels=2, buffer=512)
pygame.init()        
screen = pygame.display.set_mode((768,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

#Tạo các biến cho trò chơi
gravity = 0.25
bird_movement=0
bird_movement_1 =0
game_active = False
score = 0
high_score = 0
page=0

#Màn hình chờ
screen_waitting = pygame.image.load('assets/back5.png').convert()
screen_waitting = pygame.transform.scale2x(screen_waitting)

screen_helloing = pygame.image.load('assets/back5.png').convert()
screen_helloing = pygame.transform.scale2x(screen_helloing)
screen_waitting_countdown_time = 30000
hello_countdown =1
#chèn background
bg = pygame.image.load('assets/back5.png').convert()
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
bird_rect = bird.get_rect(center = (100,300))

#Tạo chim 2
bird1_down= pygame.transform.scale2x(pygame.image.load('assets/red1.png')).convert_alpha()
bird1_mid= pygame.transform.scale2x(pygame.image.load('assets/red2.png')).convert_alpha()
bird1_up= pygame.transform.scale2x(pygame.image.load('assets/red3.png')).convert_alpha()
bird1_list= [bird1_down,bird1_mid,bird1_up]
bird1_index=0
bird1 = bird1_list[bird1_index]
bird1_rect = bird1.get_rect(center = (100,300))

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
game_over_rect = game_over_surface.get_rect(center = (384,384))
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
    #print(game_active)
    #print(page)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #print(mouse_x,mouse_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or page==-1:
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
            if event.key == pygame.K_SPACE and game_active == False :
                #score_sound.play()
                if check2==1:
                    game_active = True
                    pipe_list.clear()
                    dem=0
                    bird_rect.center = (100,300)
                    bird_movement = 0
                    score=0 
                else :
                    game_active = True
                    pipe_list.clear()
                    dem=0
                    bird_rect.center = (100,300)
                    bird_movement = 0
                    bird1_rect.center = (200,300)
                    bird_movement_1 = 0
                    score=0
                page=6
            
        if event.type == pygame.MOUSEBUTTONDOWN and game_active == False:
            if page==0 :
                if mouse_x>=330 and mouse_x<=440 and mouse_y>=370 and mouse_y<=450:
                    page=6
                    game_active = True
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
                        score_sound.play()
                    
                    
                elif mouse_x>=340 and mouse_x<=440 and mouse_y>=470 and mouse_y<=550:
                    page = 1
                    score_sound.play()
                    screen_setting()
                elif mouse_x>=330 and mouse_x<=440 and mouse_y>=570 and mouse_y<=640:
                    page =-1
                    score_sound.play()
            elif page==6:
                page=0
            elif page ==1:
                if mouse_x>=340 and mouse_x<=440 and mouse_y>=170 and mouse_y<=250:
                    page =2
                    score_sound.play()
                    screen_pick_music()
                elif mouse_x>=340 and mouse_x<=440 and mouse_y>=280 and mouse_y<=350:
                    screen_pick_bird()
                    page = 3
                    score_sound.play()
                elif mouse_x>=340 and mouse_x<=440 and mouse_y>=370 and mouse_y<=450:
                    screen_pick_place()
                    page=4
                    score_sound.play()
                elif mouse_x>=340 and mouse_x<=440 and mouse_y>=470 and mouse_y<=550:
                    screen_pick_mode()
                    page=5
                    score_sound.play()
                elif mouse_x>=340 and mouse_x<=440 and mouse_y>=570 and mouse_y<=650:
                    page=0

            elif page == 2:
                if mouse_x>=350 and mouse_x<=450 and mouse_y>=670 and mouse_y<=750:
                    page =1
                elif mouse_x>=30 and mouse_x<=230 and mouse_y>=150 and mouse_y<=230:
                    back_sound = pygame.mixer.Sound('sound/back2.mp3')
                    score_sound.play()
                elif mouse_x>=30 and mouse_x<=230 and mouse_y>=250 and mouse_y<=330:
                    back_sound = pygame.mixer.Sound('sound/K391.mp3')
                    score_sound.play()
                elif mouse_x>=30 and mouse_x<=230 and mouse_y>=350 and mouse_y<=430:
                    back_sound = pygame.mixer.Sound('sound/backs.mp3')
                    score_sound.play()
                elif mouse_x>=30 and mouse_x<=230 and mouse_y>=450 and mouse_y<=530:
                    back_sound = pygame.mixer.Sound('sound/Cung_anh.mp3')
                    score_sound.play()
                elif mouse_x>=500 and mouse_x<=700 and mouse_y>=150 and mouse_y<=230:
                    back_sound = pygame.mixer.Sound('sound/i_do.mp3')
                    score_sound.play()
                elif mouse_x>=500 and mouse_x<=700 and mouse_y>=250 and mouse_y<=330:
                    back_sound = pygame.mixer.Sound('sound/Viet_Nam.mp3')
                    score_sound.play()
                elif mouse_x>=500 and mouse_x<=700 and mouse_y>=350 and mouse_y<=430:
                    back_sound = pygame.mixer.Sound('sound/Cat_Doi.mp3')
                    score_sound.play()
                elif mouse_x>=500 and mouse_x<=700 and mouse_y>=450 and mouse_y<=530:
                    back_sound = pygame.mixer.Sound('sound/Ngay_em.mp3')
                    score_sound.play()

            elif page==3:
                if mouse_x>=350 and mouse_x<=450 and mouse_y>=670 and mouse_y<=750:
                    page =1
            elif page==4:
                if mouse_x>=350 and mouse_x<=450 and mouse_y>=670 and mouse_y<=750:
                    page =1
            elif page ==5:
                if mouse_x>=350 and mouse_x<=450 and mouse_y>=670 and mouse_y<=750:
                    page =1
                elif mouse_x>=320 and mouse_x<=430 and mouse_y>=270 and mouse_y<=350:
                    check2=1
                    score_sound.play()
                elif mouse_x>=330 and mouse_x<=430 and mouse_y>=370 and mouse_y<=450:
                    check2=2
                    score_sound.play()
                elif mouse_x>=330 and mouse_x<=430 and mouse_y>470 and mouse_y<=550:
                    check2=3
                    score_sound.play()

        if event.type == spawnpipe and check2!=3 :
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
             
    if game_active and page==6:
        #chim
        bg_x_pos-=1
        draw_bg()
        if(bg_x_pos<= -768):
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
        floor_x_pos-=2
        draw_floor()
        if floor_x_pos <=-432:
            floor_x_pos = 0  
    elif game_active== False and page==0:
        screen_heloo()
        
    elif game_active == False and page== 6 :
        draw_bg()
        draw_floor()
        high_score=update_score(score,high_score)
        score_display('game_over')
        screen.blit(game_over_surface,game_over_rect)
        back_sound.stop()
        back_sound_countdown=100
    elif game_active== False and page ==1:
        screen_setting()
    #floor
    pygame.display.update()
    clock.tick(120)
