import pygame
from pygame.locals import *

AllowTextInput = True
StartTextInput = False
IMETextEditing = False
Text = ""
EditPos = 0
IMEText = ""
IMEStart = 0

TextBoxLocation = (0,600)
Skin_Arrow = None

MaxLength_width = 464
def insertChar(mystring, position, chartoinsert):
    longi = len(mystring)
    mystring = mystring[:position] + chartoinsert + mystring[position:] 
    return mystring

def update():
    global AllowTextInput, IMETextEditing, StartTextInput, Text, IMEText, IMEStart, EditPos, Skin_Arrow, MaxLength_width
    global screen

    if (Skin_Arrow == None):
        Skin_Arrow = pygame.UPG.WindowSkin.subsurface((168,24,16,16))
    
    if (not AllowTextInput):
        StartTextInput = False
        IMETextEditing = False
        Text = ""
        
        return
    
    if StartTextInput:
        if (IMETextEditing):
            img_text = pygame.UPG.DefaultFont.render(insertChar(Text, EditPos, insertChar(IMEText, IMEStart , "_")),1, (255,255,255))
        else:
            img_text = pygame.UPG.DefaultFont.render(insertChar(Text, EditPos, "_"),1, (255,255,255))

        if (img_text.get_width() > MaxLength_width):
            img_text = img_text.subsurface((img_text.get_width()-MaxLength_width, 0, MaxLength_width, img_text.get_height()))
        pygame.screen.blit( Skin_Arrow, TextBoxLocation )
        pygame.screen.blit( img_text, (TextBoxLocation[0]+16, TextBoxLocation[1]) )
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print(event.key)
            if event.key == K_RETURN:
                if not StartTextInput:
                    StartTextInput = True
                    pygame.key.start_text_input()
                else:               
                    if IMETextEditing:
                        IMETextEditing = False
                        continue
                
                    print(Text)
                    Text = ""
                    EditPos = 0
                    pygame.key.stop_text_input()

                    StartTextInput = False
            elif event.key == K_BACKSPACE:
                if StartTextInput and not IMETextEditing:
                    if (len(Text) > 0):
                        Text = Text[:-1]

                        EditPos = max(0,EditPos-1)

            elif event.key == K_LEFT:
                if not StartTextInput or IMETextEditing:
                    continue

                EditPos = max(0,EditPos-1)
            elif event.key == K_RIGHT:
                if not StartTextInput or IMETextEditing:
                    continue

                EditPos = min(len(Text),EditPos+1)
            
        elif event.type == TEXTINPUT:
            IMETextEditing = False
            IMEText = ""
            Text = insertChar(Text, EditPos, event.text)
            EditPos += len(event.text)
            pygame.key.set_text_input_rect(pygame.Rect(TextBoxLocation,(240,240)))
            
        elif event.type == TEXTEDITING:
            if not event.text == '':
                IMETextEditing = True
            else:
                IMETextEditing = False
            IMEText = event.text
            IMEStart = event.start
            pygame.key.set_text_input_rect(pygame.Rect(TextBoxLocation,(240,240)))

screen = pygame.display.set_mode((1020, 740))
running = True
while running:
    update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.display.update()

pygame.quit()