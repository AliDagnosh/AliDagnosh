import pygame
from pygame.locals import *
import sys
import string
import subprocess
import time
import textwrap
import threading


# تهيئة اللعبة
pygame.init()
pygame.mixer.init()

# إعداد الشاشة
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("لعبة بايثون")

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

class level():
    global time_af
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
        
        self.game_over=False
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stage")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
    
    def set_data(self, questions, answers, correct_answer,stars):
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
        #delay(0.1)
        global time_af
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

        

        self.screen.blit(choice_1, image_rect_choice_1.topleft)
        self.screen.blit(choice_2, image_rect_choice_2.topleft)
        self.screen.blit(choice_3, image_rect_choice_3.topleft)
        self.screen.blit(choice_4, image_rect_choice_4.topleft)
        
        self.show_question()
        self.show_answers()

        


        pygame.display.flip()
        # تأخير لمدة 500 ميلي ثانية (نصف ثانية)
        pygame.time.delay(1)
        # إخفاء الصورة
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
                print("is new")
            similar_count=self.similar_count
            draw_result(False)
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
            count_q_txt = self.font.render("Question "+str(self.counter_questions)+"/9", True, BLACK)
            self.screen.blit(count_q_txt, (190, 50))
    
    
        
        
        
     
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



is_easy=False
# تصغير حجم الصورة
new_width = 200
new_height = 200
done=False
# load sound 
click_Sound = pygame.mixer.Sound("click_002.OGG")
cicksound = pygame.mixer.Sound("click_002.OGG")
loss_sound = pygame.mixer.Sound("lose.wav")

win_sound = pygame.mixer.Sound("win.wav")
timer_sound = pygame.mixer.Sound("timer.mp3")
music_sound = pygame.mixer.Sound("music.mp3")

image_back = pygame.image.load("back.png")
image_back = pygame.transform.scale(image_back, (30, 30))
image_rect_back = image_back.get_rect()
image_rect_back.topleft = (740, 20)

image_on_music = pygame.image.load("on_music.png")
image_on_music = pygame.transform.scale(image_on_music, (30, 30))
image_rect_on_music = image_on_music.get_rect()
image_rect_on_music.topleft = (700, 20)

image_up_volume = pygame.image.load("up_volume.png")
image_up_volume = pygame.transform.scale(image_up_volume, (30, 30))
image_rect_up_volume = image_up_volume.get_rect()
image_rect_up_volume.topleft = (660, 20)

image_down_volume = pygame.image.load("down_volume.png")
image_down_volume = pygame.transform.scale(image_down_volume, (30, 30))
image_rect_down_volume = image_down_volume.get_rect()
image_rect_down_volume.topleft = (620, 20)



time_af = 0
time_asia = 0
time_australia=0
time_north_amrica=0
time_south_amrica=0
time_europ=0
in_result=False
similar_count=0

BLACK = (0,0,0)

level_E_M_H =0

lock=Image("lock1.png",30,30)

star=Image("star.png",80,80)
x_star=Image("star1.png",80,80)
star_on_map=Image("star.png",20,20)
x_star_on_map=Image("star1.png",20,20)
btn_back_to_map = pygame.image.load("button.png")
btn_back_to_map = pygame.transform.scale(btn_back_to_map, (220, 100))


image_rect_btn_back_to_map = btn_back_to_map.get_rect()
image_rect_btn_back_to_map.topleft = (310, 400)
def draw_star_in_level():
    print("0000000")
    print(level_africa.get_stars())
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

def remove_decimal(number):
    return int(number)

def draw_result(time_is_over):
        #delay(0.2)
        global in_result
        reset_timer()
        timer_sound.stop()
        
        in_result=True
         
        map_bg.blit(screen,0,0)

        image_bg = pygame.image.load("btn_bg.png")
        screen.blit(image_bg, (120, 80)) 

        screen.blit(choice_1, image_rect_btn_back_to_map.topleft)
        text = font.render("Ok", True, BLACK)
        screen.blit(text, (400, 440))
        if time_is_over:
            result_text = "Time is Over"
            text = font.render(result_text, True, (255,0,0))
        else:
            result_text = "correct :"+str(similar_count)
            text = font.render(result_text, True, BLACK)
            if similar_count<7 and similar_count >=5:
                star.blit(screen,270,20)
                x_star.blit(screen,360,20)
                x_star.blit(screen,450,20)
                win_sound.play()
            if similar_count<9 and similar_count >=7:
                star.blit(screen,270,20)
                star.blit(screen,360,20)
                x_star.blit(screen,450,20)
                win_sound.play()
            if similar_count==9:
                star.blit(screen,270,20)
                star.blit(screen,360,20)
                star.blit(screen,450,20)
                win_sound.play()
            if similar_count<5:
                x_star.blit(screen,270,20)
                x_star.blit(screen,360,20)
                x_star.blit(screen,450,20)
                loss_sound.play()
        print(similar_count)
        #text = font.render(result_text, True, BLACK)
        screen.blit(text, (190, 130))
          
        
questions_africa = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]

answers_africa = [
    ["", "", "", ""],
    [" ", "", "", ""],
    ["", "", "", ""],
    [" ", "", "", ""],
    ["", "", " ", ""],
    ["  ", " ", " ", " "],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""]
]

correct_answers_africa = [1, 1, 3, 4, 2, 1, 1, 2, 1]

