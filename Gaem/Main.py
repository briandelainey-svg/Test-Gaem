import pygame
import random

# --- CONFIG ---
WIDTH, HEIGHT = 240, 480
GRID_SIZE = 24
COLS, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# Shapes
SHAPES = [
    [[1],[1],[1],[1]],             # I
    [[1,0,0],[1,1,1]],             # J
    [[0,0,1],[1,1,1]],             # L
    [[1,1],[1,1]],                 # O
    [[0,1,1],[1,1,0]],             # S
    [[0,1,0],[1,1,1]],             # T
    [[1,1,0],[0,1,1]]              # Z
]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# --- PIECE CLASS ---
class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

# --- GRID ---
grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

def valid_move(piece, dx, dy):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                nx = piece.x + x + dx
                ny = piece.y + y + dy
                if nx < 0 or nx >= COLS or ny >= ROWS:
                    return False
                if ny >= 0 and grid[ny][nx] != BLACK:
                    return False
    return True

def lock_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = piece.color

def clear_lines():
    global grid
    new_grid = [row for row in grid if any(cell == BLACK for cell in row)]
    lines_cleared = ROWS - len(new_grid)
    for _ in range(lines_cleared):
        new_grid.insert(0, [BLACK for _ in range(COLS)])
    grid = new_grid
    return lines_cleared

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, grid[y][x],
                             (x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, GRAY,
                             (x*GRID_SIZE, y*GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def draw_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, piece.color,
                    ((piece.x + x)*GRID_SIZE, (piece.y + y)*GRID_SIZE,
                     GRID_SIZE, GRID_SIZE))

# --- GAME LOOP ---
piece = Piece()
fall_time = 0
fall_speed = 500
score = 0

running = True
while running:
    dt = clock.tick(60)
    fall_time += dt

    screen.fill(BLACK)

    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and valid_move(piece, -1, 0):
                piece.x -= 1
            if event.key == pygame.K_RIGHT and valid_move(piece, 1, 0):
                piece.x += 1
            if event.key == pygame.K_DOWN and valid_move(piece, 0, 1):
                piece.y += 1
            if event.key == pygame.K_UP:
                old_shape = piece.shape
                piece.rotate()
                if not valid_move(piece, 0, 0):
                    piece.shape = old_shape

    # Falling
    if fall_time > fall_speed:
        if valid_move(piece, 0, 1):
            piece.y += 1
        else:
            lock_piece(piece)
            score += clear_lines() * 100
            piece = Piece()
            if not valid_move(piece, 0, 0):
                print("Game Over! Score:", score)
                running = False
        fall_time = 0

    draw_grid()
    draw_piece(piece)

    pygame.display.flip()

pygame.quit()