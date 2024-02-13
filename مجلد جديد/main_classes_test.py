import pygame
from pygame.locals import *
import sys
import string
import subprocess
import time
import textwrap
import threading





class Time__():
    def init(self):
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






# تهيئة اللعبة
pygame.init()

# إعداد الشاشة
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("لعبة بايثون")

# تصغير حجم الصورة
new_width = 200
new_height = 200

BLACK = (0,0,0)

def delay(seconds):
    time.sleep(seconds)
class Image:
    def __init__(self, name_image, width, height):
        self.name_image = name_image
        self.width = width
        self.height = height
        self.image = pygame.image.load(name_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        
    def set_values(self, name_image, width, height):
        self.name_image = name_image
        self.width = width
        self.height = height
        self.image = pygame.image.load(name_image)
        self.image = pygame.transform.scale(self.image, (width, height))
        
    def get_name(self):
        return self.name_image
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def blit(self, screen, x, y):
        screen.blit(self.image, (x, y))
        
    def rect(self):
        self.rect_ = self.image.get_rect()
        self.rect_.topleft = (50, 200)
        if event.type == MOUSEBUTTONDOWN:
            if self.rect_.collidepoint(event.pos):
                print("Is clicked")
        return True

in_result=False
similar_count=0
class level():
    global similar_count
    def __init__(self, questions, answers, correct_answer,stars):
        self.score = 0
        self.stars=stars
        self.list_correct = correct_answer
        self.list_answer = []
        self.counter_questions = 0
        self.counter_answers = 0
        self.questions = questions
        self.answers = answers
        self.num_questions = len(self.questions)
        self.is_equal=False
        self.similar_count= similar_count
        self.level_done=False
        
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stage")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
    
    def draw_background_level(self):
        delay(0.1)
        global similar_count
        map_bg.blit(screen,0,0)
        #self.screen.fill((220, 220, 220))
        self.image_bg = pygame.image.load("btn_bg.png")
        self.screen.blit(image_bg, (150, 20))

        self.choice_1 = Image("button.png",220,100)
        image_rect_choice_1 = self.choice_1.image.get_rect()
        image_rect_choice_1.topleft = (100, 300)

        self.choice_2 = Image("button.png",220,100)
        image_rect_choice_2 = self.choice_2.image.get_rect()
        image_rect_choice_2.topleft = (500, 300)

        self.choice_3 = Image("button.png",220,100)
        image_rect_choice_3 = self.choice_3.image.get_rect()
        image_rect_choice_3.topleft = (100, 400)

        self.choice_4 = Image("button.png",220,100)
        image_rect_choice_4 = self.choice_4.image.get_rect()
        image_rect_choice_4.topleft = (500, 400)

        

        self.screen.blit(choice_1, image_rect_choice_1.topleft)
        self.screen.blit(choice_2, image_rect_choice_2.topleft)
        self.screen.blit(choice_3, image_rect_choice_3.topleft)
        self.screen.blit(choice_4, image_rect_choice_4.topleft)
        
        self.show_question()
        self.show_answers()

        pygame.display.flip()
    
    def answer(self, choice):
        global total_score
        global similar_count
        self.draw_background_level()
        
        if self.counter_questions <= self.num_questions:
            self.list_answer.append(choice)
            print(self.list_answer)
            
        if self.counter_questions == self.num_questions:
            print(self.list_answer)
            global in_result
            for i in range(len(self.list_answer)):
                if self.list_answer[i] == self.list_correct[i]:
                    self.similar_count += 1
                    
            if self.list_answer == self.list_correct:
                print("Correct")
                self.score += 10
                self.is_equal=True
            else:
                print("Wrong")
                print(self.list_correct)
            global in_level
            self.list_answer.clear()
            total_score+=self.score
            init_continents()
            #in_level=False
            in_result=True
            if(not self.level_done):
                if self.similar_count<7 and self.similar_count >=5:
                    self.stars=1
                    self.level_done=True
                if self.similar_count<9 and self.similar_count >=7:
                    self.stars=2
                    self.level_done=True
                if self.similar_count==9:
                    self.stars=3
                    self.level_done=True
                if self.similar_count<5:
                    self.stars=0
            similar_count=self.similar_count
            draw_result()
            #draw_map()
            self.counter_questions = 0
            self.counter_answers = 0
    def get_correct_num(self):
        return self.similar_count
    def show_question(self):
        if self.counter_questions < self.num_questions:
            question = self.questions[self.counter_questions]
            wrapped_text = textwrap.wrap(question, width=30)  # تقسيم السؤال إلى أسطر باستخدام عرض 30 حرفًا (يمكنك تعديل القيمة حسب احتياجاتك)

            # عرض السؤال في سطرين إذا كان طويلاً
            if len(wrapped_text) > 1:
                y_position = 130
                for line in wrapped_text:
                    question_text = self.font.render(line, True, BLACK)
                    self.screen.blit(question_text, (190, y_position))
                    y_position += 30  # تحديد المسافة العمودية بين الأسطر
            else:
                question_text = self.font.render(question, True, BLACK)
                self.screen.blit(question_text, (190, 130))

            self.counter_questions += 1
        
    
    def show_answers(self):
        if self.counter_answers < self.num_questions:
            answer_choices = self.answers[self.counter_answers]
            x = 120
            y = 340
            for i, choice in enumerate(answer_choices):
                answer_text = self.font.render( choice, True, BLACK)
                self.screen.blit(answer_text, (x, y))
                if i == 1:
                    x += 410
                    y = 340
                else:
                    y += 100
            self.counter_answers += 1
    def get_stars(self):
        return self.stars
    def get_last_similar_count(self):
        global similar_count
        similar_count=self.similar_count
        return self.similar_count



star=Image("star.png",80,80)
x_star=Image("star1.png",80,80)
star_on_map=Image("star.png",20,20)
x_star_on_map=Image("star1.png",20,20)
btn_back_to_map = pygame.image.load("button.png")
btn_back_to_map = pygame.transform.scale(btn_back_to_map, (220, 100))


image_rect_btn_back_to_map = btn_back_to_map.get_rect()
image_rect_btn_back_to_map.topleft = (310, 400)
def draw_star_in_level():
   #print("3stars")
    if level_africa.level_done:
        if level_africa.get_stars()==3:
            star_on_map.blit(screen,360,275)
            star_on_map.blit(screen,380,275)
            star_on_map.blit(screen,400,275)
        if level_africa.get_stars()==2:
            star_on_map.blit(screen,360,275)
            star_on_map.blit(screen,380,275)
            x_star_on_map.blit(screen,400,275)
        if level_africa.get_stars()==1:
            star_on_map.blit(screen,360,275)
            x_star_on_map.blit(screen,380,275)
            x_star_on_map.blit(screen,400,275)
        if level_africa.get_stars()==0:
            x_star_on_map.blit(screen,360,275)
            x_star_on_map.blit(screen,380,275)
            x_star_on_map.blit(screen,400,275)

    if level_asia.level_done:
        if level_asia.get_stars()==3:
            star_on_map.blit(screen,510,190)
            star_on_map.blit(screen,530,190)
            star_on_map.blit(screen,550,190)
        if level_asia.get_stars()==2:
            star_on_map.blit(screen,510,190)
            star_on_map.blit(screen,530,190)
            x_star_on_map.blit(screen,550,190)
        if level_asia.get_stars()==1:
            star_on_map.blit(screen,510,190)
            x_star_on_map.blit(screen,530,190)
            x_star_on_map.blit(screen,550,190)
        if level_asia.get_stars()==0:
            x_star_on_map.blit(screen,510,190)
            x_star_on_map.blit(screen,530,190)
            x_star_on_map.blit(screen,550,190)
    if level_europe.level_done:
        if level_europe.get_stars()==3:
            star_on_map.blit(screen,375,185)
            star_on_map.blit(screen,395,185)
            star_on_map.blit(screen,415,185)
        if level_europe.get_stars()==2:
            star_on_map.blit(screen,375,185)
            star_on_map.blit(screen,395,185)
            x_star_on_map.blit(screen,415,185)
        if level_europe.get_stars()==1:
            star_on_map.blit(screen,375,185)
            x_star_on_map.blit(screen,395,185)
            x_star_on_map.blit(screen,415,185)
        if level_europe.get_stars()==0:
            x_star_on_map.blit(screen,375,185)
            x_star_on_map.blit(screen,395,185)
            x_star_on_map.blit(screen,415,185)

    if level_australia.level_done:
        if level_australia.get_stars()==3:
            star_on_map.blit(screen,634,410)
            star_on_map.blit(screen,654,410)
            star_on_map.blit(screen,674,410)
        if level_australia.get_stars()==2:
            star_on_map . blit(screen,634,410)
            star_on_map . blit(screen,654,410)
            x_star_on_map.blit(screen,674,410)
        if level_australia.get_stars()==1:
            star_on_map . blit(screen,634,410)
            x_star_on_map.blit(screen,654,410)
            x_star_on_map.blit(screen,674,410)
        if level_australia.get_stars()==0:
            x_star_on_map.blit(screen,634,410)
            x_star_on_map.blit(screen,654,410)
            x_star_on_map.blit(screen,674,410)

    if level_south_america.level_done:
        if level_south_america.get_stars()==3:
            star_on_map.blit(screen,70,160 )
            star_on_map.blit(screen,90,160 )
            star_on_map.blit(screen,110,160)
        if level_south_america.get_stars()==2:
            star_on_map . blit(screen,70,160 )
            star_on_map . blit(screen,90,160 )
            x_star_on_map.blit(screen,110,160)
        if level_south_america.get_stars()==1:
            star_on_map . blit(screen,70,160 )
            x_star_on_map.blit(screen,90,160 )
            x_star_on_map.blit(screen,110,160)
        if level_south_america.get_stars()==0:
            x_star_on_map.blit(screen,70,160 )
            x_star_on_map.blit(screen,90,160 )
            x_star_on_map.blit(screen,110,160)
            #====================================================================
    if level_north_america.level_done:
        if level_north_america.get_stars()==3:
            star_on_map.blit(screen,150,345)
            star_on_map.blit(screen,170,345)
            star_on_map.blit(screen,190,345)
        if level_north_america.get_stars()==2:
            star_on_map . blit(screen,150,345)
            star_on_map . blit(screen,170,345)
            x_star_on_map.blit(screen,190,345)
        if level_north_america.get_stars()==1:
            star_on_map . blit(screen,150,345)
            x_star_on_map.blit(screen,170,345)
            x_star_on_map.blit(screen,190,345)
        if level_north_america.get_stars()==0:
            x_star_on_map.blit(screen,150,345)
            x_star_on_map.blit(screen,170,345)
            x_star_on_map.blit(screen,190,345)
            #=============================================================

def draw_result():
        #delay(0.2)
        global in_result
        in_result=True
        result_text = "correct :"+str(similar_count)
        print(similar_count)
        map_bg.blit(screen,0,0)
        ##screen.fill((220, 220, 220))
        image_bg = pygame.image.load("btn_bg.png")
        screen.blit(image_bg, (120, 80)) 

        text = font.render(result_text, True, BLACK)
        screen.blit(text, (190, 130))

        
        screen.blit(choice_1, image_rect_btn_back_to_map.topleft)
        text = font.render("Ok", True, BLACK)
        screen.blit(text, (400, 440))
        if similar_count<7 and similar_count >=5:
            star.blit(screen,270,20)
            x_star.blit(screen,360,20)
            x_star.blit(screen,450,20)
        if similar_count<9 and similar_count >=7:
            star.blit(screen,270,20)
            star.blit(screen,360,20)
            x_star.blit(screen,450,20)
        if similar_count==9:
            star.blit(screen,270,20)
            star.blit(screen,360,20)
            star.blit(screen,450,20)
        if similar_count<5:
            x_star.blit(screen,270,20)
            x_star.blit(screen,360,20)
            x_star.blit(screen,450,20)
          
    #    if level_africa.get_last_similar_count()<7 and level_africa.get_last_similar_count() >=5:
    #        star.blit(screen,270,20)
    #        x_star.blit(screen,360,20)
    #        x_star.blit(screen,450,20)
    #    if level_africa.get_last_similar_count()<9 and level_africa.get_last_similar_count() >=7:
    #        star.blit(screen,270,20)
    #        star.blit(screen,360,20)
    #        x_star.blit(screen,450,20)
    #    if level_africa.get_last_similar_count()==9:
    #        star.blit(screen,270,20)
    #        star.blit(screen,360,20)
    #        star.blit(screen,450,20)
    #    if level_africa.get_last_similar_count()<5:
    #        x_star.blit(screen,270,20)
    #        x_star.blit(screen,360,20)
    #        x_star.blit(screen,450,20)
        


total_score = 0
# أفريقيا
questions_africa = [
    "What is the capital of Egypt?",
    "Which country is known as the 'Rainbow Nation'?",
    "What is the official language of Nigeria?",
    "Which city is considered the 'Gateway to Africa'?",
    "Which country is famous for the Serengeti National Park?",
    "What is the currency of South Africa?",
    "Which country is home to the Nile River?",
    "What is the official language of Kenya?",
    "Which city is the capital of Morocco?",
    ""
]

answers_africa = [
    ["Cairo", "Johannesburg", "Lagos", "Nairobi"],
    ["South Africa", "Egypt", "Morocco", "Nigeria"],
    ["English", "Arabic", "Swahili", "French"],
    ["Cape Town", "Lagos", "Nairobi", "Cairo"],
    ["Tanzania", "Kenya", "South Africa", "Ethiopia"],
    ["South African Rand", "Egyptian Pound", "Nigerian Naira", "Kenyan Shilling"],
    ["Egypt", "Sudan", "Nigeria", "Tanzania"],
    ["Swahili", "English", "Arabic", "French"],
    ["Rabat", "Cairo", "Nairobi", "Casablanca"],
    ["", "", "", ""]
]

correct_answers_africa = [1, 1, 3, 4, 2, 1, 1, 2, 1]

level_africa = level(questions_africa, answers_africa, correct_answers_africa,0)  
# آسيا
questions_asia = [
    "What is the capital of China?",
    "Which country is known as the 'Land of the Rising Sun'?",
    "What is the official language of India?",
    "Which city is considered the financial hub of Asia?",
    "Which country is famous for the Taj Mahal?",
    "What is the currency of Japan?",
    "Which country is home to Mount Everest?",
    "What is the official language of South Korea?",
    "Which city is the capital of Thailand?",
    "Which country is known for its Great Wall?"
]

answers_asia = [
    ["Beijing", "Shanghai", "Tokyo", "New Delhi"],
    ["Japan", "China", "South Korea", "Thailand"],
    ["Hindi", "Mandarin", "English", "Arabic"],
    ["Hong Kong", "Singapore", "Tokyo", "Seoul"],
    ["India", "China", "Thailand", "Japan"],
    ["Japanese Yen", "Chinese Yuan", "Indian Rupee", "South Korean Won"],
    ["Nepal", "India", "China", "Bhutan"],
    ["Korean", "Japanese", "Thai", "Mandarin"],
    ["Bangkok", "Singapore", "Kuala Lumpur", "Jakarta"],
    ["China", "India", "Japan", "South Korea"]
]

correct_answers_asia = [1, 2, 1, 3, 1, 2, 1, 4, 1] 
level_asia = level(questions_asia, answers_asia, correct_answers_asia,0)

# أوروبا
questions_europe = [
    "What is the capital of France?",
    "Which country is known as the 'Land of Pasta and Pizza'?",
    "What is the official language of Germany?",
    "Which city is considered the 'City of Love'?",
    "Which country is famous for its windmills and tulip fields?",
    "What is the currency of the United Kingdom?",
    "Which country is home to the Acropolis?",
    "What is the official language of Spain?",
    "Which city is the capital of Russia?",
    "Which country is known for its Colosseum?"
]

answers_europe = [
    ["Paris", "Rome", "Berlin", "Madrid"],
    ["Italy", "France", "Germany", "Spain"],
    ["German", "French", "Italian", "Spanish"],
    ["Paris", "Rome", "Berlin", "Athens"],
    ["Netherlands", "Belgium", "France", "Italy"],
    ["British Pound", "Euro", "US Dollar", "Swiss Franc"],
    ["Greece", "Italy", "Spain", "Turkey"],
    ["Spanish", "German", "French", "Italian"],
    ["Moscow", "St. Petersburg", "Kiev", "Warsaw"],
    ["Italy", "France", "Germany", "Greece"]
]

correct_answers_europe = [1, 2, 1, 1, 1, 1, 1, 4, 1]

level_europe = level(questions_europe, answers_europe, correct_answers_europe,0) 

# أمريكا الجنوبية
questions_south_america = [
    "What is the capital of Brazil?",
    "Which country is known for the Galapagos Islands?",
    "What is the official language of Argentina?",
    "Which city is considered the 'Paris of South America'?",
    "Which country is famous for Machu Picchu?",
    "What is the currency of Chile?",
    "Which country is home to Angel Falls?",
    "What is the official language of Colombia?",
    "Which city is the capital of Peru?",
    "Which country is known for the Amazon Rainforest?"
]

answers_south_america = [
    ["Brasília", "Buenos Aires", "Rio de Janeiro", "São Paulo"],
    ["Ecuador", "Brazil", "Colombia", "Peru"],
    ["Spanish", "Portuguese", "English", "French"],
    ["Buenos Aires", "Lima", "Santiago", "São Paulo"],
    ["Peru", "Brazil", "Colombia", "Ecuador"],
    ["Chilean Peso", "Brazilian Real", "Argentine Peso", "Peruvian Sol"],
    ["Venezuela", "Brazil", "Colombia", "Argentina"],
    ["Spanish", "Portuguese", "English", "French"],
    ["Lima", "Bogotá", "Quito", "Santiago"],
    ["Brazil", "Colombia", "Peru", "Ecuador"]
]

correct_answers_south_america = [1, 1, 1, 2, 1, 4, 3, 1, 2]
level_south_america = level(questions_south_america, answers_south_america, correct_answers_south_america,0)  

# أستراليا
questions_australia = [
    "What is the capital of Australia?",
    "Which country is known for the Sydney Opera House?",
    "What is the official language of Australia?",
    "Which city is considered the 'City of Sails'?",
    "Which country is famous for the Great Barrier Reef?",
    "What is the currency of Australia?",
    "Which country is home to Ayers Rock (Uluru)?",
    "What is the official language of New Zealand?",
    "Which city is the capital of New Zealand?",
    "Which country is known for its kangaroos?"
]

answers_australia = [
    ["Canberra", "Sydney", "Melbourne", "Brisbane"],
    ["Australia", "New Zealand", "Fiji", "Papua New Guinea"],
    ["English", "Australian", "Maori", "Aboriginal"],
    ["Auckland", "Sydney", "Melbourne", "Brisbane"],
    ["Australia", "New Zealand", "Fiji", "Indonesia"],
    ["Australian Dollar", "New Zealand Dollar", "Fijian Dollar", "Papua New Guinean Kina"],
    ["Australia", "New Zealand", "Fiji", "Indonesia"],
    ["English", "Australian", "Maori", "Aboriginal"],
    ["Wellington", "Auckland", "Christchurch", "Queenstown"],
    ["Australia", "New Zealand", "Fiji", "Papua New Guinea"]
]

correct_answers_australia = [1, 1, 1, 2, 1, 1, 1, 1, 1, 1]
level_australia = level(questions_australia, answers_australia, correct_answers_australia,0)  

# أمريكا الشمالية
questions_north_america = [
    "What is the capital of the United States?",
    "Which country is known for maple syrup?",
    "What is the official language of Canada?",
    "Which city is considered the 'Big Apple'?",
    "Which country is famous for the Grand Canyon?",
    "What is the currency of Mexico?",
    "Which country is home to Niagara Falls?",
    "What is the official language of the United States?",
    "Which city is the capital of Canada?",
    "Which country is known for Hollywood?"
]

answers_north_america = [
    ["Washington, D.C.", "New York City", "Los Angeles", "Toronto"],
    ["Canada", "United States", "Mexico", "Jamaica"],
    ["English", "Spanish", "French", "German"],
    ["New York City", "Los Angeles", "Chicago", "Toronto"],
    ["United States", "Canada", "Mexico", "Brazil"],
    ["Mexican Peso", "Canadian Dollar", "American Dollar", "Jamaican Dollar"],
    ["United States", "Canada", "Mexico", "Brazil"],
    ["English", "Spanish", "French", "German"],
    ["Ottawa", "Toronto", "Vancouver", "Montreal"],
    ["United States", "Canada", "Mexico", "Brazil"]
]

correct_answers_north_america = [1, 2, 1, 1, 1, 2, 2, 1, 1, 1]
level_north_america = level(questions_north_america, answers_north_america, correct_answers_north_america,0)  

choice_1_ = Image("button.png",210,100)
choice_2 = Image("button.png",210,100)
choice_3 = Image("button.png",210,100)
choice_4 = Image("button.png",210,100)

choice_1 = pygame.image.load("button.png")
choice_1 = pygame.transform.scale(choice_1, (220, 100))


image_rect_chioce1 = choice_1.get_rect()
image_rect_chioce1.topleft = (100, 300)

choice_2 = pygame.image.load("button.png")
choice_2 = pygame.transform.scale(choice_2, (220, 100))
image_rect_choice_2 = choice_2.get_rect()
image_rect_choice_2.topleft = (500, 300)

choice_3 = pygame.image.load("button.png")
choice_3 = pygame.transform.scale(choice_3, (220, 100))
image_rect_choice_3 = choice_3.get_rect()
image_rect_choice_3.topleft = (100, 400)

choice_4 = pygame.image.load("button.png")
choice_4 = pygame.transform.scale(choice_4, (220, 100))
image_rect_choice_4 = choice_4.get_rect()
image_rect_choice_4.topleft = (500, 400)

def init_continents():
    global is_africa
    global is_ustralia
    global is_erup
    global is_asia
    global is_amrica2
    global is_amrica1
    is_africa=False
    is_ustrali=False
    is_erup=False
    is_asia=False
    is_amrica2=False
    is_amrica1=False




#=====================================================================
    





map_bg = Image("map2.png",screen_width,screen_height)
africa=Image("africa.png",new_width,new_height)
asia=Image("asia.png",new_width+80, new_height)
ustralia=Image("ustralia.png",new_width-100, new_height-110)
amrica1=Image("amrica1.png",new_width-50, new_height)
amrica2=Image("amrica2.png",new_width+50, new_height)
erup=Image("erup.png",new_width-40, new_height-115)

asia_lock=Image("asia_lock.png",new_width+80, new_height)
ustralia_lock=Image("ustralia_lock.png",new_width-100, new_height-110)
amrica1_lock=Image("amrica1_lock.png",new_width-50, new_height)
amrica2_lock=Image("amrica2_lock.png",new_width+50, new_height)
erup_lock=Image("erup_lock.png",new_width-40, new_height-115)

button=Image("button.png",new_width-40, new_height-115)

continue_img=Image("continuous.png",new_width-170, new_height-170)

help_img=Image("help.png",50, 50)

clock = pygame.time.Clock()

#مواقع القارات
x_africa = 290
y_africa = 250
x_asia=436
y_asia=164
x_ustralia=600
y_ustralia=400
x_amrica1=120
y_amrica1=320
x_amrica2=0
y_amrica2=135
x_erup=320
y_erup=168
#التحقق من الضغط على القارات
is_in_map=False
is_in_main_menu=False
is_africa=False
is_asia=False
is_ustralia=False
is_amrica1=False
is_amrica2=False
is_erup=False
counter=0

total_points=0
image_rect_asia = continue_img.image.get_rect()
image_rect_asia.topleft = (x_asia+90, y_asia+50)
# تعريف مستطيل الصورة
image_rect_africa = continue_img.image.get_rect()
image_rect_africa.topleft = (x_africa+90, y_africa+50)
#============================
image_rect_ustralia = continue_img.image.get_rect()
image_rect_ustralia.topleft = (x_ustralia+50, y_ustralia+30)
#===========================
#============================
image_rect_amrica1 = continue_img.image.get_rect()
image_rect_amrica1.topleft = (x_amrica1+50, y_amrica1+50)
#===========================
#============================
image_rect_amrica2 = continue_img.image.get_rect()
image_rect_amrica2.topleft = (x_amrica2+90, y_amrica2+50)
#===========================
image_rect_erup = continue_img.image.get_rect()
image_rect_erup.topleft = (x_erup+70, y_erup+40)
#===========================
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)