total_score = 0
level_africa =       level(questions_africa,answers_africa,correct_answers_africa,0)
level_asia =         level(questions_africa,answers_africa,correct_answers_africa,0)
level_europe =       level(questions_africa,answers_africa,correct_answers_africa,0)
level_south_america =level(questions_africa,answers_africa,correct_answers_africa,0)
level_australia =    level(questions_africa,answers_africa,correct_answers_africa,0)
level_north_america =level(questions_africa,answers_africa,correct_answers_africa,0)
def fill_data(level):
    global level_africa  
    global level_asia 
    global level_europe      
    global level_south_america 
    global level_australia    
    global level_north_america 
    # Easy Questions
    easy_africa_questions = [
        "What is the capital of Egypt?",
        "What is the capital of Morocco?",
        "What is the capital of South Africa?",
        "What is the capital of Nigeria?",
        "What is the capital of Kenya?",
        "What is the capital of Algeria?",
        "What is the capital of Tunisia?",
        "What is the capital of Zimbabwe?",
        "What is the capital of Ghana?",
        "What is the capital of Ethiopia?"
    ]

    easy_africa_answers = [
        ["Cairo", "Johannesburg", "Nairobi", "Lagos"],
        ["Rabat", "Nigeria", "Kenya", "Ghana"],
        ["Kenya", "Tanzania", "Pretoria", "Botswana"],
        ["South African Rand", "Egyptian Pound", "Nigerian Naira", "Abuja"],
        ["Johannesburg", "Nairobi", "Pretoria", "Lagos"],
        ["Algiers", "Kenya", "Uganda", "Ethiopia"],
        ["Tunis", "Lagos", "Morocco", "Sudan"],
        ["Uganda", "Harare", "Egypt", "Morocco"],
        ["Accra", "Lake Tanganyika", "Lake Malawi", "Lake Chad"],
        ["Egypt", "Sudan", "Algeria", "Morocco"]
    ]
    correct_answers_africa_easy = [1, 1, 3, 4, 2, 1, 1, 2, 1]
    # Medium Questions
    medium_africa_questions = [
        "What is the largest country in Africa in terms of land area?",
        "Which African country has the highest population?",
        "Which African country ranks second in terms of population?",
        "Which African country is the smallest in terms of land area?",
        "What is the total population of Egypt?",
        "What is the total population of South Africa?",
        "What is the total population of Nigeria?",
        "What is the total population of Ethiopia?",
        "What is the total population of Algeria?",
        "What is the total population of Kenya?"
    ]

    medium_africa_answers = [
        ["Nigeria", "South Africa", "Ethiopia", "Algeria"],
        ["Nigeria", "Swahili", "Tigrinya", "Arabic"],
        ["Kenya", "Ethiopia", "South Africa", "Botswana"],
        ["Kenyan Shilling", "Seychelles", "Ghanaian Cedi", "South African Rand"],
        ["104 million", "Nairobi", "Addis Ababa", "Cairo"],
        ["20  million", "60 million", "72 million", "90 million"],
        ["200 million", "Kalahari Desert", "214 million", "Nubian Desert"],
        ["110 million", "10 million", "118 million", "102 million"],
        ["10 million", "32 million", "40 million", "45 million"],
        ["South Africa", "Ethiopia", "Kenya", "Tanzania"]
    ]
    correct_answers_africa_medium = [4, 1, 2, 2, 1, 2, 3, 3, 4]
    # Hard Questions
    hard_africa_questions = [
        "Which African country was not colonized by European powers?",
        "What is the highest mountain peak in Africa?",
        "What is the largest lake in Africa by volume?",
        "Which ancient civilization is located in the region of Nubia between Egypt and Sudan?",
        "What is the longest river in Africa?",
        "What is the largest tropical rainforest in Africa?",
        "Which city has the highest population density in Africa?",
        "What is the major desert that spans across several countries in North Africa?",
        "What is the currency used in South Africa?",
        "Which country is famous for its white sandy beaches in Zanzibar?"
    ]

     
    hard_africa_answers = [
        ["Rwanda", "Ethiopia", "Burundi", "Kenya"],
        [" Mount Kenya ", " Mount Rwenzori", "Mount Kilimanjaro", " Mount Meru"],
        ["Lake Tanganyika","Lake Victoria ","Lake Malawi"," Lake Chad"],
        ["Ancient Egypt", "Axumite Empire", "Mali Empire", "The Kingdom of Kush"],
        [" Congo River"," The Nile River","Niger River"," Zambezi River"],
        ["The Congo Rainforest", " Okavango Delta", "Serengeti National Park", "Sahara Desert"],
        ["Cape Town","Lagos, Nigeria","Johannesburg","Nairobi"],
        ["Kalahari Desert", "Namib Desert", "Libyan Desert", "The Sahara Desert"],
        ["Nigerian Naira", "Kenyan Shilling", "Egyptian Pound"," South African Rand"],
        [" ", "", "", " "]

    ]
    correct_answers_africa_hard=[ 2,3, 3, 4, 2, 1, 2, 4, 4]
    
