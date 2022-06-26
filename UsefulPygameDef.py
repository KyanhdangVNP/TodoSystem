import os
from turtle import title
import eyed3
import pygame
from ToDoList import pixelFont

#|  PYGAME FUNCTIONS |
#Def that calculate all text rect width and height:
def calSizeText(text = "", fontName = "Fonts/MinecraftBold.otf", size = 24, boxWidth = None):
    if not text == "":
        #Tạo ra font, chữ:
        font = pygame.font.Font(fontName, size)
        
        #Tìm ra giá trị x và y của text chuẩn bị vẽ:
        lines = text.splitlines()
        max_length = 0
        
        lineIndex = 0
        while lineIndex < len(lines):
            line = lines[lineIndex]
            #print(lines)
            if not boxWidth == None:
                word = font.render(line, 0, "black")
                lineWidth = word.get_width()
                lineChange1 = line
                lineChange2 = ""
                #print(f"""line: {line}
#lineWidth > boxWidth: {lineWidth > boxWidth}
#lineWidth: {lineWidth}""")
                if lineWidth > boxWidth:
                    wordList = line.split()
                    if not len(wordList) < 2:
                        #print("Moving word")
                        lineChange2List = []
                        while lineWidth > boxWidth and not len(wordList) < 2:
                            lastWord = wordList[-1]
                            wordList.pop()
                            lineChange1 = " ".join(wordList)
                            lineChange2 = lastWord
                            lines[lineIndex] = lineChange1
                            lineChange2List.insert(0, lineChange2)
                            lineWidth = font.render(lineChange1, 0, "black").get_width()
                        lines.insert(lineIndex + 1, " ".join(lineChange2List))
                        if lineWidth > boxWidth:
                            lineChange2 = ""
                        #print(lines)
                        #print(lineChange1)
                        #print(lineChange2)
                    if lineWidth > boxWidth:
                        #print("Moving Key")
                        while lineWidth > boxWidth:
                            lineChange2 = lineChange1[-1] + lineChange2
                            lineChange1 = lineChange1[:-1]
                            word = font.render(lineChange1, 0, "black")
                            lineWidth = word.get_width()
                        lines[lineIndex] = lineChange1
                        lines.insert(lineIndex + 1, lineChange2)
            lineIndex += 1
        
        for line in lines:
            if(len(line) > max_length):
                max_length = len(line)
                max_len_line = line
        textPrint = font.render(max_len_line, 1, "black")
        
        #Create loop to calculate height and width all text when rendered:
        textWidth = textPrint.get_width()
        textHeight = len(lines) * size

        return [textWidth, textHeight]

#Def Draw text:
def drawText(screen, text = "", fontName = "Fonts/MinecraftRegular.otf", size=24, x = 0, y = 0, color = "black", alpha = 255, alignX = "left", alignY = "left", boxWidth = None):
    if not text == "":
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
        
        lineIndex = 0
        while lineIndex < len(lines):
            line = lines[lineIndex]
            #print(lines)
            if not boxWidth == None:
                word = font.render(line, 0, color)
                lineWidth = word.get_width()
                lineChange1 = line
                lineChange2 = ""
                k = 0
                #print(f"""line: {line}
