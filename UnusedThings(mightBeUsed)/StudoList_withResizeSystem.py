from tkinter.tix import WINDOW


pixelFont = "Fonts/PixelFontVietHoa.otf"


#Some defs for shorting the code in many screens, loops:
def settingsMenuTick(backScreenName):
    global screenName, BGType, themeType, musicCurrent

    drawText(display, "| SETTINGS |", pixelFont, 48, SCREEN_WIDTH / 2, 10, themeType, None, "center")
    settings_BackBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 88)
    settings_BackBtn.draw(display, "BACK", pixelFont, 40, themeType, themeType)

    if settings_BackBtn.hovering(70, 80):
        print("GOING BACK TO MAIN MENU SCREEN...")
        BGType = "normal"
        screenName = backScreenName

    #Draw theme setting:
    drawText(display, "Theme:", pixelFont, 45, 64, 90, themeType)
    settings_ThemeBtn.changeXY(290, 85)
    settings_ThemeBtn.draw(display, "", None, None, None, themeType)

    if settings_ThemeBtn.hovering(70, 80):
        print("CHANGING THEME...")
        if themeType == "light":
            themeType = "dark"
        else:
            themeType = "light"

    #Draw volume setting:
    drawText(display, "Volume:", pixelFont, 45, SCREEN_WIDTH - 250, 90, themeType, 255, "right")
    settings_VolumeBtn.changeXY(SCREEN_WIDTH - 200, 85)
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
    settings_VolumeBtn.draw(display)

    if settings_VolumeBtn.hovering(70, 80):
        if pygame.mixer.music.get_volume() == 1.0:
            pygame.mixer.music.set_volume(0.0)
        elif pygame.mixer.music.get_volume() == 0.0:
            pygame.mixer.music.set_volume(1.0)

    #Draw audio setting:
    drawText(display, "Music:", pixelFont, 45, 64, 174, themeType)
    settings_MusicBoard.changeXY(SCREEN_WIDTH / 2, 242)
    settings_MusicBoard.draw(display, "", None, None, None, themeType)

    drawText(display, musicInfo["title"], pixelFont, 35, SCREEN_WIDTH / 2, 262, themeType, None, "center")
    drawText(display, "Artist: " + musicInfo["artist"], pixelFont, 35, SCREEN_WIDTH / 2, 316, themeType, None, "center")
    settings_Music_ChangePrevious.changeXY(SCREEN_WIDTH / 2 - 415, 270)
    settings_Music_ChangePrevious.draw(display, "", None, None, None, themeType)
    if settings_Music_ChangePrevious.hovering(75, 85):
        musicCurrent = musicList[musicList.index(musicCurrent) - 1]
        print("Changing music...")

    settings_Music_ChangeNext.changeXY(SCREEN_WIDTH / 2 + 415, 270)
    settings_Music_ChangeNext.draw(display, "", None, None, None, themeType)
    if settings_Music_ChangeNext.hovering(75, 85):
        if musicList.index(musicCurrent) + 1 == len(musicList):
            musicCurrent = musicList[0]
        else:
            musicCurrent = musicList[musicList.index(musicCurrent) + 1]
        print("Changing music...")
    
    #Draw languages settings:
    drawText(display, "Languages:", pixelFont, 45, 64, 390, themeType)
    settings_LanguagesBoard.changeXY(SCREEN_WIDTH / 2, 442)
    settings_LanguagesBoard.draw(display, "", None, None, None, themeType)


