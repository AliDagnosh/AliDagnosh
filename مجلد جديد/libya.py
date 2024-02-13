import pygame
import time

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)

# Define questions and answers
questions = [
    "question 1",
    "question 2",
    "question 3",
    "question 4",
]
answers = [
    ["Berlin", "London", "Paris", "Rome"],
    ["Brasília", "São Paulo", "Rio de Janeiro", "Barcelona"],
    ["Mediterranean Sea", "Red Sea", "Indian Ocean", "Atlantic Ocean"],
    ["Berlin", "London", "Paris", "Rome"],
]
list_africa_correct = [1, 1, 3, 2]

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

# Create the font
font = pygame.font.Font(None, 40)

# Create the background image
image_bg = pygame.Surface(screen.get_size())
image_bg.fill(GRAY)

# Create the answer choices
choice_1 = font.render("Choice 1", True, BLACK)
choice_2 = font.render("Choice 2", True, BLACK)
choice_3 = font.render("Choice 3", True, BLACK)
choice_4 = font.render("Choice 4", True, BLACK)

# Initialize variables
counter_questions = 0
list_answer = []

class GameTimer:
    def __init__(self):
        self.LEVELS = 10
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)

# Create the game timer
timer = GameTimer()

def answer(choice):
    global counter_questions, list_answer

    if counter_questions < len(questions):
        list_answer.append(choice)

    if counter_questions == len(questions) - 1:
        print(list_answer)
        if list_answer == list_africa_correct:
            print("Correct")
        else:
            print("Wrong")

        list_answer.clear()
        counter_questions = -1

    counter_questions += 1

def show_question():
    if counter_questions < len(questions):
        question_text = font.render(questions[counter_questions], True, BLACK)
        screen.blit(question_text, (190, 130))
    else:
        print("Reached the end of the questions")

def show_answers():
    if counter_questions < len(answers):
        answer_choices = answers[counter_questions]
        x = 120
        y = 340
        for i, choice in enumerate(answer_choices):
            answer_text = font.render(str(i + 1) + ". " + choice, True, BLACK)
            screen.blit(answer_text, (x, y))
            if i == 1:
                x += 410
                y = 340
            else:
                y += 100

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 100 <= mouse_pos[0] <= 300 and 300 <= mouse_pos[1] <= 340:
                answer(1)
            elif 500 <= mouse_pos[0] <= 700 and 300 <= mouse_pos[1] <= 340:
                answer(2)
            elif 100 <= mouse_pos[0] <= 300 and 400 <= mouse_pos[1] <= 440:
                answer(3)
            elif 500 <= mouse_pos[0] <= 700 and 400 <= mouse_pos[1] <= 440:
                answer(4)

    # Clear the screen
    screen.blit(image_bg, (0, 0))

    # Show question and answer choices
    show_question()
    show_answers()

    # Show the game timer
    time_text = font.render("Time: " + str(timer.get_level_time()) + " seconds", True, BLACK)
    screen.blit(time_text, (20, 20))

    # Start the timer when the first question is shown