#================================================================================
    easy_asia_questions = [
        "What is the capital of China?",
        "Which city is the capital of India?",
        "What is the capital of Japan?",
        "Which city is the capital of South Korea?",
        "What is the capital of Indonesia?",
        "Which city is the capital of Saudi Arabia?",
        "What is the capital of Turkey?",
        "Which city is the capital of Iran?",
        "What is the capital of Thailand?",
        "Which city is the capital of Vietnam?"
    ]

    easy_asia_answers = [
        [ "Shanghai", "Hong Kong","Beijing", "Tokyo"],
        [ "Mumbai","New Delhi", "Kolkata", "Chennai"],
        [ "Kyoto","Tokyo", "Osaka", "Hiroshima"],
        ["Seoul", "Busan", "Incheon", "Daegu"],
        ["Jakarta", "Bali", "Surabaya", "Bandung"],
        [ "Jeddah", "Mecca", "Medina","Riyadh"],
        [ "Istanbul", "Izmir","Ankara", "Antalya"],
        [ "Shiraz", "Isfahan", "Mashhad","Tehran",],
        ["Bangkok", "Phuket", "Chiang Mai", "Pattaya"],
        [ "Ho Chi Minh City","Hanoi", "Da Nang", "Nha Trang"]
    ]
    correct_answers_asia_easy = [3, 2, 2, 1, 1, 4, 3, 4, 1, 2]
    # Medium Questions
    medium_asia_questions = [
        "What is the largest country in Asia by land area?",
        "Which country in Asia has the smallest land area?",
        "What is the most populous country in Asia?",
        "Which country in Asia has the lowest population?",
        "What is the land area of Russia?",
        "What is the population of China?",
        "Which country in Asia has the highest population density?",
        "What is the population of India?",
        "How many square kilometers is Kazakhstan?",
        "Which country in Asia has the highest population growth rate?"
         ]

    medium_asia_answers = [
        ["Russia", "China", "India", "Saudi Arabia"],
        ["Maldives", "Lebanon", "Bahrain", "Singapore"],
        ["China", "India", "Indonesia", "Pakistan"],
        [ "Bhutan", "Brunei", "Timor-Leste", "Maldives"],
        [ "9,596,961", "3,287,263", "1,960,582","17,098,242"],
        ["1,409,517,397", "1,369,098,528", "273,523,615", "220,892,340"],
        ["Singapore", "Bangladesh", "Lebanon", "Taiwan"],
        ["1,366,417,754", "1,366,417,754", "1,366,417,754", "1,366,417,754"],
        ["2,724,900", "2,724,900", "2,724,900", "2,724,900"],
        ["Bahrain", "Qatar", "Maldives", "Timor-Leste"]
    ]
    correct_answers_asia_medium = [1, 3, 1, 4, 4, 1, 2, 1, 2, 3]
    # Hard Questions
    hard_asia_questions = [
        "What is the capital city of Kyrgyzstan?",
        "Which mountain range stretches across northern Afghanistan, southern Tajikistan, and northwest Pakistan?",
        "What is the official language of Turkmenistan?",
        "What is the name of the island located in the Bay of Bengal known for its beautiful beaches and coral reefs?",
        "Which country in Asia has the highest peak in the world?",
        "What is the former name of Myanmar?",
        "Which city in India is known as the 'Pink City'?",
        "What is the largest mosque in the world located in Mecca, Saudi Arabia?",
        "Which country in Asia is the only one without a rectangular flag?",
        "What is the name of the famous ancient citadel located in Afghanistan?"
    ]

    hard_asia_answers = [
        [ "Almaty","Bishkek", "Tashkent", "Dushanbe"],
        [ "Pamir Mountains", "Tian Shan","Hindu Kush", "Karakoram Range"],
        [ "Uzbek", "Russian","Turkmen", "Kazakh"],
        ["Andaman Island", "Maldives", "Sri Lanka", "Lakshadweep"],
        [ "China", "India", "Pakistan","Nepal"],
        [ "Thailand","Burma", "Cambodia", "Laos"],
        [ "Agra","Jaipur", "Mumbai", "Kolkata"],
        ["Masjid al-Haram", "Al-Masjid an-Nabawi", "Sheikh Zayed Grand Mosque", "Sultan Ahmed Mosque"],
        ["Nepal", "Bhutan", "Maldives", "Cyprus"],
        ["Bagram", "Herat", "Kabul", "Kandahar"]
        ]
    correct_answers_asia_hard = [2, 3, 3, 1, 4, 2, 2, 1, 3, 3]
        # Easy Questions
   #=======================================================================================================
    easy_europe_questions = [
        "What is the capital city of France?",
        "Which city is the capital of Germany?",
        "What is the capital of Italy?",
        "Which city is the capital of Spain?",
        "What is the capital city of the United Kingdom?",
        "Which city is the capital of Russia?",
        "What is the capital of Greece?",
        "Which city is the capital of Sweden?",
        "What is the capital city of Poland?",
        "Which city is the capital of Switzerland?"
    ]

    easy_europe_answers = [
        [ "Madrid", "Rome","Paris", "London"],
        ["Berlin", "Vienna", "Amsterdam", "Athens"],
        ["Rome", "Warsaw", "Lisbon", "Stockholm"],
        [ "Dublin","Madrid", "Prague", "Bucharest"],
        [ "Oslo","London", "Copenhagen", "Helsinki"],
        ["Moscow", "Budapest", "Sofia", "Reykjavik"],
        [ "Ljubljana", "Tallinn", "Riga","Athens"],
        ["Stockholm", "Belgrade", "Zagreb", "Brussels"],
        [ "Bucharest", "Vilnius","Warsaw", "Valletta"],
        ["Bern", "Dublin", "Prague", "Vienna"]
    ]
    correct_answers_europe_easy = [3, 1, 1, 2, 2, 1, 4, 1, 3, 1]
    # Medium Questions
    medium_europe_questions = [
        "What is the land area of France in square kilometers?",
        "How many people live in Germany approximately?",
        "What is the land area of Italy in square kilometers?",
        "Approximately, how many people live in Spain?",
        "What is the land area of the United Kingdom in square kilometers?",
        "Approximately, how many people live in Russia?",
        "What is the land area of Greece in square kilometers?",
        "Approximately, how many people live in Sweden?",
        "What is the land area of Poland in square kilometers?",
        "Approximately, how many people live in Switzerland?"
    ]

    medium_europe_answers = [
        ["551,695", "357,022", "301,340", "643,801"],
        [ "61 million","83 million", "74 million", "45 million"],
        [ "357,022", "551,695","301,340", "301,336"],
        [ "62 million","47 million", "37 million", "46 million"],
        [ "130,279", "503,796", "245,857","243,610"],
        [ "142 million","145 million", "170 million", "110 million"],
        [ "110,994", "131,957","131,957", "246,201"],
        ["10 million", "5 million", "7 million", "9 million"],
        ["312,696", "321,346", "300,000", "512,696"],
        [ "5 million", "9 million", "11 million","8 million"]
    ]
    correct_answers_europe_meduim = [1, 2, 3, 2, 4, 2, 3, 1, 1, 4]
    # Hard Questions
    hard_europe_questions = [
        "Which country in Europe is known as the 'Land of Fire and Ice'?",
        "What is the highest mountain in Europe?",
        "Which river flows through the city of Prague?",
        "Which country in Europe has the most UNESCO World Heritage Sites?",
        "Which city is considered the fashion capital of Europe?",
        "What is the official currency of Switzerland?",
        "Which country has the largest population in Europe?",
        "What is the name of the famous palace located near Vienna, Austria?",
        "Which country is home to the famous Neuschwanstein Castle?",
        "Which city is known as the 'City of Bridges'?"
    ]

    hard_europe_answers = [
        ["Iceland", "Norway", "Sweden", "Finland"],
        [ "Mont Blanc","Mount Elbrus", "Mount Etna", "Mount Olympus"],
        ["Vltava", "Rhine", "Danube", "Seine"],
        ["Italy", "Germany", "France", "Spain"],
        ["Milan", "Paris", "London", "Rome"],
        ["Swiss franc", "Euro", "Pound sterling", "Krona"],
        ["Germany", "France", "United Kingdom", "Russia"],
        ["Schönbrunn Palace", "Versailles Palace", "Buckingham Palace", "Hermitage Museum"],
        ["Germany", "Austria", "Switzerland", "Czech Republic"],
        ["Venice", "Amsterdam", "Prague", "Paris"]
    ]
    correct_answers_europe_hard = [1, 2, 1, 1, 1, 1, 4, 1, 2, 3]
