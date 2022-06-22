import os
import eyed3
import pygame

#|  PYGAME FUNCTIONS |

#Def Draw text:
def drawText(screen, text = "", fontName = "Fonts/MinecraftRegular.otf", size=24, x = 0, y = 0, color = "black", alpha = 255, alignX = "left", alignY = "center"):
    if color == "light":
        color = "black"
    elif color == "dark":
        color = "light gray"
    
    if alpha == None:
        alpha = 255
    #Tạo ra font, chữ:
    font = pygame.font.Font(fontName, size)
    
    #Tìm ra giá trị x và y của text chuẩn bị vẽ:
    lines = text.splitlines()
    max_length = 0
    
    for line in lines:
        if(len(line) > max_length):
            max_length = len(line)
            max_len_line = line
    xIndex = lines.index(max_len_line)
    textPrint = font.render(lines[xIndex], 1, (255,255,255))

    yPrintText = y
    if alignY == "center":
        yPrintText -= textPrint.get_height()
    
    #Vẽ chữ lên màn hình:
    for i, l in enumerate(lines):
        word = font.render(l, 0, color)
        word.set_alpha(alpha)
        xPrintText = x
        if alignX == "right":
            xPrintText -= word.get_width()
        elif alignX == "center":
            xPrintText -= (word.get_width() / 2)
        screen.blit(word, (xPrintText, (yPrintText + size*i)))

#Class Button, tạo ra nút có thể nhấn được:
class button():
    def __init__(self, x, y, imagePath, sizePercent, alignRect, themeChanging = False, imagePath_dark = None):
        if imagePath == None:
            self.image = None
            self.originalImg = None
            width = 0 
            height = 0

            self.rect = pygame.Rect((0, 0), (0, 0))
            self.rect.topleft = (x, y)
        else:
            self.themeChanging = themeChanging
            if themeChanging == True:
                self.image_dark = pygame.image.load(imagePath_dark).convert_alpha()
            
            self.originalImg = pygame.image.load(imagePath).convert_alpha()
            self.angle = 0
            self.image_light = self.originalImg
            width = self.originalImg.get_width() 
            height = self.originalImg.get_height()
            self.image = pygame.transform.scale(self.originalImg, (int(width * sizePercent / 100), int(height * sizePercent / 100)))
            self.alpha = 255

            self.sizePercent = sizePercent
            self.sizeX = width
            self.sizeY = height
            self.rect =self.image.get_rect()
            self.rect.topleft = (x, y)
        self.alignRectX = alignRect
    
        self.clicked = False
        self.waitClicked = False

    def draw(self, screen, text = "", fontName = "Fonts/MinecraftRegular.otf", size = 24, color = "black", themeType = None):
        #Set color (changing image of button) depends on theme right now
        if not self.themeChanging == False:
            if themeType == "light":
                self.changeImg(self.image_light, self.sizePercent, self.rect.x, self.rect.y)
            elif themeType == "dark":
                self.changeImg(self.image_dark, self.sizePercent, self.rect.x, self.rect.y)
        
        #Set text in button depends on the theme right now
        if color == "light":
            color = "black"
        elif color == "dark":
            color = "light gray"
        
        self.isColliding = False
        self.action = False

        #print(f"""self.rect.x BEFORE: {self.rect.x}
#self.rect BEFORE: {self.rect}
#self.alignRectX BEFORE: {self.alignRectX}""")

        if self.alignRectX == "center":
            self.rect.x -= self.image.get_width() / 2
        elif self.alignRectX == "right":
            self.rect.x -= self.image.get_width
        
        #print(f"""self.rect.x: {self.rect.x}
