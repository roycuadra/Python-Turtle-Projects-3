import turtle
import math
import sys


def l_v_t(t, s):  # Draws left vertical top half line
    t.lt(90)
    t.fd(s)
    t.pu()
    t.bk(s)
    t.pd()
    t.rt(90)


def l_v_b(t, s):  # Draws left vertical bottom half line
    t.lt(90)
    t.bk(s)
    t.pu()
    t.fd(s)
    t.pd()
    t.rt(90)


def l_v_f(t, s):  # Draws left vertical full line
    l_v_t(t, s)
    l_v_b(t, s)


def m_v_p(t, s):  # Positions cursor for middle line
    t.pu()
    t.fd(s / 2)
    t.pd()


def m_v_t(t, s):  # Draws middle vertical top half line
    m_v_p(t, s)
    l_v_t(t, s)
    m_v_r(t, s)


def m_v_b(t, s):  # Draws middle vertical bottom half line
    m_v_p(t, s)
    l_v_b(t, s)
    m_v_r(t, s)


def m_v_f(t, s):  # Draws middle vertical full line
    m_v_p(t, s)
    l_v_f(t, s)
    m_v_r(t, s)


def m_v_r(t, s):  # Returns curson from middle line
    t.pu()
    t.bk(s / 2)
    t.pd()


def r_v_p(t, s):  # Positions cursor for left line
    t.pu()
    t.fd(s)
    t.pd()


def r_v_t(t, s):  # Draws right vertical top half line
    r_v_p(t, s)
    l_v_t(t, s)
    r_v_r(t, s)


def r_v_b(t, s):  # Draws right vertical bottom half line
    r_v_p(t, s)
    l_v_b(t, s)
    r_v_r(t, s)


def r_v_f(t, s):  # Draws right vertical full line
    r_v_p(t, s)
    l_v_f(t, s)
    r_v_r(t, s)


def r_v_r(t, s):  # Returns cursor from right line
    t.pu()
    t.bk(s)
    t.pd()


def m_h_l(t, s):  # Draws middle horizontal left half line
    t.fd(s / 2)
    t.pu()
    t.bk(s / 2)
    t.pd()


def m_h_r(t, s):  # Draws middle horizontal right half line
    t.pu()
    t.fd(s / 2)
    t.pd()
    t.fd(s / 2)
    t.pu()
    t.bk(s)
    t.pd()


def m_h_f(t, s):  # Draws middle horizontal full line
    m_h_l(t, s)
    m_h_r(t, s)


def t_h_p(t, s):  # Positions cursor for top line
    t.pu()
    t.lt(90)
    t.fd(s)
    t.pd()
    t.rt(90)


def t_h_l(t, s):  # Draws top horizontal left half line
    t_h_p(t, s)
    m_h_l(t, s)
    t_h_r(t, s)


def t_h_r(t, s):  # Draws top horizontal right half line
    t_h_p(t, s)
    m_h_r(t, s)
    t_h_r(t, s)


def t_h_f(t, s):  # Draws top horizontal full line
    t_h_p(t, s)
    m_h_l(t, s)
    m_h_r(t, s)
    t_h_r(t, s)


def t_h_r(t, s):  # Returns cursor from top line
    t.pu()
    t.lt(90)
    t.bk(s)
    t.pd()
    t.rt(90)


def b_h_p(t, s):  # Positions cursor for bottom line
    t.pu()
    t.lt(90)
    t.bk(s)
    t.pd()
    t.rt(90)


def b_h_l(t, s):  # Draws bottom horizontal left half line
    b_h_p(t, s)
    m_h_l(t, s)
    b_h_r(t, s)


def b_h_r(t, s):  # Draws bottom horizontal right half line
    b_h_p(t, s)
    m_h_r(t, s)
    b_h_r(t, s)


def b_h_f(t, s):  # Draws bottom horizontal full line
    b_h_p(t, s)
    m_h_l(t, s)
    m_h_r(t, s)
    b_h_r(t, s)


