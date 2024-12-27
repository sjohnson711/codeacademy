import pygame, sys, time, random

# Game speed (controls the refresh rate for movement)
speed = 15

# Window dimensions
frame_size_x = 720
frame_size_y = 480

# Initialize pygame modules (returns a tuple with the number of successes and failures)
check_errors = pygame.init()
if check_errors[1] > 0:  # If any module failed to initialize
    print(f"Error {check_errors[1]}")
else:
    print("Game Successfully initialized")

# Set up the game window
pygame.display.set_caption("Snake Game")  # Title of the window
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))  # Window size

# Define colors using RGB values
black = pygame.Color(0, 0, 0)  # Background color
white = pygame.Color(255, 255, 255)  # Text color
red = pygame.Color(255, 0, 0)  # Food color
green = pygame.Color(0, 255, 0)  # Snake color
blue = pygame.Color(0, 0, 255)  # (Unused) optional color

# Control the game refresh rate (frames per second)
fps_controller = pygame.time.Clock()

# Size of each "square" in the snake and food
square_size = 20

# Initialize game variables
def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction
    direction = "RIGHT"  # Initial movement direction
    head_pos = [120, 60]  # Starting position of the snake's head
    snake_body = [[120, 60]]  # Initial snake body (1 block)
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size]  # Random food position
    food_spawn = True  # Flag to indicate if food is available
    score = 0  # Player's score

init_vars()  # Initialize all game variables

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)  # Set font type and size
    score_surface = score_font.render("Score: " + str(score), True, color)  # Create a score surface
    score_rect = score_surface.get_rect()  # Get the rectangle around the text
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)  # Top-left position for score
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)  # Center position for game over screen
    game_window.blit(score_surface, score_rect)  # Draw the score onto the game window

# Main game loop
while True:
    # Handle input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Handle key presses
            # Change direction based on arrow keys or WASD
            if (event.key == pygame.K_UP or event.key == ord("w")) and direction != "DOWN":
                direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")) and direction != "UP":
                direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")) and direction != "RIGHT":
                direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake by updating the head position
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    elif direction == "RIGHT":
        head_pos[0] += square_size

    # Wrap around if the snake goes off the screen
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    # Eating the food
    snake_body.insert(0, list(head_pos))  # Add a new block to the snake
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False  # Remove the food
    else:
        snake_body.pop()  # Remove the last block if no food eaten

    # Spawn new food if it was eaten
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
        food_spawn = True

    # Draw the game
    game_window.fill(black)  # Clear the screen
    for pos in snake_body:  # Draw the snake
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], square_size, square_size))
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], square_size, square_size))  # Draw the food

    # Check for collisions with the snake's body
    for block in snake_body[1:]:  # Ignore the head
        if head_pos[0] == block[0] and head_pos[1] == block[1]:  # Collision detected
            init_vars()  # Reset the game

    # Display the score
    show_score(1, white, 'consolas', 20)
    pygame.display.update()  # Refresh the game window

    # Control the frame rate
    fps_controller.tick(speed)





