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

# تحميل الصورة
image = pygame.image.load("libya.png")
# تصغير حجم الصورة
new_width = 200
new_height = 150
image = pygame.transform.scale(image, (new_width, new_height))

image2 = pygame.image.load("morroco.png")
image2 = pygame.transform.scale(image2, (new_width, new_height))

# المتغيرات الأساسية
clock = pygame.time.Clock()
x = 0
y = 250
counter = 0
# تعريف مستطيل الصورة
image_rect = image.get_rect()
image_rect.topleft = (x, y)
#============================
image_rect2 = image2.get_rect()
image_rect2.topleft = (x + 500, y)
#===========================

# تحضير النص
font = pygame.font.Font(None, 36)  # تعيين الخط وحجم النص

# حلقة اللعبة الرئيسية
while True:
    # معالجة الأحداث
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            # التحقق من النقر على المستطيل
            if image_rect.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("تم النقر على الصورة!")
                subprocess.Popen(["python", "libya.py"])
                
            if image_rect2.collidepoint(event.pos):
                # يتم تنفيذ الحدث هنا عند النقر على الصورة
                print("تم النقر على الصورة!")
                counter += 1
                
            
    # تحديث اللعبة

    # رسم اللعبة
    screen.fill((0, 0, 0))  # تعبئة الشاشة باللون الأسود
    # رسم العناصر الأخرى في اللعبة

    # عرض الصورة
    screen.blit(image, (x, y))  # حيث (x, y) هي إحداثيات الصورة على الشاشة
    screen.blit(image2, (x + 500, y))
    
    # عرض النص
    text = font.render(f"العداد: {counter}", True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(10, 10))  # حوض النص في منتصف الشاشة
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    

    # تحديث الشاشة
    pygame.display.update()
    clock.tick(60)  # تحديث بمعدل 60 إطارًا في الثانية

# إغلاق اللعبة بشكل نظيف
pygame.quit()