def b_h_r(t, s):  # Returns cursor from bottom line
    t.pu()
    t.lt(90)
    t.fd(s)
    t.pd()
    t.rt(90)


def d_d_f(t, s):  # Draws diagonal down full line
    t_h_p(t, s)
    t.rt(94 - math.degrees(math.tan(s / (s * 2))))
    t.fd(math.hypot(s * 2, s))
    t.pu()
    t.bk(math.hypot(s * 2, s))
    t.pd()
    t.lt(94 - math.degrees(math.tan(s / (s * 2))))
    t_h_r(t, s)


def d_u_f(t, s):  # Draws diagonal up full line
    b_h_p(t, s)
    t.lt(94 - math.degrees(math.tan(s / (s * 2))))
    t.fd(math.hypot(s * 2, s))
    t.pu()
    t.bk(math.hypot(s * 2, s))
    t.pd()
    t.rt(94 - math.degrees(math.tan(s / (s * 2))))
    b_h_r(t, s)


def t_l_a(t, s):  # Draws top left accent
    t_h_p(t, s)
    t.bk(s / 10)
    t.pu()
    t.fd(s / 10)
    t.pd()
    t_h_r(t, s)


def b_l_a(t, s):  # Draws bottom left accent
    b_h_p(t, s)
    t.bk(s / 10)
    t.pu()
    t.fd(s / 10)
    t.pd()
    b_h_r(t, s)


def b_r_a(t, s):  # Draws bottom right accent
    b_h_p(t, s)
    t.pu()
    t.fd(s)
    t.fd(s / 10)
    t.pd()
    t.bk(s / 10)
    t.pu()
    t.bk(s)
    t.pd()
    b_h_r(t, s)


def next_char(t, s):
    t.pu()
    t.fd(s * 2)
    t.pd()


def let_a(t, s):  # Draws A
    l_v_f(t, s)
    r_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)


def let_b(t, s):  # Draws B
    l_v_f(t, s)
    r_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
    t_l_a(t, s)
    b_l_a(t, s)


def let_c(t, s):  # Draws C
    l_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_d(t, s):  # Draws D
    l_v_f(t, s)
    r_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
    t_l_a(t, s)
    b_l_a(t, s)


def let_e(t, s):  # Draws E
    l_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_f(t, s):  # Draws F
    l_v_f(t, s)
    m_h_f(t, s)
    t_h_f(t, s)


def let_g(t, s):  # Draws G
    l_v_f(t, s)
    r_v_b(t, s)
    m_h_r(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_h(t, s):  # Draws H
    l_v_f(t, s)
    r_v_f(t, s)
    m_h_f(t, s)


def let_i(t, s):  # Draws I
    m_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_j(t, s):  # Draws J)
    m_v_f(t, s)
    t_h_f(t, s)
    b_h_l(t, s)


def let_k(t, s):  # Draws K
    l_v_f(t, s)
    m_v_t(t, s)
    r_v_b(t, s)
    m_h_f(t, s)


def let_l(t, s):  # Draws L
    l_v_f(t, s)
    b_h_f(t, s)


def let_m(t, s):  # Draws M
    l_v_f(t, s)
    m_v_t(t, s)
    r_v_f(t, s)
    t_h_f(t, s)


def let_n(t, s):  # Draws N
    l_v_f(t, s)
    r_v_f(t, s)
    d_d_f(t, s)


def let_o(t, s):  # Draws O
    l_v_f(t, s)
    r_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_p(t, s):  # Draws P
    l_v_f(t, s)
    r_v_t(t, s)
    m_h_f(t, s)
    t_h_f(t, s)


def let_q(t, s):  # Draws Q
    l_v_f(t, s)
    r_v_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)
    b_r_a(t, s)


def let_r(t, s):  # Draws R
    l_v_f(t, s)
    m_v_b(t, s)
    r_v_t(t, s)
    m_h_f(t, s)
    t_h_f(t, s)


def let_s(t, s):  # Draws S
    l_v_t(t, s)
    r_v_b(t, s)
    m_h_f(t, s)
    t_h_f(t, s)
    b_h_f(t, s)