#=================================================================================
    easy_australia_questions = [
        "What is the capital city of Australia?",
        "Which city is the capital of New Zealand?",
        "What is the capital of Papua New Guinea?",
        "Which city is the capital of Fiji?",
        "What is the capital city of Indonesia?",
        "Which city is the capital of Vanuatu?",
        "What is the capital of Timor-Leste?",
        "Which city is the capital of Tonga?",
        "What is the capital city of Samoa?",
        "Which city is the capital of the Solomon Islands?"
    ]

    easy_australia_answers = [
        [ "Sydney", "Melbourne","Canberra", "Brisbane"],
        [ "Auckland","Wellington", "Christchurch", "Queenstown"],
        ["Port Moresby", "Lae", "Madang", "Kimbe"],
        ["Suva", "Nadi", "Lautoka", "Labasa"],
        [ "Bali", "Surabaya", "Bandung","Jakarta"],
        ["Port Vila", "Luganville", "Norsup", "Isangel"],
        [ "Baucau","Dili", "Aileu", "Suai"],
        ["Nuku'alofa", "Neiafu", "Haveluloto", "Pangai"],
        ["Apia", "Vaitele", "Faleula", "Siusega"],
        ["Honiara", "Gizo", "Auki", "Tulagi"]
        ]
    correct_answers_australia_easy = [3, 2, 1, 1, 4, 1, 2, 1, 1, 1]
    # Medium Questions
    medium_australia_questions = [
        "What is the land area of Australia in square kilometers?",
        "Approximately, how many people live in Australia?",
        "What is the land area of Papua New Guinea in square kilometers?",
        "Approximately, how many people live in Papua New Guinea?",
        "What is the land area of New Zealand in square kilometers?",
        "Approximately, how many people live in New Zealand?",
        "What is the land area of Fiji in square kilometers?",
        "Approximately, how many people live in Fiji?",
        "What is the land area of Vanuatu in square kilometers?",
        "Approximately, how many people live in Vanuatu?"
        ]

    medium_australia_answers = [
        ["7,692,024", "8,987,645", "6,543,910", "9,596,961"],
        ["25 million", "30 million", "20 million", "35 million"],
        [ "567,891","462,840", "320,825", "402,978"],
        [ "5 million","8 million", "7 million", "10 million"],
        ["268,021", "289,912", "303,342", "270,467"],
        [ "3 million", "4 million","5 million", "6 million"],
        [ "15,413", "20,182", "12,157","18,274"],
        ["900,000", "700,000", "1.2 million", "500,000"],
        ["12,189", "8,678", "10,457", "14,682"],
        ["300,000", "150,000", "250,000", "400,000"]
        ]
    correct_answers_australia_medium = [1, 1, 2, 2, 1, 3, 4, 1, 1, 1]
    # Hard Questions
    

    
    # Hard Questions
    hard_australia_questions = [
        "Which Australian state is the largest by area?",
        "What is the name of the world's largest coral reef system located in Australia?",
        "Which city in Australia is known as the 'Harbour City'?",
        "What is the name of the famous rock formation in the Northern Territory of Australia?",
        "Which Australian state is home to the Great Barrier Reef?",
        "What is the highest mountain in Australia?",
        "Which city is the capital of Australia's Northern Territory?",
        "What is the name of the famous beach in Sydney, Australia?",
        "Which Australian state is known for its wine regions such as the Barossa Valley and McLaren Vale?",
        "What is the name of the famous wildlife sanctuary located in Queensland, Australia?"
        ]

    hard_australia_answers = [
       [ "Queensland","Western Australia", "New South Wales", "Northern Territory"],
        [ "Ningaloo Reef","Great Barrier Reef", "Whitsunday Reef", "Coral Sea Reef"],
        ["Sydney", "Melbourne", "Brisbane", "Perth"],
        [ "Kakadu", "The Pinnacles", "Wave Rock","Uluru"],
        [ "New South Wales","Queensland", "Victoria", "Western Australia"],
        [ "Mount Everest", "Mount Cook","Mount Kosciuszko", "Mount Kilimanjaro"],
        [ "Perth", "Brisbane","Darwin", "Adelaide"],
        [ "Manly Beach","Bondi Beach", "Cottesloe Beach", "Surfers Paradise Beach"],
        ["South Australia", "Victoria", "Western Australia", "New South Wales"],
        ["Australia Zoo", "Kangaroo Island Wildlife Park", "Lone Pine Koala Sanctuary", "Taronga Zoo"]
    ]
    correct_answers_australia_hard = [2, 2, 1, 4, 2, 3, 3, 2, 1, 1]
