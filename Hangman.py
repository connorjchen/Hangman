import pygame, sys, os
import HangmanClass
pygame.init()
pygame.mixer.pre_init(44100, 16, 2)

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, filename)

animalList = ['Llama', 'Giraffe', 'Panda', 'Penguin', 'Shark', 'Snake', 'Tiger',
               'Sheep', 'Goose', 'Elephant', 'Rabbit', 'Flamingo', 'Starfish', 'Crocodile', 'Alligator']

countryList = ['Australia', 'China', 'Russia', 'Brazil', 'Canada', 'Italy', 'Spain', 'Korea', 'Japan', 'Germany', 'Israel',
               'Mexico', 'France', 'Bangladesh', 'India', 'Argentina']

fruitList = ['Apple', 'Grape', 'Orange', 'Mango', 'Coconut', 'Banana', 'Kiwi', 'Pear',
             'Lime', 'Lemon', 'Blueberry', 'Blackberry', 'Watermelon', 'Strawberry', 'Passionfruit']

colorList = ['Turquoise', 'Blue', 'Red', 'Yellow', 'Green', 'Black', 'White', 'Brown', 'Pink',
             'Purple', 'Maroon', 'Grey', 'Gold', 'Silver']

statesList = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware",
              "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois",
              "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
              "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey",
              "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
              "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

hangman = HangmanClass.Hangman(animalList)
hangman.resetGame()

screenWidth = 860
screenHeight = 670
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Hangman")

clock = pygame.time.Clock()

baseFont = pygame.font.Font(None, 70)
headerFont = pygame.font.Font(None, 32)
watermarkFont = pygame.font.Font(None, 20)

inputHeader = 'Guess Letter/Word:'
outputHeader = 'Feedback:'
currentWordHeader = 'Current Word:'
usedLettersHeader = 'Used Letters:'
#watermark = 'Connor J. Chen'
currentWordList = ''
inputText = ''
outputText = ''
animalHeader = 'Animals'
countryHeader = 'Countries'
fruitHeader = 'Fruits'
colorHeader = 'Colors'
stateHeader = 'States'

refreshLogoPath = find_data_file('img/refresh.png')
mutePath = find_data_file('img/mute.png')
notMutePath = find_data_file('img/notMute.png')
hangman0Path = find_data_file('img/hangman0.png')
hangman1Path = find_data_file('img/hangman1.png')
hangman2Path = find_data_file('img/hangman2.png')
hangman3Path = find_data_file('img/hangman3.png')
hangman4Path = find_data_file('img/hangman4.png')
hangman5Path = find_data_file('img/hangman5.png')
hangman6Path = find_data_file('img/hangman6.png')
backgroundPath = find_data_file('img/paperBackground.jpg')
iconPath = find_data_file('img/hangmanLogo.png')
wrongSoundPath = find_data_file('sound/wrong.wav')
correctSoundPath = find_data_file('sound/correct.wav')
lostSoundPath = find_data_file('sound/lost.wav')
wonSoundPath = find_data_file('sound/won.wav')

refreshLogo = pygame.image.load(refreshLogoPath)
mute = pygame.image.load(mutePath)
notMute = pygame.image.load(notMutePath)
hangman0 = pygame.image.load(hangman0Path)
hangman1 = pygame.image.load(hangman1Path)
hangman2 = pygame.image.load(hangman2Path)
hangman3 = pygame.image.load(hangman3Path)
hangman4 = pygame.image.load(hangman4Path)
hangman5 = pygame.image.load(hangman5Path)
hangman6 = pygame.image.load(hangman6Path)
background = pygame.image.load(backgroundPath)
icon = pygame.image.load(iconPath)

background = pygame.transform.scale(background, (screenWidth, screenHeight))
icon = pygame.transform.scale(icon, (32, 32))

pygame.display.set_icon(icon)

wrongSound = pygame.mixer.Sound(wrongSoundPath)
correctSound = pygame.mixer.Sound(correctSoundPath)
lostSound = pygame.mixer.Sound(lostSoundPath)
wonSound = pygame.mixer.Sound(wonSoundPath)