x_str=300
y_str=100
x_opt=300
y_opt=200
x_qut=300
y_qut=300
    
image_Start = pygame.image.load("button.png")
image_Start = pygame.transform.scale(image_Start, (220, 100))
image_rect_start = image_Start.get_rect()
image_rect_start.topleft = (300, 100)

image_option = pygame.image.load("button.png")
image_option = pygame.transform.scale(image_option, (220, 100))
image_rect_option = image_option.get_rect()
image_rect_option.topleft = (300, 200)

image_quit = pygame.image.load("button.png")
image_quit = pygame.transform.scale(image_quit, (220, 100))
image_rect_quit = image_quit.get_rect()
image_rect_quit.topleft = (300, 300)

image_bg = pygame.image.load("btn_bg.png")
image_bg = pygame.transform.scale(image_bg, (500, 250))

def main_menu(y_s,y_o,y_q):
    
    global is_in_main_menu
    is_in_main_menu=True
    map_bg.blit(screen,0,0)
    #screen.blit(image_bg,(x_str-150,y_str-70))
    screen.blit(image_Start,(x_str,y_str+y_s))
    screen.blit(image_option,(x_opt,y_opt+y_o))
    screen.blit(image_quit,(x_qut,y_qut+y_q))
    # عرض النص
    text_start = font.render(f"START", True, (255, 255, 255))
    text_rect_s = text_start.get_rect(topleft=(375, 139+y_s))  # حوض النص في منتصف الشاشة
    screen.blit(text_start, text_rect_s)
    # عرض النص
    text_option = font.render(f"OPTION", True, (255, 255, 255))
    text_rect_o = text_option.get_rect(topleft=(365, 240+y_o))  # حوض النص في منتصف الشاشة
    screen.blit(text_option, text_rect_o)
    # عرض النص
    text_quit = font.render(f"QUIT", True, (255, 255, 255))
    text_rect_q = text_quit.get_rect(topleft=(380, 340+y_q))  # حوض النص في منتصف الشاشة
    screen.blit(text_quit, text_rect_q)
    #Time()

    if event.type == MOUSEBUTTONDOWN:
        if image_rect_option.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Option")
        if image_rect_start.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Stert")
                map()
        if image_rect_quit.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Quit")

