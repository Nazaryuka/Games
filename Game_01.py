import pygame

screen_size = (600, 400)

pygame.init()
screen = pygame.display.set_mode(screen_size)
done = False
last_dir = 'R'
bullets = []
BLACK = (0,0,0)
RED = (0,255,0)



class bullet:
    def __init__(self, x, y, direction, speed, power):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.power = power
    color = RED
    bullet_x_change = 0
    bullet_y_change = 0
    bullet_width = 0
    bullet_height = 0

    def build(self):
        if self.direction[pygame.K_UP]:
            self.bullet_y_change = -self.speed
            self.bullet_width = 2
            self.bullet_height = 10
        elif self.direction[pygame.K_DOWN]:
            self.bullet_y_change = self.speed
            self.bullet_width = 2
            self.bullet_height = 10
        elif self.direction[pygame.K_RIGHT]:
            self.bullet_x_change = self.speed
            self.bullet_width = 10
            self.bullet_height = 2
        elif self.direction[pygame.K_LEFT]:
            self.bullet_x_change = -self.speed
            self.bullet_width = 10
            self.bullet_height = 2

    def draw(self):
        self.x += self.bullet_x_change
        self.y += self.bullet_y_change
        pygame.draw.rect(screen,  self.color , (self.x, self.y, self.bullet_width, self.bullet_height))


class tank:
    def __init__(self, name, patrons, life, color):
        self.patrons = patrons
        self.name = name
        self.life = life
        self.color = color

    x = 0
    y = 0
    direction = None
    shoot_direction = None
    bullets = []


    def move(self):
        if self.direction[pygame.K_DOWN]:
            player.y += 5
            self.shoot_direction = self.direction
        elif self.direction[pygame.K_UP]:
            player.y -= 5
            self.shoot_direction = self.direction
        elif self.direction[pygame.K_RIGHT]:
            player.x += 5
            self.shoot_direction = self.direction
        elif self.direction[pygame.K_LEFT]:
            player.x -= 5
            self.shoot_direction = self.direction


    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 10, 10))
        for bulet in self.bullets:
            bulet.draw()


    def shoot(self):
        temp = bullet(self.x, self.y, self.shoot_direction, 5, 2)
        temp.build()
        self.bullets.append(temp)
        return temp





player = tank("Nazarius", 100, 3, BLACK)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        player.shoot()


    screen.fill((255,255,255))
    player.direction = key
    player.move()
    player.draw()



    pygame.display.flip()