#self.rect: {self.rect}
#self.alignRectX: {self.alignRectX}""")
        
        #Lấy vị trí của chuột trên màn hình:
        pos = pygame.mouse.get_pos()
        
        #Kiểm tra vị trí của chuột có chạm vào nút không:
        if self.rect.collidepoint(pos):
            self.isColliding = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                if self.waitClicked == False:
                    self.waitClicked = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            if self.waitClicked == True:
                self.waitClicked = False
                self.action = True
            self.clicked = False

        #Vẽ nút bấm lên màn hình:
        if not self.image == None:
            self.image.set_alpha(self.alpha)
            screen.blit(self.image, (self.rect.x, self.rect.y))
            #self.rect = self.image.get_rect()
        
        #Vẽ chữ lên màn hình:
        if not text == '':
            self.text = text
            
            #Tạo ra font, chữ:
            font = pygame.font.Font(fontName, size)
            
            #Tìm ra giá trị x và y của text chuẩn bị vẽ:
            lines = text.splitlines()
            max_length = 0
            
            for line in lines:
                if(len(line) > max_length):
                    max_length = len(line)
                    max_len_line = line
            xIndex = lines.index(max_len_line)
            textPrint = font.render(lines[xIndex], 1, (255,255,255))
            
            if self.image == None:
                xPrintText = self.rect.x - (textPrint.get_width() / 2)
                yPrintText = self.rect.y - (textPrint.get_height() / 2 * len(lines))
            else:
                xPrintText = self.rect.x + (self.image.get_width() / 2) - (textPrint.get_width() / 2)
                yPrintText = self.rect.y + (self.image.get_height() / 2) - (textPrint.get_height() / 2 * len(lines))
            
            #Vẽ chữ lên màn hình:
            for i, l in enumerate(lines):
                word = font.render(l, 0, color)
                screen.blit(word, (xPrintText, (yPrintText + size*i)))
        
        
        return self.action
    
    #Tạo ra hàm chỉnh lại thành ảnh vẽ khác:
    def changeImg(self, imgChange, size = "balance", x = 0, y = 0):
        if type(imgChange) == str:
            imgChange = pygame.image.load(imgChange)
        if size == "balance":
            size = self.sizePercent
            x = self.rect.x
            y = self.rect.y
        width = imgChange.get_width()
        height = imgChange.get_height()
        self.image = pygame.transform.scale(imgChange, (int(width * size / 100), int(height * size / 100)))
        self.originalImg = imgChange
        
        self.rect =self.image.get_rect()
        self.rect.topleft = (x, y)
        if not self.angle == 0:
            self.rotate(self.angle)
    
    def changeSize(self, percent, x = None, y = None):
        #print(self.sizePercent)
        #print(f"image width: {self.image.get_width()}, image original width: {self.originalImg.get_width()}")
        #print(f"Rect X before: {self.rect.x}")
        #print(f"Rect Y before: {self.rect.y}")
        
        if not percent == None:
            width = self.originalImg.get_width()
            height = self.originalImg.get_height()
            sizeChangeWidth = width / 100 * percent
            sizeChangeHeight = height / 100 * percent
            self.image = pygame.transform.scale(self.originalImg, (int(sizeChangeWidth), int(sizeChangeHeight))).convert_alpha()
        else:
            self.image = pygame.transform.scale(self.originalImg, (x, y)).convert_alpha()
        
        xPos, yPos = self.rect.x, self.rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (xPos, yPos)
        self.sizePercent = percent
        if not self.angle == 0:
            self.rotate(self.angle)
        
        #print(f"Rect X after: {self.rect.width}")
        #print(f"Rect Y after: {self.rect.height}")
    def changeXY(self, x, y):
        self.rect.topleft = (x, y)
    def changeAlpha(self, alpha):
        self.alpha = alpha
    def changeAlign(self, alignRect):
        self.alignRectX = alignRect
    def rotate(self, angle):
        if angle == "vertical":
            self.image = pygame.transform.flip(self.image, True, False)
        elif angle == "horizontal":
            self.image = pygame.transform.flip(self.image, False, True)
        self.image = pygame.transform.rotate(self.image, 180)
        self.angle = angle


#Pygame.mixer, play musics and sounds:
#Play music:
def playMusic(musicPath):
    pygame.mixer.music.load(musicPath)
    pygame.mixer.music.play(-1)


#| eyed3 Functions |
def getAudioInfo(path):
    audio = eyed3.load(path)
    title = audio.tag.title
    artist = audio.tag.artist
    album = audio.tag.album
    album_artist = audio.tag.album_artist
    audioInfo = {
        "title": title,
        "artist": artist,
        "album": album,
        "album_artist": album_artist
    }
    return audioInfo