def let_t(t, s):  # Draws T)
    m_v_f(t, s)
    t_h_f(t, s)


def let_u(t, s):  # Draws U
    l_v_f(t, s)
    r_v_f(t, s)
    b_h_f(t, s)
    b_r_a(t, s)


def let_v(t, s):  # Draws v
    t_h_p(t, s)
    t.rt(90 - math.degrees(math.tan((s / 2) / (s * 2))))
    t.fd(math.hypot(s * 2, s / 2))
    t.lt(180 - math.degrees(math.tan((s / 2) / (s * 2))) * 2)
    t.fd(math.hypot(s * 2, s / 2))
    t.rt(90 - math.degrees(math.tan((s / 2) / (s * 2))))
    t.pu()
    t.bk(s)
    t_h_r(t, s)


def let_w(t, s):  # Draws W
    l_v_f(t, s)
    m_v_b(t, s)
    r_v_f(t, s)
    b_h_f(t, s)


def let_x(t, s):
    d_d_f(t, s)
    d_u_f(t, s)


def let_y(t, s):  # Draws Y
    l_v_t(t, s)
    m_v_b(t, s)
    r_v_t(t, s)
    m_h_f(t, s)


def let_z(t, s):  # Draws Z
    t_h_f(t, s)
    b_h_f(t, s)
    d_u_f(t, s)


def main():
#    sys.setExecutionLimit(35000)

    size1 = 25  # Height for main body letters

    size2 = 10  # Height for smaller letters

    wn = turtle.Screen()  # Creates the turtle screen
    wn.setup(1500, size1 + 40)

    turt1 = turtle.Turtle()  # Creates the turtle
    turt1.speed(0)

    name = input("What is your first name (14 character maximum, Roman alphabet only, and no punctuation please)?\n")

    turt1.pu()  # Positions the turtle for first letter
    turt1.bk(720)
    turt1.pd()

    next_char(turt1, size1)  # Prints a space between words
    next_char(turt1, size1)

    for char in name:  # Loops through the characters in the string and returns
        if char.lower() == "a":  # the corresponding function
            let_a(turt1, size1)
        elif char.lower() == "b":
            let_b(turt1, size1)
        elif char.lower() == "c":
            let_c(turt1, size1)
        elif char.lower() == "d":
            let_d(turt1, size1)
        elif char.lower() == "e":
            let_e(turt1, size1)
        elif char.lower() == "f":
            let_f(turt1, size1)
        elif char.lower() == "g":
            let_g(turt1, size1)
        elif char.lower() == "h":
            let_h(turt1, size1)
        elif char.lower() == "i":
            let_i(turt1, size1)
        elif char.lower() == "j":
            let_j(turt1, size1)
        elif char.lower() == "k":
            let_k(turt1, size1)
        elif char.lower() == "l":
            let_l(turt1, size1)
        elif char.lower() == "m":
            let_m(turt1, size1)
        elif char.lower() == "n":
            let_n(turt1, size1)
        elif char.lower() == "o":
            let_o(turt1, size1)
        elif char.lower() == "p":
            let_p(turt1, size1)
        elif char.lower() == "q":
            let_q(turt1, size1)
        elif char.lower() == "r":
            let_r(turt1, size1)
        elif char.lower() == "s":
            let_s(turt1, size1)
        elif char.lower() == "t":
            let_t(turt1, size1)
        elif char.lower() == "u":
            let_u(turt1, size1)
        elif char.lower() == "v":
            let_v(turt1, size1)
        elif char.lower() == "w":
            let_w(turt1, size1)
        elif char.lower() == "x":
            let_x(turt1, size1)
        elif char.lower() == "y":
            let_y(turt1, size1)
        elif char.lower() == "z":
            let_z(turt1, size1)
        next_char(turt1, size1)

    turt1.color("white")  # Turns the cursor white to hide it

    wn.exitonclick()


if __name__ == "__main__":
    main()



