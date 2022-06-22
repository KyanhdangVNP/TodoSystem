#Def Draw text:
def drawText(text, fontName = None, size = 24, x = 0, y = 0, color = "black", align = "left"):
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

    xPrintText = x
    yPrintText = y
    if align == "right":
        xPrintText -= textPrint.get_width()
    elif align == "center":
        xPrintText -= (textPrint.get_width() / 2)
    
    #Vẽ chữ lên màn hình:
    for i, l in enumerate(lines):
        word = font.render(l, 0, color)
        screen.blit(word, (xPrintText, (yPrintText + size*i)))

#Class Button, tạo ra nút có thể nhấn được:
class button():
    def __init__(self, x, y, image, sizePercent, alignRect):
        if image == None:
            self.image = None
            self.originalImg = None
            width = 0 
            height = 0

            self.rect = pygame.Rect((0, 0), (0, 0))
            self.rect.topleft = (x, y)
        else:
            width = image.get_width() 
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * sizePercent / 100), int(height * sizePercent / 100)))
            self.originalImg = image

            self.sizePercent = sizePercent
            self.sizeX = width
            self.sizeY = height
            self.rect =self.image.get_rect()
            self.rect.topleft = (x, y)
        self.alignRectX = alignRect
    
        self.clicked = False
        self.waitClicked = False

    def draw(self, text, fontName, size, color):
        global screen
        
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
    def changeImg(self, imgChange, x, y, size):
        width = imgChange.get_width()
        height = imgChange.get_height()
        self.image = pygame.transform.scale(imgChange, (int(width * size), int(height * size)))
        self.originalImg = imgChange
        
        self.rect =self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def changeSize(self, percent, x, y):
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
        
        #print(f"Rect X after: {self.rect.width}")
        #print(f"Rect Y after: {self.rect.height}")
    def changeXY(self, x, y):
        self.rect.topleft = (x, y)