#==================================================================================
        # Easy Questions
    easy_south_america_questions = [
        "What is the capital city of Brazil?",
        "Which city is the capital of Argentina?",
        "What is the capital of Colombia?",
        "Which city is the capital of Peru?",
        "What is the capital city of Chile?",
        "Which city is the capital of Ecuador?",
        "What is the capital of Bolivia?",
        "Which city is the capital of Venezuela?",
        "What is the capital city of Paraguay?",
        "Which city is the capital of Uruguay?"
    ]

    easy_south_america_answers = [
        ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
        ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
        [ "Medellín","Bogotá", "Cali", "Barranquilla"],
        ["Lima", "Arequipa", "Cusco", "Trujillo"],
        [ "Valparaíso", "Concepción", "La Serena","Santiago"],
        [ "Guayaquil", "Cuenca","Quito", "Manta"],
        ["La Paz", "Santa Cruz", "Sucre", "Cochabamba"],
        [ "Maracaibo","Caracas", "Valencia", "Barquisimeto"],
        ["Asunción", "Ciudad del Este", "Encarnación", "Luque"],
        ["Montevideo", "Salto", "Punta del Este", "Ciudad de la Costa"]
    ]
    correct_answers_south_america_easy = [1, 1, 2, 1, 4, 3, 1, 2, 1, 1]

    # Medium Questions
    medium_south_america_questions = [
        "What is the land area of Brazil in square kilometers?",
        "Approximately, how many people live in Brazil?",
        "What is the land area of Argentina in square kilometers?",
        "Approximately, how many people live in Argentina?",
        "What is the land area of Colombia in square kilometers?",
        "Approximately, how many people live in Colombia?",
        "What is the land area of Peru in square kilometers?",
        "Approximately, how many people live in Peru?",
        "What is the land area of Venezuela in square kilometers?",
        "Approximately, how many people live in Venezuela?"
    ]

    medium_south_america_answers = [
        [ "9,631,418","8,515,767", "7,032,216", "10,158,789"],
        [ "180 million","210 million", "240 million", "260 million"],
        ["2,780,400", "3,061,274", "2,736,690", "3,289,080"],
        [ "40 million", "50 million","45 million", "55 million"],
        ["1,138,910", "1,276,539", "1,011,678", "1,362,023"],
        ["50 million", "45 million", "55 million", "60 million"],
        ["1,285,216", "1,107,415", "1,496,093", "1,376,289"],
        [ "35 million", "25 million", "40 million","30 million"],
        ["916,445", "1,005,234", "842,356", "1,124,678"],
        ["28 million", "32 million", "25 million", "35 million"]
    ]
    correct_answers_south_america_medium = [2, 2, 1, 3, 1, 1, 1, 4, 1, 1]
    # Hard Questions
    hard_south_america_questions = [
        "Which country in South America has the highest population?",
        "What is the official language of Suriname?",
        "Which country in South America has the highest elevation?",
        "What is the name of the world's highest waterfall located in Venezuela?",
        "Which country in South America is the smallest by land area?",
        "What is the name of the indigenous ruins located in Peru?",
        "Which country in South America has the largest economy?",
        "What is the name of the famous soccer player from Argentina?",
        "Which country in South America is the largest by land area?",
        "What is the name of the vibrant neighborhood in Rio de Janeiro, Brazil?"
    ]

    hard_south_america_answers = [
        ["Brazil", "Colombia", "Argentina", "Peru"],
        [ "English", "Spanish","Dutch", "Portuguese"],
        [ "Argentina", "Ecuador","Bolivia", "Chile"],
        ["Angel Falls", "Iguazu Falls", "Kaieteur Falls", "Salto Ángel"],
        [ "Uruguay","Suriname", "Guyana", "French Guiana"],
        ["Machu Picchu", "Teotihuacan", "Chichen Itza", "Nazca Lines"],
        [ "Argentina","Brazil", "Colombia", "Chile"],
        [ "Neymar", "Cristiano Ronaldo", "Pele","Lionel Messi"],
        ["Brazil", "Argentina", "Peru", "Colombia"],
        ["Copacabana", "Ipanema", "Santa Teresa", "Leblon"]
    ]
    correct_answers_south_america_hard = [1, 3, 3, 1, 2, 1, 2, 4, 1, 1]
#======================================================================================
        # Easy Questions
    easy_north_america_questions = [
        "What is the capital city of Canada?",
        "Which city is the capital of the United States?",
        "What is the capital of Mexico?",
        "Which city is the capital of Cuba?",
        "What is the capital city of Jamaica?",
        "Which city is the capital of Haiti?",
        "What is the capital of Costa Rica?",
        "Which city is the capital of Panama?",
        "What is the capital city of Guatemala?",
        "Which city is the capital of El Salvador?"
    ]

    easy_north_america_answers = [
        ["Ottawa", "Toronto", "Vancouver", "Montreal"],
        ["Washington, D.C.", "New York City", "Los Angeles", "Chicago"],
        [ "Cancun","Mexico City", "Tijuana", "Guadalajara"],
        ["Havana", "Santiago de Cuba", "Varadero", "Camagüey"],
        [ "Montego Bay", "Ocho Rios","Kingston", "Negril"],
        ["Port-au-Prince", "Cap-Haïtien", "Jacmel", "Gonaïves"],
        [ "Liberia", "Cartago", "Alajuela","San José"],
        ["Panama City", "Colon", "David", "La Chorrera"],
        ["Guatemala City", "Antigua Guatemala", "Quetzaltenango", "Chichicastenango"],
        ["San Salvador", "Santa Ana", "Soyapango", "Apopa"]
    ]
    correct_answers_north_america_easy = [1, 1, 2, 1, 3, 1, 4, 1, 1, 1]

    # Medium Questions
    medium_north_america_questions = [
        "What is the land area of Canada in square kilometers?",
        "Approximately, how many people live in Canada?",
        "What is the land area of the United States in square kilometers?",
        "Approximately, how many people live in the United States?",
        "What is the land area of Mexico in square kilometers?",
        "Approximately, how many people live in Mexico?",
        "What is the land area of Cuba in square kilometers?",
        "Approximately, how many people live in Cuba?",
        "What is the land area of Haiti in square kilometers?",
        "Approximately, how many people live in Haiti?"
        ]
    medium_north_america_answers = [
        ["9,984,670", "8,654,120", "10,345,890", "7,891,340"],
        [ "30 million","37 million", "40 million", "45 million"],
        ["8,987,650",  "9,826,630", "10,234,560", "9,631,418"],
        ["330 million", "300 million", "350 million", "380 million"],
        [ "1,758,546", "2,038,500","1,964,375", "1,845,543"],
        ["126 million", "110 million", "140 million", "120 million"],
        [ "97,032", "120,567", "105,234","109,884"],
        ["11 million", "9 million", "13 million", "15 million"],
        ["27,750", "23,509", "31,865", "29,830"],
        ["11 million", "9 million", "13 million", "15 million"]
    ]
    correct_answers_north_america_medium = [1, 2, 2, 1, 3, 1, 4, 1, 1, 1]
    # Hard Questions
    hard_north_america_questions = [
        "Which country in North America has the largest land area?",
        "What is the official language of Canada?",
        "Which country in North America has the highest population density?",
        "What is the name of the famous national park located in the United States that features the Old Faithful geyser?",
        "Which country in North America has the longest coastline?",
        "What is the name of the ancient Mayan city in Mexico?",
        "Which country in North America has the largest indigenous population?",
        "What is the name of the famous music festival held annually in California, United States?",
        "Which country in North America is known for its production of maple syrup?",
        "What is the name of the iconic suspension bridge in San Francisco, United States?"
        ]

    hard_north_america_answers = [
        ["Canada", "United States", "Mexico", "Greenland"],
        [ "French","English", "Spanish", "Dutch"],
        [ "El Salvador", "Jamaica","Haiti", "Mexico"],
        ["Yellowstone National Park", "Yosemite National Park", "Grand Canyon National Park", "Glacier National Park"],
        ["Canada", "United States", "Mexico", "Greenland"],
        [ "Tulum","Chichen Itza", "Teotihuacan", "Palenque"],
        [ "Honduras","Mexico", "Guatemala", "Canada"],
        ["Coachella", "Bonnaroo", "Lollapalooza", "Glastonbury"],
        ["Canada", "United States", "Mexico", "Cuba"],
        ["Golden Gate Bridge", "Brooklyn Bridge", "George Washington Bridge", "Verrazzano-Narrows Bridge"]
    ]
    correct_answers_north_america_hard = [1, 2, 3, 1, 1, 2, 2, 1, 1, 1]

    if level=="easy":
        level_africa.        set_data(easy_africa_questions, easy_africa_answers,               correct_answers_africa_easy,        0)  
        level_asia.          set_data(easy_asia_questions,          easy_asia_answers,          correct_answers_asia_easy,          0)
        level_europe.        set_data(easy_europe_questions,        easy_europe_answers,        correct_answers_europe_easy,        0) 
        level_south_america. set_data(easy_south_america_questions, easy_south_america_answers, correct_answers_south_america_easy,0)  
        level_australia.     set_data(easy_australia_questions,     easy_australia_answers,     correct_answers_australia_easy,     0)  
        level_north_america. set_data(easy_north_america_questions, easy_north_america_answers, correct_answers_north_america_easy,0)  

    elif level=="medium":
        level_africa.        set_data(medium_africa_questions,        medium_africa_answers,        correct_answers_africa_medium,       0)  
        level_asia.          set_data(medium_asia_questions,          medium_asia_answers,          correct_answers_asia_medium,         0)
        level_europe.        set_data(medium_europe_questions,        medium_europe_answers,        correct_answers_europe_meduim,       0) 
        level_south_america. set_data(medium_south_america_questions, medium_south_america_answers, correct_answers_south_america_medium,0)  
        level_australia.     set_data(medium_australia_questions,     medium_australia_answers,     correct_answers_australia_medium,    0)  
        level_north_america. set_data(medium_north_america_questions, medium_north_america_answers, correct_answers_north_america_medium,0) 
    elif level=="hard":
        level_africa.        set_data(hard_africa_questions,        hard_africa_answers,        correct_answers_africa_hard,0)  
        level_asia.          set_data(hard_asia_questions,          hard_asia_answers,          correct_answers_asia_hard,0)
        level_europe.        set_data(hard_europe_questions,        hard_europe_answers,        correct_answers_europe_hard,0) 
        level_south_america. set_data(hard_south_america_questions, hard_south_america_answers, correct_answers_south_america_hard,0)  
        level_australia.     set_data(hard_australia_questions,     hard_australia_answers,     correct_answers_australia_hard,0)  
        level_north_america. set_data(hard_north_america_questions, hard_north_america_answers, correct_answers_north_america_hard,0) 
    












 
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

