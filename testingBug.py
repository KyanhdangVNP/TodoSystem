pixelFont = "Fonts/PixelFontVietHoa.otf"

if __name__ == "__main__":
    #Importing Moudles and Python files:
    import os #For searching file in the folder and for system things. (System minor things)
    import pygame #For like all main stuffs to renders and creates the display screen. (IMPORTANT)
    import csv #For saving & loading .csv files. (Saving system)
    from UsefulPygameDef_copy import * #Just for making code faster with all useful Pygame defs that I made. (Useful defs)

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
        #menu_fileBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)
        optionsBtn = button(SCREEN_WIDTH / 2, 300, blankBtnImg, 100, ["center"], False)

        #Starting Pygame screen:
        clock = pygame.time.Clock()
        screenFinalAction = None
        screenName = "mainMenu"
        BGType = "normal"
        running = True
        while running:
            
            SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

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
            screen.blit(BGImg, (0, 0))
            optionsBtn.changeXY(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 120)
            optionsBtn.draw(screen, "Settings", pixelFont, 45, themeType, themeType)
            if optionsBtn.action:
                screenName = "mainMenu_settings"
                BGType = "blur"
                    

            for event in pygame.event.get():
                
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
            
            clock.tick(30)
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
        sliderBoard = button(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, "img/SliderBoard.png", 65, ["center"])
        sliderBoard.touchable = False
        sliderBtn = button(0, SCREEN_HEIGHT - 64, "img/SliderBtn.png", 50, ["center"])
        sliderBtn.setSlider(0, 100, 32, SCREEN_WIDTH - 32)

        #Setting up main menu buttons (buttons on the top of screen):
        menu_fileBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)
        menu_fileBtn_board = button(95, 14, "img/FileMenuBoard.png", 50, ["center"], False)
        menu_fileBtn_board.brightnessTouch = False
        menu_fileBtn_newBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_openBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_saveAsBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_exitBtn = button(95, 14, "img/FileMenu_BtnBoard.png", 50, ["center"], False)
        menu_fileBtn_newBtn.test = "newBtn"

        menu_editBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)


        menu_settingsBtn = button(24, 24, blankBtnImg, 13, ["center"], True, blankBtn_darkImg)


        menuOpening = None

        #Setting up default template to-do list:
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        toDoLists = []
        for i in range(len(weekday)):
            k = toDoList(weekday[i], ["none"], i + 1)
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
                BGImg = pygame.image.load("img/MainBG_dark.png").convert_alpha()
            else:
                BGImg = pygame.image.load("img/MainBG.png").convert_alpha()
            
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
            #Printing sliderBtmn values for testing errors
            #print(sliderBtn.slider_value)
            #print(pygame.mouse.get_pos()[0])
            #print(f"SliderBtnX: {sliderBtn.rect.x + sliderBtn.image.get_width() / 2}")
            #Draw menu buttons:
            drawRect(screen, 0, 0, SCREEN_WIDTH, 75, (205, 235, 243), 200)

            menu_fileBtn.changeXY(80, 6)
            menu_fileBtn.draw(screen, "File", pixelFont, 24, "black")
            if menu_fileBtn.action:
                if menuOpening == "file":
                    menuOpening = None
                else:
                    menuOpening = "file"

            menu_editBtn.changeXY(224, 6)
            menu_editBtn.draw(screen, "Edit", pixelFont, 24, "black")
            if menu_editBtn.hovering(50,56):
                if menuOpening == "edit":
                    menuOpening = None
                else:
                    menuOpening = "edit"
            

            menu_settingsBtn.changeXY(368, 6)
            menu_settingsBtn.draw(screen, "Settings", pixelFont, 24, "black")
            if menu_settingsBtn.hovering(50,56):
                if menuOpening == "settings":
                    menuOpening = None
                else:
                    menuOpening = "settings"

            #Draw To-do lists:
            for i in toDoLists:
                if i.drawList(screen, events, sliderBtn.slider_value, len(toDoLists)) == "createNewColumn":
                    toDoLists.append(toDoList("united list", ["United work"], len(toDoLists) + 1))
            
            #Checking that is the top menu is clicked ouside the opening menu so that the opening menu closes:
            if menu_fileBtn.clickedOutside and menu_fileBtn_board.clickedOutside:
                menuOpening = None
            
            #Draw the opening menu (The code should on the bottom so that it will be draw after and in front of other things):
            if not menuOpening == None:
                if menuOpening == "file":
                    menu_fileBtn_board.changeXY(176, 50)
                    menu_fileBtn_board.draw(screen)

                    menu_fileBtn_newBtn.changeXY(176, 70)
                    menu_fileBtn_newBtn.draw(screen)
                    #if menu_fileBtn_newBtn.action:
                    #    screenFinalAction = "mainScreen"
                    
                    menu_fileBtn_openBtn.changeXY(176, 70 + (40 * 1))
                    menu_fileBtn_openBtn.draw(screen, "Open", pixelFont, 24, "black", None, "left", (60, 0))
                    if menu_fileBtn_openBtn.action:
                        openFile()
                    
                    menu_fileBtn_saveAsBtn.changeXY(176, 70 + (40 * 2))
                    menu_fileBtn_saveAsBtn.draw(screen, "Save As", pixelFont, 24, "black", None, "left", (60, 0))
                    if menu_fileBtn_saveAsBtn.action:
                        pass

                    menu_fileBtn_exitBtn.changeXY(176, 70 + (40 * 3))
                    menu_fileBtn_exitBtn.draw(screen, "Exit", pixelFont, 24, "black", None, "left", (60, 0))
                    if menu_fileBtn_exitBtn.action:
                        screenFinalAction = "mainMenu"


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
            
            pygame.display.flip() # Flip the screen...??
            pygame.display.update() # Updating the screen.

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
    icon = pygame.image.load("icon.png").convert_alpha() #Load Pygame screen icon image.
    pygame.display.set_icon(icon) #Set Pygame screen icon.


    #Initzile:
    pygame.mixer.pre_init(44100, 16, 2, 4096) #Initzile Pygame.mixer to get the mixer runs faster.
    pygame.init() # Initzile Pygame.
    SCREEN_WIDTH = 1050 #Varible for the screen width.
    SCREEN_HEIGHT = 600 # Varible for the screen height.
    SCREEN_WIDTH_LAST = SCREEN_WIDTH # Varible for checking the difference between screen_width and screen_width last.
    SCREEN_HEIGHT_LAST = SCREEN_HEIGHT # Varible for checking the difference between screen_height and screen_height last.
    screenName = "mainMenu" # Set up screenName for the main menu scene.
    themeType = "light" # Set up theme for the screen ("light" is default).
    FPS = 60 # Set up FPS (60 is default).

    #Starting main menu of program:
    # Setting up the music list in folder Musics:
    musicList = os.listdir("./Musics") # Get list of music file names in folder Musics.
    musicCurrent = musicList[5] # Set up default starting music for the program.
    musicLast = musicCurrent # Set up music last.
    musicInfo = getAudioInfo(f"Musics/{musicCurrent}") # Get default starting music info.
    playMusic(f"Musics/{musicCurrent}") # Play default starting music to the program when first run.
    pygame.mixer.music.set_volume(1.0) # Set up volume (1.0 is default, 1.0 is full volume).

    screenFinalAction = "mainMenu" # Important varible to set up the whole Main menu screen at the start of the program.
    CheckScreenFinalAction(screenFinalAction) # Running the whole main menu screen with value "mainMenu".