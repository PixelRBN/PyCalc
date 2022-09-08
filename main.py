import pygame
from numpy import array
import re
from gui import gui, buttons, button_rects, display, win_screen, clock
pygame.init()

py_text = ""        # Used for Calculation
py_inp_op = ""      # Display text top
ans = 0
num_list = []
rgx = re.compile(r'(?<!\.)\b(0+)([1-9])+\b')


def maths():
    global py_text, py_inp_op
    str(py_inp_op)
    for b_rect in button_rects:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if b_rect.collidepoint(pygame.mouse.get_pos()):
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


def list_to_num(list1):
    global num
    for _ in num_list:
        if list1[0] == ".":
            list1[0] = "0.0"
        num = float("".join(map(str, list1)))
    return num


num = 0
ops = [gui.b_plus_rect, gui.b_minus_rect, gui.b_mul_rect, gui.b_div_rect, gui.b_equal_rect, gui.b_clear_rect, gui.b_ac_rect]
op_sym = ["+", "-", "/", "*"]

list_conv = []
num_array = array([0])
num_ans = 0
typing_num1 = True
num2_first = True
equalpressed = False
i = 0   # value for num_array
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

            if py_inp_op == ".":
                py_inp_op = "0."
            if py_text == ".":
                py_text = "0."

            for op in ops:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if op.collidepoint(pygame.mouse.get_pos()):
                        num1 = num_list
                        num_list = []
                        b = list_to_num(num_list)
                        typing_num1 = False

            if not typing_num1:
                if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(pygame.mouse.get_pos()):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        maths()

                        for op in ops:
                            if op.collidepoint(pygame.mouse.get_pos()):

                                list_conv.append(list_to_num(num_list))
                                num_array = list_conv

                                # AC
                                if op == gui.b_ac_rect:
                                    list_conv = []
                                    num_array = i = b = a = num = ans = 0
                                    py_text = py_inp_op = ""

                                # Clear
                                if op == gui.b_clear_rect:
                                    py_text = py_text[:-1]
                                    py_inp_op = py_inp_op[:-1]

                                # Equal
                                if op == gui.b_equal_rect:
                                    disp_txt.append(str(b))
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
                                    disp_txt.append(str(a))
                                    disp_txt.append("+")

                                # Difference
                                if op == gui.b_minus_rect:
                                    a = num_array[i]
                                    i = i + 1
                                    if num_ans == 0:
                                        num_ans = 1
                                        a = 0
                                    num_ans = num_ans - a

                                    if equalpressed:
                                        disp_txt.append("-")
                                        num_array[i-1] = 0
                                        equalpressed = False

                                    disp_txt.append(str(num_array[i-1]))
                                    disp_txt.append("-")

                                # Multiplication
                                if op == gui.b_mul_rect:
                                    a = num_array[i]
                                    i = i + 1
                                    if num_ans == 0:
                                        num_ans = num_array[i-1]
                                    else:
                                        num_ans = num_ans * a

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
                                        num_ans = num_ans / a

                                    if equalpressed:
                                        disp_txt.append("/")
                                        a = 1
                                        equalpressed = False

                                    disp_txt.append(str(a))
                                    disp_txt.append("/")

    # Input Display

    if not disp_txt:
        disp_txt = ["0"]

    if disp_txt[-1] == "*" or disp_txt[-1] == "/":
        disp_txt.append("1")

    for operator in op_sym:
        if disp_txt[-1] == operator:
            disp_txt.append("0")

    txt = " ".join(disp_txt)

    # Regex to remove leading zero
    py_text = rgx.sub(r'\2', py_text)
    # print(py_text)

    if equalpressed:
        if py_text == "":
            py_text = "0"
        if py_text[-1:] in op_sym or py_text[-1:] == ".":
            py_text = py_text[:-1]
        try:
            ans = eval(py_text)
        except SyntaxError:
            py_inp_op = "Syntax Error"
        disp_txt.clear()
        disp_txt.append(str(ans))
        py_text = str(ans)
    else:
        disp_txt.pop()

    # Text
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