choice_5 = pygame.image.load("button.png")
choice_5 = pygame.transform.scale(choice_4, (220, 100))
image_rect_choice_5 = choice_5.get_rect()
image_rect_choice_5.topleft = (100, 200)

def init_continents():
    global is_africa
    global is_ustralia
    global is_erup
    global is_asia
    global is_amrica2
    global is_amrica1
    is_africa=False
    is_ustralia=False
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
game_level=""
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
                click_Sound.play()
                print("Africa")
                is_africa=True
                
                #screen.fill((220, 220, 220))
                #screen.blit(af_level,100,100)
                #af_level.blit(screen,0,0)
                level_africa.similar_count=0
                level_africa.draw_background_level()
                if not is_easy:
                    timer_sound.play()
                #show_question()
            if image_rect_asia.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                click_Sound.play()
                is_asia=True
                print("Asia")
                level_asia.similar_count=0
                level_asia.draw_background_level()
                #draw_backGround_level(0)
                if not is_easy:
                    timer_sound.play()
                
            if image_rect_ustralia.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة\
                click_Sound.play()
                is_ustralia=True
                level_australia.similar_count=0
                level_australia.draw_background_level()
                print("Ustralia")
                if not is_easy:
                    timer_sound.play()
                
            if image_rect_amrica1.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                click_Sound.play()
                is_amrica1=True
                level_north_america.similar_count=0
                level_north_america.draw_background_level()
                print("amrica")
                if not is_easy:
                    timer_sound.play()
                
            if image_rect_amrica2.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                click_Sound.play()
                is_amrica2=True
                level_south_america.similar_count=0
                level_south_america.draw_background_level()
                print("amrica")
                if not is_easy:
                    timer_sound.play()
                
            if image_rect_erup.collidepoint(event.pos) and is_in_main_menu==False:
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                click_Sound.play()
                is_erup=True
                level_europe.similar_count=0
                level_europe.draw_background_level()
                print("Erup")
                if not is_easy:
                    timer_sound.play()
            
                
    
    # عرض الصورة
    #africa.blit()
    if(is_africa==False and is_amrica1==False and is_amrica2==False and is_asia==False and is_erup==False and is_ustralia ==False):
        draw_map()
        print("DSFF")
        in_result=False
        
        

        
def draw_map():
        global in_level
        global done
        in_level=False
        screen.fill((220, 220, 220))
        screen.blit(image_back,(740,20))
        screen.blit(image_on_music,(700,20))
        screen.blit(image_up_volume,(660,20))
        screen.blit(image_down_volume,(620,20))
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
        if(level_south_america.get_stars()>=1):
            done=True
        #continue_img.blit(screen,x_ustralia+50, y_ustralia+30)
        #continue_img.blit(screen,x_amrica1+50, y_amrica1+50)
        #continue_img.blit(screen,x_amrica2+90, y_amrica2+50)
        #continue_img.blit(screen,x_erup+70, y_erup+40)
        #=========================================================
        global game_level
    # عرض النص
        text = font.render(f"Game Level : {game_level}", True, BLACK)
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


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (190, 190, 190)
# الخطوط
font = pygame.font.Font(None, 32)
# أزرار القائمة الرئيسية
start_button_rect = pygame.Rect(100, 200, 200, 50)
dictionary_button_rect = pygame.Rect(100, 300, 200, 50)
quit_button_rect = pygame.Rect(100, 400, 200, 50)
# أزرار قائمة الخيارات
level1_button_rect = pygame.Rect(400, 200, 200, 50)
level2_button_rect = pygame.Rect(400, 300, 200, 50)
level3_button_rect = pygame.Rect(400, 400, 200, 50)

