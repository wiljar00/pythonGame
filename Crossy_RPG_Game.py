import pygame

SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

class Game:
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.game_screeen = pygame.display.set_mode((width, height))
        self.game_screeen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('images/player.png', 375, 700, 50, 50)

        non_player_character1 = NonPlayerCharacter('images/enemy.png', 20, 600, 50, 50)
        non_player_character1.SPEED *= level_speed
        non_player_character2 = NonPlayerCharacter('images/enemy.png', self.width - 40, 400, 50, 50)
        non_player_character2.SPEED *= level_speed
        non_player_character3 = NonPlayerCharacter('images/enemy.png', self.width - 40, 200, 50, 50)
        non_player_character3.SPEED *= level_speed

        treasure = GameObject('images/treasure.png', 375, 80, 50, 50)

        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screeen.fill(WHITE_COLOR)
            self.game_screeen.blit(self.image, (0, 0))

            treasure.draw(self.game_screeen)

            player_character.move(direction, self.height)
            player_character.draw(self.game_screeen)

            non_player_character1.move(self.width)
            non_player_character1.draw(self.game_screeen)

            if level_speed > 1:
                non_player_character2.move(self.width)
                non_player_character2.draw(self.game_screeen)
            if level_speed > 2:
                non_player_character3.move(self.width)
                non_player_character3.draw(self.game_screeen)

            if player_character.detect_collision(non_player_character1):
                is_game_over = True
                did_win = False
                lose_text = font.render('You Lost!', True, BLUE_COLOR)
                self.game_screeen.blit(lose_text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            if player_character.detect_collision(non_player_character2):
                is_game_over = True
                did_win = False
                lose_text = font.render('You Lost!', True, BLUE_COLOR)
                self.game_screeen.blit(lose_text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            if player_character.detect_collision(non_player_character3):
                is_game_over = True
                did_win = False
                lose_text = font.render('You Lost!', True, BLUE_COLOR)
                self.game_screeen.blit(lose_text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                win_text = font.render('You Won!', True, BLUE_COLOR)
                self.game_screeen.blit(win_text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break

            pygame.display.update()
            clock.tick(self.TICK_RATE)

        if did_win:
            self.run_game_loop(level_speed + .5)
        else:
            return


class GameObject:
    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
    
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True

class NonPlayerCharacter(GameObject):
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
    
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
pygame.init()
new_game = Game('images/background.png',SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)
pygame.quit()
quit()
