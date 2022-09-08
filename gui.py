import pygame

win_size = (500, 700)
display = pygame.Surface(win_size)
clock = pygame.time.Clock()
win_screen = pygame.display.set_mode(win_size)


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
    b_ac_rect = b_ac.get_rect(topleft=(380, 270))
    b_dot = pygame.image.load('assets/gui/buttons/dot.png').convert_alpha()
    b_dot_rect = b_dot.get_rect(topleft=(256, 270))
    b_bracket_r = pygame.image.load('assets/gui/buttons/bracket_right.png').convert_alpha()
    b_bracket_r_rect = b_bracket_r.get_rect(topleft=(190, 270))
    b_bracket_l = pygame.image.load('assets/gui/buttons/bracket_left.png').convert_alpha()
    b_bracket_l_rect = b_bracket_l.get_rect(topleft=(133, 270))

    # Display
    num_display = pygame.image.load('assets/gui/buttons/display.png').convert_alpha()
    num_display_rect = num_display.get_rect(topleft = (18, 45))
    bg = pygame.image.load('assets/gui/buttons/Bg.png').convert()
    bg_rect = bg.get_rect(topleft= (0,0))


def buttons():
    display.blit(gui.bg, gui.bg_rect)
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
    display.blit(gui.b_bracket_l, gui.b_bracket_l_rect)
    display.blit(gui.b_bracket_r, gui.b_bracket_r_rect)


button_rects = [gui.b_0_rect, gui.b_1_rect, gui.b_2_rect, gui.b_3_rect, gui.b_4_rect, gui.b_5_rect, gui.b_6_rect, gui.b_7_rect, gui.b_8_rect, gui.b_equal_rect,
                gui.b_9_rect, gui.b_plus_rect, gui.b_minus_rect, gui.b_div_rect, gui.b_clear_rect, gui.b_ac_rect, gui.b_dot_rect, gui.b_mul_rect, gui.b_bracket_l_rect, gui.b_bracket_r_rect]


