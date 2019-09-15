
import snake as sn
import pygame
import sys
blue = (0,255,255)
red = (220,20,60)
black = (0,0,0)
text = "Welcome to my snake game!!!"
text2 = "You can use both'w''a''s''d' or 'up''down''left''right' to control your snake!"
text3 = "You need to notice that you can only move vertically!"
text4 = "It means you can only turn right/left when you are up/down."
text5 = "Good Luck!!!Don't hit the wall or yourself!!!"
text6 = "Press 'Escape' to return to menu."
main_menu_font_path = "./font/"
main_menu_image_path = "./image/"
size = (1280,720)

def write(ins,text,sz,color):
    '''
   This function here prints the sentences on the screen
    '''
    fontObj = pygame.font.SysFont('arial', 32)
    textSurfaceObj = fontObj.render(text, True,color )
    # Putting the sentences in right places
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = sz
    ins.blit(textSurfaceObj, textRectObj)

def difficult():
    '''
    It allows user to choose the difficulty they want.
    '''
    dif = pygame.display.set_mode(size)
    pygame.display.set_caption('Easy?Difficult?!')
    dif_b = pygame.image.load(main_menu_image_path + 'diff.jpg').convert()
    dif.blit(dif_b, (0, 0))
    write(dif, "EASY",(640,120),red)
    write(dif, "MODERATE",(640,320),red)
    write(dif, "DIFFICULT",(640,520),red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                # Setting the button range for easy.
                if 594<= x <= 676:
                    if 105<= y <= 132:
                        sn.main(10)
                        gameover(sn.score)
                    # Setting the button range for moderate.
                if 560<= x <= 721:
                    if 305<= y <= 335:
                        sn.main(30)
                        gameover(sn.score)
                # Setting the button range for exit difficult.
                if 569<= x <= 716:
                    if 506<= y <= 535:
                        sn.main(45)
                        gameover(sn.score)
        pygame.display.update()


    
def instruction():
    """
    This function below gives the tutorial to the user.
    """
    ins = pygame.display.set_mode(size)
    pygame.display.set_caption('Instruction!!!!')
    ins_b = pygame.image.load(main_menu_image_path + 'wood.jpg').convert()
    ins.blit(ins_b, (0, 0))
    write(ins, text,(640,120),blue)
    write(ins, text2,(640,200),blue)
    write(ins, text3, (640, 280),blue)
    write(ins, text4, (640, 360),blue)
    write(ins, text5, (640, 440),blue)
    write(ins, text6, (640, 650),blue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    menu()
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def gameover(score):
    '''
    This function generates the screen after the snake is dead.
    user can choose to go back to menu or exit directly.
    '''
    good = pygame.display.set_mode(size)
    pygame.display.set_caption('Game over!!!')
    good_b = pygame.image.load(main_menu_image_path + 'gameover.png').convert()
    good.blit(good_b, (0, 0))
    write(good,"Your score is "+str(score),(640,180),blue)
    write(good,"Press 'r' to back to menu",(640,590),red)
    write(good, "Press 'Enter' to quit", (640, 650),red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 13:
                    pygame.quit()
                    sys.exit()
                elif event.key == 114:
                    menu()
        pygame.display.update()


def run():
    '''
    This screen is displayed after the user hit the 'exit' button on the main menu.
    '''
    go = pygame.display.set_mode(size)
    pygame.display.set_caption('BYE BYE!!!!')
    go_b = pygame.image.load(main_menu_image_path + 'bye.jpg').convert()
    go.blit(go_b, (0, 0))
    write(go, "Student : Huang HongFei", (640, 50), (139,69,19))
    write(go, "See you next time XD", (640, 100), (139,69,19))
    write(go, "Press 'ESCAPE' to back to menu", (640, 480), red)
    write(go, "Press 'Enter' to back to exit", (640, 550), red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    # When user hit escape , back to menu.
                    menu()
                    pygame.quit()
                    sys.exit()
                if event.key == 13:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def menu():
    '''
    This is the main function that generates the menu.
    '''
    global play
    pygame.init()
    background = pygame.image.load(main_menu_image_path + 'background.jpg')
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("This is menu!!!")
    frame_rate = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                # Setting the button range for starting the game.
                if 578<= x <= 969:
                    if 362<= y <= 435:
                        difficult()
                    # Setting the button range for instruction.
                    if 478 <= y <= 552:
                        instruction()
                # Setting the button range for exit button.
                if 1184<= x <= 1233:
                    if 684<= y <= 712:
                        run()
        # display background
        display.blit(background,(0,0))
        # Display the exit button.
        write(display, "Exit", (1210,700), red)
        pygame.display.flip()
        frame_rate.tick(15)

menu()
