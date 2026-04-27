import pygame
import random


# Constantes
GRID_SIZE_x = 40
GRID_SIZE_y= 25
CELL_SIZE = 32

WIDTH = GRID_SIZE_x * CELL_SIZE 
HEIGHT = GRID_SIZE_y * CELL_SIZE 


#GRID_SIZE = 21.3

#WIDTH = GRID_SIZE * CELL_SIZE
#HEIGHT = GRID_SIZE * CELL_SIZE/(1.596)
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (50, 205, 50)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)



class Unit():
    
    def __init__(self, name, x, y, size, game):#, health, nbre_move, defense, attacks):
        super().__init__() # initializes the sprite class by calling its constructor with super()
        self.name = name
        self.x = x # Character x position
        self.y = y # Character y position
        self.size = size # character image size
        self.health = 0
        self.nbre_move = 0
        self.defense = 0
        self.attaques = []
        self.distance_attack = 0
        self.attack_power = 0
        self.red_cases = []
        self.offsets = []
        self.attaque_selectionne = "No_Action"
        self.is_selected = False # variable used in the draw() method to display the character
        self.cases=[]
        self.distance_maxi_attack = 1
        self.attaque_selectionne_index = 0  # Indice de l'attaque sélectionnée
        self.game = game
        self.image = pygame.Surface(size)
        self.green_cases=[]
 

    def move(self, dx, dy): # method defining player movements
        """Moves the unit by dx, dy, only if the target cell is valid."""
        # Calculate target position
        target_x = self.x + dx
        target_y = self.y + dy

        # Check if target position is in green cells
        if (target_x, target_y) in self.green_cases:
            self.x = target_x
            self.y = target_y
        else:
            print("Invalid move: outside allowed cells.")


    def update_green_case(self,player_units,enemy_units): # method to update movement cells
        
        if self.name == "Captain_America" : 
            perso = perso_Captain_america(self.x,self.y,self.size, self.game)            
        elif self.name == "Hulk" :
            perso = perso_Hulk(self.x,self.y,self.size, self.game)           
        elif self.name == "Ironman" :
            perso = perso_Ironman(self.x,self.y,self.size, self.game)           
        elif self.name == "Spiderman" :
            perso = perso_Spiderman(self.x,self.y,self.size, self.game)           
        elif self.name == "Thor" :
            perso = perso_Thor(self.x,self.y,self.size, self.game)           
        elif self.name == "Groot" : 
            perso = perso_Groot(self.x,self.y,self.size, self.game)            
        elif self.name == "Wolverine" :
            perso = perso_Wolverine(self.x,self.y,self.size, self.game)            
        elif self.name == "Black_Panther" :
            perso = perso_Black_panther(self.x,self.y,self.size, self.game)           
        elif self.name == "Starlord" :
            perso = perso_Starlord(self.x,self.y,self.size, self.game)           
        elif self.name == "Yondu" :
            perso = perso_Yondu(self.x,self.y,self.size, self.game)           
        elif self.name == "Torch" : 
            perso = perso_Torch(self.x,self.y,self.size, self.game)           
        elif self.name == "Jane_Storm" :
            perso = perso_Jane_storm(self.x,self.y,self.size, self.game)           
        elif self.name == "Chose" :    
            perso = perso_Chose(self.x,self.y,self.size, self.game)            
        elif self.name == "Dr_Strange" :
            perso = perso_Dr_strange(self.x,self.y,self.size, self.game)
        else:
            raise ValueError(f"Unrecognized character: {self.name}")
        
        self.green_cases=[] # reset green cells to avoid keeping old ones
        self.green_cases.append((self.x, self.y)) # add the initial cell where the player is
        
         # obstacle cells
        
        for y in range(0,6):
            for x in range(0, 16):
                self.cases.append((x, y))
        for y in range(0,3):
            for x in range(15, 41):
                self.cases.append((x, y))
      
        for x in range(0, 27):
            self.cases.append((x, 22))

        for y in range(18,26):
            for x in range(25, 41):
                self.cases.append((x, y))

        
        for y in range(0, 25):
            self.cases.append((0, y))

        for x in range(37,41):
            for y in range(0, 25):
                self.cases.append((x, y))     
    
        for x in range(5,13):
            for y in range(14,17):
                self.cases.append((x,y)) 
        
        for x in range(0,5):
            
            for y in range(14,16):
                self.cases.append((x,y)) 
                
                
        for x in range(25,40):
            for y in range(9,11):
                self.cases.append((x,y))
        
        if self.is_selected:

            for dx, dy in perso.offsets:
                # Calculate cell coordinates
                green_x = self.x + dx 
                green_y = self.y + dy 

                # FIRST CHECK: Verify the cell is within the grid boundaries
                if 0 <= green_x < GRID_SIZE_x and 0 <= green_y < GRID_SIZE_y:
                    # SECOND CHECK: Verify if the cell is occupied by a unit (player or enemy)
                    cell_occupied = False
                    for player in player_units + enemy_units:
                        if player.x == green_x and player.y == green_y:
                            cell_occupied = True
                            break
                    # THIRD CHECK: obstacle cells
                    if self.name != "Ironman" and self.name != "Thor" and self.name != "Torch" :
                        for x,y in self.cases:
                            if x==green_x and y==green_y:
                                cell_occupied = True
                                break
                    else :
                        for x,y in self.cases:
                            if x==green_x and y==green_y:
                                cell_occupied = False
                    
                    # If the cell is not occupied, add it to the green cells list
                    if not cell_occupied:
                        self.green_cases.append((green_x, green_y))
                    
    
    def draw_green_case(self, screen): # method to draw movement cells
        color = GREEN
        for green_x,green_y in self.green_cases:
            pygame.draw.rect(screen, color, (green_x*CELL_SIZE, green_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)  # Draw the borders


    def update_red_case(self, attack): # method to update attack cells
        self.red_cases=[] # reset red cells to avoid keeping old ones
        self.red_cases.append((self.x, self.y)) # add the initial cell where the player is
        
        if attack == "No_Action":
            self.attaque_selectionne = Aucune_action()

        if attack == "Fists" :
            self.attaque_selectionne = Poings()
        
        elif attack == "Claws" :
            self.attaque_selectionne = Griffes()

        elif attack == "Shield_Throw" :
            self.attaque_selectionne = Lancer_bouclier()

        elif attack == "Break_Defenses" :
            self.attaque_selectionne = Briser_les_defenses()
        
        elif attack == "Laser" :
            self.attaque_selectionne = Laser()
        
        elif attack == "Missile":
            self.attaque_selectionne = Missile()
        
        elif attack == "Block_Opponent":
            self.attaque_selectionne = Bloquer_adversaire()

        elif attack == "Web_Attack":
            self.attaque_selectionne = Attaque_toile()
        
        elif attack == "Hammer":
            self.attaque_selectionne = Marteau()
        
        elif attack == "Lightning":
            self.attaque_selectionne = Foudre()
        
        elif attack == "Branch_Attack":
            self.attaque_selectionne = Attaque_branche()
        
        elif attack == "Protection":
            self.attaque_selectionne = Protection()
        
        elif attack == "Guns":
            self.attaque_selectionne = Pistolets()
        
        elif attack == "Yaka_Arrow":
            self.attaque_selectionne = Fleche_yaka()

        elif attack == "Fireball":
            self.attaque_selectionne = Boule_de_feu()

        elif attack == "Heal":
            self.attaque_selectionne = Soigner()

        elif attack == "Projectile":
            self.attaque_selectionne = Projectile()
          

        if self.is_selected:

            for dx, dy in self.attaque_selectionne.offsets:
                # Calcul des coordonnées de la case
                red_x = self.x + dx 
                red_y = self.y + dy

                # FIRST CHECK: Verify the cell is within the grid boundaries
                if 0 <= red_x < GRID_SIZE_x and 0 <= red_y < GRID_SIZE_y:
                    self.red_cases.append((red_x, red_y))
                
    
    def draw_red_case(self, screen): # method to draw attack cells based on the attack 
        color = RED
        for red_x,red_y in self.red_cases:
            pygame.draw.rect(screen, color, (red_x*CELL_SIZE, red_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Draw the borders
    
      
    def attack(self, type_attack, target, target_health): # method used for attacks
        """Attacks a target unit."""
        
        if type_attack.name == "Heal" :
            for target in self.player_units :
                for red_x, red_y in self.red_cases :
                    if target.x == red_x and  target.y == red_y :
                        target_health = target.health_max
                    else :
                        target_health = target_health
           
        
        elif type_attack.name == "Break_Defenses" :
            for red_x, red_y in self.red_cases :
                    if target.x == red_x and  target.y == red_y :
                        target.defense = 0
                        target_health = target_health - type_attack.attack_power*type_attack.chance*(1 - target.defense/100)/type_attack.distance_attack

        elif type_attack.name == "Protection" :
            for red_x, red_y in self.red_cases :
                    if target.x == red_x and  target.y == red_y :
                        target.attack_power = 0
                        
        else :
            for red_x, red_y in self.red_cases :
                if target.x == red_x and  target.y == red_y :
                    target_health = target_health - type_attack.attack_power*type_attack.chance*(1 - target.defense/100)/type_attack.distance_attack
                
                else :
                    target_health = target_health

        return target_health
    

    def eni_attack(self, type_attack, target, target_health): # method used for attacks
        """Attacks a target unit."""
        
        if type_attack.name == "Heal" :
            for target in self.enemy_units :
                if abs(target.x - self.x) == 1 and  abs(target.y-self.x) == 1 :
                    target_health = target.health_max
                else :
                    target_health = target_health           
        
        elif type_attack.name == "Break_Defenses" :
            if abs(target.x - self.x) == 1 and  abs(target.y-self.x) == 1 :
                target.defense = 0

        else :
            if abs(target.x - self.x) <= 2 and  abs(target.y-self.y) <= 2 :
                target_health = target_health - type_attack.attack_power*type_attack.chance*(1 - target.defense/100)/type_attack.distance_attack
                
            else :
                target_health = target_health

        return target_health
    

    def draw(self, screen): # method to set the image corresponding to the selected player
        """Displays the unit on the screen."""
         
        # Generate the image of the chosen player
        if self.name == "Captain_America" :   
            self.sprite_sheet = pygame.image.load('Characters/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # remove the white color of the background

        elif self.name == "Hulk" :           
            self.sprite_sheet = pygame.image.load('Characters/avengers2.jpg.png')
            self.image = self.get_image(52,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Ironman" :
            self.sprite_sheet = pygame.image.load('Characters/avengers.png')
            self.image = self.get_image(150,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Spiderman" :
            self.sprite_sheet = pygame.image.load('Characters/avengers3.png')
            self.image = self.get_image(150,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Thor" :
            self.sprite_sheet = pygame.image.load('Characters/avengers.png')
            self.image = self.get_image(295,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0])
            
        elif self.name == "Groot" :       
            self.sprite_sheet = pygame.image.load('Characters/galaxy2.png')
            self.image = self.get_image(150,0)
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Wolverine" :
            self.sprite_sheet = pygame.image.load('Characters/x_men.png')
            self.image = self.get_image(0,192) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Black_Panther" :           
            self.sprite_sheet = pygame.image.load('Characters/avengers3.png')
            self.image = self.get_image(0,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0])
            
        elif self.name == "Starlord" :
            self.sprite_sheet = pygame.image.load('Characters/galaxy.png')
            self.image = self.get_image(0,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Yondu" :
            self.sprite_sheet = pygame.image.load('Characters/galaxy.png')
            self.image = self.get_image(295,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Torch" :
            self.sprite_sheet = pygame.image.load('Characters/4_fantastic.png')
            self.image = self.get_image(295, 193) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Jane_Storm" :
            self.sprite_sheet = pygame.image.load('Characters/4_fantastic.png')
            self.image = self.get_image(150,0) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Chose" :
            self.sprite_sheet = pygame.image.load('Characters/4_fantastic.png')
            self.image = self.get_image(0,193) 
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 
            
        elif self.name == "Dr_Strange" :
            self.sprite_sheet = pygame.image.load('Characters/doctor_strange.png')
            self.image = self.get_image(0,0)
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) 

        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))
        
        
    def get_image(self,x,y): # method to crop the desired portion of the png image
        image=pygame.Surface([52,52])
        image.blit(self.sprite_sheet,(10,0),(x,y,42,52))
        return image
  
    
    def draw_health_bar(self, screen, health): # method to display the health bar
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        bar_length = CELL_SIZE  # Bar length
        bar_height = 3   # Bar height

        # Calculate width based on HP
        fill = (health / self.health_max) * bar_length

        # Bar position (just above the character)
        bar_x = self.x
        bar_y = self.y 

        # Draw the background bar (outline)
        pygame.draw.rect(screen, BLACK, (bar_x*CELL_SIZE , bar_y*CELL_SIZE , bar_length + 2, bar_height + 2))
        # Draw the current health bar
        pygame.draw.rect(screen, RED, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, bar_length, bar_height))  # Empty bar
        pygame.draw.rect(screen, BLUE, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, fill, bar_height))     # Filled bar
    
    def assign_character_class(self) : # method to create character instances
        if self.name == "Captain_America" : 
            perso = perso_Captain_america(self.x,self.y,self.size, self.game)            
        elif self.name == "Hulk" :
            perso = perso_Hulk(self.x,self.y,self.size, self.game)           
        elif self.name == "Ironman" :
            perso = perso_Ironman(self.x,self.y,self.size, self.game)           
        elif self.name == "Spiderman" :
            perso = perso_Spiderman(self.x,self.y,self.size, self.game)           
        elif self.name == "Thor" :
            perso = perso_Thor(self.x,self.y,self.size, self.game)           
        elif self.name == "Groot" : 
            perso = perso_Groot(self.x,self.y,self.size, self.game)            
        elif self.name == "Wolverine" :
            perso = perso_Wolverine(self.x,self.y,self.size, self.game)            
        elif self.name == "Black_Panther" :
            perso = perso_Black_panther(self.x,self.y,self.size, self.game)           
        elif self.name == "Starlord" :
            perso = perso_Starlord(self.x,self.y,self.size, self.game)           
        elif self.name == "Yondu" :
            perso = perso_Yondu(self.x,self.y,self.size, self.game)           
        elif self.name == "Torch" : 
            perso = perso_Torch(self.x,self.y,self.size, self.game)           
        elif self.name == "Jane_Storm" :
            perso = perso_Jane_storm(self.x,self.y,self.size, self.game)           
        elif self.name == "Chose" :    
            perso = perso_Chose(self.x,self.y,self.size, self.game)            
        elif self.name == "Dr_Strange" :
            perso = perso_Dr_strange(self.x,self.y,self.size, self.game)
        else:
            raise ValueError(f"Unrecognized character: {self.name}")
        return perso
# creation of each character class - TO CONFIRM AS IT MAY NOT BE NECESSARY

    def assign_attack_class(self, indice) : # method to create skill instances 
        if self.list_attaques[indice] == "No_Action" :
            attaque_selectionne = Aucune_action()
            if self.game.Musique :
                self.game.sound_manager.bruit("Attendre")
                                
        elif self.list_attaques[indice] == "Fists" :
            attaque_selectionne = Poings()
            if self.game.Musique :
                self.game.sound_manager.bruit("Combat")
        
        elif self.list_attaques[indice] == "Claws" :
            attaque_selectionne = Griffes()
            if self.game.Musique :
                self.game.sound_manager.bruit("Claws")


        elif self.list_attaques[indice] == "Shield_Throw" :
            attaque_selectionne = Lancer_bouclier()
            if self.game.Musique :
                self.game.sound_manager.bruit("Boomerang")

        elif self.list_attaques[indice] == "Break_Defenses" :
            attaque_selectionne = Briser_les_defenses()
            if self.game.Musique :
                self.game.sound_manager.bruit("Casser_mur")
        
        elif self.list_attaques[indice] == "Laser" :
            attaque_selectionne = Laser()
            if self.game.Musique :
                self.game.sound_manager.bruit("Laser")
        
        elif self.list_attaques[indice] == "Missile":
            attaque_selectionne = Missile()
            if self.game.Musique :
                self.game.sound_manager.bruit("Explosion")
        
        elif self.list_attaques[indice] == "Block_Opponent":
            attaque_selectionne = Bloquer_adversaire()
            if self.game.Musique :
                self.game.sound_manager.bruit("Combat_v3")

        elif self.list_attaques[indice] == "Web_Attack":
            attaque_selectionne = Attaque_toile()
            if self.game.Musique :
                self.game.sound_manager.bruit("Pistolet_silencieux")
        
        elif self.list_attaques[indice] == "Hammer":
            attaque_selectionne = Marteau()
            if self.game.Musique :
                self.game.sound_manager.bruit("Coup_marteau")
        
        elif self.list_attaques[indice] == "Lightning":
            attaque_selectionne = Foudre()
            if self.game.Musique :
                self.game.sound_manager.bruit("Foudre_v2")
        
        elif self.list_attaques[indice] == "Branch_Attack":
            attaque_selectionne = Attaque_branche()
            if self.game.Musique :
                self.game.sound_manager.bruit("Combat_v4")
        
        elif self.list_attaques[indice] == "Protection":
            attaque_selectionne = Protection()
            if self.game.Musique :
                self.game.sound_manager.bruit("Protection")
        
        elif self.list_attaques[indice] == "Guns":
            attaque_selectionne = Pistolets()
            if self.game.Musique :
                self.game.sound_manager.bruit("Tir_rafale_v2")
        
        elif self.list_attaques[indice] == "Yaka_Arrow":
            attaque_selectionne = Fleche_yaka()
            if self.game.Musique :
                self.game.sound_manager.bruit("Fleche")

        elif self.list_attaques[indice] == "Fireball":
            attaque_selectionne = Boule_de_feu()
            if self.game.Musique :
                self.game.sound_manager.bruit("Boule_feu")

        elif self.list_attaques[indice] == "Heal":
            attaque_selectionne = Soigner()
            if self.game.Musique :
                self.game.sound_manager.bruit("Soin")

        elif self.list_attaques[indice] == "Projectile":
            attaque_selectionne = Projectile()
            if self.game.Musique :
                self.game.sound_manager.bruit("Projectile")
        else:
            raise ValueError(f"Unrecognized attack: {self.list_attaques[indice]}")
        return attaque_selectionne


""" CHARACTER CLASSES """

class perso_Captain_america(Unit):
    def __init__(self, x, y, size, game):
        super().__init__("Captain_America", x, y, size, game)
        self.__health = 100
        self.health_max = 100
        self.distance_maxi_attack = 2
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Shield_Throw" ]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),  
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1) , 
                (0, 0)]

    def get_health (self):
        return self.__health    
    
