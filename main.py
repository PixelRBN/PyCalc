import pygame
import array as arr
pygame.init()

win_size = (500, 700)
clock = pygame.time.Clock()
win_screen = pygame.display.set_mode(win_size)
display = pygame.Surface(win_size)


# GUI

class gui:
    b_0 = pygame.image.load('assets/gui/buttons/0.png').convert_alpha()
    b_0_rect = b_0.get_rect(topleft=(25, 596))
    b_1 = pygame.image.load('assets/gui/buttons/1.png').convert_alpha()
    b_1_rect = b_1.get_rect(topleft=(116, 596))
    b_2 = pygame.image.load('assets/gui/buttons/2.png').convert_alpha()
    b_2_rect = b_2.get_rect(topleft=(207, 596))
    b_3 = pygame.image.load('assets/gui/buttons/3.png').convert_alpha()
    b_3_rect = b_3.get_rect(topleft=(298, 596))
    b_4 = pygame.image.load('assets/gui/buttons/4.png').convert_alpha()
    b_4_rect = b_4.get_rect(topleft=(25, 482))
    b_5 = pygame.image.load('assets/gui/buttons/5.png').convert_alpha()
    b_5_rect = b_5.get_rect(topleft=(116, 482))
    b_6 = pygame.image.load('assets/gui/buttons/6.png').convert_alpha()
    b_6_rect = b_6.get_rect(topleft=(207, 482))
    b_7 = pygame.image.load('assets/gui/buttons/7.png').convert_alpha()
    b_7_rect = b_7.get_rect(topleft=(298, 482))
    b_8 = pygame.image.load('assets/gui/buttons/8.png').convert_alpha()
    b_8_rect = b_8.get_rect(topleft=(25, 375))
    b_9 = pygame.image.load('assets/gui/buttons/9.png').convert_alpha()
    b_9_rect = b_9.get_rect(topleft=(116, 375))

    b_equal = pygame.image.load('assets/gui/buttons/equal.png').convert_alpha()
    b_equal_rect = b_equal.get_rect(topleft=(389, 596))
    b_plus = pygame.image.load('assets/gui/buttons/plus.png').convert_alpha()
    b_plus_rect = b_plus.get_rect(topleft=(389, 482))
    b_minus = pygame.image.load('assets/gui/buttons/minus.png').convert_alpha()
    b_minus_rect = b_minus.get_rect(topleft=(389, 375))
    b_div = pygame.image.load('assets/gui/buttons/divide.png').convert_alpha()
    b_div_rect = b_div.get_rect(topleft=(298, 375))
    b_mul = pygame.image.load('assets/gui/buttons/multiply.png').convert_alpha()
    b_mul_rect = b_mul.get_rect(topleft=(207, 375))

    # Special Buttons
    b_clear = pygame.image.load('assets/gui/buttons/clear.png').convert_alpha()
    b_clear_rect = b_clear.get_rect(topleft=(10, 270))
    b_ac = pygame.image.load('assets/gui/buttons/ac.png').convert_alpha()
    b_ac_rect = b_ac.get_rect(topleft=(133, 270))
    b_dot = pygame.image.load('assets/gui/buttons/dot.png').convert_alpha()
    b_dot_rect = b_dot.get_rect(topleft=(256, 270))
    b_opt = pygame.image.load('assets/gui/buttons/option.png').convert_alpha()
    b_opt_rect = b_opt.get_rect(topleft=(379, 270))

    # Display
    num_display = pygame.image.load('assets/gui/buttons/display.png').convert_alpha()
    num_display_rect = num_display.get_rect(topleft = (25, 55))


def buttons():
    display.blit(gui.b_0, gui.b_0_rect)
    display.blit(gui.b_1, gui.b_1_rect)
    display.blit(gui.b_2, gui.b_2_rect)
    display.blit(gui.b_3, gui.b_3_rect)
    display.blit(gui.b_4, gui.b_4_rect)
    display.blit(gui.b_5, gui.b_5_rect)
    display.blit(gui.b_6, gui.b_6_rect)
    display.blit(gui.b_7, gui.b_7_rect)
    display.blit(gui.b_8, gui.b_8_rect)
    display.blit(gui.b_9, gui.b_9_rect)

    display.blit(gui.b_equal, gui.b_equal_rect)
    display.blit(gui.b_plus, gui.b_plus_rect)
    display.blit(gui.b_minus, gui.b_minus_rect)
    display.blit(gui.b_div, gui.b_div_rect)
    display.blit(gui.b_mul, gui.b_mul_rect)

    display.blit(gui.b_clear, gui.b_clear_rect)
    display.blit(gui.b_ac, gui.b_ac_rect)
    display.blit(gui.b_dot, gui.b_dot_rect)
    display.blit(gui.b_opt, gui.b_opt_rect)