font = pygame.font.Font(None, 36)  # تعيين الخط وحجم النص

is_select_level=False       
def select_level(y_e,y_m,y_h):
    
    global is_in_main_menu
    is_in_main_menu=True
    map_bg.blit(screen,0,0)
    #screen.blit(image_bg,(x_str-150,y_str-70))
    screen.blit(image_Start,(x_str,y_str+y_e))
    screen.blit(image_option,(x_opt,y_opt+y_m))
    screen.blit(image_quit,(x_qut,y_qut+y_h))
    # عرض النص
    text_start = font.render(f"Easy", True, (255, 255, 255))
    text_rect_s = text_start.get_rect(topleft=(375, 139+y_e))  # حوض النص في منتصف الشاشة
    screen.blit(text_start, text_rect_s)
    # عرض النص
    text_option = font.render(f"Medium", True, (255, 255, 255))
    text_rect_o = text_option.get_rect(topleft=(365, 240+y_m))  # حوض النص في منتصف الشاشة
    screen.blit(text_option, text_rect_o)
    # عرض النص
    text_quit = font.render(f"Hard", True, (255, 255, 255))
    text_rect_q = text_quit.get_rect(topleft=(380, 340+y_h))  # حوض النص في منتصف الشاشة
    screen.blit(text_quit, text_rect_q)
    #Time()

    if event.type == MOUSEBUTTONDOWN:
        if image_rect_option.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Midume")
        if image_rect_start.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Easy")
        if image_rect_quit.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Hard")

