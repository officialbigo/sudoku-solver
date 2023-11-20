import pygame
import sys
GREEN = (0, 255, 0)

def valid(board, c, x, y):
    for i in range(9):
        if board[x][i] == c:
            return False
        if board[i][y] == c:
            return False
        if board[(3*(x//3)+i//3)][3*(y//3)+i%3]==c:
            return False
    return True


def sudoku_solver(board,window):
    for x in range(9):
        for y in range(9):
            if board[x][y] == -1:
                for c in range(1, 10):
                    if valid(board, c, x, y):
                        board[x][y] = c
                        update_grid_pass(board, window,x,y)
                        pygame.time.wait(100)
                        if sudoku_solver(board,window):
                            return True
                        else:
                            board[x][y] = -1
                            update_grid_fail(board,window,x,y)
                            pygame.time.wait(100)
                return False
    return True

pygame.init()
WIDTH, HEIGHT = 540, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

button_x, button_y = 250, 550  # Position of the button
button_width, button_height = 100, 50  # Size of the button
button_color = BLACK
button_text = "Solve"  # Text on the button
button_font = pygame.font.SysFont(None, 30)
button_text_color = WHITE

def draw_button():
    pygame.draw.rect(WINDOW, button_color, (button_x, button_y, button_width, button_height))
    text_surface = button_font.render(button_text, True, button_text_color)
    text_rect = text_surface.get_rect(center=(button_x + button_width / 2, button_y + button_height / 2))
    WINDOW.blit(text_surface, text_rect)

def is_clicked(pos):
    return button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height


def update_grid_fail(board, window, current_x, current_y):
    window.fill(WHITE)  # Clear the window before drawing the grid

    cell_size = WIDTH // 9  # Calculate cell size based on window dimensions

    for i in range(9):
        for j in range(9):
            cell_x, cell_y = j * cell_size, i * cell_size
            pygame.draw.rect(window, GRAY, (cell_x, cell_y, cell_size, cell_size), 1)

            # Highlight the currently updated cell with red borders
            if i == current_x and j == current_y:
                pygame.draw.rect(window, RED, (cell_x, cell_y, cell_size, cell_size), 3)

            # Display numbers in non-empty cells
            if board[i][j] != -1:
                font = pygame.font.Font(None, 36)  # Define font for numbers
                text_surface = font.render(str(board[i][j]), True, BLACK)
                text_rect = text_surface.get_rect(center=(cell_x + cell_size // 2, cell_y + cell_size // 2))
                window.blit(text_surface, text_rect)

    pygame.display.update()


def update_grid_pass(board, window, current_x, current_y):
    window.fill(WHITE)  # Clear the window before drawing the grid

    cell_size = WIDTH // 9  # Calculate cell size based on window dimensions

    for i in range(9):
        for j in range(9):
            cell_x, cell_y = j * cell_size, i * cell_size
            pygame.draw.rect(window, GRAY, (cell_x, cell_y, cell_size, cell_size), 1)

            # Highlight the currently updated cell with red borders
            if i == current_x and j == current_y:
                pygame.draw.rect(window, GREEN, (cell_x, cell_y, cell_size, cell_size), 3)

            # Display numbers in non-empty cells
            if board[i][j] != -1:
                font = pygame.font.Font(None, 36)  # Define font for numbers
                text_surface = font.render(str(board[i][j]), True, BLACK)
                text_rect = text_surface.get_rect(center=(cell_x + cell_size // 2, cell_y + cell_size // 2))
                window.blit(text_surface, text_rect)

    pygame.display.update()

def draw_grid(grid):
    cell_size = WIDTH // 9
    font = pygame.font.SysFont(None, 40)  # Define a font for displaying numbers

    for i in range(9):
        for j in range(9):
            if grid[i][j] != -1:  # Only render non-empty cells
                text = font.render(str(grid[i][j]), True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2)
                WINDOW.blit(text, text_rect.topleft)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(WINDOW, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 3)
            pygame.draw.line(WINDOW, BLACK, (i * cell_size, 0), (i * cell_size, WIDTH), 3)
        else:
            pygame.draw.line(WINDOW, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 1)
            pygame.draw.line(WINDOW, BLACK, (i * cell_size, 0), (i * cell_size, WIDTH), 1)

selected_cell = (0, 0) 



def get_number_input(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            return 1
        elif event.key == pygame.K_2:
            return 2
        elif event.key == pygame.K_3:
            return 3
        elif event.key == pygame.K_4:
            return 4
        elif event.key == pygame.K_5:
            return 5
        elif event.key == pygame.K_6:
            return 6
        elif event.key == pygame.K_7:
            return 7
        elif event.key == pygame.K_8:
            return 8
        elif event.key == pygame.K_9:
            return 9
    return None




grid=[  [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]


running = True
while running:
    WINDOW.fill(WHITE)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #mouse_pos = pygame.mouse.get_pos()
            if is_clicked(mouse_pos):  # Check if the mouse click is within the button area
                # Perform the function (e.g., clear the grid)
                sudoku_solver(grid,WINDOW)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Move to the next cell on pressing "Enter"
                selected_cell = (selected_cell[0], (selected_cell[1] + 1) % 9)  # Move to the next column
                if selected_cell[1] == 0:  # Move to the next row when reaching the end of the row
                    selected_cell = ((selected_cell[0] + 1) % 9, 0)
            elif event.key == pygame.K_BACKSPACE:  # Move to the previous cell on pressing "Backspace"
                selected_cell = (selected_cell[0], (selected_cell[1] - 1) % 9)  # Move to the previous column
                if selected_cell[1] == 8:  # Move to the previous row when reaching the beginning of the row
                    selected_cell = ((selected_cell[0] - 1) % 9, 8)
            else:
                number = get_number_input(event)
                if number is not None:
                    row, col = selected_cell
                    grid[row][col] = number  # Update the grid with the entered number

    # Rendering the grid

    # Display the mouse coordinates in the console

    # Draw a red circle at the mouse position
    pygame.draw.circle(WINDOW, RED, mouse_pos, 10)
    WINDOW.fill(WHITE)
    draw_grid(grid)
    draw_button() 
    # Highlighting the selected cell (optional)
    cell_size = WIDTH // 9
    row, col = selected_cell
    pygame.draw.rect(WINDOW, RED, (col * cell_size, row * cell_size, cell_size, cell_size), 3)

    pygame.display.update()

pygame.quit()
sys.exit()


    
