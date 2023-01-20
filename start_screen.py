import pygame


start = True
size = (800, 600)
green = (0, 150, 0)

button_pos = (250, 400)
button_size = (325, 40)
button_txt = "Начать новую игру"

basic_txt = "???"
basic_pos = (100, 10)

win_pos = (250, 200)
win_txt = ["", "Вы победили!", "Вы проиграли :c"]
win_or_loss = 0



def start_screen(screen): ##отрисовка
    font = pygame.font.Font(None, 50)
    screen.fill(green)
    pygame.draw.rect(screen, "white", (*button_pos, *button_size), 0)
    text1 = font.render(basic_txt, True, "white")
    text2 = font.render(win_txt[win_or_loss], True, "white")
    text3 = font.render(button_txt, True, green)
    screen.blit(text1, basic_pos)
    screen.blit(text2, win_pos)
    screen.blit(text3, button_pos)
    


#наверное это удобно сделать общей частью, но оно тут есть, чтобы отдельно тестить
pygame.init()
screen = pygame.display.set_mode(size)   


if start:
    running = True
    while running:
        start_screen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                st = True
                for i in range(2):
                    if event.pos[i] < button_pos[i] or event.pos[i] > button_pos[i] + button_size[i]:
                        st = False
                if st:
                    start = False
                    running = False
        pygame.display.flip()
    if start:
        pygame.quit()
    else:
        pass #если ты хочешь вставить какое-то действие после нажаттия на кнопку, но до работы с экраном игры
             #то можно сделать это тут