font = pygame.font.Font(None, 36)  # تعيين الخط وحجم النص
    




score=0

af_level = Image("af_level.png",screen_width,screen_height)
def map():
    
    is_in_main_menu=False
    global counter 
    global is_africa
    global is_asia
    global is_ustralia
    global is_amrica1
    global is_amrica2
    global is_erup
    global score
    global in_result
    # تحضير النص
    if event.type == MOUSEBUTTONDOWN:
            if image_rect_btn_back_to_map.collidepoint(event.pos) and in_result:
                    print("zczsadxc")
            # التحقق من النقر على المستطيل
            if image_rect_africa.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة

                is_africa=True
                
                #screen.fill((220, 220, 220))
                #screen.blit(af_level,100,100)
                #af_level.blit(screen,0,0)
                level_africa.similar_count=0
                level_africa.draw_background_level()
                print("Africa")
                #show_question()
            if image_rect_asia.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                is_asia=True
                print("Asia")
                level_asia.similar_count=0
                level_asia.draw_background_level()
                #draw_backGround_level(0)
                
            if image_rect_ustralia.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                is_ustralia=True
                level_australia.similar_count=0
                level_australia.draw_background_level()
                print("Ustralia")
            if image_rect_amrica1.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                is_amrica1=True
                level_north_america.similar_count=0
                level_north_america.draw_background_level()
                print("amrica")
            if image_rect_amrica2.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                is_amrica2=True
                level_south_america.similar_count=0
                level_south_america.draw_background_level()
                print("amrica")
            if image_rect_erup.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                is_erup=True
                level_europe.similar_count=0
                level_europe.draw_background_level()
                print("Erup")

    # عرض الصورة
    #africa.blit()
    if(is_africa==False and is_amrica1==False and is_amrica2==False and is_asia==False and is_erup==False and is_ustralia ==False):
        draw_map()
        in_result=False

        
