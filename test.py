import pygame
from pygame.locals import *

pygame.init()

win_size = (1200, 600)
window = pygame.display.set_mode(win_size)

# الألوان
WHITE = (220, 220, 220)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# الخطوط
font = pygame.font.Font(None, 32)
back_ground= pygame.image.load("D.png")
back_ground=pygame.transform.scale(back_ground, (1200, 600))
# أزرار القائمة الرئيسية
africa_button_rect =        pygame.Rect(100, 100, 200, 40)
asia_button_rect =          pygame.Rect(100, 160, 200, 40)
erup_button_rect =          pygame.Rect(100, 220, 200, 40)
australia_button_rect =     pygame.Rect(100, 280, 200, 40)
north_amrica_button_rect =  pygame.Rect(100, 340, 200, 40)
south_amrica_button_rect =  pygame.Rect(100, 400, 200, 40)
exit_button_rect =          pygame.Rect(100, 500, 200, 40)

# أزرار قائمة الخيارات
level1_button_rect = pygame.Rect(0, 0, 200, 40)
level2_button_rect = pygame.Rect(0, 0, 200, 40)
level3_button_rect = pygame.Rect(0, 0, 200, 40)
back_button_rect = pygame.Rect(400, 500, 200, 40)  # تعريف مستطيل زر الرجوع

main_menu_button_rect = pygame.Rect(900, 30, 200, 40)
is_in_main_menu = True
is_in_options_menu = False
options_menu_slide = 800  # الانزلاق الأولي لقائمة الخيارات