class perso_Hulk(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Hulk", x, y, size, game)
        self.__health = 150
        self.health_max = 150
        self.distance_maxi_attack = 2
        self.nbre_move = 4
        self.defense = 90
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists", "Break_Defenses"]
        
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2), 
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), 
                (0, 0)]
        

    def get_health (self):
        return self.__health

class perso_Ironman (Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Ironman", x, y, size, game)
        self.__health = 100
        self.health_max = 100
        self.distance_maxi_attack = 3
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Laser", "Missile"]
        
        self.offsets = [
                (-6, 0), (6, 0), (0, -6), (0, 6),
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-1, -3), (-1, 3), (-2, -3), (-2, 3), (1, -3), (1, 3), (2, -3), (2, 3),
                (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, -2), (-3, 2), (3, -2), (3, 2), (-3, -3), (-3, 3), (3, -3), (3, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), 
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]

    def get_health (self):
        return self.__health    
        
class perso_Spiderman(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Spiderman", x, y, size, game)
        self.__health = 90
        self.health_max = 90
        self.distance_maxi_attack = 2
        self.nbre_move = 6
        self.defense = 50
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Block_Opponent", "Web_Attack"]
        
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), 
                (0, 0)]

    def get_health (self):
        return self.__health    
    
class perso_Thor(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Thor", x, y, size, game)
        self.__health = 150
        self.health_max = 150
        self.distance_maxi_attack = 3
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Hammer", "Lightning"]
        
        self.offsets = [
                (-6, 0), (6, 0), (0, -6), (0, 6),
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-1, -3), (-1, 3), (-2, -3), (-2, 3), (1, -3), (1, 3), (2, -3), (2, 3),
                (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, -2), (-3, 2), (3, -2), (3, 2), (-3, -3), (-3, 3), (3, -3), (3, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), 
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]
    
    def get_health (self):
        return self.__health