back_button_rect = pygame.Rect(400, 500, 200, 50)  # تعريف مستطيل زر الرجوع



is_in_main_menu = True
is_in_options_menu = False
clock = pygame.time.Clock()
is_running = True

def effect_mouse():
    # تحميل الصورة
    global image_effect
    image_effect=pygame.transform.scale(image_effect, (30, 30))
    # حجم الصورة
    #image_width, image_height = image_effect.get_size()

    # تحديد موقع الصورة بموضع المؤشر
    image_rect = image_effect.get_rect()
    image_rect.center = pygame.mouse.get_pos()
    # عرض الصورة
    screen.blit(image_effect, image_rect)
    pygame.display.flip()
    # تأخير لمدة 500 ميلي ثانية (نصف ثانية)
    pygame.time.delay(10)
    # إخفاء الصورة
    pygame.display.flip()
    pygame.display.update()
Timer=0
def Time_():
    x=67
    global Timer
    global time_af
    global time_asia
    global time_australia
    global time_north_amrica
    global time_south_amrica
    global time_europ
     
    if is_africa:
        time_af+=1
        txt_Time(time_af,x)
        
        
    if is_asia:
        time_asia+=1
        txt_Time(time_asia,x)
    if is_ustralia:
        time_australia+=1
        txt_Time(time_australia,x)
    if is_amrica1:
        time_north_amrica+=1
        txt_Time(time_north_amrica,x)
    if is_amrica2:
        time_south_amrica+=1
        txt_Time(time_south_amrica,x)
    if is_erup:
        time_europ+=1
        txt_Time(time_europ,x)

def txt_Time(Time,x):
    if Time % x ==0:
        global name_sound
        #cicksound.play()

        
            
    
    txt_ = font.render(f" {Time/x} ", True, (0, 0, 0))
    text_rec = txt_.get_rect(topleft=(690, 60))  # حوض النص في منتصف الشاشة
    screen.blit(txt_, text_rec)
    if Time/x == 22:
        

# الانتظار لستة ثوانٍ
       
        print("game over")
        draw_result(True)
        loss_sound.play()
        init_continents()
        reset_timer()
        level_africa.list_answer=[]
        level_africa.counter_answers=0
        level_africa.counter_questions=0

        level_asia.list_answer=[]
        level_asia.counter_answers=0
        level_asia.counter_questions=0

        level_australia.list_answer=[]
        level_australia.counter_answers=0
        level_australia.counter_questions=0

        level_europe.list_answer=[]
        level_europe.counter_answers=0
        level_europe.counter_questions=0

        level_north_america.list_answer=[]
        level_north_america.counter_answers=0
        level_north_america.counter_questions=0

        level_south_america.list_answer=[]
        level_south_america.counter_answers=0
        level_south_america.counter_questions=0
        #level_africa.set_counters()


        

def reset_timer():
    global time_af
    global time_asia
    global time_australia
    global time_north_amrica
    global time_south_amrica
    global time_europ
    time_af=0
    time_asia=0
    time_australia=0
    time_north_amrica=0
    time_south_amrica=0
    time_europ=0


volume_music=0.1
click_Sound.set_volume(volume_music*2)
music_sound.set_volume(volume_music)
music_sound.play(-1)