#lineWidth > boxWidth: {lineWidth > boxWidth}
#lineWidth: {lineWidth}""")
                if lineWidth > boxWidth:
                    wordList = line.split()
                    if not len(wordList) < 2:
                        #print("Moving word")
                        lineChange2List = []
                        while lineWidth > boxWidth and not len(wordList) < 2:
                            lastWord = wordList[-1]
                            wordList.pop()
                            lineChange1 = " ".join(wordList)
                            lineChange2 = lastWord
                            lines[lineIndex] = lineChange1
                            lineChange2List.insert(0, lineChange2)
                            lineWidth = font.render(lineChange1, 0, color).get_width()
                        if lineWidth > boxWidth:
                            lineChange2 = ""
                            k += 1
                        else:
                            lines.insert(lineIndex + 1, " ".join(lineChange2List))
                        #print(lines)
                        #print(lineChange1)
                        #print(lineChange2)
                    if lineWidth > boxWidth:
                        #print("Moving Key")
                        while lineWidth > boxWidth:
                            lineChange2 = lineChange1[-1] + lineChange2
                            lineChange1 = lineChange1[:-1]
                            word = font.render(lineChange1, 0, color)
                            lineWidth = word.get_width()
                        lines[lineIndex] = lineChange1
                        if k == 1:
                            lineChange2 += " " + " ".join(lineChange2List)
                        lines.insert(lineIndex + 1, lineChange2)
            lineIndex += 1
        
        for line in lines:
            if(len(line) > max_length):
                max_length = len(line)
                max_len_line = line
        xIndex = lines.index(max_len_line)
        textPrint = font.render(lines[xIndex], 1, (255,255,255))

        yPrintText = y
        if alignY == "center":
            yPrintText -= len(lines) * size / 2
        
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
        if len(alignRect) == 1:
            alignRect.append("Left")
        self.alignRectX = alignRect[0]
        self.alignRectY = alignRect[1]
    
        self.clicked = False
        self.waitClicked = False

    def draw(self, screen, text = "", fontName = "Fonts/MinecraftRegular.otf", size = 24, color = "black", themeType = None):
        #Set color (changing image of button) depends on theme right now
        if not self.themeChanging == False:
            if themeType == "light":
                self.changeImg(self.image_light, "balance")
            elif themeType == "dark":
                self.changeImg(self.image_dark, "balance")
        
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
            self.rect.x -= self.image.get_width()
        if self.alignRectY == "center":
            self.rect.y -= self.image.get_height() / 2
        
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
        if not self.sizePercent == None:
            self.image = pygame.transform.scale(imgChange, (int(width * size / 100), int(height * size / 100)))
        else:
            self.image = pygame.transform.scale(imgChange, (self.sizeX, self.sizeY))

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
            self.sizeX = self.image.get_width()
            self.sizeY = self.image.get_height()
        
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
    
    #Some minor functions that help making the button more fancy:
    #Def that's making size effect when hovering buttons and check if clicked:
    def hovering(self, sizeNotActive, sizeActive):
        if self.isColliding:
            if self.action:
                return True
            self.changeSize(self.sizePercent + ((sizeActive - self.sizePercent) / 3), None, None)
            #self.changeSize(12, None, None)
        else:
            self.changeSize(self.sizePercent + ((sizeNotActive - self.sizePercent) / 3), None, None)
            #self.changeSize(20, None, None)
        return False
    
    #Button slider functions:
    def setSlider(self, minValue = 0, maxValue = 100, startX = 0, endX = 0):
        self.slider_minValue = minValue
        self.slider_maxValue = maxValue
        self.slider_startX = startX
        self.slider_endX = endX
        self.slider_value = minValue
    def setSliderX(self, startX, endX):
        self.slider_startX = startX
        self.slider_endX = endX
    def setSliderValue(self):
        #Get mouseX, mouseY position:
        mouseX, mouseY = pygame.mouse.get_pos()
        self.slider_value = mouseX / self.slider_valuePerPercent
        if self.slider_value > self.slider_maxValue:
            self.slider_value = self.slider_maxValue
        elif self.slider_value < self.slider_minValue:
            self.slider_value = self.slider_minValue
    def drawSlider(self, screen):
        self.slider_valuePerPercent = (self.slider_endX - self.slider_startX) / (self.slider_maxValue - self.slider_minValue)
        self.changeXY(self.slider_startX + ((self.slider_value - self.slider_minValue) * self.slider_valuePerPercent), self.rect.y)
        self.draw(screen)

#Pygame rect functions:
def drawRect(screen, x, y, width, height, color, alpha = 255, align = None, roundness = 0, outlineSize = 0):
    rect = pygame.Surface((width, height), pygame.SRCALPHA)
    if align == "center":
        x -= rect.get_width() / 2
        #y -= rect.get_height() / 2
    pygame.draw.rect(rect, color, rect.get_rect(), outlineSize, roundness)
    rect.set_alpha(alpha)
    screen.blit(rect, (x, y))



