import pygame
from pygame.locals import *
import sys
import subprocess

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


# تحميل الصورة
image_africa = pygame.image.load("africa.png")
image_africa = pygame.transform.scale(image_africa, (new_width, new_height))
image_lock_africa = pygame.image.load("continuous.png")
image_lock_africa = pygame.transform.scale(image_lock_africa, (new_width-170, new_height-170))
#===================================================================================


image_asia = pygame.image.load("asia.png")
image_asia = pygame.transform.scale(image_asia, (new_width+80, new_height))
image_lock_asia = pygame.image.load("continuous.png")
image_lock_asia = pygame.transform.scale(image_lock_asia, (new_width-170, new_height-170))
#===================================================================================

image_ustralia = pygame.image.load("ustralia.png")
image_ustralia = pygame.transform.scale(image_ustralia, (new_width-100, new_height-110))
image_lock_ustralia = pygame.image.load("continuous.png")
image_lock_ustralia = pygame.transform.scale(image_lock_ustralia, (new_width-170, new_height-170))
#===================================================================================

image_amrica1 = pygame.image.load("amrica1.png")
image_amrica1 = pygame.transform.scale(image_amrica1, (new_width-50, new_height))
image_lock_amrica1 = pygame.image.load("continuous.png")
image_lock_amrica1 = pygame.transform.scale(image_lock_amrica1, (new_width-170, new_height-170))
#===================================================================================

image_amrica2 = pygame.image.load("amrica2.png")
image_amrica2 = pygame.transform.scale(image_amrica2, (new_width+50, new_height))
image_lock_amrica2 = pygame.image.load("continuous.png")
image_lock_amrica2 = pygame.transform.scale(image_lock_amrica2, (new_width-170, new_height-170))
#===================================================================================

image_erup = pygame.image.load("erup.png")
image_erup = pygame.transform.scale(image_erup, (new_width-40, new_height-115))
image_lock_erup = pygame.image.load("continuous.png")
image_lock_erup = pygame.transform.scale(image_lock_erup, (new_width-170, new_height-170))
#===================================================================================
image_help = pygame.image.load("help.png")
image_help = pygame.transform.scale(image_help, (50, 50))

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

total_points=0
# تعريف مستطيل الصورة
image_rect_africa = image_lock_africa.get_rect()
image_rect_africa.topleft = (x_africa+90, y_africa+50)
#============================
image_rect_asia = image_lock_asia.get_rect()
image_rect_asia.topleft = (x_asia+90, y_asia+50)
#===========================
#============================
image_rect_ustralia = image_lock_ustralia.get_rect()
image_rect_ustralia.topleft = (x_ustralia+50, y_ustralia+30)
#===========================
#============================
image_rect_amrica1 = image_lock_amrica1.get_rect()
image_rect_amrica1.topleft = (x_amrica1+50, y_amrica1+50)
#===========================
#============================
image_rect_amrica2 = image_lock_amrica2.get_rect()
image_rect_amrica2.topleft = (x_amrica2+90, y_amrica2+50)
#===========================
image_rect_erup = image_lock_erup.get_rect()
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
image_bg = pygame.transform.scale(image_bg, (550, 450))

def main_menu(y_s,y_o,y_q):
    screen.blit(image_bg,(x_str-150,y_str-70))
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


    if event.type == MOUSEBUTTONDOWN:
        if image_rect_option.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Option")
        if image_rect_start.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Stert")
        if image_rect_quit.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Quit")

font = pygame.font.Font(None, 36)  # تعيين الخط وحجم النص
def map():
    counter =0

    # تحضير النص
    
    
            
    if event.type == MOUSEBUTTONDOWN:
            # التحقق من النقر على المستطيل
            if image_rect_africa.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Africa")
                
            if image_rect_asia.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Asia")
                counter += 1
            if image_rect_ustralia.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Ustralia")
            if image_rect_amrica1.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("amrica")
            if image_rect_amrica2.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("amrica")
            if image_rect_erup.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("Erup")
 
    # عرض الصورة
    screen.blit(image_africa, (x_africa, y_africa))  # حيث (x, y) هي إحداثيات الصورة على الشاشة
    screen.blit(image_asia, (x_asia, y_asia))
    screen.blit(image_ustralia, (x_ustralia, y_ustralia))
    screen.blit(image_amrica1, (x_amrica1, y_amrica1))
    screen.blit(image_amrica2, (x_amrica2, y_amrica2))
    screen.blit(image_erup, (x_erup, y_erup))
    #========================================================
    screen.blit(image_lock_africa, (x_africa+90, y_africa+50))
    screen.blit(image_lock_asia, (x_asia+90, y_asia+50))
    screen.blit(image_lock_ustralia, (x_ustralia+50, y_ustralia+30))
    screen.blit(image_lock_amrica1, (x_amrica1+50, y_amrica1+50))
    screen.blit(image_lock_amrica2, (x_amrica2+90, y_amrica2+50))
    screen.blit(image_lock_erup, (x_erup+70, y_erup+40))
    #=========================================================
    screen.blit(image_help, (730, 15))
    text_help = font.render(f" {counter} X", True, (0, 0, 0))
    text_rect_help = text_help.get_rect(topleft=(690, 30))  # حوض النص في منتصف الشاشة
    screen.blit(text_help, text_rect_help)
    
    # عرض النص
    text = font.render(f"Level of progress: {counter}", True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(10, 10))  # حوض النص في منتصف الشاشة
    screen.blit(text, text_rect)
    
is_start=False

# حلقة اللعبة الرئيسية
while True:
    
    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if image_rect_start.collidepoint(event.pos):
                is_start=True
            if image_rect_quit.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            
        if is_start:
            screen.fill((220, 220, 220))
            map()
        else:
            screen.fill((220, 220, 220))
            main_menu(0,0,0)
        if image_rect_start.collidepoint(pygame.mouse.get_pos()) and is_start==False:
            screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
            main_menu(-3,0,0)
        if image_rect_option.collidepoint(pygame.mouse.get_pos()) and is_start==False:
            screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
            main_menu(0,-3,0)
        if image_rect_quit.collidepoint(pygame.mouse.get_pos()) and is_start==False:
            screen.fill((220, 220, 220))
        # تكبير الزر إذا وجد المؤشر فوقه
            main_menu(0,0,-3)
    


    
    pygame.display.update()
    clock.tick(60)  # تحديث بمعدل 60 إطارًا في الثانية

    
# إغلاق اللعبة بشكل نظيف