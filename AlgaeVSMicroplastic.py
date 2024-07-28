import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = pygame.Color("white")
RED = pygame.Color("red")
BLUE = pygame.Color("blue")
BLACK = pygame.Color("black")
YELLOW = pygame.Color("yellow")

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("AlgaeVSMicroplastic")

# Load background image
background = pygame.image.load('image/background.jpg').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load boss texture
boss_texture = pygame.image.load("image/boss.png").convert_alpha()
boss_texture = pygame.transform.scale(boss_texture, (175, 175))

# Load player image
player_image = pygame.image.load("image/player.png").convert_alpha()
player_image = pygame.transform.scale(player_image, (140, 140))

# Load enemy image
enemy_image = pygame.image.load("image/enemy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (70, 70))

# Load special enemy image
special_enemy_image = pygame.image.load("image/specialenemy.png").convert_alpha()
special_enemy_image = pygame.transform.scale(special_enemy_image, (70, 70))

# Load bullet image
bullet_image = pygame.image.load("image/bullet.png").convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (40, 40))

# Load escape menu image
esc_menu_image = pygame.image.load("image/esc_menu.png").convert_alpha()
esc_menu_image = pygame.transform.scale(esc_menu_image, (500, 500))

# Load quit and restart button images
quit_button_image = pygame.image.load("image/quit.png").convert_alpha()
restart_button_image = pygame.image.load("image/restart.png").convert_alpha()