#| IMPORTANT FUNCTIONS TO CREATES TO-DO LISTS |
class toDoListRect():
    def __init__(self, cardText = "unkown", font = "Fonts/MinecraftBold.otf", fontSize = 20, width = 240, height = 70, textWidth = 0, id = "card"):
        self.cardText = cardText
        self.font = font
        self.fontSize = fontSize
        self.textWidth = textWidth
        self.width = width
        self.height = height

        #Important varibles:
        self.activating = False
        self.id = id
        
        #Clicked varibles:
        self.waitClicked = False
        self.clicked = False
        self.isColliding = False
        #print(self.cardText)
    def draw(self, screen, events, x, y, xText, yText):
        self.rect = pygame.Rect(x - (self.width / 2), y, self.width, self.height)
        self.isColliding = False
        self.action = False
        pos = pygame.mouse.get_pos()
        #Kiểm tra vị trí của chuột có chạm vào nút không:
        if pygame.mouse.get_pressed()[0] == 1:
            if self.rect.collidepoint(pos):
                self.isColliding = True
                if self.clicked == False:
                    if self.waitClicked == False:
                        self.waitClicked = True
                        if self.id == "newColumnBtn":
                            self.action = True
                    self.clicked = True
            else:
                self.activating = False
        if pygame.mouse.get_pressed()[0] == 0:
            if not self.rect.collidepoint(pos):
                self.waitClicked = False
            elif self.waitClicked == True:
                self.waitClicked = False
                self.action = True
            self.clicked = False
        
        #Check if card is activated to edit text on text box in that card:
        #print(self.cardText)
        if self.id == "card":
            if self.activating:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE and not self.cardText == "":
                            self.cardText = self.cardText[:-1]
                        else:
                            self.cardText += event.unicode
        
        #Check if action equal True to add outline to textbox::
        if self.action:
            self.activating = True

        if self.id == "card":
            textAlign = "left"
            rectColor = "white"
        else:
            textAlign = "center"
            rectColor = "light gray"

        drawRect(screen, x, y, self.width, self.height, rectColor, 200, "center", 8)
        if len(self.cardText) > 0:
            drawText(screen, self.cardText, pixelFont, self.fontSize, xText, yText, "black", 255, textAlign, "left", self.textWidth)
        if self.activating and self.id == "card":
            drawRect(screen, x, y, self.width, self.height, "black", 200, "center", 8, 3)

