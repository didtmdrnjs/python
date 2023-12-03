import pygame
import random
import time

pygame.init()

screen_width = 1550
screen_height = 880
screen = pygame.display.set_mode((screen_width, screen_height))

titlei = pygame.image.load("title.png")
background = pygame.image.load("background.png")
background1 = pygame.image.load("background1.png")
background2 = pygame.image.load("background2.png")
background3 = pygame.image.load("background3.png")
background4 = pygame.image.load("background4.png")
_3 = pygame.image.load("3.png")
_2 = pygame.image.load("2.png")
_1 = pygame.image.load("1.png")
_0 = pygame.image.load("0.png")
win = pygame.image.load("win.png")
lose = pygame.image.load("lose.png")
rjatk = pygame.image.load("rjatkchoice.png")
chdtk = pygame.image.load("chdtkchoice.png")
p_hp = pygame.image.load("hp.png")
e_hp = pygame.image.load("hp.png")
p_mana = pygame.image.load("mana.png")
e_mana = pygame.image.load("mana.png")
p_bullet = pygame.image.load("bullet.png")
e_bullet = pygame.image.load("bullet.png")
p_rjarl = pygame.image.load("rjawl.png")
p_rjarl_size = p_rjarl.get_rect().size
p_rjarl_width = p_rjarl_size[0]
p_rjarl_height = p_rjarl_size[1]
e_rjarl = pygame.image.load("rjawl.png")
e_rjarl_size = e_rjarl.get_rect().size
e_rjarl_width = e_rjarl_size[0]
e_rjarl_height = e_rjarl_size[1]
p_b1 = pygame.image.load("bullet_damage.png")
p_b1_size = p_b1.get_rect().size
p_b1_width = p_b1_size[0]
p_b1_height = p_b1_size[1]
e_b1 = pygame.image.load("bullet_damage.png")
e_b1_size = e_b1.get_rect().size
e_b1_width = e_b1_size[0]
e_b1_height = e_b1_size[1]
p_b2 = pygame.image.load("bullet_damage.png")
p_b2_size = p_b2.get_rect().size
p_b2_width = p_b2_size[0]
p_b2_height = p_b2_size[1]
e_b2 = pygame.image.load("bullet_damage.png")
e_b2_size = e_b2.get_rect().size
e_b2_width = e_b2_size[0]
e_b2_height = e_b2_size[1]
p_b3 = pygame.image.load("bullet_damage.png")
p_b3_size = p_b3.get_rect().size
p_b3_width = p_b3_size[0]
p_b3_height = p_b3_size[1]
e_b3 = pygame.image.load("bullet_damage.png")
e_b3_size = e_b3.get_rect().size
e_b3_width = e_b3_size[0]
e_b3_height = e_b3_size[1]
p_b4 = pygame.image.load("bullet_damage.png")
p_b4_size = p_b4.get_rect().size
p_b4_width = p_b4_size[0]
p_b4_height = p_b4_size[1]
e_b4 = pygame.image.load("bullet_damage.png")
e_b4_size = e_b4.get_rect().size
e_b4_width = e_b4_size[0]
e_b4_height = e_b4_size[1]
p_b5 = pygame.image.load("bullet_damage.png")
p_b5_size = p_b5.get_rect().size
p_b5_width = p_b5_size[0]
p_b5_height = p_b5_size[1]
e_b5 = pygame.image.load("bullet_damage.png")
e_b5_size = e_b5.get_rect().size
e_b5_width = e_b5_size[0]
e_b5_height = e_b5_size[1]
p_b6 = pygame.image.load("bullet_damage.png")
p_b6_size = p_b6.get_rect().size
p_b6_width = p_b6_size[0]
p_b6_height = p_b6_size[1]
e_b6 = pygame.image.load("bullet_damage.png")
e_b6_size = e_b6.get_rect().size
e_b6_width = e_b6_size[0]
e_b6_height = e_b6_size[1]
q_down = pygame.image.load("q_down.png")
q_up = pygame.image.load("q_up.png")
w_down = pygame.image.load("w_down.png")
w_up = pygame.image.load("w_up.png")
shift_down = pygame.image.load("shift_down.png")
shift_up = pygame.image.load("shift_up.png")
s_down = pygame.image.load("s_down.png")
s_up = pygame.image.load("s_up.png")

pygame.display.set_caption("project")

player_hp = 0
enemy_hp = 0
player_hp_c = 0
enemy_hp_c = 0
player_hp_p = 0
player_hp_m = 0
enemy_hp_p = 850
enemy_hp_m = 0
mana = 150
bullet = 10
player_mana = 0
enemy_mana = 0
player_bullet = 3
enemy_bullet = 3
player_e = 0
enemy_e = 850
player_mana_m = 0
enemy_mana_m = 0
player_bullet_m = 0
enemy_bullet_m = 0
playerx = 0
playery = 0
enemyx = 0
enemyy = 0
pw_start_time = 0.0
pw_end_time = 0.0
pq_start_time = 0.0
pq_end_time = 0.0
pe_start_time = 0.0
pe_end_time = 0.0
pemove = 0
pd_start_time = 0.0
pd_end_time = 0.0
pd = False
ps_start_time = 0.0
ps_end_time = 0.0
ps_x = -100
ps_y = -100
psx = 0
psy = 0
mouse_x = 0
mouse_y = 0
ew_start_time = 0.0
ew_end_time = 0.0
eq_start_time = 0.0
eq_end_time = 0.0
ee_start_time = 0.0
ee_end_time = 0.0
eemove = 0
ed_start_time = 0.0
ed_end_time = 0.0
ed = False
es_start_time = 0.0
es_end_time = 0.0
es_x = -100
es_y = -100
esx = 0
esy = 0
pb1_x = -100
pb1_y = -100
pb2_x = -100
pb2_y = -100
pb3_x = -100
pb3_y = -100
pb4_x = -100
pb4_y = -100
pb5_x = -100
pb5_y = -100
pb6_x = -100
pb6_y = -100
eb1_x = -100
eb1_y = -100
eb2_x = -100
eb2_y = -100
eb3_x = -100
eb3_y = -100
eb4_x = -100
eb4_y = -100
eb5_x = -100
eb5_y = -100
eb6_x = -100
eb6_y = -100
pb1x = 0
pb1y = 0
pb2x = 0
pb2y = 0
pb3x = 0
pb3y = 0
pb4x = 0
pb4y = 0
pb5x = 0
pb5y = 0
pb6x = 0
pb6y = 0
eb1x = 0
eb1y = 0
eb2x = 0
eb2y = 0
eb3x = 0
eb3y = 0
eb4x = 0
eb4y = 0
eb5x = 0
eb5y = 0
eb6x = 0
eb6y = 0
p_reload_s = 0
p_reload_e = 0
e_reload_s = 0
e_reload_e = 0
speed = 1 
jump = 0.0
jumptlfgod = False
ground = True
e_jump = 0.0
e_jumptlfgod = False
e_ground = True
p_choice= 1
e_choice = 1
win_value = False
p_damage = True
e_damage = True
pb1_damage = True
pb2_damage = True
pb3_damage = True
pb4_damage = True
pb5_damage = True
pb6_damage = True
eb1_damage = True
eb2_damage = True
eb3_damage = True
eb4_damage = True
eb5_damage = True
eb6_damage = True
p_d = 1
e_d = 0
e_tlfgod = 0
pb_dus_cnt = 0
background_r = 0