class perso_Groot(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Groot", x, y, size, game)
        self.__health = 120
        self.health_max = 120
        self.distance_maxi_attack = 2
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["No_Action","Branch_Attack", "Protection"]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  
                (-1, -1), (1, 1), (-1, 1), (1, -1) , 
                (0, 0)]
    
    def get_health (self):
        return self.__health
        
class perso_Wolverine(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Wolverine", x, y, size, game)   
        self.__health = 150
        self.health_max = 150
        self.distance_maxi_attack = 2
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Claws"]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  
                (0, 0)]

    def get_health (self):
        return self.__health    

class perso_Black_panther(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Black_Panther", x, y, size, game)
        self.__health = 130
        self.health_max = 130
        self.distance_maxi_attack = 2
        self.nbre_move = 4
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Claws"]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  
                (0, 0)]

    def get_health (self):
        return self.__health    
    
class perso_Starlord (Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Starlord", x, y, size, game)
        self.__health = 90
        self.health_max = 90
        self.distance_maxi_attack = 3
        self.nbre_move = 6
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Guns"]
        
        self.offsets = [
                (-1, -3), (-1, 3), (1,-3), (1, 3), (-2, -3), (-2, 3), (2, -3), (2, 3),
                (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, -2), (-3, 2), (3, -2), (3, 2), (-3, -3), (-3, 3), (3, -3), (3, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2), 
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]

    def get_health (self):
        return self.__health    
        
class  perso_Yondu(Unit):
    def __init__(self, x, y, size, game):
        super().__init__("Yondu", x, y, size, game)
        self.__health = 130
        self.health_max = 130
        self.distance_maxi_attack = 3
        self.nbre_move = 3
        self.defense = 50
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Yaka_Arrow"]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1), 
                (-1, -1), (1, 1), (-1, 1), (1, -1) , 
                (0, 0)]

    def get_health (self):
        return self.__health    
        
