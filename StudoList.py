pixelFont = "Fonts/MinecraftBold.otf"

if __name__ == "__main__":
    #Importing Moudles and Python files:
    import os
    import pygame
    from UsefulPygameDef import *

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
    
    #Defs of screens:
    def mainMenu():
        global screen
        global SCREEN_WIDTH
        global SCREEN_WIDTH_LAST
        global SCREEN_HEIGHT_LAST
        global SCREEN_HEIGHT

        global FPS
        global screenName
        global themeType
        global screenFinalAction

        global musicInfo
        global musicList
        global musicCurrent
        global musicLast

        #Load btn:
        PJTitle = button(SCREEN_WIDTH / 2, 100, "img/PJTitleButCooler.png", 90, ["center"])
        PJMinorTitle = button(SCREEN_WIDTH / 2, 180, "img/PJMinorTitle.png", 20, ["center"])

        startBtn = button(SCREEN_WIDTH / 2, 185, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        optionsBtn = button(SCREEN_WIDTH / 2, 300, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        exitBtn = button(SCREEN_WIDTH / 2, 415, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        isClickedToContinute = False
        flashingText = pygame.USEREVENT + 1
        mainMenuStart= False
        countFlashingText = 0
        clickedToContinute_alpha = None

        #SETTINGS PREPARING:
        settings_BackBtn = button(150, 215, blankBtnImg, 8, ["center"], True, blankBtn_darkImg)
        settings_ThemeBtn = button(SCREEN_WIDTH / 2, 100, "img/LightThemeBtn.png", 10, ["center"], True, "img/NightThemeBtn.png")

        settings_VolumeBtn = button(SCREEN_WIDTH - 240, 100, "img/VolumeBtn.png", 10, ["center"])

        settings_MusicBoard = button(SCREEN_WIDTH / 2, 347, "img/Settings_MusicBoard.png", 13, ["center"], True, "img/MusicBoard_dark.png")
        settings_Music_ChangeLast = button(80, 347, "img/ArrowBtn2.png", 10, ["center"], True, "img/ArrowBtn2_dark.png")
        settings_Music_ChangeNext = button(SCREEN_WIDTH - 80, 347, "img/ArrowBtn2.png", 10, ["center"], True, "img/ArrowBtn2_dark.png")
        settings_Music_ChangeLast.rotate("horizontal")

        #Starting Pygame screen:
        screenFinalAction = None
        screenName = "mainMenu"
        BGType = "normal"
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
                    if startBtn.hovering(20, 22):
                        screenFinalAction = "mainScreen"
                    
                    optionsBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120)
                    optionsBtn.draw(screen, "Settings", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                    if optionsBtn.hovering(20, 22):
                        screenName = "mainMenu_settings"
                        BGType = "blur"

                    exitBtn.changeXY(SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT - 120)
                    exitBtn.draw(screen, "Exit", "Fonts\MinecraftBold.otf", 45, themeType, themeType)
                    if exitBtn.hovering(20, 22):
                        screenFinalAction = "exitProgram"
                    
                    #Draw a little credit text on the top right corner in the main menu
                    drawText(screen, "Made my Ky Anh and Thien Long", "Fonts\MinecraftBold.otf", 24, SCREEN_WIDTH - 15, 12, themeType, None, "right")
                
                if screenName == "mainMenu_settings":
                    drawText(screen, "| SETTINGS |", "Fonts\MinecraftBold.otf", 48, SCREEN_WIDTH / 2, 15, themeType, None, "center")
                    settings_BackBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
                    settings_BackBtn.draw(screen, "BACK", "Fonts\MinecraftBold.otf", 40, themeType, themeType)
                    
                    if settings_BackBtn.hovering(14, 16):
                        print("GOING BACK TO MAIN MENU SCREEN...")
                        screenName = "mainMenu"
                        BGType = "normal"
                    
                    #Draw theme setting:
                    drawText(screen, "Theme:", "Fonts\MinecraftBold.otf", 45, 64, 105, themeType)
                    settings_ThemeBtn.changeXY(290, 100)
                    settings_ThemeBtn.draw(screen, "", None, None, None, themeType)
                    
                    if settings_ThemeBtn.hovering(14, 16):
                        print("CHANGING THEME...")
                        if themeType == "light":
                            themeType = "dark"
                        else:
                            themeType = "light"

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

                    if settings_VolumeBtn.hovering(14, 16):
                        if pygame.mixer.music.get_volume() == 1.0:
                            pygame.mixer.music.set_volume(0.0)
                        elif pygame.mixer.music.get_volume() == 0.0:
                            pygame.mixer.music.set_volume(1.0)

                    #Draw audio setting:
                    drawText(screen, "Music:", "Fonts\MinecraftBold.otf", 45, 64, 224, themeType)
                    settings_MusicBoard.changeXY(SCREEN_WIDTH / 2, 300)
                    settings_MusicBoard.draw(screen, "", None, None, None, themeType)

                    drawText(screen, musicInfo["title"], "Fonts\MinecraftBold.otf", 35, SCREEN_WIDTH / 2, 320, themeType, None, "center")
                    drawText(screen, "Artist: " + musicInfo["artist"], "Fonts\MinecraftBold.otf", 35, SCREEN_WIDTH / 2, 374, themeType, None, "center")
                    settings_Music_ChangeLast.changeXY(SCREEN_WIDTH / 2 - 415, 322)
                    settings_Music_ChangeLast.draw(screen, "", None, None, None, themeType)
                    if settings_Music_ChangeLast.hovering(15, 17):
                        musicCurrent = musicList[musicList.index(musicCurrent) - 1]
                        print("Changing music...")
                    
                    settings_Music_ChangeNext.changeXY(SCREEN_WIDTH / 2 + 415, 322)
                    settings_Music_ChangeNext.draw(screen, "", None, None, None, themeType)
                    if settings_Music_ChangeNext.hovering(15, 17):
                        if musicList.index(musicCurrent) + 1 == len(musicList):
                            musicCurrent = musicList[0]
                        else:
                            musicCurrent = musicList[musicList.index(musicCurrent) + 1]
                        print("Changing music...")
                    

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
                    screenFinalAction = "exitProgram"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screenFinalAction = "exitProgram"
            
            if not screenFinalAction == None:
                break
            
            pygame.display.flip()
            pygame.display.update()
        
        CheckScreenFinalAction(screenFinalAction)
    
    def mainScreen():
        global screen
        global SCREEN_WIDTH
        global SCREEN_WIDTH_LAST
        global SCREEN_HEIGHT_LAST
        global SCREEN_HEIGHT

        global FPS
        global screenName
        global themeType
        global screenFinalAction

        global musicInfo
        global musicList
        global musicCurrent
        global musicLast

        #Load btn:
        #Setting up slider:
        xScroll = 0
        sliderBoard = button(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, "img/SliderBoard.png", 13, ["center"])
        sliderBtn = button(0, SCREEN_HEIGHT - 64, "img/SliderBtn.png", 10, ["center"])
        sliderBtn.setSlider(0, 100, 32, SCREEN_WIDTH - 32)

        #Setting up main menu buttons (buttons on the top of screen):
        menu_fileBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)
        menu_editBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)
        menu_settingsBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)

        #Setting up default template to-do list:
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        works = [["Learn Math", "Study English", "Coding StudoList project", "Learn coding"], ["Do house work", "Cook breakfast", "Learn to make music"], ["Coding StudoList project", "Learn Physics", "Learn English", "Doing art requests"], ["Learn to make game :)", "Learn Math", "Do homeworks", "Making game"], ["Exercising", "Do housework", "Clean the house", "Playing Piano"], ["Making script for game", "Coding StudoList project", "Making music", "Go play football"], ["Playing games", "Go play football", "Making musics", "Drawing arts for own and requests -_-"]]
        toDoLists = []
        for i in range(len(weekday)):
            k = toDoList(weekday[i], works[i], i + 1)
            toDoLists.append(k)

        #Starting Pygame screen:
        screenFinalAction = None
        screenName = "mainMenu"
        running = True
        while running:
            #Get events:
            events = pygame.event.get()

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
                BGImg = pygame.image.load("img/MainBG_dark.png")
            else:
                BGImg = pygame.image.load("img/MainBG.png")
            
            BGImg = pygame.transform.scale(BGImg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            screen.blit(BGImg, (0, 0))

            #Draw slider:
            sliderBoard.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 59)
            sliderBoard.changeSize(None, SCREEN_WIDTH - 64, sliderBoard.image.get_height())
            sliderBoard.draw(screen, "", None, None, None, themeType)
            if sliderBoard.clicked:
                sliderBtn.setSliderValue()

            sliderBtn.setSliderX(38, SCREEN_WIDTH - 38)
            sliderBtn.changeXY(sliderBtn.rect.x, SCREEN_HEIGHT - 68)
            sliderBtn.drawSlider(screen)

            #Draw menu buttons:
            drawRect(screen, 0, 0, SCREEN_WIDTH, 75, (205, 235, 243), 200)

            menu_fileBtn.changeXY(95, 14)
            menu_fileBtn.draw(screen, "File", "Fonts/MinecraftBold.otf", 24, "black")
            if menu_fileBtn.hovering(10,11):
                pass
            menu_editBtn.changeXY(250, 14)
            menu_editBtn.draw(screen, "Edit", "Fonts/MinecraftBold.otf", 24, "black")
            if menu_editBtn.hovering(10,11):
                pass
            menu_settingsBtn.changeXY(405, 14)
            menu_settingsBtn.draw(screen, "Settings", "Fonts/MinecraftBold.otf", 24, "black")
            if menu_settingsBtn.hovering(10,11):
                pass

            #Draw To-do lists:
            for i in toDoLists:
                if i.drawList(screen, events, sliderBtn.slider_value, len(toDoLists)) == "createNewColumn":
                    toDoLists.append(toDoList("united list", ["United work"], len(toDoLists) + 1))

            
            for event in events:
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
                    screenFinalAction = "exitProgram"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screenFinalAction = "exitProgram"
                        
            if not screenFinalAction == None:
                break
            
            pygame.display.flip()
            pygame.display.update()

        CheckScreenFinalAction(screenFinalAction)

    
    #Def to check screen final action to change to new screen
    def CheckScreenFinalAction(action):
        if action == "mainMenu":
            print("|| MAIN MENU... ||")
            mainMenu()
        elif action == "mainScreen":
            print("|| MAIN SCREEN... ||")
            mainScreen()
        elif action == "exitProgram":
            print("|| PROJECT QUITTING... ||")
            pygame.quit()
    
    #Load fonts:


    #Load image assets:
    blankBtnImg = "img/blankBtn.png"
    blankBtn_darkImg = "img/blankBtn_dark.png"
    arrowBtnImg = "img/ArrowBtn.png"
    arrowBtnImg_dark = "img/ArrowBtn_dark.png"

    #Load project default varibles:
    SCREEN_WIDTH = 1050 #Screen width size.
    SCREEN_HEIGHT = 600 #Screen height size.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) #Set Pygame screen.
    pygame.display.set_caption("StudoList | Made by Staregos") #Set Pygame screen caption.
    icon = pygame.image.load("icon.png") #Load Pygame screen icon image.
    pygame.display.set_icon(icon) #Set Pygame screen icon.


    #Initzile:
    pygame.init()
    SCREEN_WIDTH = 1050
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH_LAST = SCREEN_WIDTH
    SCREEN_HEIGHT_LAST = SCREEN_HEIGHT
    screenName = "mainMenu"
    themeType = "light"
    FPS = 60

    #Starting main menu of program:
    musicList = os.listdir("./Musics")
    musicCurrent = musicList[5]
    musicLast = musicCurrent
    musicInfo = getAudioInfo(f"Musics/{musicCurrent}")
    playMusic(f"Musics/{musicCurrent}")
    pygame.mixer.music.set_volume(1.0)

    screenFinalAction = "mainMenu"
    CheckScreenFinalAction(screenFinalAction)