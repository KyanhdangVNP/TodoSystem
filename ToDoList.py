if __name__ == "__main__":
    #Importing Moudles and Python files:
    import os
    import pygame
    from UsefulPygameDef import *
    
    #Preparing Pygame:
    #Initzile:
    pygame.init()
    SCREEN_WIDTH = 1050
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("To-do List | Made by team 3 (Kyanh, Thien Long)")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    #Preparing console log:
    print(" ----------------------------------------------------------------------")
    print("""
████████╗ ██████╗       ██████╗  ██████╗     ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗      ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║█████╗██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
   ██║   ██║   ██║╚════╝██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝      ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
   ╚═╝    ╚═════╝       ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   """)
    print(" ----------------------------------------------------------------------")

    print()
    print("Welcome to To-do list system, a program that helps people can shelduce their jobs, works in their lists so that they can do their works faster and better.")
    print()
    print("The system is now loading, please wait...")

    #Load fonts:


    #Load btn:
    blankBtnImg = "img/blankBtn.png"
    blankBtn_darkImg = "img/blankBtn_dark.png"

    PJTitle = button(SCREEN_WIDTH / 2, 100, "img/PJTitleButCooler.png", 90, "center")
    PJMinorTitle = button(SCREEN_WIDTH / 2, 180, "img/PJMinorTitle.png", 20, "center")

    startBtn = button(SCREEN_WIDTH / 2, 185, blankBtnImg, 20, "center", True, blankBtn_darkImg)
    optionsBtn = button(SCREEN_WIDTH / 2, 300, blankBtnImg, 20, "center", True, blankBtn_darkImg)
    exitBtn = button(SCREEN_WIDTH / 2, 415, blankBtnImg, 20, "center", True, blankBtn_darkImg)
    isClickedToContinute = False
    flashingText = pygame.USEREVENT + 1
    mainMenuStart= False
    countFlashingText = 0
    clickedToContinute_alpha = None

    #SETTINGS PREPARING:
    arrowBtnImg = "img/ArrowBtn.png"
    arrowBtnImg_dark = "img/ArrowBtn_dark.png"
    settings_BackBtn = button(150, 215, blankBtnImg, 8, "center", True, blankBtn_darkImg)
    settings_ThemeBtn = button(SCREEN_WIDTH / 2, 100, "img/LightThemeBtn.png", 10, "center", True, "img/NightThemeBtn.png")

    settings_VolumeBtn = button(SCREEN_WIDTH - 240, 100, "img/VolumeBtn.png", 10, "center")

    settings_MusicBoard = button(SCREEN_WIDTH / 2, 347, "img/Settings_MusicBoard.png", 13, "center", True, "img/MusicBoard_dark.png")
    settings_Music_ChangeLast = button(80, 347, arrowBtnImg, 10, "center", True, arrowBtnImg_dark )
    settings_Music_ChangeNext = button(SCREEN_WIDTH - 80, 347, arrowBtnImg, 10, "center", True, arrowBtnImg_dark)
    settings_Music_ChangeLast.rotate("horizontal")


    #Music preparing:
    musicList = os.listdir("./Musics")
    musicCurrent = musicList[5]
    musicLast = musicCurrent
    playMusic(f"Musics/{musicCurrent}")
    musicInfo = getAudioInfo(f"Musics/{musicCurrent}")
    pygame.mixer.music.set_volume(1.0)

    #Starting Pygame screen:
    screenName = "mainMenu"
    BGType = "normal"
    themeType = "light"
    FPS = 60
    running = True
    while running:
        #Music system:
        if not musicCurrent == musicLast:
            playMusic(f"Musics/{musicCurrent}")
            musicInfo = getAudioInfo(f"Musics/{musicCurrent}")
            musicLast = musicCurrent

        #Get width, height screen:
        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
        #print(SCREEN_WIDTH, SCREEN_HEIGHT)

        #Draw Background:
        if themeType == "dark":
            if BGType == "normal":
                BGImg = pygame.image.load("img/MainBG_dark.png")
            elif BGType == "blur":
                BGImg = pygame.image.load("img/MainBG_dark_Blur.png")
            #elif BGType == "noText":
            #    BGImg = pygame.image.load("img/MainBG_NoText_dark.png")
        else:
            if BGType == "normal":
                BGImg = pygame.image.load("img/MainBG.png")
            elif BGType == "blur":
                BGImg = pygame.image.load("img/MainBG_Blur.png")
            #elif BGType == "noText":
            #    BGImg = pygame.image.load("img/MainBG_NoText.png")
        
        BGImg = pygame.transform.scale(BGImg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        screen.blit(BGImg, (0, 0))

        #Draw things:
        if screenName == "mainMenu":
            PJTitle.changeSize(round(SCREEN_HEIGHT / 6.7))
            PJTitle.changeXY(SCREEN_WIDTH / 2, 224)
            PJTitle.draw(screen, "", "", "", "")

            PJMinorTitle.changeSize(round(SCREEN_HEIGHT / 64))
            PJMinorTitle.changeXY(SCREEN_WIDTH / 2, 320)
            PJMinorTitle.draw(screen, "", "", "", "")

            #print(PJTitle.rect)
            PJTitle.rect.topleft = (0, 0)
        
        if mainMenuStart == False:
            drawText(screen, "Click any button to start program", "Fonts\MinecraftBold.otf", 32, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, themeType, clickedToContinute_alpha,"center")
            if pygame.mouse.get_pressed()[0] == 1 and isClickedToContinute == False:
                pygame.time.set_timer(flashingText, 200, 5)
                isClickedToContinute = True
        if mainMenuStart:
            if screenName == "mainMenu":
                startBtn.changeXY(SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT - 120)
                startBtn.draw(screen, "Start", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                
                if startBtn.isColliding:
                    if startBtn.action:
                        print("START PROGRAM GO BRR")
                    startBtn.changeSize(startBtn.sizePercent + ((22 - startBtn.sizePercent) / 3), None, None)
                    #startBtn.changeSize(12, None, None)
                else:
                    startBtn.changeSize(startBtn.sizePercent + ((20 - startBtn.sizePercent) / 3), None, None)
                    #startBtn.changeSize(20, None, None)
                

                optionsBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120)
                optionsBtn.draw(screen, "Settings", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                if optionsBtn.isColliding:
                    if optionsBtn.action:
                        screenName = "mainMenu_settings"
                        BGType = "blur"
                        print("SETTINGS PROJECT GO BRR")
                    optionsBtn.changeSize(optionsBtn.sizePercent + ((22 - optionsBtn.sizePercent) / 3), None, None)
                else:
                    optionsBtn.changeSize(optionsBtn.sizePercent + ((20 - optionsBtn.sizePercent) / 3), None, None)

                exitBtn.changeXY(SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT - 120)
                exitBtn.draw(screen, "Exit", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                if exitBtn.isColliding:
                    if exitBtn.action:
                        print("EXIT PROJECT GO BRR")
                        running = False
                    exitBtn.changeSize(exitBtn.sizePercent + ((22 - exitBtn.sizePercent) / 3), None, None)
                else:
                    exitBtn.changeSize(exitBtn.sizePercent + ((20 - exitBtn.sizePercent) / 3), None, None)
                
                #Draw a little credit text on the top right corner in the main menu
                drawText(screen, "Made my Kyanh |N| SkyDra", "Fonts\MinecraftBold.otf", 24, SCREEN_WIDTH - 15, 12, themeType, None, "right")
            
            if screenName == "mainMenu_settings":
                drawText(screen, "| SETTINGS |", "Fonts\MinecraftBold.otf", 48, SCREEN_WIDTH / 2, 15, themeType, None, "center")
                settings_BackBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
                settings_BackBtn.draw(screen, "BACK", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                
                if settings_BackBtn.isColliding:
                    if settings_BackBtn.action:
                        print("GOING BACK TO MAIN MENU SCREEN...")
                        screenName = "mainMenu"
                        BGType = "normal"
                    settings_BackBtn.changeSize(settings_BackBtn.sizePercent + ((15 - settings_BackBtn.sizePercent) / 3), None, None)
                else:
                    settings_BackBtn.changeSize(settings_BackBtn.sizePercent + ((13 - settings_BackBtn.sizePercent) / 3), None, None)
                
                #Draw theme setting:
                drawText(screen, "Theme:", "Fonts\MinecraftBold.otf", 45, 64, 105, themeType)
                settings_ThemeBtn.changeXY(290, 100)
                settings_ThemeBtn.draw(screen, "", None, None, None, themeType)
                
                if settings_ThemeBtn.isColliding:
                    if settings_ThemeBtn.action:
                        print("CHANGING THEME...")
                        if themeType == "light":
                            themeType = "dark"
                        else:
                            themeType = "light"
                    settings_ThemeBtn.changeSize(settings_ThemeBtn.sizePercent + ((16 - settings_ThemeBtn.sizePercent) / 3), None, None)
                else:
                    settings_ThemeBtn.changeSize(settings_ThemeBtn.sizePercent+ ((14 - settings_ThemeBtn.sizePercent) / 3), None, None)

                #Draw volume setting:
                drawText(screen, "Volume:", "Fonts\MinecraftBold.otf", 45, SCREEN_WIDTH - 250, 105, themeType, 255, "right")
                settings_VolumeBtn.changeXY(SCREEN_WIDTH - 200, 100)
                #Change images of volumeBtn (it's special cuz it has 4 images).
                if themeType == "light":
                    if pygame.mixer.music.get_volume() == 1.0:
                        settings_VolumeBtn.changeImg("img/VolumeBtn.png")
                    elif pygame.mixer.music.get_volume() == 0.0:
                        settings_VolumeBtn.changeImg("img/VolumeBtn_Muted.png")
                
                elif themeType == "dark":
                    if pygame.mixer.music.get_volume() == 1.0:
                        settings_VolumeBtn.changeImg("img/VolumeBtn_dark.png")
                    elif pygame.mixer.music.get_volume() == 0.0:
                        settings_VolumeBtn.changeImg("img/VolumeBtn_Muted_dark.png")
                settings_VolumeBtn.draw(screen)
                
                if settings_VolumeBtn.isColliding:
                    if settings_VolumeBtn.action:
                        if pygame.mixer.music.get_volume() == 1.0:
                            pygame.mixer.music.set_volume(0.0)
                        elif pygame.mixer.music.get_volume() == 0.0:
                            pygame.mixer.music.set_volume(1.0)
                    settings_VolumeBtn.changeSize(settings_VolumeBtn.sizePercent + ((16 - settings_VolumeBtn.sizePercent) / 3), None, None)
                else:
                    settings_VolumeBtn.changeSize(settings_VolumeBtn.sizePercent+ ((14 - settings_VolumeBtn.sizePercent) / 3), None, None)

                #Draw audio setting:
                drawText(screen, "Music:", "Fonts\MinecraftBold.otf", 45, 64, 224, themeType)
                settings_MusicBoard.changeXY(SCREEN_WIDTH / 2, 300)
                settings_MusicBoard.draw(screen, "", None, None, None, themeType)

                drawText(screen, musicInfo["title"], "Fonts\MinecraftBold.otf", 35, SCREEN_WIDTH / 2, 320, themeType, None, "center")
                drawText(screen, "Artist: " + musicInfo["artist"], "Fonts\MinecraftBold.otf", 35, SCREEN_WIDTH / 2, 374, themeType, None, "center")
                settings_Music_ChangeLast.changeXY(64, 347)
                settings_Music_ChangeLast.draw(screen, "", None, None, None, themeType)
                if settings_Music_ChangeLast.isColliding:
                    if settings_Music_ChangeLast.action:
                        musicCurrent = musicList[musicList.index(musicCurrent) - 1]
                        print("Changing music...")
                    
                    settings_Music_ChangeLast.changeSize(settings_Music_ChangeLast.sizePercent + ((15 - settings_Music_ChangeLast.sizePercent) / 3), None, None)
                else:
                    settings_Music_ChangeLast.changeSize(settings_Music_ChangeLast.sizePercent + ((13 - settings_Music_ChangeLast.sizePercent) / 3), None, None)
                
                settings_Music_ChangeNext.changeXY(SCREEN_WIDTH - 64, 347)
                settings_Music_ChangeNext.draw(screen, "", None, None, None, themeType)
                if settings_Music_ChangeNext.isColliding:
                    if settings_Music_ChangeNext.action:
                        if musicList.index(musicCurrent) + 1 == len(musicList):
                            musicCurrent = musicList[0]
                        else:
                            musicCurrent = musicList[musicList.index(musicCurrent) + 1]
                        print("Changing music...")
                    
                    settings_Music_ChangeNext.changeSize(settings_Music_ChangeNext.sizePercent + ((15 - settings_Music_ChangeNext.sizePercent) / 3), None, None)
                else:
                    settings_Music_ChangeNext.changeSize(settings_Music_ChangeNext.sizePercent + ((13 - settings_Music_ChangeNext.sizePercent) / 3), None, None)
                

        for event in pygame.event.get():
            if event.type == flashingText:
                if clickedToContinute_alpha == None:
                    clickedToContinute_alpha = 0
                else:
                    clickedToContinute_alpha = None
                countFlashingText += 1
                if countFlashingText >= 5:
                    mainMenuStart = True
            
            #Get another value of screen width, screen height and check if the screen size is different, so that the screen changes into BG size.
            if event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH_LAST, SCREEN_HEIGHT_LAST = pygame.display.get_surface().get_size()
                if SCREEN_WIDTH != SCREEN_WIDTH_LAST:
                    screen = pygame.display.set_mode((event.size[0], event.size[0] / 1.75), pygame.RESIZABLE)
                    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                    print(event.size)
                elif SCREEN_HEIGHT != SCREEN_HEIGHT_LAST:
                    screen = pygame.display.set_mode((event.size[1] * 1.75, event.size[1]), pygame.RESIZABLE)
                    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                    print(event.size)
                
                if SCREEN_HEIGHT < 510 or SCREEN_WIDTH < 892.5:
                    screen = pygame.display.set_mode((510 * 1.75, 510), pygame.RESIZABLE)
                    print(event.size)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.flip()
        pygame.display.update()

    print("|| PROJECT QUITTING... ||")
    pygame.quit()