clock = pygame.time.Clock()
is_running = True
easy= True
def questions(continent,lvl):
    global text_render
    if continent == "africa":
        if lvl =="easy":
            text = """
                Africa - Easy
                What is the capital of Egypt? Cairo
                What is the capital of Morocco? - Rabat
                What is the capital of South Africa? - Pretoria (executive), Cape Town (legislative), Bloemfontein (judicial)
                What is the capital of Nigeria? - Abuja
                What is the capital of Kenya? - Nairobi
                What is the capital of Algeria? - Algiers
                What is the capital of Tunisia? - Tunis
                What is the capital of Zimbabwe? - Harare
                What is the capital of Ghana? - Accra
                What is the capital of Ethiopia? - Addis Ababa
                """
        if lvl =="medium":
            text= """
                Africa - Medium
                What is the largest country in Africa in terms of land area? - Algeria
                Which African country has the highest population? - Nigeria
                Which African country ranks second in terms of population? - Ethiopia
                Which African country is the smallest in terms of land area? - Seychelles
                What is the total population of Egypt? - 104 million
                What is the total population of South Africa? - 60 million
                What is the total population of Nigeria? - 211 million
                What is the total population of Ethiopia? - 120 million
                What is the total population of Algeria? - 44 million
                """
        if lvl == "hard":
            text = """"
                Which African country was not colonized by European powers? - Ethiopia
                What is the highest mountain peak in Africa? - Mount Kilimanjaro
                What is the largest lake in Africa by volume? - Lake Victoria
                Which ancient civilization is located in the region of Nubia between Egypt and Sudan? - The Kingdom of Kush (Nubia)
                What is the longest river in Africa? - The Nile River
                What is the largest tropical rainforest in Africa? - The Congo Rainforest
                Which city has the highest population density in Africa? - Lagos, Nigeria
                What is the major desert that spans across several countries in North Africa? - The Sahara Desert
                What is the currency used in South Africa? - South African Rand
                Which country is famous for its white sandy beaches in Zanzibar? - Tanzania
            """
    if continent == "asia":
        if lvl =="easy":
            text = """
                "What is the capital of China?" - Beijing
                "Which city is the capital of India?" - New Delhi
                "What is the capital of Japan?" - Tokyo
                "Which city is the capital of South Korea?" - Seoul
                "What is the capital of Indonesia?" - Jakarta
                "Which city is the capital of Saudi Arabia?" - Riyadh
                "What is the capital of Turkey?" - Ankara
                "Which city is the capital of Iran?" - Tehran
                "What is the capital of Thailand?" - Bangkok
                "Which city is the capital of Vietnam?" - Hanoi
                """
        if lvl =="medium":
            text= """
                "What is the largest country in Asia by land area?" - Russia
                "Which country in Asia has the smallest land area?" - Maldives
                "What is the most populous country in Asia?" - China
                "Which country in Asia has the lowest population?" - Bhutan
                "What is the land area of Russia?" - Approximately 17.1 million square kilometers
                "What is the population of China?" - Approximately 1.4 billion
                "Which country in Asia has the highest population density?" - Bangladesh
                "What is the population of India?" - Approximately 1.3 billion
                "How many square kilometers is Kazakhstan?" - Approximately 2.7 million square kilometers
                "Which country in Asia has the highest population growth rate?" - Oman
                """
        if lvl == "hard":
            text = """"
                "What is the capital city of Kyrgyzstan?" - Bishkek
                "Which mountain range stretches across northern Afghanistan, southern Tajikistan, and northwest Pakistan?" - Hindu Kush
                "What is the official language of Turkmenistan?" - Turkmen
                "What is the name of the island located in the Bay of Bengal known for its beautiful beaches and coral reefs?" - Andaman Islands
                "Which country in Asia has the highest peak in the world?" - Nepal (Mount Everest)
                "What is the former name of Myanmar?" - Burma
                "Which city in India is known as the 'Pink City'?" - Jaipur
                "What is the largest mosque in the world located in Mecca, Saudi Arabia?" - Masjid al-Haram (Great Mosque of Mecca)
                "Which country in Asia is the only one without a rectangular flag?" - Nepal
                "What is the name of the famous ancient citadel located in Afghanistan?" - Bagram
            """
    if continent == "erup":
        if lvl =="easy":
            text = """
                "What is the capital city of France?" - Paris
                "Which city is the capital of Germany?" - Berlin
                "What is the capital of Italy?" - Rome
                "Which city is the capital of Spain?" - Madrid
                "What is the capital city of the United Kingdom?" - London
                "Which city is the capital of Russia?" - Moscow
                "What is the capital of Greece?" - Athens
                "Which city is the capital of Sweden?" - Stockholm
                "What is the capital city of Poland?" - Warsaw
                "Which city is the capital of Switzerland?" - Bern
                """
        if lvl =="medium":
            text= """
                "What is the land area of France in square kilometers?" - 551,695 square kilometers.
                "How many people live in Germany approximately?" - Approximately 83 million.
                "What is the land area of Italy in square kilometers?" - 301,340 square kilometers.
                "Approximately, how many people live in Spain?" - Approximately 47 million.
                "What is the land area of the United Kingdom in square kilometers?" - 242,500 square kilometers.
                "Approximately, how many people live in Russia?" - Approximately 145 million.
                "What is the land area of Greece in square kilometers?" - 131,957 square kilometers.
                "Approximately, how many people live in Sweden?" - Approximately 10.4 million.
                "What is the land area of Poland in square kilometers?" - 312,696 square kilometers.
                "Approximately, how many people live in Switzerland?" - Approximately 8.7 million.
                """
        if lvl == "hard":
            text = """"
                "Which country in Europe is known as the 'Land of Fire and Ice'?" - Iceland
                "What is the highest mountain in Europe?" - Mount Elbrus
                "Which river flows through the city of Prague?" - Vltava River
                "Which country in Europe has the most UNESCO World Heritage Sites?" - Italy
                "Which city is considered the fashion capital of Europe?" - Paris
                "What is the official currency of Switzerland?" - Swiss Franc
                "Which country has the largest population in Europe?" - Russia
                "What is the name of the famous palace located near Vienna, Austria?" - Schönbrunn Palace
                "Which country is home to the famous Neuschwanstein Castle?" - Germany
                "Which city is known as the 'City of Bridges'?" - Venice
            """
    if continent == "australia":
        if lvl =="easy":
            text = """
                "What is the capital city of Australia?" - Canberra
                "Which city is the capital of New Zealand?" - Wellington
                "What is the capital of Papua New Guinea?" - Port Moresby
                "Which city is the capital of Fiji?" - Suva
                "What is the capital city of Indonesia?" - Jakarta
                "Which city is the capital of Vanuatu?" - Port Vila
                "What is the capital of Timor-Leste?" - Dili
                "Which city is the capital of Tonga?" - Nuku'alofa
                "What is the capital city of Samoa?" - Apia
                "Which city is the capital of the Solomon Islands?" - Honiara
                """
        if lvl =="medium":
            text= """
                "What is the land area of Australia in square kilometers?" - 7,692,024 square kilometers.
                "Approximately, how many people live in Australia?" - Approximately 25.7 million.
                "What is the land area of Papua New Guinea in square kilometers?" - 462,840 square kilometers.
                "Approximately, how many people live in Papua New Guinea?" - Approximately 9.1 million.
                "What is the land area of New Zealand in square kilometers?" - 268,021 square kilometers.
                "Approximately, how many people live in New Zealand?" - Approximately 4.9 million.
                "What is the land area of Fiji in square kilometers?" - 18,274 square kilometers.
                "Approximately, how many people live in Fiji?" - Approximately 898,760.
                "What is the land area of Vanuatu in square kilometers?" - 12,189 square kilometers.
                "Approximately, how many people live in Vanuatu?" - Approximately 307,145.
                """
        if lvl == "hard":
            text = """"
                "Which Australian state is the largest by area?" - Western Australia.
                "What is the name of the world's largest coral reef system located in Australia?" - Great Barrier Reef.
                "Which city in Australia is known as the 'Harbour City'?" - Sydney.
                "What is the name of the famous rock formation in the Northern Territory of Australia?" - Uluru (previously known as Ayers Rock).
                "Which Australian state is home to the Great Barrier Reef?" - Queensland.
                "What is the highest mountain in Australia?" - Mount Kosciuszko.
                "Which city is the capital of Australia's Northern Territory?" - Darwin.
                "What is the name of the famous beach in Sydney, Australia?" - Bondi Beach.
                "Which Australian state is known for its wine regions such as the Barossa Valley and McLaren Vale?" - South Australia.
                "What is the name of the famous wildlife sanctuary located in Queensland, Australia?" - Australia Zoo.
            """
    if continent == "south_amrica":
        if lvl =="easy":
            text = """
                "What is the capital city of Brazil?" - Brasília.
                "Which city is the capital of Argentina?" - Buenos Aires.
                "What is the capital of Colombia?" - Bogotá.
                "Which city is the capital of Peru?" - Lima.
                "What is the capital city of Chile?" - Santiago.
                "Which city is the capital of Ecuador?" - Quito.
                "What is the capital of Bolivia?" - Sucre (constitutional capital) and La Paz (seat of government and executive capital).
                "Which city is the capital of Venezuela?" - Caracas.
                "What is the capital city of Paraguay?" - Asunción.
                "Which city is the capital of Uruguay?" - Montevideo.
                """
        if lvl =="medium":
            text= """
                "What is the land area of Brazil in square kilometers?" - 8,515,767 square kilometers.
                "Approximately, how many people live in Brazil?" - Approximately 213.99 million.
                "What is the land area of Argentina in square kilometers?" - 2,780,400 square kilometers.
                "Approximately, how many people live in Argentina?" - Approximately 45.38 million.
                "What is the land area of Colombia in square kilometers?" - 1,141,748 square kilometers.
                "Approximately, how many people live in Colombia?" - Approximately 50.88 million.
                "What is the land area of Peru in square kilometers?" - 1,285,216 square kilometers.
                "Approximately, how many people live in Peru?" - Approximately 33.29 million.
                "What is the land area of Venezuela in square kilometers?" - 916,445 square kilometers.
                "Approximately, how many people live in Venezuela?" - Approximately 28.52 million.
                """
        if lvl == "hard":
            text = """"
                "Which country in South America has the highest population?" - Brazil.
                "What is the official language of Suriname?" - Dutch.
                "Which country in South America has the highest elevation?" - Argentina (with the Andes mountain range).
                "What is the name of the world's highest waterfall located in Venezuela?" - Angel Falls.
                "Which country in South America is the smallest by land area?" - Suriname.
                "What is the name of the indigenous ruins located in Peru?" - Machu Picchu.
                "Which country in South America has the largest economy?" - Brazil.
                "What is the name of the famous soccer player from Argentina?" - Lionel Messi.
                "Which country in South America is the largest by land area?" - Brazil.
                "What is the name of the vibrant neighborhood in Rio de Janeiro, Brazil?" - Copacabana.
            """
    if continent == "north_amrica":
        if lvl =="easy":
            text = """
                "What is the capital city of Canada?" - Ottawa.
                "Which city is the capital of the United States?" - Washington, D.C.
                "What is the capital of Mexico?" - Mexico City.
                "Which city is the capital of Cuba?" - Havana.
                "What is the capital city of Jamaica?" - Kingston.
                "Which city is the capital of Haiti?" - Port-au-Prince.
                "What is the capital of Costa Rica?" - San José.
                "Which city is the capital of Panama?" - Panama City.
                "What is the capital city of Guatemala?" - Guatemala City.
                "Which city is the capital of El Salvador?" - San Salvador.
                """
        if lvl =="medium":
            text= """
                "What is the land area of Canada in square kilometers?" - 9,984,670 square kilometers.
                "Approximately, how many people live in Canada?" - Approximately 38 million.
                "What is the land area of the United States in square kilometers?" - 9,631,418 square kilometers.
                "Approximately, how many people live in the United States?" - Approximately 331 million.
                "What is the land area of Mexico in square kilometers?" - 1,964,375 square kilometers.
                "Approximately, how many people live in Mexico?" - Approximately 126 million.
                "What is the land area of Cuba in square kilometers?" - 109,884 square kilometers.
                "Approximately, how many people live in Cuba?" - Approximately 11 million.
                "What is the land area of Haiti in square kilometers?" - 27,750 square kilometers.
                "Approximately, how many people live in Haiti?" - Approximately 11 million.
                """
        if lvl == "hard":
            text = """"
                "Which country in North America has the largest land area?" - Canada.
                "What is the official language of Canada?" - Canada has two official languages: English and French.
                "Which country in North America has the highest population density?" - Haiti.
                "What is the name of the famous national park located in the United States that features the Old Faithful geyser?" - Yellowstone National Park.
                "Which country in North America has the longest coastline?" - Canada.
                "What is the name of the ancient Mayan city in Mexico?" - There are several Mayan cities in Mexico, but one of the most famous is Chichen Itza.
                "Which country in North America has the largest indigenous population?" - Mexico.
                "What is the name of the famous music festival held annually in California, United States?" - Coachella.
                "Which country in North America is known for its production of maple syrup?" - Canada.
                "What is the name of the iconic suspension bridge in San Francisco, United States?" - The Golden Gate Bridge.
            """
    



    # تحويل النص إلى سطر واحد
    lines = text.strip().split('\n')
    text_render = [font.render(line, True, (0, 0, 0)) for line in lines]
     # عرض النص سطرًا بسطر
