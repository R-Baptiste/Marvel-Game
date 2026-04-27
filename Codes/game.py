import pygame 
import random
import pytmx
import pyscroll
import pygame
import numpy as np
from moviepy import VideoFileClip

from unit import *
from menu import *
from sound import *


fond = pygame.image.load('Menu/Wallpaper.png')

class Game:
    
    
    def __init__(self, screen):
        
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1220, 700
        self.display = pygame.Surface((self.DISPLAY_W ,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W ,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)


        self.main_menu = MainMenu(self) # instantiation of self.main_menu from MainMenu class in menu.py
        self.options = OptionsMenu(self) # instantiation of self.options from OptionsMenu class in menu.py
        self.credits = CreditsMenu(self) # instantiation of self.credits from CreditsMenu class in menu.py
        
        
        self.Choix_Personnages_1 = Character_Selection_Menu_1(self) # instantiation of self.Choix_Personnages_1 from Character_Selection_Menu_1 in menu.py
        self.Choix_Personnages_2 = Character_Selection_Menu_2(self) # instantiation of self.Choix_Personnages_2 from Character_Selection_Menu_2 in menu.py
        self.Choix_Personnages_3 = Character_Selection_Menu_3(self) # instantiation of self.Choix_Personnages_3 from Character_Selection_Menu_3 in menu.py
        self.Choix_Personnages_4 = Character_Selection_Menu_4(self) # instantiation of self.Choix_Personnages_4 from Character_Selection_Menu_4 in menu.py
        self.Choix_Carte = Map_Selection_Menu(self)
        self.curr_menu = self.main_menu

        # manage sound
        self.sound_manager = SoundManager()
        self.Volume = Volume(self)
        self.Musique = Volume(self)

         # Game mode
        self.Mode = Mode(self)
        self.game_mode_menu = Mode(self)

        self.selected_attack_obj = No_Action()
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        self.menu_attaques = False
        self.selected_attack = False
        self.list_enemy_health = []
        self.list_player_health = []
        self.player_units = []
        self.enemy_units = []
        self.is_selected = False
        
    
    def draw_attack_menu(self) :
        """Draw the attack menu."""
        # Black background in the lower left corner
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 530, 250, 150 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 530, 250, 150), 2)  # Bordure blanche

    

        list_attacks = self.attaques
        # Draw each attack in the rectangle
        for i, attaque in enumerate(list_attacks):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Highlight selected attack
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 550 + i * 30))  # Position attacks

    def cases_teleportation(self, screen):
        self.cases_tp = [(4, 6), (3, 16), (27, 11)]  # List of teleportation cells

        for player in self.player_units + self.enemy_units:  # Iterate through players and enemies
            for i in range(0, len(self.cases_tp)):  # Iterate through valid indices of the teleportation cells list
                if (player.x, player.y) == self.cases_tp[i]:
                    # Select an arrival cell different from the current cell
                    available_cases = [0, 1, 2]  # Teleportation cell indices
                    available_cases.remove(i)  # Remove the current cell index

                    # Choose an arrival cell from the remaining indices
                    r = random.choice(available_cases)
                    (self.arrivex,self.arrivey) = self.cases_tp[r]  # Select the arrival cell
                    player.x, player.y = (self.arrivex+1,self.arrivey+1)  # Update player coordinates
                    break  # Exit the loop as soon as a teleportation is performed
                    
                
                
    def cases_soin(self, screen):
     
        self.case_soin=[[23,10],[24,10],[24,11],[23,11],[7,17],[8,17],[7,18],[8,18]]
        color = WHITE
        color1=(20,255,20)
        half_size = CELL_SIZE // 2  # Half the cell size
        line_width = 15  # Cross line thickness
      
        for i, player in enumerate(self.player_units):
            for j in range(0,len(self.case_soin)):
                if player.x==self.case_soin[j][0] and player.y== self.case_soin[j][1]:
                    hero_selected = player.assign_character_class()
                    self.list_player_health[i] = hero_selected.health_max
                    print (f"{hero_selected.name} was healed")
        return self.list_player_health


    def cases_degat(self, screen):
        self.case_degat = [[13,15],[14,15],[15,15],[16,15],[17,15],[18,15],[19,13],[20,13],[21,13],[22,13],[23,13],[24,13]]
       
        degat = 5
        
        for i, player in enumerate(self.player_units) :
            for j in range(0,len(self.case_degat)):
                if player.x==self.case_degat[j][0] and player.y== self.case_degat[j][1]:
                    player_health = self.list_player_health[i]
                    player_health -= degat
                    print(player_health)
                    print("player was injured on the minefield")
                    self.list_player_health[i] = player_health
        
        for i, enemy in enumerate(self.enemy_units) :
            for j in range(0,len(self.case_degat)):
                if enemy.x==self.case_degat[j][0] and enemy.y== self.case_degat[j][1]:
                    enemy_health = self.list_enemy_health[i]
                    enemy_health -= degat
                    print(enemy_health)
                    print("enemy was injured on the minefield")
                    self.list_enemy_health[i] = enemy_health
        
        return self.list_enemy_health
                  

    def handle_player_turn(self):
        """Player turn"""
        print ("START OF PLAYER TURN")

        for selected_unit in self.player_units:
            selected_unit.is_selected = True
            has_acted = False            
            selected_unit.update_green_case(self.player_units, self.enemy_units)
            hero_selected = selected_unit.assign_character_class()
            health = hero_selected.get_health()
            self.selected_attack_index = 0
            nbre_move = hero_selected.nbre_move
            defense = hero_selected.defense
            print (f"unit is: {selected_unit.name}")
            print(f"Health points: {health}, move_count = {nbre_move}, defense = {defense}")
            self.flip_display()
            
            while not has_acted:
                
                # Important: this loop handles Pygame events
                for event in pygame.event.get():

                    # Handle window close
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    # Handle keyboard keys
                    elif event.type == pygame.KEYDOWN:
                        if self.menu_attaques == False :
                        # Movement (arrow keys)
                            dx, dy = 0, 0
                            if event.key == pygame.K_LEFT:
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                dx = 1
                            elif event.key == pygame.K_UP and not self.menu_attaques:
                                dy = -1
                                
                            elif event.key == pygame.K_DOWN and not self.menu_attaques:
                                dy = 1
                                
                            selected_unit.move(dx, dy)
                            
                        

                        # Attack (space key) ends the turn
                            if event.key == pygame.K_SPACE:
                                self.attaques = hero_selected.list_attaques
                                self.menu_attaques = True # activate attack menu

                            # Navigate attack menu
                        if self.menu_attaques :
                            selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            if event.key == pygame.K_DOWN:
                                self.selected_attack_index = (self.selected_attack_index + 1) % len(self.attaques) # Navigate attack menu vers le haut
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            elif event.key == pygame.K_UP:
                                self.selected_attack_index = (self.selected_attack_index - 1) % len(self.attaques) # Navigate attack menu vers le bas
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            elif event.key == pygame.K_RETURN :
                                self.selected_attack = True
                                self.menu_attaques = False
                                attaque_selectionne = hero_selected.assign_attack_class(self.selected_attack_index)

                                for i, enemy in enumerate (self.enemy_units) :
                                    enemy_selected = enemy.assign_character_class() 
                                    enemy_health = self.list_enemy_health[i]                           
                                    new_enemy_health = selected_unit.attack(attaque_selectionne, enemy_selected, enemy_health)
                                    self.list_enemy_health[i] = new_enemy_health

                                    if enemy_health <= 0 :
                                        print(f"{enemy.name} is dead") 
                                        self.enemy_units.remove(enemy)
                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                    self.flip_display()   

        return self.list_enemy_health
                            
                
    def handle_player_2_turn(self):
        """Player turn"""
        print ("START OF PLAYER TURN")
        for selected_unit in self.enemy_units:
            selected_unit.is_selected = True
            has_acted = False
            
    
            selected_unit.update_green_case(self.enemy_units, self.player_units)
            hero_selected = selected_unit.assign_character_class()
            #health = hero_selected.get_health()
            self.selected_attack_index = 0
            self.flip_display()
            
            while not has_acted:
                
                # Important: this loop handles Pygame events
                for event in pygame.event.get():

                    # Handle window close
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()


                    # Handle keyboard keys
                    elif event.type == pygame.KEYDOWN:
                        if self.menu_attaques == False :
                        # Movement (arrow keys)
                            dx, dy = 0, 0
                            if event.key == pygame.K_LEFT:
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                dx = 1
                            elif event.key == pygame.K_UP and not self.menu_attaques:
                                dy = -1
                                
                            elif event.key == pygame.K_DOWN and not self.menu_attaques:
                                dy = 1
                                
                            selected_unit.move(dx, dy)
                            
                        

                        # Attack (space key) ends the turn
                            if event.key == pygame.K_SPACE:
                                self.attaques = hero_selected.list_attaques
                                self.menu_attaques = True # activate attack menu

                            # Navigate attack menu

                        if self.menu_attaques :
                            selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            if event.key == pygame.K_DOWN:
                                self.selected_attack_index = (self.selected_attack_index + 1) % len(self.attaques) # Navigate attack menu vers le haut
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            elif event.key == pygame.K_UP:
                                self.selected_attack_index = (self.selected_attack_index - 1) % len(self.attaques) # Navigate attack menu vers le bas
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            elif event.key == pygame.K_RETURN :
                                self.selected_attack = True
                                self.menu_attaques = False
                                attaque_selectionne = hero_selected.assign_attack_class(self.selected_attack_index)
                                
                                for i, player in enumerate (self.player_units) :
                                    player_selected = player.assign_character_class()  
                                    player_health = self.list_player_health[i]    
                                    new_player_health = selected_unit.attack(attaque_selectionne, player_selected, player_health)
                                    self.list_player_health[i] = new_player_health

                                    if player_health <= 0 :
                                        print(f"{player.name} is dead") 
                                        self.player_units.remove(player)
                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                    self.flip_display()   

        return self.list_player_health

    def find_closest_green_case(self, green_cases, target_x, target_y):
        """Find the green cell closest to the target."""
        return min(green_cases, key=lambda case: abs(case[0] - target_x) + abs(case[1] - target_y))


    
    def handle_enemy_turn(self):
        """Very simple AI for enemies."""
        print ("START OF ENEMY TURN")
        
        for enemy in self.enemy_units:
            
            enemy_selected = enemy.assign_character_class()
            print(f"CHOSEN ENEMY IS {enemy_selected.name}")
              
            # Choose the closest target
            enemy.is_selected = True
            enemy.update_green_case(self.player_units, self.enemy_units)
            
            # Determine the closest target
            target_1 = self.player_units[0]
            target_2 = self.player_units[1]
            dist_1 = np.sqrt((target_1.x - enemy.x) ** 2 + (target_1.y - enemy.y) ** 2)
            dist_2 = np.sqrt((target_2.x - enemy.x) ** 2 + (target_2.y - enemy.y) ** 2)
            target = target_1 if dist_1 < dist_2 else target_2

            i = self.player_units.index(target) 
            print (f"index for targeted player choice is i = {i}")
            
            # Move toward target
            best_green_case = self.find_closest_green_case(enemy.green_cases, target.x, target.y)
            for step in range(10, 0, -1):  # Start by trying maximum movement (10)
                dx = step if enemy.x < best_green_case[0] else -step if enemy.x > best_green_case[0] else 0
                dy = step if enemy.y < best_green_case[1] else -step if enemy.y > best_green_case[1] else 0

                # Attempt to move
                previous_x, previous_y = enemy.x, enemy.y  # Save current position
                enemy.move(dx, dy)
            
                # Vérifier si le déplacement a été effectué
                if (enemy.x, enemy.y) != (previous_x, previous_y):  # If position changed
                    break  # Stop loop as soon as a movement is performed

            # Attack if possible
            
            player_selected = target.assign_character_class() 
            # choose an attack
            if abs(enemy.x - player_selected.x) <= enemy.distance_maxi_attack and abs(enemy.y - player_selected.y) <= enemy.distance_maxi_attack :
                enemy_attack = random.choice(enemy_selected.list_attaques[1:])
                indice = enemy_selected.list_attaques.index(enemy_attack)
                print (f"index for enemy attack is {indice}" )
                enemy_attack_selected = enemy_selected.assign_attack_class(indice) 
                print (f"enemy attack is {enemy_attack_selected.name}")
                player_health = self.list_player_health[i]
                print (f"MY LIFE HANGS BY {player_health}")
                new_player_health = enemy_selected.eni_attack(enemy_attack_selected, player_selected, player_health)
                self.list_player_health[i] = new_player_health
                print (f"DEATH IF I DO BLI {new_player_health}")
            else :
                enemy_attack_selected = No_Action()
                print("I chose not to attack")

                player_health = self.list_player_health[i]

            if player_health <= 0:
                print(f"{target.name} is dead")
                self.player_units.remove(target)
            
            self.flip_display()

            enemy.is_selected = False
            pygame.time.wait(1000)
        play = True
        return play, self.list_player_health

    def flip_display(self):
        """Displays the map and game elements."""
        # Load map data
        tmx_data = pytmx.util_pygame.load_pygame('map_cyber.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        
        # Render the map
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1  # Adjust if necessary
        
        # Pyscroll group for sprites and map
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=5)
       
        # Draw the map
        self.group.update()
        self.group.draw(self.screen)
        
        # draw logo
        logo_marvel=pygame.image.load('Map/Marvel_Logo.png')
        logo_marvel=pygame.transform.scale(logo_marvel,(32*9,32*3))
        self.screen.blit(logo_marvel,(32*4,12))

        # Draw text
        door=pygame.image.load('Map/Door.png')
        door=pygame.transform.scale(door,(32,32))
        self.screen.blit(door,(32*25 + 10,32*18 + 10))
        teleport=pygame.image.load('Map/Text_teleport.png')
        teleport=pygame.transform.scale(teleport,(32*6,32))
        self.screen.blit(teleport,(32*26 + 10,32*18 + 10))

        heal=pygame.image.load('Map/Heal.png')
        heal=pygame.transform.scale(heal,(32,32))
        self.screen.blit(heal,(32*25 + 10,32*19 + 10))
        heal_texte=pygame.image.load('Map/Text_heal.png')
        heal_texte=pygame.transform.scale(heal_texte,(32*3,32))
        self.screen.blit(heal_texte,(32*26 + 10,32*19 + 10))

        damage=pygame.image.load('Map/Damage.png')
        damage=pygame.transform.scale(damage,(32,32))
        self.screen.blit(damage,(32*25 + 10, 32*20 + 10))
        damage_text=pygame.image.load('Map/Text_damage.png')
        damage_text=pygame.transform.scale(damage_text,(32*4 - 15,32))
        self.screen.blit(damage_text,(32*26 + 10,32*20 + 10))

        # Draw teleportation cells
        self.cases_teleportation(self.screen)
        # Draw healing cells
        self.cases_soin(self.screen)
        # Draw damage cells
        self.cases_degat(self.screen) 
        
        # Add a grid
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, -1)

        # Add unit/player sprites
        for i, perso in enumerate(self.enemy_units) :
            perso_selected = perso.assign_character_class()
            health_perso = self.list_enemy_health[i]
            perso.draw(self.screen)
            perso_selected.draw_health_bar(self.screen, health_perso)

            if perso.is_selected :
                perso.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso.draw_red_case(self.screen, )

            
        for i, perso1 in enumerate(self.player_units):
            perso1_selected = perso1.assign_character_class()
            health_perso1 = self.list_player_health[i]
            perso1.draw(self.screen)
            perso1_selected.draw_health_bar(self.screen, health_perso1)
            
            if perso1.is_selected :
                if self.menu_attaques == False :
                    perso1.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso1.draw_red_case(self.screen, )


         # If the attack menu is active, draw it on top
        if self.menu_attaques:  
            self.draw_attack_menu()

        pygame.display.flip()


    def flip_display_ecran_final(self):
        """Displays the map and game elements."""
        fond_fin = pygame.image.load('Fond_ecran.png')
        self.display.blit(fond_fin, (0, 0))

        if (len(self.enemy_units) == 0) and self.game_mode :
            print("All enemies have been eliminated!")
            self.draw_text_black('Victory !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victory !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victory !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victory !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victory !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
            
        elif (len(self.player_units) == 0) and self.game_mode :
            print("All players have been eliminated!")
            self.draw_text_black('Defeat !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Defeat !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Defeat !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Defeat !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Defeat !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)

        elif (len(self.enemy_units) == 0) and not(self.game_mode) :
            print("All player 2 units have been eliminated!")
            self.draw_text_black('Victory P1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victory P1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victory P1 !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victory P1 !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victory P1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
            
        elif (len(self.player_units) == 0) and not(self.game_mode) :
            print("All player 1 units have been eliminated!")
            self.draw_text_black('Victory P2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victory P2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victory P2 !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victory P2 !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victory P2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
        self.window.blit(self.display, (0, 0)) 
        pygame.display.update()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text_white(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_black(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    
    # Fonction pour afficher la vidéo
    def play_video(self,clip):
        clock = pygame.time.Clock()
        for frame in clip.iter_frames(fps=30, dtype="uint8"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            # Convertir l'image pour Pygame et l'afficher
            pygame_frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            self.screen.blit(pygame_frame, (0, 0))
            pygame.display.update()
            clock.tick(30)

def main():

    
    
    # Initialize Pygame
    pygame.init()
    
    # Instantiate the window
    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("Marvel Game")
    
    # Instantiate the game
    game = Game(screen)
    
    clip = VideoFileClip("intro_video.mp4")
    game.play_video(clip)
    
    while game.running:
        game.curr_menu.display_menu()
        if (game.playing):
            break
                     
    player1 = Unit(game.Choix_Personnages_1.game_personnage, 15, 10, [32,32], game)
    hero1 = player1.assign_character_class()
    hero_health1 = hero1.get_health()
    game.player_units.append(player1)
    game.list_player_health.append(hero_health1)
    player2 = Unit(game.Choix_Personnages_2.game_personnage, 15, 12, [32,32], game)
    hero2 = player2.assign_character_class()
    hero_health2 = hero2.get_health() 
    game.player_units.append(player2)
    game.list_player_health.append(hero_health2) 
        
    print (f"NUMBER OF HEALTH POINTS OF {player1.name} = {hero_health1}")
    print (f"NUMBER OF HEALTH POINTS OF {player2.name} = {hero_health2}")


    #game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 0, 9, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             #Unit(game.Choix_Personnages_4.game_personnage, 1, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]

    player3 = Unit(game.Choix_Personnages_3.game_personnage, 22, 19, [32,32], game)
    hero3 = player3.assign_character_class()
    hero_health3 = hero3.get_health()
    game.enemy_units.append(player3)
    game.list_enemy_health.append(hero_health3)
    player4 = Unit(game.Choix_Personnages_4.game_personnage, 23, 19, [32,32], game)
    hero4 = player4.assign_character_class()
    hero_health4 = hero4.get_health()
    game.enemy_units.append(player4)
    game.list_enemy_health.append(hero_health4)

    print (f"NUMBER OF HEALTH POINTS OF {player3.name} = {hero_health3}")
    print (f"NUMBER OF HEALTH POINTS OF {player4.name} = {hero_health4}")

    print(f"player list: {game.player_units}")
    print(f"player health list: {game.list_player_health}")
    print(f"enemy list: {game.enemy_units}")
    print(f"enemy health list: {game.list_enemy_health}")

    play = True
    iter = 0
    
    # Main game loop
    while play and iter<100 :
        game.handle_player_turn()
        if (len(game.enemy_units) == 0) :
            game.flip_display_ecran_final()
            pygame.time.wait(5000)
            play = False
        if game.game_mode :
            game.handle_enemy_turn()  
            if (len(game.player_units) == 0) :
                game.flip_display_ecran_final()
                pygame.time.wait(5000)
                play = False
        else :
            game.handle_player_2_turn()
            if (len(game.player_units) == 0) :
                game.flip_display_ecran_final()
                pygame.time.wait(5000)
                play = False
        iter += 1
        if (len(game.player_units) != 0) and (len(game.enemy_units) != 0) :
            game.flip_display()
    return game.list_player_health, game.list_enemy_health 


if __name__ == "__main__":
    main()