button_rects = [gui.b_0_rect, gui.b_1_rect, gui.b_2_rect, gui.b_3_rect, gui.b_4_rect, gui.b_5_rect, gui.b_6_rect, gui.b_7_rect, gui.b_8_rect, gui.b_equal_rect,
                gui.b_9_rect, gui.b_plus_rect, gui.b_minus_rect, gui.b_div_rect, gui.b_clear_rect, gui.b_ac_rect, gui.b_opt_rect, gui.b_dot_rect, gui.b_mul_rect]

py_inp = 0
py_text = ""
py_inp_op = ""
ans = 0
num_list = []


def maths():
    global py_text, py_inp_op
    str(py_inp_op)
    for rect in button_rects:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(pygame.mouse.get_pos()):
                mouse_pos = pygame.mouse.get_pos()

                if equalpressed:
                    py_inp_op = str(ans)

                # Numbers
                if gui.b_0_rect.collidepoint(mouse_pos):
                    num_list.append(0)
                    py_text += "0"
                    py_inp_op += "0"
                if gui.b_1_rect.collidepoint(mouse_pos):
                    num_list.append(1)
                    py_text += "1"
                    py_inp_op += "1"
                if gui.b_2_rect.collidepoint(mouse_pos):
                    num_list.append(2)
                    py_text += "2"
                    py_inp_op += "2"
                if gui.b_3_rect.collidepoint(mouse_pos):
                    num_list.append(3)
                    py_text += "3"
                    py_inp_op += "3"
                if gui.b_4_rect.collidepoint(mouse_pos):
                    num_list.append(4)
                    py_text += "4"
                    py_inp_op += "4"
                if gui.b_5_rect.collidepoint(mouse_pos):
                    num_list.append(5)
                    py_text += "5"
                    py_inp_op += "5"
                if gui.b_6_rect.collidepoint(mouse_pos):
                    num_list.append(6)
                    py_text += "6"
                    py_inp_op += "6"
                if gui.b_7_rect.collidepoint(mouse_pos):
                    num_list.append(7)
                    py_text += "7"
                    py_inp_op += "7"
                if gui.b_8_rect.collidepoint(mouse_pos):
                    num_list.append(8)
                    py_text += "8"
                    py_inp_op += "8"
                if gui.b_9_rect.collidepoint(mouse_pos):
                    num_list.append(9)
                    py_text += "9"
                    py_inp_op += "9"

                    # Operators
                if gui.b_plus_rect.collidepoint(mouse_pos):
                    py_inp_op += "+"
                    py_text += "+"
                    print("a")
                if gui.b_minus_rect.collidepoint(mouse_pos):
                    py_inp_op += "-"
                    py_text += "-"
                if gui.b_mul_rect.collidepoint(mouse_pos):
                    py_inp_op += "x"
                    py_text += "*"
                if gui.b_div_rect.collidepoint(mouse_pos):
                    py_inp_op += "÷"
                    py_text += "/"
                if gui.b_dot_rect.collidepoint(mouse_pos):
                    num_list.append('.')
                    py_text += "."
                    py_inp_op += "."


num = 0
ops = [gui.b_plus_rect, gui.b_minus_rect, gui.b_mul_rect, gui.b_div_rect, gui.b_equal_rect, gui.b_clear_rect]
op_sym = ["+", "-", "/", "*"]


def list_to_num(list1):
    global num
    for i in num_list:
        num = float("".join(map(str, list1)))
    return num

num_array = arr.array('f', [0, 0, 0, 0, 0])



num_ans = 0

typing_num1 = True
num2_first = True
equalpressed = False

i = 0
b = 0