#To the main code!
if __name__ == "__main__":
    #Importing Moudles and Python files:
    import os #For searching file in the folder and for system things. (System minor things)
    import pygame #For like all main stuffs to renders and creates the display display. (IMPORTANT)
    import csv #For saving & loading .csv files. (Saving system)
    from ProjectDefs import * #Just for making code faster with all useful Pygame defs that I made. (Useful defs)

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
        global display
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

        #Importing settings display:
        global settings_BackBtn
        global settings_ThemeBtn

        global settings_VolumeBtn

        global settings_MusicBoard

        global settings_Music_ChangePrevious
        global settings_Music_ChangeNext

        #Load btn:
        PJTitle = button(SCREEN_WIDTH / 2, 100, "img/PJTitleButCooler.png", 90, ["center"])
        PJMinorTitle = button(SCREEN_WIDTH / 2, 180, "img/PJMinorTitle.png", 20, ["center"])
        PJTitle.touchable, PJMinorTitle.touchable = False, False

        startBtn = button(SCREEN_WIDTH / 2, 185, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        optionsBtn = button(SCREEN_WIDTH / 2, 300, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        exitBtn = button(SCREEN_WIDTH / 2, 415, blankBtnImg, 20, ["center"], True, blankBtn_darkImg)
        isClickedToContinute = False
        flashingText = pygame.USEREVENT + 1
        mainMenuStart= False
        countFlashingText = 0
        clickedToContinute_alpha = None

        #Starting Pygame display:
        screenFinalAction = None
        screenName = "mainMenu"
        BGType = "normal"
        running = True
        while running:
            #Fill all the screen with black color:
            screen.fill("black")
            display.fill("black")

            #Music system:
            if not musicCurrent == musicLast:
                playMusic(f"Musics/{musicCurrent}")
                musicInfo = getAudioInfo(f"Musics/{musicCurrent}")
                musicLast = musicCurrent

            #Get width, height display:
            #print(SCREEN_WIDTH, SCREEN_HEIGHT)

            #Draw Background:
            if themeType == "dark":
                if BGType == "normal":
                    BGImg = pygame.image.load("img/MainBG_dark.png").convert_alpha()
                elif BGType == "blur":
                    BGImg = pygame.image.load("img/MainBG_dark_Blur.png").convert_alpha()
                #elif BGType == "noText":
                #    BGImg = pygame.image.load("img/MainBG_NoText_dark.png").convert_alpha()
            else:
                if BGType == "normal":
                    BGImg = pygame.image.load("img/MainBG.png").convert_alpha()
                elif BGType == "blur":
                    BGImg = pygame.image.load("img/MainBG_Blur.png").convert_alpha()
                #elif BGType == "noText":
                #    BGImg = pygame.image.load("img/MainBG_NoText.png").convert_alpha()
            
            BGImg = pygame.transform.scale(BGImg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            display.blit(BGImg, (0, 0))

            #Draw things:
            if screenName == "mainMenu":
                PJTitle.changeSize(round(SCREEN_HEIGHT / 6.7))
                PJTitle.changeXY(SCREEN_WIDTH / 2, 224)
                PJTitle.draw(display, "", "", "", "")

                PJMinorTitle.changeSize(round(SCREEN_HEIGHT / 64))
                PJMinorTitle.changeXY(SCREEN_WIDTH / 2, 320)
                PJMinorTitle.draw(display, "", "", "", "")

                #print(PJTitle.rect)
                PJTitle.rect.topleft = (0, 0)
            
            if mainMenuStart == False:
                drawText(display, "Click any button to start program", pixelFont, 32, SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100, themeType, clickedToContinute_alpha,"center")
                if pygame.mouse.get_pressed()[0] == 1 and isClickedToContinute == False:
                    pygame.time.set_timer(flashingText, 200, 5)
                    isClickedToContinute = True
            if mainMenuStart:
                if screenName == "mainMenu":
                    BGType = "normal"
                    startBtn.changeXY(SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT - 120)
                    startBtn.draw(display, "Start", pixelFont, 45, themeType, themeType)
                    if startBtn.hovering(100, 108):
                        screenFinalAction = "mainScreen"
                    
                    optionsBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120)
                    optionsBtn.draw(display, "Settings", pixelFont, 45, themeType, themeType)
                    if optionsBtn.hovering(100, 108):
                        print("CHANING TO SETTINGS SCREEN...")
                        screenName = "mainMenu_settings"
                        BGType = "blur"

                    exitBtn.changeXY(SCREEN_WIDTH / 2 + 300, SCREEN_HEIGHT - 120)
                    exitBtn.draw(display, "Exit", pixelFont, 45, themeType, themeType)
                    if exitBtn.hovering(100, 108):
                        screenFinalAction = "exitProgram"
                    
                    #Draw a little credit text on the top right corner in the main menu
                    drawText(display, "Made by Staregos Team", pixelFont, 24, SCREEN_WIDTH - 15, 12, themeType, None, "right")
                
                if screenName == "mainMenu_settings":
                    settingsMenuTick("mainMenu")

            for event in pygame.event.get():
                if event.type == flashingText:
                    if clickedToContinute_alpha == None:
                        clickedToContinute_alpha = 0
                    else:
                        clickedToContinute_alpha = None
                    countFlashingText += 1
                    if countFlashingText >= 5:
                        mainMenuStart = True
                
                #Get another value of display width, display height and check if the display size is different, so that the display changes into BG size.
                #if event.type == pygame.VIDEORESIZE:
                #    SCREEN_WIDTH_LAST, SCREEN_HEIGHT_LAST = pygame.display.get_surface().get_size()
                #    if SCREEN_WIDTH != SCREEN_WIDTH_LAST:
                #        display = pygame.display.set_mode((event.size[0], event.size[0] / 1.75), pygame.RESIZABLE)
                #        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                #        print(event.size)
                #    elif SCREEN_HEIGHT != SCREEN_HEIGHT_LAST:
                #        display = pygame.display.set_mode((event.size[1] * 1.75, event.size[1]), pygame.RESIZABLE)
                #        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                #        print(event.size)
                #    
                #    if SCREEN_HEIGHT < 510 or SCREEN_WIDTH < 892.5:
                #        display = pygame.display.set_mode((510 * 1.75, 510), pygame.RESIZABLE)
                #        print(event.size)

                
                if event.type == pygame.QUIT:
                    screenFinalAction = "exitProgram"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screenFinalAction = "exitProgram"
            
            WINDOW_SIZE = pygame.display.get_surface().get_size()
            WINDOW_SIZE_PERCENT = WINDOW_SIZE[0] / WINDOW_SIZE[1]
            print(f"""ORIGINAL: {SCREEN_SIZE_PERCENT},
NOW: {WINDOW_SIZE_PERCENT}""")

            WINDOW_SIZE_LISTED = list(WINDOW_SIZE)

            if WINDOW_SIZE_PERCENT > SCREEN_SIZE_PERCENT:
                print("Width is wider")
                WINDOW_SIZE_LISTED[0] = WINDOW_SIZE[1] * SCREEN_SIZE_PERCENT
            if WINDOW_SIZE_PERCENT < SCREEN_SIZE_PERCENT:
                print("Height is higher")
                WINDOW_SIZE_LISTED[1] = WINDOW_SIZE[0] / SCREEN_SIZE_PERCENT

            print(f"SizePercentAfter: {WINDOW_SIZE_LISTED[0] / WINDOW_SIZE_LISTED[1]}, SIZE: {WINDOW_SIZE_LISTED}")

            surface = pygame.transform.scale(display, WINDOW_SIZE_LISTED)
            surfaceXY = [(WINDOW_SIZE[0] / 2) - (WINDOW_SIZE_LISTED[0] / 2), (WINDOW_SIZE[1] / 2) - (WINDOW_SIZE_LISTED[1] / 2)]
            screen.blit(surface, surfaceXY)
            
            if not screenFinalAction == None:
                break
            
            pygame.display.flip()
            pygame.display.update()
    
    def mainScreen():
        global display
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
        sliderBoard = button(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, "img/SliderBoard.png", 65, ["center"])
        sliderBoard.brightnessTouch = False
        sliderBtn = button(0, SCREEN_HEIGHT - 64, "img/SliderBtn.png", 50, ["center"])
        sliderBtn.setSlider(0, 100, 32, SCREEN_WIDTH - 32)

        #Setting up main menu buttons (buttons on the top of display):
        menu_fileBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)
        menu_fileBtn_board = button(95, 14, "img/FileMenuBoard.png", 50, ["center"], False)
        menu_fileBtn_board.brightnessTouch = False
        menu_fileBtn_newBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_openBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_saveAsBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_exitBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)

        menu_editBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)


        menu_settingsBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)


        menuOpening = None

        #Setting up default template to-do list:
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        toDoLists = []
        for i in range(len(weekday)):
            k = toDoList(weekday[i], ["none"], i + 1)
            toDoLists.append(k)

        #Starting Pygame display:
        BGType = "normal"
        screenFinalAction = None
        screenName = "mainScreen"
        running = True
        while running:
            #Get events:
            events = pygame.event.get()

            #Music system:
            if not musicCurrent == musicLast:
                playMusic(f"Musics/{musicCurrent}")
                musicInfo = getAudioInfo(f"Musics/{musicCurrent}")
                musicLast = musicCurrent

            #Get width, height display:
            SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
            #print(SCREEN_WIDTH, SCREEN_HEIGHT)

            #Draw Background:
            if themeType == "dark":
                if BGType == "normal":
                    BGImg = pygame.image.load("img/MainBG_dark.png").convert_alpha()
                elif BGType == "blur":
                    BGImg = pygame.image.load("img/MainBG_dark_Blur.png").convert_alpha()
                #elif BGType == "noText":
                #    BGImg = pygame.image.load("img/MainBG_NoText_dark.png").convert_alpha()
            else:
                if BGType == "normal":
                    BGImg = pygame.image.load("img/MainBG.png").convert_alpha()
                elif BGType == "blur":
                    BGImg = pygame.image.load("img/MainBG_Blur.png").convert_alpha()
                #elif BGType == "noText":
                #    BGImg = pygame.image.load("img/MainBG_NoText.png").convert_alpha()
            
            BGImg = pygame.transform.scale(BGImg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            display.blit(BGImg, (0, 0))

            if screenName == "mainScreen":
                BGType = "normal"
                #Draw slider:
                sliderBoard.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 59)
                sliderBoard.changeSize(None, SCREEN_WIDTH - 64, sliderBoard.image.get_height())
                sliderBoard.draw(display, "", None, None, None, themeType)
                if sliderBoard.clicked:
                    sliderBtn.setSliderValue()

                sliderBtn.setSliderX(38, SCREEN_WIDTH - 38)
                sliderBtn.changeXY(sliderBtn.rect.x, SCREEN_HEIGHT - 68)
                sliderBtn.drawSlider(display)
                #Printing sliderBtmn values for testing errors
                #print(sliderBtn.slider_value)
                #print(pygame.mouse.get_pos()[0])
                #print(f"SliderBtnX: {sliderBtn.rect.x + sliderBtn.image.get_width() / 2}")
                #Draw menu buttons:
                drawRect(display, 0, 0, SCREEN_WIDTH, 75, (205, 235, 243), 200)

                menu_fileBtn.changeXY(80, 6)
                menu_fileBtn.draw(display, "File", pixelFont, 24, "black")
                if menu_fileBtn.hovering(50,56):
                    if menuOpening == "file":
                        menuOpening = None
                    else:
                        menuOpening = "file"

                menu_editBtn.changeXY(224, 6)
                menu_editBtn.draw(display, "Edit", pixelFont, 24, "black")
                if menu_editBtn.hovering(50,56):
                    if menuOpening == "edit":
                        menuOpening = None
                    else:
                        menuOpening = "edit"
                

                menu_settingsBtn.changeXY(368, 6)
                menu_settingsBtn.draw(display, "Settings", pixelFont, 24, "black")
                if menu_settingsBtn.hovering(50,56):
                    screenName = "settingsMenu"
                    BGType = "blur"

                #Draw To-do lists:
                for i in toDoLists:
                    toDoListReturnValue = i.drawList(display, events, sliderBtn.slider_value, len(toDoLists))
                    if not toDoListReturnValue == None and "createNewColumn" in toDoListReturnValue:
                        toDoLists.append(toDoList("united list", ["United work"], len(toDoLists) + 1))
                
                #Draw the opening menu (The code should on the bottom so that it will be draw after and in front of other things):
                if not menuOpening == None:
                    if menuOpening == "file":
                        menu_fileBtn_board.changeXY(176, 50)
                        menu_fileBtn_board.draw(display)

                        menu_fileBtn_newBtn.changeXY(176, 70)
                        menu_fileBtn_newBtn.draw(display, "New", pixelFont, 24, "black", None, "left", (60, 0))
                        if menu_fileBtn_newBtn.action:
                            screenFinalAction = "mainScreen"
                        
                        menu_fileBtn_openBtn.changeXY(176, 70 + (40 * 1))
                        menu_fileBtn_openBtn.draw(display, "Open", pixelFont, 24, "black", None, "left", (60, 0))
                        if menu_fileBtn_openBtn.action:
                            toDoLists = openFile()
                        
                        menu_fileBtn_saveAsBtn.changeXY(176, 70 + (40 * 2))
                        menu_fileBtn_saveAsBtn.draw(display, "Save As", pixelFont, 24, "black", None, "left", (60, 0))
                        if menu_fileBtn_saveAsBtn.action:
                            saveFile(toDoLists)

                        menu_fileBtn_exitBtn.changeXY(176, 70 + (40 * 3))
                        menu_fileBtn_exitBtn.draw(display, "Exit", pixelFont, 24, "black", None, "left", (60, 0))
                        if menu_fileBtn_exitBtn.action:
                            screenFinalAction = "exitProgram"
                    
                #Checking that is the top menu is clicked ouside the opening menu so that the opening menu closes:
                if menu_fileBtn.clickedOutside and menu_fileBtn_board.clickedOutside:
                    menuOpening = None
            
            
            
            if screenName == "settingsMenu":
                settingsMenuTick("mainScreen")


            for event in events:
                #Get another value of display width, display height and check if the display size is different, so that the display changes into BG size.
                if event.type == pygame.VIDEORESIZE:
                    SCREEN_WIDTH_LAST, SCREEN_HEIGHT_LAST = pygame.display.get_surface().get_size()
                    if SCREEN_WIDTH != SCREEN_WIDTH_LAST:
                        display = pygame.display.set_mode((event.size[0], event.size[0] / 1.75), pygame.RESIZABLE)
                        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                        print(event.size)
                    elif SCREEN_HEIGHT != SCREEN_HEIGHT_LAST:
                        display = pygame.display.set_mode((event.size[1] * 1.75, event.size[1]), pygame.RESIZABLE)
                        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
                        print(event.size)
                    
                    if SCREEN_HEIGHT < 510 or SCREEN_WIDTH < 892.5:
                        display = pygame.display.set_mode((510 * 1.75, 510), pygame.RESIZABLE)
                        print(event.size)
                if event.type == pygame.QUIT:
                    screenFinalAction = "exitProgram"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        screenFinalAction = "exitProgram"
                        
            if not screenFinalAction == None:
                break
            
            pygame.display.flip() # Flip the display...??
            pygame.display.update() # Updating the display.


    
    #Def to check display final action to change to new display
    def CheckScreenFinalAction():
        global screenFinalAction
        if screenFinalAction == "mainMenu":
            print("|| MAIN MENU... ||")
            mainMenu()
        elif screenFinalAction == "mainScreen":
            print("|| MAIN SCREEN... ||")
            mainScreen()
        elif screenFinalAction == "exitProgram":
            print("|| PROJECT QUITTING... ||")
            pygame.quit()
            return False
        
        CheckScreenFinalAction()
    
    #Load fonts:


    #Load image assets:
    blankBtnImg = "img/blankBtn.png"
    blankBtn_darkImg = "img/blankBtn_dark.png"
    arrowBtnImg = "img/ArrowBtn.png"
    arrowBtnImg_dark = "img/ArrowBtn_dark.png"


    #Load project default varibles:
    SCREEN_WIDTH = 1050 #Screen width size.
    SCREEN_HEIGHT = 600 #Screen height size.
    SCREEN_SIZE_PERCENT = SCREEN_WIDTH / SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE, 32) #Set Pygame display.
    display = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("StudoList | Made by Staregos") #Set Pygame display caption.
    icon = pygame.image.load("icon.png").convert_alpha() #Load Pygame display icon image.
    pygame.display.set_icon(icon) #Set Pygame display icon.


    #Initzile:
    pygame.mixer.pre_init(44100, 16, 2, 4096) #Initzile Pygame.mixer to get the mixer runs faster.
    pygame.init() # Initzile Pygame.
    SCREEN_WIDTH = 1050 #Varible for the display width.
    SCREEN_HEIGHT = 600 # Varible for the display height.
    SCREEN_WIDTH_LAST = SCREEN_WIDTH # Varible for checking the difference between screen_width and screen_width last.
    SCREEN_HEIGHT_LAST = SCREEN_HEIGHT # Varible for checking the difference between screen_height and screen_height last.
    screenName = "mainMenu" # Set up screenName for the main menu scene.
    themeType = "light" # Set up theme for the display ("light" is default).
    FPS = 60 # Set up FPS (60 is default).


    #LOADING OBJECTS FOR MANY SCREENS:
    #SETTINGS PREPARING:
    settings_BackBtn = button(150, 215, blankBtnImg, 8, ["center"], True, blankBtn_darkImg)
    settings_ThemeBtn = button(SCREEN_WIDTH / 2, 100, "img/LightThemeBtn.png", 10, ["center"], True, "img/NightThemeBtn.png")

    settings_VolumeBtn = button(SCREEN_WIDTH - 240, 100, "img/VolumeBtn.png", 10, ["center"])

    settings_MusicBoard = button(SCREEN_WIDTH / 2, 347, "img/Settings_MusicBoard.png", 65, ["center"], True, "img/MusicBoard_dark.png")
    settings_MusicBoard.touchable = False
    
    settings_Music_ChangePrevious = button(80, 347, "img/ArrowBtn.png", 10, ["center"], True, "img/ArrowBtn_dark.png")
    settings_Music_ChangeNext = button(SCREEN_WIDTH - 80, 347, "img/ArrowBtn.png", 10, ["center"], True, "img/ArrowBtn_dark.png")
    settings_Music_ChangePrevious.rotate("horizontal")

    settings_LanguagesBoard = button(SCREEN_WIDTH / 2, 547, "img/LanguagesBoard.png", 65, ["center"], True, "img/LanguagesBoard.png")
    settings_LanguagesBoard.touchable = False

    settings_Languages_ChangePrevious = button(80, 547, "img/ArrowBtn.png", 10, ["center"], True, "img/ArrowBtn_dark.png")
    settings_Languages_ChangeNext = button(SCREEN_WIDTH - 80, 547, "img/ArrowBtn.png", 10, ["center"], True, "img/ArrowBtn_dark.png")
    settings_Languages_ChangePrevious.rotate("horizontal")


    #Starting main menu of program:
    # Setting up the music list in folder Musics:
    musicList = os.listdir("./Musics") # Get list of music file names in folder Musics.
    musicCurrent = musicList[5] # Set up default starting music for the program.
    musicLast = musicCurrent # Set up music last.
    musicInfo = getAudioInfo(f"Musics/{musicCurrent}") # Get default starting music info.
    playMusic(f"Musics/{musicCurrent}") # Play default starting music to the program when first run.
    pygame.mixer.music.set_volume(1.0) # Set up volume (1.0 is default, 1.0 is full volume).

    screenFinalAction = "mainMenu" # Important varible to set up the whole Main menu display at the start of the program.
    CheckScreenFinalAction() # Running the whole main menu display with value "mainMenu".