def draw_map():
        global in_level
        in_level=False
        screen.fill((220, 220, 220))
        africa.blit(screen,x_africa,y_africa)
        asia_lock.blit(screen,x_asia,y_asia)
        ustralia_lock.blit(screen,x_ustralia,y_ustralia)
        amrica1_lock.blit(screen,x_amrica1,y_amrica1)
        amrica2_lock.blit(screen,x_amrica2,y_amrica2)
        erup_lock.blit(screen,x_erup,y_erup)
        #========================================================
        continue_img.blit(screen,x_africa+90, y_africa+50)
        if(level_africa.get_stars()>=1):
            asia.blit(screen,x_asia,y_asia)
            continue_img.blit(screen,x_asia+90, y_asia+50)
        if(level_asia.get_stars()>=1):
            erup.blit(screen,x_erup,y_erup)
            continue_img.blit(screen,x_erup+70, y_erup+40)
        if(level_europe.get_stars()>=1):
            ustralia.blit(screen,x_ustralia,y_ustralia)
            continue_img.blit(screen,x_ustralia+50, y_ustralia+30)
        if(level_australia.get_stars()>=1):
            amrica1.blit(screen,x_amrica1,y_amrica1)
            continue_img.blit(screen,x_amrica1+50, y_amrica1+50)
        if(level_north_america.get_stars()>=1):
            amrica2.blit(screen,x_amrica2,y_amrica2)
            continue_img.blit(screen,x_amrica2+90, y_amrica2+50)
        #continue_img.blit(screen,x_ustralia+50, y_ustralia+30)
        #continue_img.blit(screen,x_amrica1+50, y_amrica1+50)
        #continue_img.blit(screen,x_amrica2+90, y_amrica2+50)
        #continue_img.blit(screen,x_erup+70, y_erup+40)
        #=========================================================
        help_img.blit(screen,730, 15)
        text_help = font.render(f" {counter} X", True, (0, 0, 0))
        text_rect_help = text_help.get_rect(topleft=(690, 30))  # حوض النص في منتصف الشاشة
        screen.blit(text_help, text_rect_help)
    # عرض النص
        text = font.render(f"Level of progress: {counter}", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(10, 10))  # حوض النص في منتصف الشاشة
        screen.blit(text, text_rect)
        draw_star_in_level()