turn_sound=False
turn_on_music=True
while is_running:
    
    if(not is_easy):
        Time_()
    
    music_sound.set_volume(volume_music)
    
    time_delta = clock.tick(60) / 1000.0
    
    #if is_in_main_menu or is_in_options_menu:
    #    effect_mouse()
    #else:
        #pygame.mouse.set_visible(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if image_rect_back.collidepoint(event.pos) and is_in_main_menu==False:
                print("back")
                delay(0.1)
                is_in_options_menu=True
                is_in_map=False
                is_easy=False
                music_sound.play()
            if image_rect_on_music.collidepoint(event.pos) and is_in_main_menu==False:
                
                if turn_on_music:
                    image_on_music = pygame.image.load("off_music.png")
                    image_on_music = pygame.transform.scale(image_on_music, (30, 30))
                    volume_music=0.0
                    #music_sound.set_volume(volume_music)
                    turn_on_music=False
                else:
                    image_on_music = pygame.image.load("on_music.png")
                    image_on_music = pygame.transform.scale(image_on_music, (30, 30))
                    volume_music=0.1
                    #music_sound.set_volume(volume_music)
                    turn_on_music=True
                print("music")
            if image_rect_up_volume.collidepoint(event.pos) and is_in_main_menu==False:
                image_on_music = pygame.image.load("on_music.png")
                image_on_music = pygame.transform.scale(image_on_music, (30, 30))
                volume_music+=0.1
                turn_on_music=True
            if image_rect_down_volume.collidepoint(event.pos) and is_in_main_menu==False:
                
                volume_music-=0.1

            if image_rect_btn_back_to_map.collidepoint(event.pos) and in_result:
                    delay(0.1)
                    print("go to map")
                    #similar_count=0
                    in_level=False
                    in_result=False
                    reset_data()
            if is_in_main_menu:
                map_bg.blit(screen,0,0)
                if start_button_rect.collidepoint(event.pos):
                    delay(0.1)
                    is_in_main_menu = False
                    is_in_options_menu = True
                    is_easy=False
                    click_Sound.play()
                elif dictionary_button_rect.collidepoint(event.pos):
                    # تنفيذ إجراء عند النقر على زر الخيارات
                    #subprocess.Popen(["python", "test.py"])
                    if(not done):
                        subprocess.Popen(["python", "textbox.py"])
                    else:
                        subprocess.Popen(["python", "test.py"])
                    print("تم النقر على زر الخيارات")
                    click_Sound.play()
                elif quit_button_rect.collidepoint(event.pos):
                    # تنفيذ إجراء عند النقر على زر الخروج
                    is_running = False
            elif is_in_options_menu:
                
                if level1_button_rect.collidepoint(event.pos):
                    delay(0.1)
                    # تنفيذ إجراء عند النقر على زر المستوى 1
                    click_Sound.play()
                    fill_data("easy")
                    map()
                    is_in_options_menu=False
                    is_in_map=True
                    is_easy=True
                    game_level="Easy"
                    print("تم النقر على زر المستوى 1")
                elif level2_button_rect.collidepoint(event.pos):
                    delay(0.1)
                    # تنفيذ إجراء عند النقر على زر المستوى 2
                    click_Sound.play()
                    music_sound.stop()
                    fill_data("medium")
                    map()
                    is_in_options_menu=False
                    is_in_map=True
                    game_level="Medium"
                    print("تم النقر على زر المستوى 2")
                elif level3_button_rect.collidepoint(event.pos):
                    delay(0.1)
                    click_Sound.play()
                    # تنفيذ إجراء عند النقر على زر المستوى 3
                    music_sound.stop()
                    fill_data("hard")
                    map()
                    is_in_options_menu=False
                    is_in_map=True
                    game_level="Hard"
                    print("تم النقر على زر المستوى 3")
                elif back_button_rect.collidepoint(event.pos):
                    delay(0.1)
                    click_Sound.play()
                    is_in_main_menu = True
                    is_in_options_menu = False
            if in_level == False and in_result==False :
                if is_in_map :
                    screen.fill((220, 220, 220))
                    map()
            if in_level and not in_result:
                #Time_()
                #cicksound.play()
                answer=0
                is_click=False
                if image_rect_chioce1.collidepoint(event.pos):
            # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce1")
                    is_click=True
                    answer=1
                    click_Sound.play()
                    #level_africa.answer(1)
                if image_rect_choice_2.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce3")
                    click_Sound.play()
                    is_click=True
                    answer=3
                    #level_africa.answer(2)
                if image_rect_choice_3.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce2")
                    click_Sound.play()
                    is_click=True
                    answer=2
                    #level_africa.answer(3)
                if image_rect_choice_4.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                    print("chioce4")
                    click_Sound.play()
                    is_click=True
                    answer=4
                
                if is_click:
                    if is_africa :
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
                pygame.display.update()


            if is_africa or is_amrica1 or is_amrica2 or is_asia or is_erup or is_ustralia == True :
                #screen.fill((220, 220, 220))
                in_level=True

    

    if is_in_main_menu:
       
        map_bg.blit(screen,0,0)
        # رسم أزرة القائمة الرئيسية
        pygame.draw.rect(screen, GRAY, start_button_rect, border_radius=25)
        pygame.draw.rect(screen, GRAY, dictionary_button_rect, border_radius=25)
        pygame.draw.rect(screen, GRAY, quit_button_rect, border_radius=25)

        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, GRAY, start_button_rect.inflate(10, 10), border_radius=25)
        if dictionary_button_rect.collidepoint(pygame.mouse.get_pos()):
            if not done:
                text_="You need to complete one of the levels to unlock the dictionary or\n enter the password"
                comment = font.render(text_, True, WHITE)
                screen.blit(comment, (20, 20))
            pygame.draw.rect(screen, GRAY, dictionary_button_rect.inflate(10, 10), border_radius=25)
        if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, GRAY, quit_button_rect.inflate(10, 10), border_radius=25)

        text = font.render("Start", True, BLACK)
        screen.blit(text, (start_button_rect.x + 50, start_button_rect.y + 10))

        text = font.render("Dictionary", True, BLACK)
        screen.blit(text, (dictionary_button_rect.x + 40, dictionary_button_rect.y + 10))

        text = font.render("Quit", True, BLACK)
        screen.blit(text, (quit_button_rect.x + 50, quit_button_rect.y + 10))
        if not done:
            lock.blit(screen,105,310)

    elif is_in_options_menu:
        #effect_mouse()
        map_bg.blit(screen,0,0)
        # رسم أزرة قائمة الخيارات
        pygame.draw.rect(screen, GRAY, level1_button_rect, border_radius=45)
        pygame.draw.rect(screen, GRAY, level2_button_rect, border_radius=25)
        pygame.draw.rect(screen, GRAY, level3_button_rect, border_radius=25)
        pygame.draw.rect(screen, GRAY, back_button_rect, border_radius=25)

        if level1_button_rect.collidepoint(pygame.mouse.get_pos()):
            text_="In this level, simple questions about country capitals will be asked.\n Note: There is no time limit in this level"
            comment = font.render(text_, True, WHITE)
            screen.blit(comment, (20, 20))
            pygame.draw.rect(screen, GRAY, level1_button_rect.inflate(10, 10), border_radius=25)
        if level2_button_rect.collidepoint(pygame.mouse.get_pos()):
            text_="In this level, questions about population and area of countries will\n be asked.\n Note: In this round, you have 24 seconds to complete the 9 questions,\n otherwise you will lose."
            comment = font.render(text_, True, WHITE)
            screen.blit(comment, (20, 20))
            pygame.draw.rect(screen, GRAY, level2_button_rect.inflate(10, 10), border_radius=25)
        if level3_button_rect.collidepoint(pygame.mouse.get_pos()):
            text_="In this level, general questions about the continent will be asked.\nNote: In this round, you have 24 seconds to complete the 9 questions,\n otherwise you will lose."
            comment = font.render(text_, True, WHITE)
            screen.blit(comment, (20, 20))
            pygame.draw.rect(screen, GRAY, level3_button_rect.inflate(10, 10), border_radius=25)
        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, GRAY, back_button_rect.inflate(10, 10), border_radius=25)

        text = font.render("Level 1", True, BLACK)
        screen.blit(text, (level1_button_rect.x + 40, level1_button_rect.y + 10))

        text = font.render("Level 2", True, BLACK)
        screen.blit(text, (level2_button_rect.x + 40, level2_button_rect.y + 10))

        text = font.render("Level 3", True, BLACK)
        screen.blit(text, (level3_button_rect.x + 40, level3_button_rect.y + 10))

        text = font.render("Back", True, BLACK)
        screen.blit(text, (back_button_rect.x + 50, back_button_rect.y + 10))
    
    pygame.display.update()

pygame.quit()