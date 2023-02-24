# # # # # # # # # import os
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def get_folder_size(folder):
# # # # # # # # #     total_size = 0
# # # # # # # # #     for path, dirs, files in os.walk(folder):
# # # # # # # # #         for f in files:
# # # # # # # # #             fp = os.path.join(path, f)
# # # # # # # # #             total_size += os.path.getsize(fp)
# # # # # # # # #     return total_size
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def format_size(size):
# # # # # # # # #     for unit in ['б', 'Кб', 'Мб', 'Гб', 'Тб']:
# # # # # # # # #         if size < 1024.0:
# # # # # # # # #             return f"{size:.2f}{unit}"
# # # # # # # # #         size /= 1024.0
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def main():
# # # # # # # # #     folder = input("Введите путь к каталогу: ")
# # # # # # # # #     sizes = {}
# # # # # # # # #     for root, dirs, files in os.walk(folder):
# # # # # # # # #         total_size = get_folder_size(root)
# # # # # # # # #         sizes[root] = total_size
# # # # # # # # #     sorted_sizes = sorted(sizes.items(), key=lambda x: x[1], reverse=True)[:10]
# # # # # # # # #     for path, size in sorted_sizes:
# # # # # # # # #         print(f"{path} - {format_size(size)}")
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     main()
# # # # # # # # #
# # # # # # # # # # import zipfile
# # # # # # # # # # import os
# # # # # # # # # # import datetime
# # # # # # # # # #
# # # # # # # # # # def make_reserve_arc(source, dest):
# # # # # # # # # #     timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# # # # # # # # # #     archive_name = f"copy_{timestamp}.zip"
# # # # # # # # # #     archive_path = os.path.join(dest, archive_name)
# # # # # # # # # #     with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
# # # # # # # # # #         for root, dirs, files in os.walk(source):
# # # # # # # # # #             for file in files:
# # # # # # # # # #                 file_path = os.path.join(root, file)
# # # # # # # # # #                 archive_path = os.path.relpath(file_path, source)
# # # # # # # # # #                 archive.write(file_path, archive_path)
# # # # # # # # # #     print(f"Созданная резервная копия: {archive_path}")
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # make_reserve_arc('path-to-file', 'path-to-file-copy')
# # # # # # # # import pygame
# # # # # # # # import sys
# # # # # # # #
# # # # # # # # pygame.init()
# # # # # # # #
# # # # # # # # size = width, height = 300, 300
# # # # # # # #
# # # # # # # # try:
# # # # # # # #     n = int(input())
# # # # # # # # except ValueError:
# # # # # # # #     print("Неправильный формат ввода")
# # # # # # # #     sys.exit()
# # # # # # # #
# # # # # # # # screen = pygame.display.set_mode(size)
# # # # # # # #
# # # # # # # # orange = pygame.Color("orange")
# # # # # # # # yellow = pygame.Color("yellow")
# # # # # # # #
# # # # # # # # step = int(height / n)
# # # # # # # #
# # # # # # # # screen.fill(yellow)
# # # # # # # #
# # # # # # # # for i in range(n):
# # # # # # # #     for j in range(n):
# # # # # # # #         x = step * i + step / 2
# # # # # # # #         y = step * j + step / 2
# # # # # # # #         size = step / 2
# # # # # # # #         pygame.draw.polygon(screen, orange, [(x, y - size), (x + size, y), (x, y + size), (x - size, y)])
# # # # # # # #
# # # # # # # # pygame.display.flip()
# # # # # # # #
# # # # # # # # while True:
# # # # # # # #     for event in pygame.event.get():
# # # # # # # #         if event.type == pygame.QUIT:
# # # # # # # #             sys.exit()
# # # # # # # import pygame
# # # # # # #
# # # # # # # pygame.init()
# # # # # # #
# # # # # # # WINDOW_WIDTH = 300
# # # # # # # WINDOW_HEIGHT = 200
# # # # # # #
# # # # # # # BRICK_WIDTH = 30
# # # # # # # BRICK_HEIGHT = 15
# # # # # # #
# # # # # # # # отступ между кирпичами
# # # # # # # MORTAR_WIDTH = 2
# # # # # # #
# # # # # # # window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# # # # # # #
# # # # # # # RED = (255, 0, 0)
# # # # # # # WHITE = (255, 255, 255)
# # # # # # #
# # # # # # # for y in range(0, WINDOW_HEIGHT, BRICK_HEIGHT + MORTAR_WIDTH):
# # # # # # #     for x in range(0, WINDOW_WIDTH, BRICK_WIDTH + MORTAR_WIDTH):
# # # # # # #         if (y // (BRICK_HEIGHT + MORTAR_WIDTH)) % 2 == 0:
# # # # # # #             # смещаем кирпич на 15 пикселей вправо
# # # # # # #             x += BRICK_WIDTH // -2
# # # # # # #         pygame.draw.rect(window, RED, (x, y, BRICK_WIDTH, BRICK_HEIGHT))
# # # # # # #         pygame.draw.rect(window, WHITE, (x, y, BRICK_WIDTH, BRICK_HEIGHT), MORTAR_WIDTH)
# # # # # # #
# # # # # # # pygame.display.flip()
# # # # # # #
# # # # # # # while True:
# # # # # # #     for event in pygame.event.get():
# # # # # # #         if event.type == pygame.QUIT:
# # # # # # #             pygame.quit()
# # # # # # #             quit()
# # # # # # import pygame
# # # # # # import sys
# # # # # #
# # # # # # # Цвета для куба
# # # # # # WHITE = (255, 255, 255)
# # # # # # GRAY_50 = (128, 128, 128)
# # # # # # GRAY_75 = (192, 192, 192)
# # # # # # BLACK = (0, 0, 0)
# # # # # #
# # # # # # # Получаем значения W и Hue из стандартного потока ввода
# # # # # # try:
# # # # # #     W, Hue = map(int, input().split())
# # # # # # except ValueError:
# # # # # #     print("Неправильный формат ввода")
# # # # # #     sys.exit()
# # # # # #
# # # # # # # Проверяем значения W и Hue на соответствие условиям задачи
# # # # # # if not (4 <= W <= 100 and W % 4 == 0 and 0 <= Hue <= 360):
# # # # # #     print("Неправильный формат ввода")
# # # # # #     sys.exit()
# # # # # #
# # # # # # # Инициализируем Pygame
# # # # # # pygame.init()
# # # # # #
# # # # # # # Создаем окно размером 300x300 пикселей
# # # # # # window = pygame.display.set_mode((300, 300))
# # # # # #
# # # # # # # Очищаем экран белым цветом
# # # # # # window.fill(WHITE)
# # # # # #
# # # # # # # Рисуем верхнюю грань куба
# # # # # # top_surface = pygame.Surface((W, W))
# # # # # # top_surface.fill(pygame.Color(0, 0, 0, 0))
# # # # # # pygame.draw.polygon(top_surface, WHITE, [(0, 0), (W, 0), (W // 2, W // 2), (0, W)])
# # # # # # top_surface.set_alpha(255)
# # # # # # window.blit(top_surface, (150 - W // 2, 75 - W // 2))
# # # # # #
# # # # # # # Рисуем боковые грани куба
# # # # # # left_side = pygame.Surface((W // 2, W))
# # # # # # left_side.fill(GRAY_50)
# # # # # # left_side.set_alpha(128)
# # # # # # window.blit(left_side, (150 - W // 2, 150 - W // 4))
# # # # # #
# # # # # # right_side = pygame.Surface((W // 2, W))
# # # # # # right_side.fill(GRAY_75)
# # # # # # right_side.set_alpha(128)
# # # # # # window.blit(right_side, (150, 150 - W // 4))
# # # # # #
# # # # # # # Рисуем переднюю грань куба
# # # # # # front_surface = pygame.Surface((W // 2, W // 2))
# # # # # # front_surface.fill(BLACK)
# # # # # # front_surface.set_alpha(128)
# # # # # # pygame.draw.polygon(front_surface, pygame.Color("hsv", Hue, 100, 75), [(0, 0), (W // 2, 0), (W // 4, W // 4)])
# # # # # # window.blit(front_surface, (150 - W // 4, 150 - W // 2))
# # # # # #
# # # # # # # Обновляем экран и ждем закрытия окна
# # # # # # pygame.display.flip()
# # # # # # while True:
# # # # # #     for event in pygame.event.get():
# # # # # #         if event.type == pygame.QUIT:
# # # # # #             sys.exit()
# # # # # import pygame
# # # # #
# # # # # # Инициализация Pygame
# # # # # pygame.init()
# # # # #
# # # # # # Создание окна
# # # # # screen_width = 800
# # # # # screen_height = 600
# # # # # screen = pygame.display.set_mode((screen_width, screen_height))
# # # # #
# # # # # # Установка заголовка окна
# # # # # pygame.display.set_caption("Прямоугольники")
# # # # #
# # # # # # Цвета
# # # # # BLACK = (0, 0, 0)
# # # # # WHITE = (255, 255, 255)
# # # # # RED = (255, 0, 0)
# # # # #
# # # # # # Список для хранения прямоугольников
# # # # # rectangles = []
# # # # #
# # # # # # Переменная для хранения координаты первой вершины прямоугольника
# # # # # start_pos = None
# # # # #
# # # # # # Флаг для отслеживания нажатия Ctrl
# # # # # ctrl_pressed = False
# # # # #
# # # # # # Главный цикл программы
# # # # # running = True
# # # # # while running:
# # # # #     for event in pygame.event.get():
# # # # #         if event.type == pygame.QUIT:
# # # # #             running = False
# # # # #         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Левая кнопка мыши нажата
# # # # #             # Запоминаем координаты первой вершины
# # # # #             start_pos = event.pos
# # # # #         elif event.type == pygame.MOUSEMOTION and start_pos is not None: # Движение мыши с зажатой левой кнопкой
# # # # #             # Рисуем прямоугольник по координатам двух вершин
# # # # #             current_pos = event.pos
# # # # #             rect = pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
# # # # #             pygame.draw.rect(screen, RED, rect, 2)
# # # # #             pygame.display.update()
# # # # #         elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # Левая кнопка мыши отпущена
# # # # #             # Добавляем прямоугольник в список
# # # # #             current_pos = event.pos
# # # # #             rect = pygame.Rect(start_pos, (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
# # # # #             rectangles.append(rect)
# # # # #             # Сбрасываем переменную start_pos
# # # # #             start_pos = None
# # # # #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL: # Левый Ctrl нажат
# # # # #             ctrl_pressed = True
# # # # #         elif event.type == pygame.KEYUP and event.key == pygame.K_LCTRL: # Левый Ctrl отпущен
# # # # #             ctrl_pressed = False
# # # # #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_z and ctrl_pressed: # Ctrl+Z нажаты
# # # # #             # Удаляем последний прямоугольник из списка
# # # # #             if rectangles:
# # # # #                 rectangles.pop()
# # # # #             # Очищаем экран и перерисовываем все прямоугольники
# # # # #             screen.fill(WHITE)
# # # # #             for rect in rectangles:
# # # # #                 pygame.draw.rect(screen, RED, rect, 2)
# # # # #             pygame.display.update()
# # # # #
# # # # #     # Обновляем экран
# # # # #     pygame.display.update()
# # # # #
# # # # # # Выход из Pygame
# # # # # pygame.quit()
# # # #
# # # #
# # # # import os
# # # # import sys
# # # #
# # # # import pygame
# # # # import requests
# # # #
# # # # map_request = "https://static-maps.yandex.ru/1.x/?ll=135.746181,-27.483765&spn=20,20&l=map"
# # # # response = requests.get(map_request)
# # # #
# # # # if not response:
# # # #     print("Ошибка выполнения запроса:")
# # # #     print(map_request)
# # # #     print("Http статус:", response.status_code, "(", response.reason, ")")
# # # #     sys.exit(1)
# # # #
# # # # # Запишем полученное изображение в файл.
# # # # map_file = "map.png"
# # # # with open(map_file, "wb") as file:
# # # #     file.write(response.content)
# # # #
# # # # # Инициализируем pygame
# # # # pygame.init()
# # # # screen = pygame.display.set_mode((600, 450))
# # # # # Рисуем картинку, загружаемую из только что созданного файла.
# # # # screen.blit(pygame.image.load(map_file), (0, 0))
# # # # # Переключаем экран и ждем закрытия окна.
# # # # pygame.display.flip()
# # # # while pygame.event.wait().type != pygame.QUIT:
# # # #     pass
# # # # pygame.quit()
# # # #
# # # # # Удаляем за собой файл с изображением.
# # # # os.remove(map_file)
# # #
# # # import pygame
# # #
# # # # Инициализация Pygame
# # # pygame.init()
# # #
# # # # Определение цветов
# # # BLACK = (0, 0, 0)
# # #
# # # # Создание окна
# # # size = (700, 500)
# # # screen = pygame.display.set_mode(size)
# # # pygame.display.set_caption("Замена курсора мыши")
# # #
# # # # Загрузка изображения курсора
# # # cursor_img = pygame.image.load('img.png')
# # #
# # # # Основной цикл программы
# # # done = False
# # # clock = pygame.time.Clock()
# # #
# # # while not done:
# # #     # Обработка событий
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             done = True
# # #
# # #     # Очистка экрана
# # #     screen.fill(BLACK)
# # #
# # #     # Проверка находится ли курсор в окне
# # #     if pygame.mouse.get_focused():
# # #         pygame.mouse.set_visible(False)
# # #         # Получение координат курсора мыши
# # #         pos = pygame.mouse.get_pos()
# # #
# # #         # Отрисовка изображения курсора в координатах курсора мыши
# # #         screen.blit(cursor_img, pos)
# # #
# # #     # Обновление экрана
# # #     pygame.display.flip()
# # #
# # #     # Ограничение частоты кадров
# # #     clock.tick(60)
# # #
# # # # Закрытие Pygame
# # # pygame.quit()
# # #
# # # import pygame
# # #
# # # pygame.init()
# # #
# # # screen_width = 300
# # # screen_height = 300
# # # screen = pygame.display.set_mode((screen_width, screen_height))
# # #
# # # player_image = pygame.image.load("img_1.png")
# # #
# # # player_x = 0
# # # player_y = 0
# # #
# # # running = True
# # # while running:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False
# # #
# # #     keys = pygame.key.get_pressed()
# # #
# # #     if keys[pygame.K_LEFT]:
# # #         # при сдвиге на 10 пикселей слишком сильно отходит
# # #         player_x -= 1
# # #     if keys[pygame.K_RIGHT]:
# # #         player_x += 1
# # #     if keys[pygame.K_UP]:
# # #         player_y -= 1
# # #     if keys[pygame.K_DOWN]:
# # #         player_y += 1
# # #
# # #     screen.fill((255, 255, 255))
# # #     screen.blit(player_image, (player_x, player_y))
# # #     pygame.display.flip()
# # #
# # # pygame.quit()
# #
# # import pygame
# #
# # class Car(pygame.sprite.Sprite):
# #     def __init__(self):
# #         super().__init__()
# #         self.image = pygame.image.load('img_2.png')
# #         self.rect = self.image.get_rect(center=(300, 50))
# #         self.speed = 2
# #
# #     def update(self):
# #         self.rect.move_ip(self.speed, 0)
# #         if self.rect.left < 0 or self.rect.right > 600:
# #             self.speed = -self.speed
# #             self.image = pygame.transform.flip(self.image, True, False)
# #
# # pygame.init()
# # screen = pygame.display.set_mode((600, 95))
# # pygame.display.set_caption("Машинка")
# #
# # car = Car()
# # all_sprites = pygame.sprite.Group(car)
# #
# # clock = pygame.time.Clock()
# #
# # running = True
# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #
# #     all_sprites.update()
# #
# #     screen.fill((255, 255, 255))
# #     all_sprites.draw(screen)
# #     pygame.display.flip()
# #
# #     clock.tick(60)
# #
# # pygame.quit()
#
# import pygame
# import random
#
# pygame.init()
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Bombs")
#
# class Bomb(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.image.load('img_3.png')
#         self.rect = self.image.get_rect(center=(x, y))
#         self.exploded = False
#         self.explosion_image = pygame.image.load('img_4.png')
#
#     def update(self):
#         if self.exploded:
#             self.image = self.explosion_image
#
# bombs = []
# for i in range(20):
#     x = random.randint(0, 450)
#     y = random.randint(0, 450)
#     bomb = Bomb(x, y)
#     bombs.append(bomb)
#
# clock = pygame.time.Clock()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             pos = pygame.mouse.get_pos()
#             for bomb in bombs:
#                 if bomb.rect.collidepoint(pos):
#                     bomb.exploded = True
#
#     for bomb in bombs:
#         if not bomb.rect.colliderect(screen.get_rect()):
#             bombs.remove(bomb)
#         bomb.update()
#
#     screen.fill((255, 255, 255))
#     for bomb in bombs:
#         screen.blit(bomb.image, bomb.rect)
#     pygame.display.flip()
#
#     clock.tick(60)
#
# pygame.quit()

# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((600, 300))
#
# image = pygame.image.load('img_6.png')
#
# x = -image.get_width()
# y = (screen.get_height() - image.get_height()) / 2
#
# speed = 200  # пикселей в секунду
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 255))
#
#     screen.blit(image, (x, y))
#
#     x += speed / pygame.time.get_ticks()  # расстояние = скорость * время
#     if x > screen.get_width()-480:
#         x = screen.get_width()-480
#         speed = 0
#
#     pygame.display.flip()
#
# pygame.quit()
import pygame
import os
import sys


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

tile_image = {'wall': load_image('img_7.png'),
              'empty': load_image('img_8.png')}
player_image = load_image('img_9.png')

tile_width = tile_height = 50


class ScreenFrame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = (0, 0, 500, 500)


class SpriteGroup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for inet in self:
            inet.get_event(event)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_image[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 15,
                                               tile_height * self.pos[1] + 5)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():

    fon = pygame.transform.scale(load_image('img_10.png'), size)
    screen.blit((fon), (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = '.'
    return new_player, x, y


def move(hero, movement):
    x, y = hero.pos
    if movement == 'up':
        if y > 0 and level_map[y - 1][x] == '.':
            hero.move(x, y - 1)
    elif movement == 'down':
        if y < max_y - 1 and level_map[y + 1][x] == '.':
            hero.move(x, y + 1)
    elif movement == 'left':
        if x > 0 and level_map[y][x - 1] == '.':
            hero.move(x - 1, y)
    elif movement == 'right':
        if x < max_x - 1 and level_map[y][x + 1] == '.':
            hero.move(x + 1, y)


if __name__ == '__main__':
    pygame.display.set_caption('Марио')
    player = None
    ranning = True
    start_screen()
    level_map = load_level('map.map')
    hero, max_x, max_y = generate_level(level_map)
    while ranning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ranning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move(hero, 'up')
                if event.key == pygame.K_DOWN:
                    move(hero, 'down')
                if event.key == pygame.K_RIGHT:
                    move(hero, 'right')
                if event.key == pygame.K_LEFT:
                    move(hero, 'left')
        screen.fill(pygame.Color('black'))
        sprite_group.draw(screen)
        hero_group.draw(screen)
        pygame.display.flip()
    pygame.quit()