clock = pygame.time.Clock()

def sh_screen() :
    if background_r == 1:
        screen.blit(background, (0, 0))
    elif background_r == 2:
        screen.blit(background1, (0, 0))
    elif background_r == 3:
        screen.blit(background2, (0, 0))
    elif background_r == 4:
        screen.blit(background3, (0, 0))
    elif background_r == 5:
        screen.blit(background4, (0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(enemy, (enemy_x, enemy_y))
    screen.blit(p_hp, (player_hp_p - player_hp_m, 0))
    screen.blit(e_hp, (enemy_hp_p + enemy_hp_m, 0))
    if p_choice == 1:
        screen.blit(p_mana, (player_e - player_mana_m, 50))
    else :
        screen.blit(p_bullet, (player_e - player_bullet_m, 50))
    if e_choice == 1:
        screen.blit(e_mana, (enemy_e + enemy_mana_m, 50))
    else :
        screen.blit(e_bullet, (enemy_e + enemy_bullet_m, 50))
    if p_choice == 1:
        if player_mana >= 20 and pq_end_time - pq_start_time >= 8:
            screen.blit(q_up, (0, 80))
        else :
            screen.blit(q_down, (0, 80))
        if player_mana >= 30 and pe_end_time - pe_start_time >= 10:
            screen.blit(w_up, (50, 80))
        else :
            screen.blit(w_down, (50, 80))
        if player_mana >= 50 and pd_end_time - pd_start_time >= 5:
            screen.blit(shift_up, (100, 80))
        else :
            screen.blit(shift_down, (100, 80))
        if player_mana >= 100 and ps_end_time - ps_start_time >= 20:
            screen.blit(s_up, (150, 80))
        else :
            screen.blit(s_down, (150, 80))
    else :
        if player_bullet >= 3 and pq_end_time - pq_start_time >= 8:
            screen.blit(q_up, (0, 80))
        else :
            screen.blit(q_down, (0, 80))
        if player_bullet >= 6 and pe_end_time - pe_start_time >= 10:
            screen.blit(w_up, (50, 80))
        else :
            screen.blit(w_down, (50, 80))
        if pd_end_time - pd_start_time >= 8:
            screen.blit(shift_up, (100, 80))
        else :
            screen.blit(shift_down, (100, 80))
        if player_bullet >= 8 and ps_end_time - ps_start_time >= 15:
            screen.blit(s_up, (150, 80))
        else :
            screen.blit(s_down, (150, 80))
    screen.blit(p_rjarl, (ps_x, ps_y))
    screen.blit(e_rjarl, (es_x, es_y))
    screen.blit(p_b1, (pb1_x, pb1_y))
    screen.blit(p_b2, (pb2_x, pb2_y))
    screen.blit(p_b3, (pb3_x, pb3_y))
    screen.blit(p_b4, (pb4_x, pb4_y))
    screen.blit(p_b5, (pb5_x, pb5_y))
    screen.blit(p_b6, (pb6_x, pb6_y))
    screen.blit(e_b1, (eb1_x, eb1_y))
    screen.blit(e_b2, (eb2_x, eb2_y))
    screen.blit(e_b3, (eb3_x, eb3_y))
    screen.blit(e_b4, (eb4_x, eb4_y))
    screen.blit(e_b5, (eb5_x, eb5_y))
    screen.blit(e_b6, (eb6_x, eb6_y))

while True:
    title = True
    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                title = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    title = False

        screen.blit(titlei, (0, 0))
        pygame.display.update()
        
    screen.blit(rjatk, (0, 0))
    pygame.display.update()
    choose = True
    while choose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choose = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                choose = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_LEFT:
                    screen.blit(rjatk, (0, 0))
                    pygame.display.update()
                    p_choice = 1
                if event.key == pygame.K_RIGHT:
                    screen.blit(chdtk, (0, 0))
                    pygame.display.update()
                    p_choice = 2
                if event.key == pygame.K_SPACE:
                    choose = False
    
    screen.blit(_3, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(_2, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(_1, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.blit(_0, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)

    if p_choice == 1:
        player_hp = 2500
        player_hp_c = 2500
        player = pygame.image.load("player_sword.png")
        player_size = player.get_rect().size
        player_width = player_size[0]
        player_height = player_size[1]
        player_x = (screen_width / 4) - (player_width / 2)
        player_y = screen_height - player_height
    else :
        player_hp = 1500
        player_hp_c = 1500
        player = pygame.image.load("player_gun.png")
        player_size = player.get_rect().size
        player_width = player_size[0]
        player_height = player_size[1]
        player_x = (screen_width / 4) - (player_width / 2)
        player_y = screen_height - player_height
        
    e_choice = random.randint(1, 2)
    
    if e_choice == 1:
        enemy_hp = 2500
        enemy_hp_c = 2500
        enemy = pygame.image.load("enemy_sword.png")
        enemy_size = enemy.get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]
        enemy_x = (screen_width / 4 * 3) - (enemy_width / 2)
        enemy_y = screen_height - enemy_height
    else :
        enemy_hp = 1500
        enemy_hp_c = 1500
        enemy = pygame.image.load("enemy_gun.png")
        enemy_size = enemy.get_rect().size
        enemy_width = enemy_size[0]
        enemy_height = enemy_size[1]
        enemy_x = (screen_width / 4 * 3) - (enemy_width / 2)
        enemy_y = screen_height - enemy_height
    
    player_mana = 0
    enemy_mana = 0
    player_bullet = 3
    enemy_bullet = 3
    
    player_mana_m = 0
    enemy_mana_m = 0
    player_hp_m = 0
    enemy_hp_m = 0
    player_bullet_m = 0
    enemy_bullet_m = 0
    
    background_r = random.randint(1, 5)

    running = True
    while running:
        dt = clock.tick(60)
        p_reload_e = time.time()
        e_reload_e = time.time()
        e_tlfgod = random.randint(0, 10)
        pq_end_time = time.time()
        pe_end_time = time.time()
        pd_end_time = time.time()
        ps_end_time = time.time()
        
        if e_choice == 1:
            if e_tlfgod == 1:
                enemyx -= speed
                e_d = 0
            if e_tlfgod == 2:
                enemyx += speed
                e_d = 1
            if e_ground == True:
                if e_tlfgod == 1:
                    e_jump = 0.25
                    e_jumptlfgod = True
                    e_ground = False
            if e_tlfgod == 4:
                eq_end_time = time.time()
                if eq_end_time - eq_start_time >= 8:
                    if enemy_mana >= 20:
                        enemy_mana -= 20
                        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
                        while enemy_x < screen_width - enemy_width and enemy_x > 0:
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            if enemy_rect.colliderect(player_rect) and e_damage == True:
                                if pd == False:
                                    player_hp_c -= 150
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                e_damage = False
                            if e_d == 1:
                                enemyx = 1
                            else :
                                enemyx = -1
                            enemy_x += enemyx * dt
                            sh_screen()
                            pygame.display.update()
                        eq_start_time = time.time()
                        enemyx = 0
                        e_damage = True
            if e_tlfgod == 5:
                ee_end_time = time.time()
                if ee_end_time - ee_start_time >= 10:
                    if enemy_mana >= 30:
                        enemy_mana -= 30
                        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
                        eemove = enemy_x
                        while enemy_x < screen_width - enemy_width and enemy_x > 0 and abs(enemy_x - eemove) <= 80:
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            if enemy_rect.colliderect(player_rect) and e_damage == True:
                                if pd == False:
                                    player_hp_c -= 200
                                else :
                                    player_hp_c -= 50
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                e_damage = False
                            if e_d == 1:
                                enemyx = 1
                            else :
                                enemyx = -1
                            enemy_x += enemyx * dt
                            sh_screen()
                            pygame.display.update()
                        ee_start_time = time.time()
                        enemyx = 0
                        e_damage = True
            if e_tlfgod == 6:
                ed_end_time = time.time()
                if ed_end_time - ed_start_time >= 8:
                    if enemy_mana >= 50:
                        enemy_mana -= 50
                        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
                        ed = True
                        enemy_x += enemyx * dt
                        sh_screen()
                        pygame.display.update()
                        ed_start_time = time.time()
            if e_tlfgod == 7:
                es_end_time = time.time()
                if es_end_time - es_start_time >= 20:
                    if enemy_mana >= 100:
                        enemy_mana -= 100
                        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
                        es_x = enemy_x + enemy_width / 2
                        es_y = enemy_y + enemy_height / 2
                        while es_x < screen_width and es_x > 0 and es_y < screen_height and es_y > 0:
                            e_tlfgod = random.randint(0, 3)
                            if e_tlfgod == 1:
                                enemyx -= speed
                                e_d = 0
                            if e_tlfgod == 2:
                                enemyx += speed
                                e_d = 1
                            if e_ground == True:
                                if e_tlfgod == 3:
                                    e_jump = 0.25
                                    e_jumptlfgod = True
                                    e_ground = False
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            e_rjarl_rect = e_rjarl.get_rect()
                            e_rjarl_rect.left = es_x
                            e_rjarl_rect.top = es_y
                            if e_jumptlfgod == True:
                                enemyy -= e_jump
                                e_jump -= 0.02
                            if e_tlfgod == 0:
                                enemyx = 0        
                            if e_rjarl_rect.colliderect(player_rect) and e_damage == True:
                                if pd == False:
                                    player_hp_c -= 400
                                else :
                                    player_hp_c -= 250
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                e_damage = False
                            esx = (player_x - enemy_x) / 1000
                            esy = (player_y - enemy_y) / 1000
                            es_x += esx * dt
                            es_y += esy * dt
                            enemy_x += enemyx * dt
                            enemy_y += enemyy * dt
                            sh_screen()
                            pygame.display.update()
                        es_start_time = time.time()
                        esx = 0
                        e_damage = True
            if e_tlfgod == 8:
                ew_end_time = time.time()
                if ew_end_time - ew_start_time >= 1:
                    if enemy_rect.colliderect(player_rect):
                        if pd == False:
                            player_hp_c -= 50
                        else :
                            pd = False
                        if p_choice == 1:
                            player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                        else :
                            player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                        ew_start_time = time.time()
        else :
            if e_tlfgod == 1:
                enemyx -= speed
                e_d = 0
            if e_tlfgod == 2:
                enemyx += speed
                e_d = 1
            if e_ground == True:
                if e_tlfgod == 1:
                    e_jump = 0.25
                    e_jumptlfgod = True
                    e_ground = False
            if e_tlfgod == 4:
                ew_end_time = time.time()
                if ew_end_time - ew_start_time >= 1.5:
                    if enemy_bullet >= 1:
                        enemy_bullet -= 1
                        enemy_bullet_m = ((bullet - enemy_bullet) / 0.1) * 7
                        eb1_x = enemy_x + (enemy_width / 2)
                        eb1_y = enemy_y + (enemy_height / 2)
                        eb1x = (player_x - eb1_x) / 100
                        eb1y = (player_y - eb1_y) / 100
                        while eb1_x < screen_width and eb1_x > 0 and eb1_y < screen_height and eb1_y > 0:
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            e_b1_rect = e_b1.get_rect()
                            e_b1_rect.left = eb1_x
                            e_b1_rect.top = eb1_y
                            if e_b1_rect.colliderect(player_rect) and e_damage == True:
                                if pd == False:
                                    player_hp_c -= 100
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                ew_start_time = time.time()
                                e_damage = False
                            eb1_x += eb1x * dt
                            eb1_y += eb1y * dt
                            sh_screen()
                            pygame.display.update()
                        e_damage = True
            if e_tlfgod == 5 and e_reload_e - e_reload_s >= 3:
                enemy_bullet += 5
                e_reload_s = time.time()
            if e_tlfgod == 6:
                eq_end_time = time.time()
                if eq_end_time - eq_start_time >= 8:
                    if enemy_bullet >= 3:
                        enemy_bullet -= 3
                        enemy_bullet_m = ((bullet - enemy_bullet) / 0.1) * 7
                        eb1_x = enemy_x + (enemy_width / 2)
                        eb1_y = enemy_y + (enemy_height / 2)
                        eb2_x = enemy_x + (enemy_width / 2)
                        eb2_y = enemy_y + (enemy_height / 2)
                        eb3_x = enemy_x + (enemy_width / 2)
                        eb3_y = enemy_y + (enemy_height / 2)
                        eb1x = (player_x - eb1_x) /10
                        eb1y = (player_y - eb1_y) / 10
                        eb2x = (player_x - eb2_x) /10
                        eb2y = (player_y - eb2_y) / 10
                        eb3x = (player_x - eb3_x) /10
                        eb3y = (player_y - eb3_y) / 10
                        while eb3_x < screen_width and eb3_x > 0 and eb3_y < screen_height and eb3_y > 0:
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            e_b1_rect = e_b1.get_rect()
                            e_b1_rect.left = eb1_x
                            e_b1_rect.top = eb1_y
                            e_b2_rect = e_b2.get_rect()
                            e_b2_rect.left = eb2_x
                            e_b2_rect.top = eb2_y
                            e_b3_rect = e_b3.get_rect()
                            e_b3_rect.left = eb3_x
                            e_b3_rect.top = eb3_y
                            eb_dus_cnt = time.time()
                            if e_b1_rect.colliderect(player_rect) and eb1_damage == True:
                                if pd == False:
                                    player_hp_c -= 120
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb1_damage = False
                            if e_b2_rect.colliderect(player_rect) and eb2_damage == True:
                                if pd == False:
                                    player_hp_c -= 120
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb2_damage = False
                            if e_b3_rect.colliderect(player_rect) and eb3_damage == True:
                                if pd == False:
                                    player_hp_c -= 120
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb3_damage = False
                            eb1_x += eb1x * dt
                            eb1_y += eb1y * dt
                            if eb_dus_cnt - eq_end_time >= 0.1:
                                eb2_x += eb2x * dt
                                eb2_y += eb2y * dt
                            if eb_dus_cnt - eq_end_time >= 0.2:
                                eb3_x += eb3x * dt
                                eb3_y += eb3y * dt
                            sh_screen()
                            pygame.display.update()
                        eq_start_time = time.time()
            if e_tlfgod == 7:
                ee_end_time = time.time()
                if ee_end_time - ee_start_time >= 10:
                    if enemy_bullet >= 6:
                        enemy_bullet -= 6
                        enemy_bullet_m = ((bullet - enemy_bullet) / 0.1) * 7
                        eb1_x = enemy_x + (enemy_width / 2)
                        eb1_y = enemy_y + (enemy_height / 2)
                        eb2_x = enemy_x + (enemy_width / 2)
                        eb2_y = enemy_y + (enemy_height / 2)
                        eb3_x = enemy_x + (enemy_width / 2)
                        eb3_y = enemy_y + (enemy_height / 2)
                        eb4_x = enemy_x + (enemy_width / 2)
                        eb4_y = enemy_y + (enemy_height / 2)
                        eb5_x = enemy_x + (enemy_width / 2)
                        eb5_y = enemy_y + (enemy_height / 2)
                        eb6_x = enemy_x + (enemy_width / 2)
                        eb6_y = enemy_y + (enemy_height / 2)
                        eb1x = (player_x - eb1_x) / 10
                        eb1y = (player_x - eb1_x) / 10
                        eb2x = (player_x - eb2_x) / 10
                        eb2y = (((player_x - eb2_x) * 2) / 3) / 10
                        eb3x = (player_x - eb3_x) / 10
                        eb3y = ((player_x - eb3_x) / 3) / 10
                        eb4x = (player_x - eb4_x) / 10
                        eb4y = -1 * ((player_x - eb4_x) / 3) / 10
                        eb5x = (player_x - eb5_x) / 10
                        eb5y = -1 * (((player_x - eb5_x) * 2) / 3) / 10
                        eb6x = (player_x - eb6_x) / 10
                        eb6y = -1 * (player_x - eb6_x) / 10
                        while eb1_x < screen_width and eb1_x > 0 and eb1_y < screen_height and eb1_y > 0 or eb2_x < screen_width and eb2_x > 0 and eb2_y < screen_height and eb2_y > 0 or eb3_x < screen_width and eb3_x > 0 and eb3_y < screen_height and eb3_y > 0 or eb4_x < screen_width and eb4_x > 0 and eb4_y < screen_height and eb4_y > 0 or eb5_x < screen_width and eb5_x > 0 and eb5_y < screen_height and eb5_y > 0 or eb6_x < screen_width and eb6_x > 0 and eb6_y < screen_height and eb6_y >0:
                            if player_x < 0:
                                player_x = 0
                            elif player_x > screen_width - player_width:
                                player_x = screen_width - player_width
                            if player_y < 0:
                                player_y = 0
                            elif player_y > screen_height - player_height:
                                player_y = screen_height - player_height
                                playery = 0
                                jumptlfgod = False
                                ground = True
                            
                            if enemy_x < 0:
                                enemy_x = 0
                            elif enemy_x > screen_width - enemy_width:
                                enemy_x = screen_width - enemy_width
                            if enemy_y < 0:
                                enemy_y = 0
                            elif enemy_y > screen_height - enemy_height:
                                enemy_y = screen_height - enemy_height
                                enemyy = 0
                                e_jumptlfgod = False
                                e_ground = True

                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            e_b1_rect = e_b1.get_rect()
                            e_b1_rect.left = eb1_x
                            e_b1_rect.top = eb1_y
                            e_b2_rect = e_b2.get_rect()
                            e_b2_rect.left = eb2_x
                            e_b2_rect.top = eb2_y
                            e_b3_rect = e_b3.get_rect()
                            e_b3_rect.left = eb3_x
                            e_b3_rect.top = eb3_y
                            e_b4_rect = e_b4.get_rect()
                            e_b4_rect.left = eb4_x
                            e_b4_rect.top = eb4_y
                            e_b5_rect = e_b5.get_rect()
                            e_b5_rect.left = eb5_x
                            e_b5_rect.top = eb5_y
                            e_b6_rect = e_b6.get_rect()
                            e_b6_rect.left = eb6_x
                            e_b6_rect.top = eb6_y
                            if e_b1_rect.colliderect(player_rect) and eb1_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb1_damage = False
                            if e_b2_rect.colliderect(player_rect) and eb2_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb2_damage = False
                            if e_b3_rect.colliderect(player_rect) and eb3_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb3_damage = False
                            if e_b4_rect.colliderect(player_rect) and eb4_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb4_damage = False
                            if e_b5_rect.colliderect(player_rect) and eb5_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb5_damage = False
                            if e_b6_rect.colliderect(player_rect) and eb6_damage == True:
                                if pd == False:
                                    player_hp_c -= 80
                                else :
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                eb6_damage = False
                            eb1_x += eb1x * dt
                            eb1_y += eb1y * dt
                            eb2_x += eb2x * dt
                            eb2_y += eb2y * dt
                            eb3_x += eb3x * dt
                            eb3_y += eb3y * dt
                            eb4_x += eb4x * dt
                            eb4_y += eb4y * dt
                            eb5_x += eb5x * dt
                            eb5_y += eb5y * dt
                            eb6_x += eb6x * dt
                            eb6_y += eb6y * dt
                            player_x += playerx * dt
                            player_y += playery * dt
                            enemy_x += enemyx * dt
                            enemy_y += enemyy * dt
                            sh_screen()
                            pygame.display.update()
                        eq_start_time = time.time()
                        eb1_damage = True
                        eb2_damage = True
                        eb3_damage = True
                        eb4_damage = True
                        eb5_damage = True
                        eb6_damage = True
            if e_tlfgod == 8:
                ed_end_time = time.time()
                if ed_end_time - ed_start_time >= 8:
                    if enemy_mana >= 50:
                        enemy_mana -= 50
                        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
                        ed = True
                        enemy_x += enemyx * dt
                        sh_screen()
                        pygame.display.update()
                        ed_start_time = time.time()
            if e_tlfgod == 9:
                es_end_time = time.time()
                if es_end_time - es_start_time >= 1.5:
                    if enemy_bullet >= 8:
                        enemy_bullet -= 8
                        enemy_bullet_m = ((bullet - enemy_bullet) / 0.1) * 7
                        eb1_x = enemy_x + (enemy_width / 2)
                        eb1_y = enemy_y + (enemy_height / 2)
                        eb1x = (player_x - eb1_x) / 10
                        eb1y = (player_y - eb1_y) / 10
                        while eb1_x < screen_width and eb1_x > 0 and eb1_y < screen_height and eb1_y > 0:
                            player_rect = player.get_rect()
                            player_rect.left = player_x
                            player_rect.top = player_y
                            enemy_rect = enemy.get_rect()
                            enemy_rect.left = enemy_x
                            enemy_rect.top = enemy_y
                            e_b1_rect = e_b1.get_rect()
                            e_b1_rect.left = eb1_x
                            e_b1_rect.top = eb1_y
                            if e_b1_rect.colliderect(player_rect) and e_damage == True:
                                if pd == False:
                                    player_hp_c -= 500
                                else :
                                    player_hp_c -= 350
                                    pd = False
                                if p_choice == 1:
                                    player_hp_m = ((player_hp - player_hp_c) / 25) * 7
                                else :
                                    player_hp_m = ((player_hp - player_hp_c) / 15) * 7
                                es_start_time = time.time()
                                e_damage = False
                            eb1_x += eb1x * dt
                            eb1_y += eb1y * dt
                            sh_screen()
                            pygame.display.update()
                        e_damage = True
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    playerx -= speed
                    p_d = 0
                if event.key == pygame.K_d:
                    playerx += speed
                    p_d = 1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_e and p_reload_e - p_reload_s >= 3:
                    player_bullet += 5
                    p_reload_s = time.time()
                if ground == True:
                    if event.key == pygame.K_SPACE:
                        jump = 0.25
                        jumptlfgod = True
                        ground = False
                if p_choice == 1:
                    if event.key == pygame.K_q:
                        if pq_end_time - pq_start_time >= 8:
                            if player_mana >= 20:
                                player_mana -= 20
                                player_mana_m = ((mana - player_mana) / 1.5) * 7
                                while player_x < screen_width - player_width and player_x > 0:
                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    if player_rect.colliderect(enemy_rect) and p_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 150
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        p_damage = False
                                    if p_d == 1:
                                        playerx = 1
                                    else :
                                        playerx = -1
                                    player_x += playerx * dt
                                    sh_screen()
                                    pygame.display.update()
                                pq_start_time = time.time()
                                playerx = 0
                                p_damage = True
                    elif event.key == pygame.K_w:
                        if pe_end_time - pe_start_time >= 10:
                            if player_mana >= 30:
                                player_mana -= 30
                                player_mana_m = ((mana - player_mana) / 1.5) * 7
                                pemove = player_x
                                while player_x < screen_width - player_width and player_x > 0 and abs(player_x - pemove) <= 80:
                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    if player_rect.colliderect(enemy_rect) and p_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 200
                                        else :
                                            enemy_hp_c -= 50
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        p_damage = False
                                    if p_d == 1:
                                        playerx = 1
                                    else :
                                        playerx = -1
                                    player_x += playerx * dt
                                    sh_screen()
                                    pygame.display.update()
                                pe_start_time = time.time()
                                playerx = 0
                                p_damage = True
                    elif event.key == pygame.K_LSHIFT:
                        if pd_end_time - pd_start_time >= 8:
                            if player_mana >= 50:
                                player_mana -= 50
                                player_mana_m = ((mana - player_mana) / 1.5) * 7
                                pd = True
                                player_x += playerx * dt
                                sh_screen()
                                pygame.display.update()
                                pd_start_time = time.time()
                    elif event.key == pygame.K_s:
                        if ps_end_time - ps_start_time >= 20:
                            if player_mana >= 100:
                                player_mana -= 100
                                player_mana_m = ((mana - player_mana) / 1.5) * 7
                                ps_x = player_x + player_width / 2
                                ps_y = player_y + player_height / 2
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                psx = (mouse_x - player_x) / 1000
                                psy = (mouse_y - player_y) / 1000
                                while ps_x < screen_width and ps_x > 0 and ps_y < screen_height and ps_y > 0:
                                    if event.key == pygame.K_a:
                                        playerx -= speed
                                        p_d = 0
                                    if event.key == pygame.K_d:
                                        playerx += speed
                                        p_d = 1
                                    if ground == True:
                                        if event.key == pygame.K_SPACE:
                                            jump = 0.25
                                            jumptlfgod = True
                                            ground = False
                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    p_rjarl_rect = p_rjarl.get_rect()
                                    p_rjarl_rect.left = ps_x
                                    p_rjarl_rect.top = ps_y
                                    if jumptlfgod == True:
                                        playery -= jump
                                        jump -= 0.02
                                    if event.type == pygame.KEYUP:
                                        if event.key == pygame.K_a or event.key == pygame.K_d:
                                            playerx = 0        
                                    if p_rjarl_rect.colliderect(enemy_rect) and p_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 400
                                        else :
                                            enemy_hp_c -= 250
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        p_damage = False
                                    ps_x += psx * dt
                                    ps_y += psy * dt
                                    player_x += playerx * dt
                                    player_y += playery * dt
                                    sh_screen()
                                    pygame.display.update()
                                ps_start_time = time.time()
                                psx = 0
                                p_damage = True
                else :
                    if event.key == pygame.K_q:
                        if pq_end_time - pq_start_time >= 8:
                            if player_bullet >= 3:
                                player_bullet -= 3
                                player_bullet_m = ((bullet - player_bullet) / 0.1) * 7
                                pb1_x = player_x + (player_width / 2)
                                pb1_y = player_y + (player_height / 2)
                                pb2_x = player_x + (player_width / 2)
                                pb2_y = player_y + (player_height / 2)
                                pb3_x = player_x + (player_width / 2)
                                pb3_y = player_y + (player_height / 2)
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                pb1x = (mouse_x - pb1_x) /10
                                pb1y = (mouse_y - pb1_y) / 10
                                pb2x = (mouse_x - pb2_x) /10
                                pb2y = (mouse_y - pb2_y) / 10
                                pb3x = (mouse_x - pb3_x) /10
                                pb3y = (mouse_y - pb3_y) / 10
                                while pb3_x < screen_width and pb3_x > 0 and pb3_y < screen_height and pb3_y > 0:
                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    p_b1_rect = p_b1.get_rect()
                                    p_b1_rect.left = pb1_x
                                    p_b1_rect.top = pb1_y
                                    p_b2_rect = p_b2.get_rect()
                                    p_b2_rect.left = pb2_x
                                    p_b2_rect.top = pb2_y
                                    p_b3_rect = p_b3.get_rect()
                                    p_b3_rect.left = pb3_x
                                    p_b3_rect.top = pb3_y
                                    pb_dus_cnt = time.time()
                                    if p_b1_rect.colliderect(enemy_rect) and pb1_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 120
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb1_damage = False
                                    if p_b2_rect.colliderect(enemy_rect) and pb2_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 120
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb2_damage = False
                                    if p_b3_rect.colliderect(enemy_rect) and pb3_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 120
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb3_damage = False
                                    pb1_x += pb1x * dt
                                    pb1_y += pb1y * dt
                                    if pb_dus_cnt - pq_end_time >= 0.1:
                                        pb2_x += pb2x * dt
                                        pb2_y += pb2y * dt
                                    if pb_dus_cnt - pq_end_time >= 0.2:
                                        pb3_x += pb3x * dt
                                        pb3_y += pb3y * dt
                                    sh_screen()
                                    pygame.display.update()
                                pq_start_time = time.time()
                    if event.key == pygame.K_w:
                        if pe_end_time - pe_start_time >= 10:
                            if player_bullet >= 6:
                                player_bullet -= 6
                                player_bullet_m = ((bullet - player_bullet) / 0.1) * 7
                                pb1_x = player_x + (player_width / 2)
                                pb1_y = player_y + (player_height / 2)
                                pb2_x = player_x + (player_width / 2)
                                pb2_y = player_y + (player_height / 2)
                                pb3_x = player_x + (player_width / 2)
                                pb3_y = player_y + (player_height / 2)
                                pb4_x = player_x + (player_width / 2)
                                pb4_y = player_y + (player_height / 2)
                                pb5_x = player_x + (player_width / 2)
                                pb5_y = player_y + (player_height / 2)
                                pb6_x = player_x + (player_width / 2)
                                pb6_y = player_y + (player_height / 2)
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                pb1x = (mouse_x - pb1_x) / 10
                                pb1y = (mouse_x - pb1_x) / 10
                                pb2x = (mouse_x - pb2_x) / 10
                                pb2y = (((mouse_x - pb2_x) * 2) / 3) / 10
                                pb3x = (mouse_x - pb3_x) / 10
                                pb3y = ((mouse_x - pb3_x) / 3) / 10
                                pb4x = (mouse_x - pb4_x) / 10
                                pb4y = -1 * ((mouse_x - pb4_x) / 3) / 10
                                pb5x = (mouse_x - pb5_x) / 10
                                pb5y = -1 * (((mouse_x - pb5_x) * 2) / 3) / 10
                                pb6x = (mouse_x - pb6_x) / 10
                                pb6y = -1 * (mouse_x - pb6_x) / 10
                                while pb1_x < screen_width and pb1_x > 0 and pb1_y < screen_height and pb1_y > 0 or pb2_x < screen_width and pb2_x > 0 and pb2_y < screen_height and pb2_y > 0 or pb3_x < screen_width and pb3_x > 0 and pb3_y < screen_height and pb3_y > 0 or pb4_x < screen_width and pb4_x > 0 and pb4_y < screen_height and pb4_y > 0 or pb5_x < screen_width and pb5_x > 0 and pb5_y < screen_height and pb5_y > 0 or pb6_x < screen_width and pb6_x > 0 and pb6_y < screen_height and pb6_y >0:
                                    if player_x < 0:
                                        player_x = 0
                                    elif player_x > screen_width - player_width:
                                        player_x = screen_width - player_width
                                    if player_y < 0:
                                        player_y = 0
                                    elif player_y > screen_height - player_height:
                                        player_y = screen_height - player_height
                                        playery = 0
                                        jumptlfgod = False
                                        ground = True
                                    
                                    if enemy_x < 0:
                                        enemy_x = 0
                                    elif enemy_x > screen_width - enemy_width:
                                        enemy_x = screen_width - enemy_width
                                    if enemy_y < 0:
                                        enemy_y = 0
                                    elif enemy_y > screen_height - enemy_height:
                                        enemy_y = screen_height - enemy_height
                                        enemyy = 0
                                        e_jumptlfgod = False
                                        e_ground = True

                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    p_b1_rect = p_b1.get_rect()
                                    p_b1_rect.left = pb1_x
                                    p_b1_rect.top = pb1_y
                                    p_b2_rect = p_b2.get_rect()
                                    p_b2_rect.left = pb2_x
                                    p_b2_rect.top = pb2_y
                                    p_b3_rect = p_b3.get_rect()
                                    p_b3_rect.left = pb3_x
                                    p_b3_rect.top = pb3_y
                                    p_b4_rect = p_b4.get_rect()
                                    p_b4_rect.left = pb4_x
                                    p_b4_rect.top = pb4_y
                                    p_b5_rect = p_b5.get_rect()
                                    p_b5_rect.left = pb5_x
                                    p_b5_rect.top = pb5_y
                                    p_b6_rect = p_b6.get_rect()
                                    p_b6_rect.left = pb6_x
                                    p_b6_rect.top = pb6_y
                                    if p_b1_rect.colliderect(enemy_rect) and pb1_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb1_damage = False
                                    if p_b2_rect.colliderect(enemy_rect) and pb2_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb2_damage = False
                                    if p_b3_rect.colliderect(enemy_rect) and pb3_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb3_damage = False
                                    if p_b4_rect.colliderect(enemy_rect) and pb4_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb4_damage = False
                                    if p_b5_rect.colliderect(enemy_rect) and pb5_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb5_damage = False
                                    if p_b6_rect.colliderect(enemy_rect) and pb6_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 80
                                        else :
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        pb6_damage = False
                                    pb1_x += pb1x * dt
                                    pb1_y += pb1y * dt
                                    pb2_x += pb2x * dt
                                    pb2_y += pb2y * dt
                                    pb3_x += pb3x * dt
                                    pb3_y += pb3y * dt
                                    pb4_x += pb4x * dt
                                    pb4_y += pb4y * dt
                                    pb5_x += pb5x * dt
                                    pb5_y += pb5y * dt
                                    pb6_x += pb6x * dt
                                    pb6_y += pb6y * dt
                                    player_x += playerx * dt
                                    player_y += playery * dt
                                    enemy_x += enemyx * dt
                                    enemy_y += enemyy * dt
                                    sh_screen()
                                    pygame.display.update()
                                pe_start_time = time.time()
                                pb1_damage = True
                                pb2_damage = True
                                pb3_damage = True
                                pb4_damage = True
                                pb5_damage = True
                                pb6_damage = True
                    if event.key == pygame.K_LSHIFT:
                        if pd_end_time - pd_start_time >= 8:
                            pd = True
                            player_x += playerx * dt
                            sh_screen()
                            pygame.display.update()
                            pd_start_time = time.time()
                    if event.key == pygame.K_s:
                        if ps_end_time - ps_start_time >= 15:
                            if player_bullet >= 8:
                                player_bullet -= 8
                                player_bullet_m = ((bullet - player_bullet) / 0.1) * 7
                                pb1_x = player_x + (player_width / 2)
                                pb1_y = player_y + (player_height / 2)
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                pb1x = (mouse_x - pb1_x) /10
                                pb1y = (mouse_y - pb1_y) / 10
                                while pb1_x < screen_width and pb1_x > 0 and pb1_y < screen_height and pb1_y > 0:
                                    player_rect = player.get_rect()
                                    player_rect.left = player_x
                                    player_rect.top = player_y
                                    enemy_rect = enemy.get_rect()
                                    enemy_rect.left = enemy_x
                                    enemy_rect.top = enemy_y
                                    p_b1_rect = p_b1.get_rect()
                                    p_b1_rect.left = pb1_x
                                    p_b1_rect.top = pb1_y
                                    if p_b1_rect.colliderect(enemy_rect) and p_damage == True:
                                        if ed == False:
                                            enemy_hp_c -= 500
                                        else :
                                            enemy_hp_c -= 350
                                            ed = False
                                        if e_choice == 1:
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                        else :
                                            enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                        p_damage = False
                                    pb1_x += pb1x * dt
                                    pb1_y += pb1y * dt
                                    sh_screen()
                                    pygame.display.update()
                                ps_start_time = time.time()
                                p_damage = True

                          
            if p_choice == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pw_end_time = time.time()
                    if pw_end_time - pw_start_time >= 1:
                        if player_rect.colliderect(enemy_rect):
                            if ed == False:
                                enemy_hp_c -= 50
                            else :
                                ed = False
                            if e_choice == 1:
                                enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                            else :
                                enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                            pw_start_time = time.time()
            else :
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pw_end_time = time.time()
                    if pw_end_time - pw_start_time >= 1.5:
                        if player_bullet >= 1:
                            player_bullet -= 1
                            player_bullet_m = ((bullet - player_bullet) / 0.1) * 7
                            pb1_x = player_x + (player_width / 2)
                            pb1_y = player_y + (player_height / 2)
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            pb1x = (mouse_x - pb1_x) /100
                            pb1y = (mouse_y - pb1_y) / 100
                            while pb1_x < screen_width and pb1_x > 0 and pb1_y < screen_height and pb1_y > 0:
                                player_rect = player.get_rect()
                                player_rect.left = player_x
                                player_rect.top = player_y
                                enemy_rect = enemy.get_rect()
                                enemy_rect.left = enemy_x
                                enemy_rect.top = enemy_y
                                p_b1_rect = p_b1.get_rect()
                                p_b1_rect.left = pb1_x
                                p_b1_rect.top = pb1_y
                                if p_b1_rect.colliderect(enemy_rect) and p_damage == True:
                                    if ed == False:
                                        enemy_hp_c -= 100
                                    else :
                                        ed = False
                                    if e_choice == 1:
                                        enemy_hp_m = ((enemy_hp - enemy_hp_c) / 25) * 7
                                    else :
                                        enemy_hp_m = ((enemy_hp - enemy_hp_c) / 15) * 7
                                    pw_start_time = time.time()
                                    p_damage = False
                                pb1_x += pb1x * dt
                                pb1_y += pb1y * dt
                                sh_screen()
                                pygame.display.update()
                            p_damage = True
                                    
        if e_tlfgod == 0:
            enemyx = 0        
                
        if ed_end_time - ed_start_time >= 3:
            ed = False
                                    
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    playerx = 0        
              
        if pd_end_time - pd_start_time >= 3:
            pd = False
        
        if jumptlfgod == True:
            playery -= jump
            jump -= 0.02
            
        if e_jumptlfgod == True:
            enemyy -= e_jump
            e_jump -= 0.02
                    
        if player_x < 0:
            player_x = 0
        elif player_x > screen_width - player_width:
            player_x = screen_width - player_width
        if player_y < 0:
            player_y = 0
        elif player_y > screen_height - player_height:
            player_y = screen_height - player_height
            playery = 0
            jumptlfgod = False
            ground = True
        
        if enemy_x < 0:
            enemy_x = 0
        elif enemy_x > screen_width - enemy_width:
            enemy_x = screen_width - enemy_width
        if enemy_y < 0:
            enemy_y = 0
        elif enemy_y > screen_height - enemy_height:
            enemy_y = screen_height - enemy_height
            enemyy = 0
            e_jumptlfgod = False
            e_ground = True

                
        if player_hp_c <= 0:
            win_value = False
            running = False
        elif enemy_hp_c <= 0:
            win_value = True
            running = False
        
        if player_mana < mana:
            player_mana += 0.5
        if enemy_mana < mana:
            enemy_mana += 0.5
        player_mana_m = ((mana - player_mana) / 1.5) * 7
        enemy_mana_m = ((mana - enemy_mana) / 1.5) * 7
        
        if player_bullet > bullet:
            player_bullet = bullet
        if enemy_bullet > bullet:
            enemy_bullet = bullet
        player_bullet_m = ((bullet - player_bullet) / 0.1) * 7
        enemy_bullet_m = ((bullet - enemy_bullet) / 0.1) * 7
        
        player_rect = player.get_rect()
        player_rect.left = player_x
        player_rect.top = player_y
    
        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x
        enemy_rect.top = enemy_y
        
        player_x += playerx * dt
        player_y += playery * dt
        enemy_x += enemyx * dt
        enemy_y += enemyy * dt
                
        sh_screen()
        
        pygame.display.update()
    
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                end = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    end = False
        if win_value == True:
            screen.blit(win, (0, 0))
        else :
            screen.blit(lose, (0, 0))
        pygame.display.update()
    
pygame.quit()