class toDoList():
    def __init__(self, title = "united", toDoList = [], posIndex = 0):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.alpha = 200
        self.FontSize = 20
    
        self.clicked = False
        self.waitClicked = False

        #To-do list important varibles:
        self.width = 240
        self.height = 80
        self.cardHeight = 80
        self.cardPadding = 10
        self.cardTextPadding = 5
        self.titleHeight = 40
        self.rect.topleft = ((self.width + 20) * posIndex, 120) # to-do list pos x y
        self.titleFontSize = 25
        self.padding = 8
        self.title = title
        self.posIndex = posIndex
        
        self.toDoList = toDoList
        self.cardList = []
        for i in toDoList:
            cardClass = toDoListRect(i, pixelFont, self.FontSize, self.width, self.height, self.width - self.cardPadding)
            self.cardList.append(cardClass)

    def drawList(self, screen, events, sliderValue, columns):
        #Check if toDoList column xPos is out of the screen or not:
        allcolumnsWidth = (30 * 2 + self.width / 2) + (self.width + (self.padding * 2) + 20) * (columns - 1)
        slideXChange = allcolumnsWidth * (sliderValue / 100)
        xPos = (30 + self.width / 2) + (self.width + (self.padding * 2) + 20) * (self.posIndex - 1)
        xPos -= slideXChange
        SCREEN_WIDTH = pygame.display.get_surface().get_size()[0]
        if xPos > (SCREEN_WIDTH + (self.width / 2) + self.padding) or xPos < (0 - (self.width / 2) - self.padding):
            return None

        #Create list of card's heights:
        cardHeightList = []
        for i in range(len(self.toDoList)):
            if len(self.toDoList[i]) > 0:
                cardTextHeight = calSizeText(self.toDoList[i], pixelFont, self.FontSize, self.width - (self.cardTextPadding * 2))[1]
                cardHeightList.append(cardTextHeight + (self.cardTextPadding * 2))
            else:
                cardHeightList.append(self.FontSize + 2)
            
        #Set width of to-do list rect depends on how many things are listed in list:
        self.height = 0
        for cardHeight in cardHeightList:
            self.height += self.cardPadding + cardHeight
        self.height += (self.padding * 2) + self.titleHeight
        #print(xPos, self.title)
        yPos = self.rect.y - (self.titleHeight / 2) - self.padding
        #Draw a transparent rect layer behind to-do list:
        drawRect(screen, xPos, yPos, self.width + (self.padding * 2), self.height, "light gray", self.alpha, "center", 8)
        #Draw title rect (Unused):
        #title = toDoListRect(self.title, pixelFont, self.titleFontSize, self.width, self.titleHeight, self.width - (self.cardTextPadding * 2))
        yPrintText = yPos + self.padding + self.cardTextPadding
        drawText(screen, self.title, pixelFont, self.titleFontSize, xPos, yPrintText, "black", 255, "center", "left")
        #drawRect(screen, xPos, yPos + self.padding, self.width, self.titleHeight, (185, 255, 255), 200, "center", 8)
        #Draw button "Create a column":
        returnValue = None
        if self.posIndex == columns:
            newColumnBtn = toDoListRect("Create new column", pixelFont, self.titleFontSize, self.width, 70, self.width, "newColumnBtn")
            newColumnBtnX = xPos + (self.width + (self.padding * 2) + 20)
            newColumnBtn.draw(screen, events, newColumnBtnX, yPos, newColumnBtnX, yPos + self.cardTextPadding - 2)
            #print(newColumnBtn.activating)
            if newColumnBtn.action:
                returnValue = "createNewColumn"

        self.isColliding = False
        self.action = False
        x = self.rect.x
        y = self.rect.y
        self.rect.x -= self.width / 2
        #self.rect.y -= self.cardHeight / 2

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
        
        #Vẽ chữ lên màn hình:
        #Tạo ra font, chữ:
        font = pygame.font.Font(pixelFont, self.titleFontSize)
        
        #Tìm ra giá trị x và y của text chuẩn bị vẽ:
        """lines = self.title.splitlines()
        max_length = 0
        
        for line in lines:
            if(len(line) > max_length):
                max_length = len(line)
                max_len_line = line
        xIndex = lines.index(max_len_line)
        textPrint = font.render(lines[xIndex], 1, (255,255,255))
        xPrintText = xPos - (textPrint.get_width() / 2)
        yPrintText = yPos + self.padding + (self.titleHeight / 2) - (textPrint.get_height() / 2 * len(lines))
        #Vẽ chữ lên màn hình:
        for i, l in enumerate(lines):
            word = font.render(l, 0, "black")
            screen.blit(word, (xPrintText, (yPrintText + self.FontSize*i)))"""

        #Changing back to original x y:
        self.rect.x = x
        self.rect.y = y

        #Draw card rects and card texts:
        cardY = yPos + self.titleHeight + self.padding + self.cardPadding
        for i in range(len(self.toDoList)):
            #self.cardDraw(screen, cardName, xPos, cardY, self.width, cardHeightList[i])
            self.toDoList[i] = self.cardList[i].cardText
            self.cardList[i].height = cardHeightList[i]
            self.cardList[i].draw(screen, events, xPos, cardY, xPos - (self.width / 2) + self.cardPadding, cardY + self.cardTextPadding - 2)
            cardY += cardHeightList[i] + self.cardPadding


        return returnValue
    
    def cardDraw(self, screen, cardName, cardX, cardY, width, height):
        drawRect(screen, cardX, cardY, width, height, "white", 200, "center", 8)
        if len(cardName) > 0:
            drawText(screen, cardName, pixelFont, self.FontSize, cardX - (self.width / 2) + self.cardPadding, cardY + self.cardTextPadding - 2, "black", 255, "left", "left", self.width - self.cardPadding)

    def changeImg(self, imgChange):
        if type(imgChange) == str:
            imgChange = pygame.image.load(imgChange)
        size = self.sizePercent
        x = self.rect.x
        y = self.rect.y
        imgWidth = imgChange.get_width()
        imgHeight = imgChange.get_height()
        if not self.sizePercent == None:
            self.image = pygame.transform.scale(imgChange, (int(imgWidth * size / 100), int(imgHeight * size / 100)))
        else:
            self.image = pygame.transform.scale(imgChange, (self.sizeX, self.sizeY))

        self.originalImg = imgChange
        self.rect =self.image.get_rect()
        self.rect.topleft = (x, y)

#| END OF TO-DO LISTS FUNCTIONS |



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