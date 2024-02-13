import pygame
from pygame.locals import *
import subprocess

# تهيئة Pygame
pygame.init()

# تهيئة الشاشة
screen_width = 500
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("صندوق النص")

# تهيئة اللون
text_color = (255, 255, 255)
error_color = (255, 0, 0)
button_color = (50, 50, 50)
button_hover_color = (70, 70, 70)
background_color = (200, 200, 200)

# تهيئة الخط
font = pygame.font.Font(None, 36)

# إنشاء صندوق النص
text_box_width = 200
text_box_height = 50
text_box = pygame.Rect(
    screen_width // 2 - text_box_width // 2,
    screen_height // 2 - text_box_height // 2,
    text_box_width,
    text_box_height,
)

# النص المدخل
input_text = ""

# إنشاء زر العودة
back_button_width = 100
back_button_height = 50
back_button = pygame.Rect(
    screen_width // 2 - text_box_width // 2 - back_button_width - 10,
    screen_height // 2 - back_button_height // 2,
    back_button_width,
    back_button_height,
)

# إنشاء زر التأكيد
ok_button_width = 100
ok_button_height = 50
ok_button = pygame.Rect(
    screen_width // 2 + text_box_width // 2 + 10,
    screen_height // 2 - ok_button_height // 2,
    ok_button_width,
    ok_button_height,
)
incorrect = font.render("", True, (255,0,0))
# الدورة الرئيسية
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            incorrect=font.render("", True, (255,0,0))
            if event.key == K_BACKSPACE:
                # حذف الحرف الأخير عند الضغط على مفتاح backspace
                input_text = input_text[:-1]
            else:
                # إضافة الحرف المطابق لمفتاح الضغط إلى النص المدخل
                input_text += event.unicode
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if ok_button.collidepoint(mouse_pos):
                    # التحقق من الشرط
                    if input_text == "1234":
                        print("تم التحقق!")
                        subprocess.Popen(["python", "test.py"])
                        running = False
                    else:
                        print("الشرط غير مطابق.")
                        input_text=""
                        incorrect = font.render("incorrect ", True, (255,0,0))
                        
                elif back_button.collidepoint(mouse_pos):
                    # العودة
                    running = False

    # مسح الشاشة بلون الخلفية
    screen.fill(background_color)

    # رسم صندوق النص بدون زوايا
    pygame.draw.rect(screen, button_color, text_box, border_radius=0)

    # إنشاء سطح النص
   
    text_surface = font.render(input_text, True, text_color)
   
    # تحديد موقع النص داخل صندوق النص
    text_rect = text_surface.get_rect(center=text_box.center)

    # إظهار النص على الشاشة
    screen.blit(text_surface, text_rect)

    # التحقق من تحويل المؤشر فوق زر العودة
    if back_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, back_button, border_radius=5)
    else:
        pygame.draw.rect(screen, button_color, back_button, border_radius=5)
    back_text_surface = font.render("Back", True, text_color)
    back_text_rect = back_text_surface.get_rect(center=back_button.center)
    screen.blit(back_text_surface,back_text_rect)

    # التحقق منتحويل المؤشر فوق زر التأكيد
    if ok_button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, button_hover_color, ok_button, border_radius=5)
    else:
        pygame.draw.rect(screen, button_color, ok_button, border_radius=5)
    ok_text_surface = font.render("OK", True, text_color)
    ok_text_rect = ok_text_surface.get_rect(center=ok_button.center)
    screen.blit(ok_text_surface, ok_text_rect)
    screen.blit(incorrect, (190, 50))
    screen.blit((font.render("Password", True, (0,0,0))), (150, 100))
    
    # تحديث الشاشة
    pygame.display.flip()

# إغلاق Pygame
pygame.quit()