# Load intro background image
intro_background_image = pygame.image.load("image/introbg.jpg").convert()
intro_background_image = pygame.transform.scale(intro_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load homepage background image
homepage_background = pygame.image.load("image/homepagebg.png").convert()
homepage_background = pygame.transform.scale(homepage_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load start button and infinite mode image
start_button_image = pygame.image.load("image/start.png").convert_alpha()
infinite_button_image = pygame.image.load("image/infinite_button.png").convert_alpha()
rules_button_image = pygame.image.load("image/rules_button.png").convert_alpha()
back_button_image = pygame.image.load("image/back_button.png").convert_alpha()
rules_left_button_image = pygame.image.load("image/rules_left_button.png").convert_alpha()
rules_right_button_image = pygame.image.load("image/rules_right_button.png").convert_alpha()

# Load phases image
phase_one_image = pygame.image.load("image/phase_one.jpg").convert()
phase_two_image = pygame.image.load("image/phase_two.jpg").convert()
phase_three_image = pygame.image.load("image/phase_three.jpg").convert()
phase_one_image = pygame.transform.scale(phase_one_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
phase_two_image = pygame.transform.scale(phase_two_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
phase_three_image = pygame.transform.scale(phase_three_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule1_image = pygame.image.load("image/rules1.jpg").convert()
rule1_image = pygame.transform.scale(rule1_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule2_image = pygame.image.load("image/rules2.jpg").convert()
rule2_image = pygame.transform.scale(rule2_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule3_image = pygame.image.load("image/rules3.jpg").convert()
rule3_image = pygame.transform.scale(rule3_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule4_image = pygame.image.load("image/rules4.jpg").convert()
rule4_image = pygame.transform.scale(rule4_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule5_image = pygame.image.load("image/rules5.jpg").convert()
rule5_image = pygame.transform.scale(rule5_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule6_image = pygame.image.load("image/rules6.jpg").convert()
rule6_image = pygame.transform.scale(rule6_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule7_image = pygame.image.load("image/rules7.jpg").convert()
rule7_image = pygame.transform.scale(rule7_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

rule_images = [rule1_image, rule2_image, rule3_image, rule4_image, rule5_image, rule6_image, rule7_image]
current_rule_index = 0  # Index of the currently displayed rule image

# Scale the button images
button_width = 200
button_height = 200
start_button_image = pygame.transform.scale(start_button_image, (button_width, button_height))
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))
restart_button_image = pygame.transform.scale(restart_button_image, (button_width, button_height))
infinite_button_image = pygame.transform.scale(infinite_button_image, (button_width, button_height))
rules_left_button_image = pygame.transform.scale(rules_left_button_image, (100, 100))
rules_right_button_image = pygame.transform.scale(rules_right_button_image, (100, 100))
rules_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 45, button_width, button_height)
rules_button_image = pygame.transform.scale(rules_button_image, (100, 100))
rules_button_rect = rules_button_image.get_rect()
rules_button_rect.center = (SCREEN_WIDTH // 2 + 250, SCREEN_HEIGHT // 2 - 125)
rules_left_button_rect = rules_left_button_image.get_rect()
rules_left_button_rect.bottomleft = (20, SCREEN_HEIGHT - 20)
rules_right_button_rect = rules_right_button_image.get_rect()
rules_right_button_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
back_button_image = pygame.transform.scale(back_button_image, (100, 100))
back_button_rect = back_button_image.get_rect(topleft=(20, 20))  # Position on top-left

# Load background music
pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.play(-1)  # Play background music indefinitely

# Clock
clock = pygame.time.Clock()

# Initialize fonts
pygame.font.init()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Global variables
global lose
global player_speed
player_speed = 10
lose = 0
score = 0
game_paused = False
last_special_spawn_score = 0  # Initialize last special spawn score
player_speed = 10  # Initial player speed
bullet_cooldown = 0.2  # Bullet cooldown in seconds

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global bullet_cooldown
        self.image = player_image
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10))
        self.last_shot_time = 0  # Timestamp of the last shot
        bullet_cooldown = 200  # Initial cooldown in milliseconds
        self.speed = player_speed  # Initial speed of the player

    def update(self):
        self.speed = player_speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        global bullet_cooldown
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > bullet_cooldown:  
            bullet = Bullet(self.rect)
            bullets.add(bullet)
            all_sprites.add(bullet)
            self.last_shot_time = now

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect(center=(random.randint(100, SCREEN_WIDTH - 100), -25))
        self.speed_x = 5
        self.speed_y = 3
        self.target_x = random.randint(100, SCREEN_WIDTH - 100)
        self.stopped = False

    def update(self):
        if not self.stopped:
            if self.rect.centerx < self.target_x:
                self.rect.x += self.speed_x
            elif self.rect.centerx > self.target_x:
                self.rect.x -= self.speed_x

            if abs(self.rect.centerx - self.target_x) <= abs(self.speed_x):
                self.stopped = True
                self.speed_x = 0

        self.rect.y += self.speed_y

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove the enemy sprite if it goes off screen

class SpecialEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = special_enemy_image
        self.rect = self.image.get_rect(midtop=(SCREEN_WIDTH / 2, 0))
        self.speed_x = 10
        self.speed_y = 5
        self.target_x = random.randint(100, SCREEN_WIDTH - 100)

    def update(self):
        if self.rect.centerx < self.target_x:
            self.rect.x += self.speed_x
        elif self.rect.centerx > self.target_x:
            self.rect.x -= self.speed_x
        
        self.rect.y += self.speed_y

        if abs(self.rect.centerx - self.target_x) <= abs(self.speed_x):
            self.target_x = random.randint(100, SCREEN_WIDTH - 100)

    def spawn_at_boss(self, boss_rect):
        self.rect.midtop = boss_rect.midtop

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.midtop = player_rect.midtop

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it goes off screen

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = boss_texture
        self.rect = self.image.get_rect(midtop=(SCREEN_WIDTH / 2, -250))
        self.health = 250
        self.max_health = 250
        self.speed = 5
        self.stopped = False
        self.last_enemy_launch = pygame.time.get_ticks()
        self.enemy_cooldown = 2000  # Cooldown for regular enemies
        self.target_x = self.rect.centerx
        self.bossbar_length = 200
        self.bossbar_height = 20
        self.bossbar_color = RED

    def update(self):
        if not self.stopped:
            self.rect.y += 5

            if self.rect.top >= SCREEN_HEIGHT // 15:
                self.stopped = True
                self.last_enemy_launch = pygame.time.get_ticks()

        now = pygame.time.get_ticks()
        if now - self.last_enemy_launch > self.enemy_cooldown:
            self.last_enemy_launch = now
            self.spawn_enemy()

        if abs(self.rect.centerx - self.target_x) <= 17.5:
            self.target_x = random.randint(100, SCREEN_WIDTH - 100)

        if self.rect.centerx < self.target_x:
            self.rect.x += self.speed
        elif self.rect.centerx > self.target_x:
            self.rect.x -= self.speed

    def spawn_enemy(self):
        enemy = Enemy()
        enemy.rect.midbottom = self.rect.midbottom
        enemies.add(enemy)
        all_sprites.add(enemy)

    def spawn_special_enemy(self):
        special_enemy = SpecialEnemy()
        special_enemy.spawn_at_boss(self.rect)
        special_enemies.add(special_enemy)
        all_sprites.add(special_enemy)

    def die(self):
        global game_paused
        game_paused = True  # Pause the game on boss defeat
        self.kill()  # Remove the boss sprite

def game_over():
    global game_paused
    global lose
    lose = 2
    game_paused = True  # Pause the game on game over

def win():
    global game_paused
    global lose
    lose = 1
    game_paused = True  # Pause the game on win

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def reset_game():
    global score, last_special_spawn_score, game_paused, player_speed, lose, bullet_cooldown, phase, last_special_spawn_score, player_speed_addon, bullet_cooldown_addon, enzyme_efficiency_addon, enzyme_efficiency

    phase = 0
    player_speed_addon = 0
    lose = 0
    enzyme_efficiency = 3
    boss.rect = boss.image.get_rect(midtop=(SCREEN_WIDTH / 2, -250))
    score = 0
    bullet_cooldown_addon = 0
    player.rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
    player.last_shot_time = 0
    bullet_cooldown = 200
    SpecialEnemy.speed_x = 10
    SpecialEnemy.speed_y = 5
    Enemy.speed_y = 3
    Boss.speed = 5
    player_speed = 10
    boss.health = 250
    boss.speed = 5
    boss.rect.midtop = (SCREEN_WIDTH / 2, -250)
    boss.stopped = False
    boss.last_enemy_launch = pygame.time.get_ticks()
    boss.target_x = boss.rect.centerx
    boss.enemy_cooldown = 2000
    enzyme_efficiency_addon = 0
    last_special_spawn_score = 0
    enemies.empty()
    special_enemies.empty()
    bullets.empty()
    all_sprites.empty()
    all_sprites.add(player)
    all_sprites.add(boss)
    boss.stopped = False  # Ensure boss can move again

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
special_enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create player and boss instances
player = Player()
boss = Boss()
all_sprites.add(player, boss)

restart_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 4, button_width, button_height)
quit_button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, SCREEN_HEIGHT // 4 + 150, button_width, button_height)

def show_rules():
    global current_rule_index
    
    # Display initial rule image
    current_rule_index = 0
    screen.blit(rule_images[current_rule_index], (0, 0))
    pygame.display.flip()  # Update screen
    
    waiting_for_esc = True
    while waiting_for_esc:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting_for_esc = False
                elif event.key == pygame.K_RIGHT and current_rule_index != 6:
                    current_rule_index += 1
                elif event.key == pygame.K_LEFT and current_rule_index != 0:
                    current_rule_index -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if back button is clicked
                if back_button_rect.collidepoint(event.pos):
                    waiting_for_esc = False
                elif rules_right_button_rect.collidepoint(event.pos) and current_rule_index != 6:
                    current_rule_index += 1
                elif rules_left_button_rect.collidepoint(event.pos) and current_rule_index != 0:
                    current_rule_index -= 1
        
        # Redraw current rule image
        screen.blit(rule_images[current_rule_index], (0, 0))
        # Draw buttons
        screen.blit(back_button_image, back_button_rect)
        if current_rule_index < 6:
            screen.blit(rules_right_button_image, rules_right_button_rect)
        if current_rule_index > 0:
            screen.blit(rules_left_button_image, rules_left_button_rect)
        
        pygame.display.flip()

def display_intro(screen):
    intro_text = (
        '''         Since the beginning of human
        plastic production, a little demon
        called microplastics has gradually
        appeared in the ocean. Cyanobacteria
        are organisms that consume these
        microplastics; the microplastics enter
        our bodies, affecting our health.
        However, with the advancement of
        human technology, our BASIS-China
        team has discovered a method to
        degrade microplastics in the ocean.
        We will implant plastic-degrading
        enzymes into cyanobacteria, allowing
        them to break down microplastics in
        the ocean. This way, the amount of
        microplastics in the ocean is decreasing
        more and more!!
        How to play:
        Use left and right key to move the algae
        Use space bar to shoot algae bullets 
        Kill the boss and also, don't let the
        microplastic hit you or go to the
        bottom of the screen
        Press esc in game for the game menu and
        press esc again to resume.
        
        Press Any key to continue . . .'''
    )

    screen.blit(intro_background_image, (0, 0))
    x, y = 100, SCREEN_HEIGHT - 50  # Start just below the screen
    clock = pygame.time.Clock()

    # Split intro_text into lines
    lines = intro_text.splitlines()

    # Calculate where the last line should stop
    last_line_y = y - len(lines) * 28

    # Scroll up the entire block of text
    while y >= last_line_y:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(intro_background_image, (0, 0))
        
        # Calculate the starting position for drawing lines
        start_y = y
        
        for i, line in enumerate(lines):
            # Calculate the y position for each line
            line_y = start_y + i * 30
            
            # Only draw the line if it's still on screen
            if line_y >= 50:  # Only draw if y is greater than or equal to 50
                draw_text(line, pygame.font.Font(None, 36), WHITE, screen, x, line_y)
        
        pygame.display.flip()

        scroll_speed = 0.55
        y -= scroll_speed

        clock.tick(60)  # Ensure smooth animation

    # Wait for user to release the key before proceeding
    waiting_for_key_release = True
    while waiting_for_key_release:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                waiting_for_key_release = False

def phase_one():
    global player_speed
    global bullet_cooldown
    screen.blit(phase_one_image, (0, 0))
    bullet_cooldown = 150
    player_speed = 10
    boss.speed = 5
    boss.health = 250

def phase_two():
    global player_speed_addon
    global bullet_cooldown
    boss.enemy_cooldown = 1500
    screen.blit(phase_two_image, (0, 0))
    bullet_cooldown += 25
    boss.speed = 7.5
    player_speed_addon -= 2
    boss.health = 150

def phase_three():
    global player_speed_addon
    global bullet_cooldown
    boss.enemy_cooldown = 750
    screen.blit(phase_three_image, (0, 0))
    bullet_cooldown += 75
    player_speed_addon -= 4
    boss.health = 100
    boss.speed = 10

# Main game loop
infinite_mode = 0
start_button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2 - 100, SCREEN_HEIGHT - 250, button_width, button_height)
infinite_button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2 + 100, SCREEN_HEIGHT - 250, button_width, button_height)
show_homepage = True
enzyme_efficiency = 3
last_special_spawn_score
bullet_cooldown_addon = 0
enzyme_efficiency_addon = 0
running = True
player_speed_addon = 0
phase = 0
display_intro(screen)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and lose == 0:
                if game_paused:
                    game_paused = False  # Resume game
                else:
                    game_paused = True  # Pause game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if show_homepage:
                # Check if mouse click is within the start button area
                if start_button_rect.collidepoint(mouse_pos):
                    show_homepage = False  # Start the game
                    infinite_mode = False
                elif infinite_button_rect.collidepoint(mouse_pos):
                    show_homepage = False  # Start the game (infinite mode)
                    infinite_mode = True
                elif rules_button_rect.collidepoint(event.pos):
                    # Handle rules button click action
                    show_rules()
            elif game_paused:
                if restart_button_rect.collidepoint(mouse_pos):
                    reset_game()
                    game_paused = False
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.time.wait(350)
                    reset_game()
                    show_homepage = True  # Return to homepage

    # Display homepage or game paused menu
    if show_homepage:
        screen.blit(homepage_background, (0, 0))
        screen.blit(rules_button_image, rules_button_rect)
        screen.blit(start_button_image, (start_button_rect.x, start_button_rect.y))
        screen.blit(infinite_button_image, infinite_button_rect)
        game_paused = False  # Ensure game isn't paused on homepage
    elif game_paused:
        tmpfont = pygame.font.Font('font/Pixeltype.ttf', 100)
        if lose == 2:
            screen.blit(esc_menu_image, (150, 50))
            screen.blit(restart_button_image, restart_button_rect)
            screen.blit(quit_button_image, quit_button_rect)
            draw_text("Game Over", tmpfont, WHITE, screen, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20)
        elif lose == 1:
            screen.blit(esc_menu_image, (150, 50))
            screen.blit(restart_button_image, restart_button_rect)
            screen.blit(quit_button_image, quit_button_rect)
            draw_text("  You WIN!!", tmpfont, WHITE, screen, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20)
        elif lose == 0:
            screen.blit(esc_menu_image, (150, 50))
            screen.blit(restart_button_image, restart_button_rect)
            screen.blit(quit_button_image, quit_button_rect)

    else:
        # Game is running

        # Check if infinite mode
        if infinite_mode == 1:
            boss.health = 250
        else:
            # Phase one
            if boss.health == 250 and phase != 1:
                phase = 1
                phase_one()  # Initialize phase one settings
                pygame.display.flip()  # Update display
                pygame.time.wait(2000)  # Wait after displaying phase image

            # Phase two
            elif boss.health == 150 and phase != 2:
                phase = 2
                phase_two()  # Initialize phase two settings
                pygame.display.flip()  # Update display
                pygame.time.wait(2000)  # Wait after displaying phase image

            # Last phase
            elif boss.health == 50 and phase != 3:
                phase = 3
                phase_three()  # Initialize phase three settings
                pygame.display.flip()  # Update display
                pygame.time.wait(2000)  # Wait after displaying phase image

        # Limit player within screen boundaries
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        # Limit addons to the player
        if player_speed_addon >= 5:
            player_speed_addon = 5
        if bullet_cooldown_addon > 50:
            bullet_cooldown_addon = 50
            enzyme_efficiency_addon -= 1
        
        # Shooting logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Update sprites
        all_sprites.update()
        
        if infinite_mode == True:
            boss.speed = 5 + score / 50
            if boss.speed >= 15:
                boss.speed = 15
            boss.enemy_cooldown = 2000 - score * 10
            if boss.enemy_cooldown <= 150:
                boss.enemy_cooldown = 150
        
        # Collision detection
        hits_player_special_enemy = pygame.sprite.spritecollide(player, special_enemies, True)
        for special_enemy in hits_player_special_enemy:
            game_over()

        hits_player_enemies = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits_player_enemies:
            game_over()

        hits_enemy_bullets = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits_enemy_bullets:
            score += 1

        for enemy in enemies.copy():
            if enemy.rect.bottom > SCREEN_HEIGHT:
                game_over()
        
        for special_enemy in special_enemies.copy():
            if special_enemy.rect.bottom > SCREEN_HEIGHT:
                game_over()
        
        if infinite_mode == False:
            hits_boss_bullets = pygame.sprite.spritecollide(boss, bullets, True)
            for hit in hits_boss_bullets:
                boss.health -= 1
                score += 1
                if boss.health <= 0:
                    boss.kill()
                    win()
        else:
            hits_boss_bullets = pygame.sprite.spritecollide(boss, bullets, True)
            for hit in hits_boss_bullets:
                score += 1

        hits_special_bullets = pygame.sprite.groupcollide(special_enemies, bullets, True, True)
        for hit_special in hits_special_bullets.items():
            rdeffectlist = [1, 2]
            rdeffect = random.choice(rdeffectlist)
            if rdeffect == 1:
                player_speed_addon += 1
            elif rdeffect == 2:
                bullet_cooldown_addon += 25
                enzyme_efficiency_addon += 1
            
            special_enemies.empty()
            
        player_speed = 10 + player_speed_addon
        bullet_cooldown = 150 - bullet_cooldown_addon
        
        # Spawn special enemy based on score
        if score > 0 and score % 40 == 0 and score != last_special_spawn_score:
            boss.spawn_special_enemy()
            last_special_spawn_score = score

        # Draw everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)

        # Draw boss health bar
        bossbar_width = int(boss.bossbar_length * (boss.health / boss.max_health))
        bossbar_rect = pygame.Rect((SCREEN_WIDTH - boss.bossbar_length) // 2 - 50, 10, bossbar_width, boss.bossbar_height)
        pygame.draw.rect(screen, boss.bossbar_color, bossbar_rect)

        # Update enzyme efficiency based on game phases (only update once per phase change)
        tmp_enzyme_efficiency = 3
        last_enzyme_efficiency = enzyme_efficiency
        if infinite_mode == 0:
            if phase == 1:
                enzyme_efficiency = 3
                tmp_enzyme_efficiency = 3
            elif phase == 2:
                enzyme_efficiency = 2
                tmp_enzyme_efficiency = 2
            elif phase == 3:
                enzyme_efficiency = 1
                tmp_enzyme_efficiency = 1
        
        enzyme_efficiency = tmp_enzyme_efficiency + enzyme_efficiency_addon

        # Draw score
        draw_text(f"Score: {score}", font, BLACK, screen, 10, 10)
        # Draw speed and bullet cooldown
        draw_text(f"Speed: {player_speed}", font, BLACK, screen, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50)
        draw_text(f"Enzyme Efficiency: {enzyme_efficiency}", font, BLACK, screen, 10, SCREEN_HEIGHT - 50)
        # Draw boss health
        if infinite_mode == 0:
            draw_text(f"Boss Health: {boss.health}", font, BLACK, screen, SCREEN_WIDTH - 275, 10)
        else:
            draw_text("Boss Health: Infinite", font, BLACK, screen, SCREEN_WIDTH - 300, 10)

    pygame.display.flip()  # Update the entire screen
    clock.tick(60)  # Control frame rate

pygame.quit() 
sys.exit()