class perso_Torch(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Torch", x, y, size, game)
        self.__health = 100
        self.health_max = 100
        self.distance_maxi_attack = 3
        self.nbre_move = 8
        self.defense = 40
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Fireball"]
        
        self.offsets = [
                (-6, 0), (6, 0), (0, -6), (0, 6),
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-1, -3), (-1, 3), (1,-3), (1, 3), (-2, -3), (-2, 3), (2, -3), (2, 3),
                (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, -2), (-3, 2), (3, -2), (3, 2), (-3, -3), (-3, 3), (3, -3), (3, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]

    def get_health (self):
        return self.__health        

class perso_Jane_storm(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Jane_Storm", x, y, size, game)
        self.__health = 70
        self.health_max = 70
        self.distance_maxi_attack = 1
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Heal"]
        
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  
                (0, 0)]

    def get_health (self):
        return self.__health    
        
class perso_Chose(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Chose", x, y, size, game)
        self.__health = 140
        self.health_max = 140
        self.distance_maxi_attack = 1
        self.nbre_move = 4
        self.defense = 80
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Break_Defenses"]
        
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]

    def get_health (self):
        return self.__health    

class perso_Dr_strange(Unit) :
    def __init__(self, x, y, size, game):
        super().__init__("Dr_Strange", x, y, size, game)
        self.__health = 80
        self.health_max = 80
        self.distance_maxi_attack = 2
        self.nbre_move = 6
        self.defense = 80
        self.attack_power = 10
        self.list_attaques = ["No_Action", "Fists","Block_Opponent","Projectile" ]
        
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-1, -3), (-1, 3), (-2, -3), (-2, 3),(1, -3), (1, 3), (2, -3), (2, 3),
                (-3, 0), (3, 0), (0, -3), (0, 3), (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, -2), (-3, 2), (3, -2), (3, 2), (-3, -3), (-3, 3), (3, -3), (3, 3), 
                (-2, 0), (2, 0), (0, -2), (0, 2), (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-2, -2), (-2, 2), (2, -2), (2, 2), (1, -2), (1, 2), (-1, -2), (-1, 2), 
                (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1),  
                (0, 0)]

    def get_health (self):
        return self.__health