inputRect = pygame.Rect(10, 10, 580, 140)
outputRect = pygame.Rect(10, 160, 580, 140)
currentWordRect = pygame.Rect(10, 310, 580, 140)
usedLettersRect = pygame.Rect(10, 460, 580, 140)
refreshBtn = pygame.Rect(600, 460, 250, 140)
animalBtn = pygame.Rect(10, 610, 160, 50)
countryBtn = pygame.Rect(180, 610, 160, 50)
fruitBtn = pygame.Rect(350, 610, 160, 50)
colorBtn = pygame.Rect(520, 610, 160, 50)
stateBtn = pygame.Rect(690, 610, 160, 50)
soundBtn = pygame.Rect(screenWidth - 28, 3, 24, 20)

colorActive = pygame.Color('gray27')
colorPassive = pygame.Color('gray15')
color = colorPassive

active = True
soundControl = True

while True:
    currentWord = hangman.getCurrentWord()
    usedLetters = ''
    usedLetters2 = ''
    for x in hangman.getUsedLetters():
        if len(usedLetters) < 20:
            usedLetters += x + ' '
        else:
            usedLetters2 += x + ' '

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                active=True
            elif soundBtn.collidepoint(event.pos):
                if soundControl == True:
                    soundControl = False
                else:
                    soundControl = True
            elif refreshBtn.collidepoint(event.pos):
                hangman.resetGame()
                inputText = ''
                outputText = ''
            elif animalBtn.collidepoint(event.pos):
                hangman = HangmanClass.Hangman(animalList)
                hangman.resetGame()
                inputText = ''
                outputText = ''
            elif countryBtn.collidepoint(event.pos):
                hangman = HangmanClass.Hangman(countryList)
                hangman.resetGame()
                inputText = ''
                outputText = ''
            elif fruitBtn.collidepoint(event.pos):
                hangman = HangmanClass.Hangman(fruitList)
                hangman.resetGame()
                inputText = ''
                outputText = ''
            elif colorBtn.collidepoint(event.pos):
                hangman = HangmanClass.Hangman(colorList)
                hangman.resetGame()
                inputText = ''
                outputText = ''
            elif stateBtn.collidepoint(event.pos):
                hangman = HangmanClass.Hangman(statesList)
                hangman.resetGame()
                inputText = ''
                outputText = ''
            else:
                active=False

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    inputText = inputText[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(inputText) > 0:
                        outputText = hangman.guessLetter(inputText)
                        inputText = ''
                        if soundControl == True:
                            if outputText == 'Incorrect':
                                pygame.mixer.Sound.play(wrongSound)
                            elif outputText == 'Correct':
                                pygame.mixer.Sound.play(correctSound)
                            elif outputText == 'You lose!':
                                pygame.mixer.Sound.play(lostSound)
                            elif outputText == 'You won!':
                                pygame.mixer.Sound.play(wonSound)
                else:
                    inputText += event.unicode

    win.fill(pygame.Color('floralwhite'))
    win.blit(background, (0, 0))

    if active:
        color = colorActive
    else:
        color = colorPassive

    if soundControl:
        soundLogo = notMute
    else:
        soundLogo = mute

    if hangman.getStrikes() == 0:
        hangmanImage = hangman0
    elif hangman.getStrikes() == 1:
        hangmanImage = hangman1
    elif hangman.getStrikes() == 2:
        hangmanImage = hangman2
    elif hangman.getStrikes() == 3:
        hangmanImage = hangman3
    elif hangman.getStrikes() == 4:
        hangmanImage = hangman4
    elif hangman.getStrikes() == 5:
        hangmanImage = hangman5
    elif hangman.getStrikes() == 6:
        hangmanImage = hangman6

    hangmanImage = pygame.transform.scale(hangmanImage, (300, 400))

    if hangman.getWordList() == animalList:
        currentWordList = 'Current Word List: Animals'
    elif hangman.getWordList() == countryList:
        currentWordList = 'Current Word List: Countries'
    elif hangman.getWordList() == fruitList:
        currentWordList = 'Current Word List: Fruits'
    elif hangman.getWordList() == colorList:
        currentWordList = 'Current Word List: Colors'
    elif hangman.getWordList() == statesList:
        currentWordList = 'Current Word List: States'

    pygame.draw.rect(win, color, inputRect)
    pygame.draw.rect(win, pygame.Color('gray15'), outputRect)
    pygame.draw.rect(win, pygame.Color('gray15'), currentWordRect)
    pygame.draw.rect(win, pygame.Color('gray15'), usedLettersRect)
    pygame.draw.rect(win, pygame.Color('skyblue'), refreshBtn)
    pygame.draw.rect(win, pygame.Color('indianred1'), animalBtn)
    pygame.draw.rect(win, pygame.Color('indianred1'), countryBtn)
    pygame.draw.rect(win, pygame.Color('indianred1'), fruitBtn)
    pygame.draw.rect(win, pygame.Color('indianred1'), colorBtn)
    pygame.draw.rect(win, pygame.Color('indianred1'), stateBtn)
 #   pygame.draw.rect(win, pygame.Color('skyblue'), soundBtn)


    inputSurface = baseFont.render(inputText,True, (255,255,255))
    inputHeaderSurface = headerFont.render(inputHeader, True, (255,255,255))
    resultSurface = baseFont.render(outputText, True, (255,255,255))
    resultHeaderSurface = headerFont.render(outputHeader, True, (255,255,255))
    currentSurface = baseFont.render(currentWord,True, (255,255,255))
    currentHeaderSurface = headerFont.render(currentWordHeader, True, (255,255,255))
    usedLetterSurface = baseFont.render(usedLetters, True, (255, 255, 255))
    usedLetterSurface2 = baseFont.render(usedLetters2, True, (255, 255, 255))
    usedLetterHeaderSurface = headerFont.render(usedLettersHeader, True, (255, 255, 255))
    currentWordListSurface = watermarkFont.render(currentWordList, True, pygame.Color('gray27'))
    animalHeaderSurface = headerFont.render(animalHeader, True, (0, 0, 0))
    countryHeaderSurface = headerFont.render(countryHeader, True, (0, 0, 0))
    fruitHeaderSurface = headerFont.render(fruitHeader, True, (0, 0, 0))
    colorHeaderSurface = headerFont.render(colorHeader, True, (0, 0, 0))
    stateHeaderSurface = headerFont.render(stateHeader, True, (0, 0, 0))
#    watermarkSurface = watermarkFont.render(watermark, True, pygame.Color('gray27'))

    win.blit(inputSurface,(inputRect.x + 5, inputRect.y + 30))
    win.blit(inputHeaderSurface, (inputRect.x + 5, inputRect.y + 5))
    win.blit(resultSurface, (outputRect.x + 5, outputRect.y + 50))
    win.blit(resultHeaderSurface, (outputRect.x + 5, outputRect.y + 5))
    win.blit(currentSurface, (currentWordRect.x + 5, currentWordRect.y + 45))
    win.blit(currentHeaderSurface, (currentWordRect.x + 5, currentWordRect.y + 5))
    win.blit(usedLetterSurface, (usedLettersRect.x + 5, usedLettersRect.y + 20))
    win.blit(usedLetterSurface2, (usedLettersRect.x + 5, usedLettersRect.y + 80))
    win.blit(usedLetterHeaderSurface, (usedLettersRect.x + 5, usedLettersRect.y + 5))
    win.blit(refreshLogo, (refreshBtn.x + 75, refreshBtn.y + 25))
    win.blit(hangmanImage, (575, 30))
    win.blit(currentWordListSurface, (600, 8))
    win.blit(animalHeaderSurface, (animalBtn.x + 35, animalBtn.y + 15))
    win.blit(countryHeaderSurface, (countryBtn.x + 26, countryBtn.y + 15))
    win.blit(fruitHeaderSurface, (fruitBtn.x + 47, fruitBtn.y + 15))
    win.blit(colorHeaderSurface, (colorBtn.x + 47, colorBtn.y + 15))
    win.blit(stateHeaderSurface, (stateBtn.x + 47, stateBtn.y + 15))
    win.blit(soundLogo, (screenWidth - 25, 2))
#    win.blit(watermarkSurface, (screenWidth - 110, screenHeight - 25))

    pygame.display.flip()
    clock.tick(60)

