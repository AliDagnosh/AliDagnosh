import pygame
import sys

# تهيئة pygame
pygame.init()

# إعداد النافذة والشاشة
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Click Image")

# الألوان
background_color = (255, 255, 255)

# تحميل الصورة
image_effect = pygame.image.load("effect1.png")
image_effect=pygame.transform.scale(image_effect, (30, 30))
# حجم الصورة
image_width, image_height = image_effect.get_size()

# حلقة الأحداث الرئيسية
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # تحديد موقع الصورة بموضع المؤشر
            image_rect = image_effect.get_rect()
            image_rect.center = pygame.mouse.get_pos()
            # عرض الصورة
            screen.blit(image_effect, image_rect)
            pygame.display.flip()
            # تأخير لمدة 500 ميلي ثانية (نصف ثانية)
            pygame.time.delay(500)
            # إخفاء الصورة
            screen.fill(background_color)
            pygame.display.flip()
    
    # رسم الشاشة
    screen.fill(background_color)
    pygame.display.flip()