def reset_data():
    global is_africa
    global is_asia
    global is_ustralia
    global is_amrica1
    global is_amrica2
    global is_erup
    is_africa=False
    is_asia=False
    is_ustralia=False
    is_amrica1=False
    is_amrica2=False
    is_erup=False
in_level = False

# حلقة اللعبة الرئيسية
while True:
     # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if image_rect_btn_back_to_map.collidepoint(event.pos) and in_result:
                    print("go to map")
                    #similar_count=0
                    in_level=False
                    in_result=False
                    reset_data()
                    
                    
            if image_rect_start.collidepoint(event.pos) :
                #is_select_level=True
                #select_level(0,0,0)
                is_in_map=True
            if image_rect_quit.collidepoint(event.pos) and is_in_map==False :
                print("quit")
                pygame.quit()
                sys.exit()
            if in_level and not in_result:
                answer=0
                
                if image_rect_chioce1.collidepoint(event.pos):
            # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce1")
                    answer=1
                    #level_africa.answer(1)
                if image_rect_choice_2.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce2")
                    answer=2
                    #level_africa.answer(2)
                if image_rect_choice_3.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce3")
                    answer=3
                    #level_africa.answer(3)
                if image_rect_choice_4.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce4")
                    answer=4
                    #level_africa.answer(4)
                if is_africa:
                    level_africa.answer(answer)
                if is_asia:
                    level_asia.answer(answer)
                if is_erup:
                    level_europe.answer(answer)
                if is_ustralia:
                    level_australia.answer(answer)
                if is_amrica1:
                    level_north_america.answer(answer)
                if is_amrica2:
                    level_south_america.answer(answer)
                
        
        if in_level == False and in_result==False :
            if is_in_map :
                screen.fill((220, 220, 220))
                map()
            else:
                screen.fill((220, 220, 220))
                main_menu(0,0,0)
            if image_rect_start.collidepoint(pygame.mouse.get_pos()) and is_in_map==False:
                screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
                main_menu(-3,0,0)
                
            if image_rect_option.collidepoint(pygame.mouse.get_pos()) and is_in_map==False:
                screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
                main_menu(0,-3,0)
            if image_rect_quit.collidepoint(pygame.mouse.get_pos()) and is_in_map==False:
                screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
                main_menu(0,0,-3)
    

        if is_africa or is_amrica1 or is_amrica2 or is_asia or is_erup or is_ustralia == True :
            #screen.fill((220, 220, 220))
            in_level=True
    
    pygame.display.update()
    clock.tick(60)  # تحديث بمعدل 60 إطارًا في الثانية

    
# إغلاق اللعبة بشكل نظيف