def print_text():
    global text_render
     # عرض النص سطرًا بسطر
    window.fill(WHITE)
    y = 50
    for render in text_render:
        window.blit(render, (50, y))
        y += 50

is_africa =False
continent=""
lvl=""
while is_running:
    
    time_delta = clock.tick(60) / 1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_in_main_menu:
                window.blit(back_ground,(0,0))
                if africa_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    print("africa")
                    continent="africa"
                elif asia_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    # تنفيذ إجراء عند النقر على زر الخيارات
                    print("asia")
                    continent="asia"
                elif erup_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    # تنفيذ إجراء عند النقر على زر الخروج
                    print("erup")
                    continent="erup"
                elif australia_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    print("australia")
                    continent="australia"
                elif south_amrica_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    # تنفيذ إجراء عند النقر على زر الخيارات
                    print("south amrica")
                    continent="south_amrica"
                elif north_amrica_button_rect.collidepoint(event.pos):
                    is_in_main_menu = False
                    is_in_options_menu = True
                    # تنفيذ إجراء عند النقر على زر الخروج
                    print("nourth amrica")
                    continent="north_amrica"
                elif exit_button_rect.collidepoint(event.pos):
                    # تنفيذ إجراء عند النقر على زر الخروج
                    print("EXIT")
                    is_running = False

            elif is_in_options_menu:
                window.fill(WHITE)
                
                if level1_button_rect.collidepoint(event.pos):
                    is_africa =True
                    is_in_options_menu=False
                    lvl="easy"
                    print("تم النقر على زر المستوى 1")
                elif level2_button_rect.collidepoint(event.pos):
                    # تنفيذ إجراء عند النقر على زر المستوى 2
                    is_in_options_menu=False
                    lvl="medium"
                    print("تم النقر على زر المستوى 2")
                elif level3_button_rect.collidepoint(event.pos):
                    # تنفيذ إجراء عند النقر على زر المستوى 3
                    lvl="hard"
                    is_in_options_menu=False
                    print("تم النقر على زر المستوى 3")
                elif back_button_rect.collidepoint(event.pos):
                    is_in_main_menu = True
                    is_in_options_menu = False

            else:
                if main_menu_button_rect.collidepoint(event.pos):
                    print("ddsdsd")
                    is_in_main_menu=True
    
    if is_in_main_menu:
        window.blit(back_ground,(0,0))
        # رسم أزرة القائمة الرئيسية
        pygame.draw.rect(window, GRAY, africa_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, asia_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, erup_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, australia_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, north_amrica_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, south_amrica_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, exit_button_rect, border_radius=25)


        if africa_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, africa_button_rect.inflate(10, 10), border_radius=25)
        if asia_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, asia_button_rect.inflate(10, 10), border_radius=25)
        if erup_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, erup_button_rect.inflate(10, 10), border_radius=25)

        if australia_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, australia_button_rect.inflate(10, 10), border_radius=25)
        if north_amrica_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, north_amrica_button_rect.inflate(10, 10), border_radius=25)
        if south_amrica_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, south_amrica_button_rect.inflate(10, 10), border_radius=25)

        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, exit_button_rect.inflate(10, 10), border_radius=25)

        # رسم نص الأزرار
        africa_txt = font.render("Africa", True, BLACK)
        asia_txt = font.render("Asia", True, BLACK)
        erup_txt = font.render("Erup", True, BLACK)

        australia_txt = font.render("Australia", True, BLACK)
        north_amrica_txt = font.render("Nourth Amrica", True, BLACK)
        south_amrica_txt = font.render("South Amrica", True, BLACK)

        exit_txt = font.render("Exit", True, BLACK)

        window.blit(africa_txt, (africa_button_rect.centerx - africa_txt.get_width() // 2,
                                 africa_button_rect.centery - africa_txt.get_height() // 2))
        window.blit(asia_txt, (asia_button_rect.centerx - asia_txt.get_width() // 2,
                                  asia_button_rect.centery - asia_txt.get_height() // 2))
        window.blit(erup_txt, (erup_button_rect.centerx - erup_txt.get_width() // 2,
                                erup_button_rect.centery - erup_txt.get_height() // 2))
        
        window.blit(australia_txt, (australia_button_rect.centerx - australia_txt.get_width() // 2,
                                 australia_button_rect.centery - australia_txt.get_height() // 2))
        window.blit(north_amrica_txt, (north_amrica_button_rect.centerx - north_amrica_txt.get_width() // 2,
                                  north_amrica_button_rect.centery - north_amrica_txt.get_height() // 2))
        window.blit(south_amrica_txt, (south_amrica_button_rect.centerx - south_amrica_txt.get_width() // 2,
                                south_amrica_button_rect.centery - south_amrica_txt.get_height() // 2))
        
        window.blit(exit_txt, (exit_button_rect.centerx - exit_txt.get_width() // 2,
                                exit_button_rect.centery - exit_txt.get_height() // 2))

    elif is_in_options_menu:
        # إنزلاق قائمة الخيارات من اليسار إلى الوسط
        #if options_menu_slide > 400:
        #    options_menu_slide -= 10
        window.blit(back_ground,(0,0))
        level1_button_rect.topleft = (100, 100)
        level2_button_rect.topleft = (100, 160)
        level3_button_rect.topleft = (100, 220)
        back_button_rect.topleft = (100, 500)

        # رسم أزرار قائمة الخيارات
        pygame.draw.rect(window, GRAY, level1_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, level2_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, level3_button_rect, border_radius=25)
        pygame.draw.rect(window, GRAY, back_button_rect, border_radius=25)

        if level1_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, level1_button_rect.inflate(10, 10), border_radius=25)
        if level2_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, level2_button_rect.inflate(10, 10), border_radius=25)
        if level3_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, level3_button_rect.inflate(10, 10), border_radius=25)
        if back_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, back_button_rect.inflate(10, 10), border_radius=25)

        # رسم نص الأزرار
        level1_text = font.render("Easy", True, BLACK)
        level2_text = font.render("Medium", True, BLACK)
        level3_text = font.render("Hard", True, BLACK)
        back_text = font.render("Back", True, BLACK)

        window.blit(level1_text, (level1_button_rect.centerx - level1_text.get_width() // 2,
                                  level1_button_rect.centery - level1_text.get_height() // 2))
        window.blit(level2_text, (level2_button_rect.centerx - level2_text.get_width() // 2,
                                  level2_button_rect.centery - level2_text.get_height() // 2))
        window.blit(level3_text, (level3_button_rect.centerx - level3_text.get_width() // 2,
                                  level3_button_rect.centery - level3_text.get_height() // 2))
        window.blit(back_text, (back_button_rect.centerx - back_text.get_width() // 2,
                                back_button_rect.centery - back_text.get_height() // 2))
    else:
        window.blit(back_ground,(0,0))
        questions(continent,lvl)
        print_text()
        pygame.draw.rect(window, GRAY, main_menu_button_rect, border_radius=25)
        if main_menu_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, GRAY, main_menu_button_rect.inflate(10, 10), border_radius=25)
        btn_txt = font.render("Main Menu", True, BLACK)
        window.blit(btn_txt, (main_menu_button_rect.centerx - btn_txt.get_width() // 2,
                                 main_menu_button_rect.centery - btn_txt.get_height() // 2))
        
    
    pygame.display.flip()

pygame.quit()