disp_txt = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        for rect in button_rects:
            if typing_num1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        maths()
                        a = list_to_num(num_list)
                        #print("num1 = ", a)

                # Number 2

            for op in ops:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if op.collidepoint(pygame.mouse.get_pos()):

                        num1 = num_list
                        num_list = []
                        b = list_to_num(num_list)
                       #print("num list", b)
                       #print("the val at here disp txt", disp_txt)

                        typing_num1 = False

            if not typing_num1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        maths()
                        num_array[i] = list_to_num(num_list)
                        for op in ops:

                            if op.collidepoint(pygame.mouse.get_pos()):

                                if op == gui.b_clear_rect:
                                    clear_list = py_text
                                    clear_char = list(clear_list[-1])
                                    py_text = py_text.rstrip(str(clear_char))

                                    test1 = list(py_inp_op[-1])

                                    py_inp_op = py_inp_op.rstrip(str(list(py_inp_op[-1])))
                                    print("test")

                                    # numbers fully dissapper prob  in py_inp op



                                # Equal
                                if op == gui.b_equal_rect:
                                   # print("for equal b val here ", b)
                                    disp_txt.append(str(b))
                                   # print("equal part")
                                    equalpressed = True

                                # Sum
                                if op == gui.b_plus_rect:

                                    a = num_array[i]
                                    i = i + 1

                                    if equalpressed:
                                        disp_txt.append("+")
                                        a = 0
                                        equalpressed = False

                                    num_ans += a
                                    #print("sum = ", num_ans)
                                    disp_txt.append(str(a))
                                   # print(" a aa ", a)
                                    disp_txt.append("+")

                                # Difference
                                if op == gui.b_minus_rect:
                                    a = num_array[i]
                                   # print("array ", num_array)
                                    i = i + 1
                                    if num_ans == 0:
                                        num_ans = 1
                                        a = 0
                                    # print(" a = ", a , "mem num = ", num_ans)
                                    num_ans = num_ans - a

                                    if equalpressed:
                                        disp_txt.append("-")
                                        num_array[i-1] = 0
                                        equalpressed = False

                                    #print("diff = ", num_ans)
                                    disp_txt.append(str(num_array[i-1]))
                                    disp_txt.append("-")

                                # Multiplication
                                if op == gui.b_mul_rect:
                                    a = num_array[i]
                                    i = i + 1
                                    if num_ans == 0:
                                        #print("working on it")
                                        num_ans = num_array[i-1]
                                    else:
                                        #print(" a = ", a, "mem num = ", num_ans)
                                        num_ans = num_ans * a
                                    #print("mul = ", num_ans)

                                    if equalpressed:
                                        disp_txt.append("*")
                                        a = 1
                                        equalpressed = False

                                    disp_txt.append(str(a))
                                    disp_txt.append("*")

                                # Division
                                if op == gui.b_div_rect:
                                    a = num_array[i]
                                    i = i + 1
                                    if num_ans == 0:
                                        num_ans = num_array[i-1]
                                    else:
                                       # print(" a = ", a, "mem num = ", num_ans)
                                        num_ans = num_ans / a

                                    if equalpressed:
                                        disp_txt.append("/")
                                        a = 1
                                        equalpressed = False

                                    #print("div = ", num_ans)
                                    disp_txt.append(str(a))
                                    disp_txt.append("/")

    # Input Display

    #print(disp_txt)

    if disp_txt == []:
        disp_txt = ["0"]

    if disp_txt[-1] == "*" or disp_txt[-1] == "/":
        disp_txt.append("1")

    for operator in op_sym:
        if disp_txt[-1] == operator:
            #print(disp_txt)
            disp_txt.append("0")

    #print(" the disp text val ", disp_txt)

    txt = " ".join(disp_txt)
    # print("the txt ", txt)

    # print("eval ", ans)


    if equalpressed:
        ans = eval(py_text)
        disp_txt.clear()
        disp_txt.append(str(ans))
        py_text = str(ans)

    else:
        disp_txt.pop()

    # Text

    print("pytext = ", py_text)

    font_size = 50
    if ans > 100000000:
        font_size = 30
    if ans > 1000000000000:
        font_size = 18

    font = pygame.font.Font('assets/fonts/Tomorrow-Regular.ttf', font_size)
    input_txt = font.render(str(py_inp_op), True, 'White')
    input_txt_rect = input_txt.get_rect(midright=(455, 90))

    font2 = pygame.font.Font('assets/fonts/Tomorrow-Regular.ttf', font_size+15)
    ans_txt = font2.render(str(ans), True, 'White')
    ans_txt_xpos = 455
    ans_txt_rect = ans_txt.get_rect(midright=(ans_txt_xpos, 165))
    if input_txt_rect.collidepoint(gui.num_display_rect.midleft):
        font_size = font_size - 10

    # GUI
    buttons()
    display.blit(gui.num_display, gui.num_display_rect)
    display.blit(input_txt, input_txt_rect)
    display.blit(ans_txt, ans_txt_rect)

    win_screen.blit(display, (0, 0))
    clock.tick(60)
    pygame.display.update()

