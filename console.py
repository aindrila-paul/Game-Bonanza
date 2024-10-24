import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Console')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (23, 145, 135)

# Paddle properties for Pong
paddle_width, paddle_height = 10, 100
paddle_speed = 10

# Ball properties for Pong
ball_size = 20
ball_speed_x, ball_speed_y = 5, 5

# Initialize scores for Pong
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Game board for Tic Tac Toe
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Function to draw the Tic Tac Toe board
def draw_tic_tac_toe():
    screen.fill(BLACK)  # Set background to black
    # Draw grid lines
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), 5)

    # Draw Xs and Os
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, WHITE, (col * 100 + 15, row * 100 + 15), (col * 100 + 85, row * 100 + 85), 5)
                pygame.draw.line(screen, WHITE, (col * 100 + 85, row * 100 + 15), (col * 100 + 15, row * 100 + 85), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, WHITE, (col * 100 + 50, row * 100 + 50), 40, 5)

# Function to check for a win in Tic Tac Toe
def check_win():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    return False

# Function to reset the Tic Tac Toe game
def reset_game():
    global board, current_player
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

# Function to draw the Pong game
def draw_pong():
    screen.fill(BLACK)  # Set background to black
    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (width // 4, 20))
    screen.blit(right_text, (width * 3 // 4 - right_text.get_width(), 20))

# Function to run the Pong game
def run_pong():
    global left_score, right_score, ball, ball_speed_x, ball_speed_y, left_paddle, right_paddle

    # Declare ball speed as global
    global ball_speed_x, ball_speed_y

    ball = pygame.Rect(width // 2, height // 2, ball_size, ball_size)
    left_score = 0
    right_score = 0
    left_paddle = pygame.Rect(50, (height - paddle_height) // 2, paddle_width, paddle_height)
    right_paddle = pygame.Rect(width - 50 - paddle_width, (height - paddle_height) // 2, paddle_width, paddle_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_s] and left_paddle.bottom < height:
            left_paddle.y += paddle_speed
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN] and right_paddle.bottom < height:
            right_paddle.y += paddle_speed

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top and bottom
        if ball.top <= 0 or ball.bottom >= height:
            ball_speed_y = -ball_speed_y

        # Ball collision with paddles
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x

        # Scoring
        if ball.left <= 0:
            right_score += 1
            ball.x, ball.y = width // 2, height // 2  # Reset ball position
        if ball.right >= width:
            left_score += 1
            ball.x, ball.y = width // 2, height // 2  # Reset ball position

        draw_pong()
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS

# Function to run the Rock-Paper-Scissors game
def run_rock_paper_scissors():
    options = ['Rock', 'Paper', 'Scissors']
    running = True
    while running:
        screen.fill(BLACK)
        font_menu = pygame.font.Font(None, 36)
        title_text = font_menu.render('Rock-Paper-Scissors', True, WHITE)
        instructions_text = font_menu.render('Press R for Rock, P for Paper, S for Scissors, Q to Quit', True, WHITE)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))
        screen.blit(instructions_text, (width // 2 - instructions_text.get_width() // 2, height // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_choice = 'Rock'
                elif event.key == pygame.K_p:
                    player_choice = 'Paper'
                elif event.key == pygame.K_s:
                    player_choice = 'Scissors'
                elif event.key == pygame.K_q:
                    running = False
                else:
                    continue
                
                computer_choice = random.choice(options)
                result_text = f'You chose {player_choice}, Computer chose {computer_choice}.'

                if player_choice == computer_choice:
                    result_text += ' It\'s a tie!'
                elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
                     (player_choice == 'Paper' and computer_choice == 'Rock') or \
                     (player_choice == 'Scissors' and computer_choice == 'Paper'):
                    result_text += ' You win!'
                else:
                    result_text += ' You lose!'

                # Display result
                screen.fill(BLACK)
                result_display = font_menu.render(result_text, True, WHITE)
                screen.blit(result_display, (width // 2 - result_display.get_width() // 2, height // 2))
                pygame.display.flip()
                pygame.time.wait(2000)  # Wait for 2 seconds before the next round

# Modify the main menu function to include Rock-Paper-Scissors
def main_menu():
    global running
    while running:
        screen.fill(BLACK)
        font_menu = pygame.font.Font(None, 24)
        title_text = font_menu.render('Select Game:', True, WHITE)
        pong_text = font_menu.render('1. Pong', True, WHITE)
        ttt_text = font_menu.render('2. Tic Tac Toe', True, WHITE)
        rps_text = font_menu.render('3. Rock-Paper-Scissors', True, WHITE)
        sn_text = font_menu.render('4. Snake Game', True, WHITE)
        quit_text = font_menu.render('5. Quit', True, WHITE)

        # Display the game options in the main menu
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 4))
        screen.blit(pong_text, (width // 2 - pong_text.get_width() // 2, height // 2 - 40))
        screen.blit(ttt_text, (width // 2 - ttt_text.get_width() // 2, height // 2))
        screen.blit(rps_text, (width // 2 - rps_text.get_width() // 2, height // 2 + 40))
        screen.blit(sn_text, (width // 2 - sn_text.get_width() // 2 + 20, height // 2 + 80))  # Shifted to the right
        screen.blit(quit_text, (width // 2 - quit_text.get_width() // 2, height // 2 + 120))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    run_pong()
                elif event.key == pygame.K_2:
                    run_tic_tac_toe()
                elif event.key == pygame.K_3:
                    run_rock_paper_scissors()
                elif event.key == pygame.K_4:
                    run_snake()
                elif event.key == pygame.K_5:
                    running = False

# Function to run the Tic Tac Toe game
def run_tic_tac_toe():
    global current_player
    reset_game()  # Reset the game board
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                x, y = event.pos
                row, col = y // 100, x // 100
                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_win():
                        print(f'Player {current_player} wins!')
                        reset_game()
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

        draw_tic_tac_toe()
        pygame.display.flip()

# Snake properties
snake_pos = [(100, 50), (90, 50), (80, 50)]  # Initial snake position
snake_direction = 'RIGHT'  # Initial direction
food_pos = (0, 0)  # Initial food position
food_spawned = True  # Flag to track if food is spawned
score = 0  # Initial score

# Function to run the Snake game
def run_snake():
    global snake_pos, snake_direction, food_pos, food_spawned, score
    snake_pos = [(100, 50), (90, 50), (80, 50)]  # Reset snake
    snake_direction = 'RIGHT'  # Reset direction
    food_spawned = True  # Reset food flag
    score = 0  # Reset score

    clock = pygame.time.Clock()  # Create a clock to control the game speed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'

        # Move the snake
        if snake_direction == 'UP':
            new_head = (snake_pos[0][0], snake_pos[0][1] - 10)
        elif snake_direction == 'DOWN':
            new_head = (snake_pos[0][0], snake_pos[0][1] + 10)
        elif snake_direction == 'LEFT':
            new_head = (snake_pos[0][0] - 10, snake_pos[0][1])
        elif snake_direction == 'RIGHT':
            new_head = (snake_pos[0][0] + 10, snake_pos[0][1])

        # Check for collision with food
        if new_head == food_pos:
            score += 1
            food_spawned = False  # Food eaten, set flag to spawn new food
        else:
            snake_pos.pop()  # Remove the last segment if no food eaten

        snake_pos.insert(0, new_head)  # Add new head to the snake

        # Check for collision with boundaries or itself
        if (new_head[0] < 0 or new_head[0] >= width or
            new_head[1] < 0 or new_head[1] >= height or
            new_head in snake_pos[1:]):
            print('Game Over! Your score was:', score)
            running = False

        # Spawn food if needed
        if not food_spawned:
            while True:
                food_pos = (random.randint(0, (width // 10) - 1) * 10,
                             random.randint(0, (height // 10) - 1) * 10)
                # Ensure food does not spawn on the snake
                if food_pos not in snake_pos:
                    food_spawned = True
                    break

        draw_snake_game()
        pygame.display.flip()
        clock.tick(15)  # Control the game speed (15 FPS)

# Function to draw the Snake game
def draw_snake_game():
    screen.fill(BLACK)  # Set background to black
    for pos in snake_pos:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))  # Draw snake segments
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))  # Draw food
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))  # Display score
    
# Start the main menu
running = True
main_menu()

# Clean up
pygame.quit()
sys.exit()