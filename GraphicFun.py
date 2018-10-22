from graphics import GraphWin, Circle, Point, Oval, Line, color_rgb
from random import randint
from math import cos, sin, pi, sqrt


def main():
    print("Welcome to Drew's graphical fun house")
    print("The available methods are:\n1: extendo_circ()\n2: circle_mover()\n3: circle_circ()\n4: line_drawer\n5: fractal_boi()\n6: circ_frac()\n7: circ_spi()")
    num = int(input("Which would you like?"))
    if num = 1:
        extendo_circ()
    elif num = 2:
        circle_mover()
    elif num = 3:
        circle_circ()
    elif num = 4:
        line_drawer()
    elif num = 5:
        fractal_boi()
    elif num = 6:
        circ_frac()
    elif num = 7:
        circ_spi()
    else:
        print("Pick a lower number\n")
        
def extendo_circ():
    win = GraphWin("My Circle", 1280, 800)
    i = 0
    while i < 640:
        y = 400
        c = Circle(Point(i,y), i)
        i += 10
        c.draw(win)


def oval_test():
    win = GraphWin("Oval Test", 1280, 800)
    w1 = 100
    h1 = 100
    w2 = 1000
    h2 = 700
    p1 = Point(w1,h1)
    p2 = Point(w2,h2)
    p1.draw(win)
    p2.draw(win)
    o1 = Oval(Point(w1, h1), Point(w2, h2))
    o1.draw(win)


def circle_mover():
    win = GraphWin("Crazy", 600, 600)
    x = 300
    y = 0
    x_inc = True
    y_inc = True
    laps = 0
    
    while laps <= 4:
        if x > 590:
            x_inc = False
            laps += 1
        elif x == 0:
            x_inc = True
            laps += 1
            
        if y > 590:
            y_inc = False
            laps += 1
        elif y == 0:
            y_inc = True
            laps += 1
             
        if x_inc:
            x += 10
        else:
            x -= 10
            
        if y_inc:
            y += 10
        else:
            y -= 10
            
        c = Circle(Point(x,y), 200)
        c.draw(win)


def circle_circ():
    circ_num = int(input("How many circles would you like? "))
    win = GraphWin("circleCirc", 800, 800)
    cx = 400
    cy = 400
    r = 200
    rr = 200
    for i in range(circ_num):
        a = (2*pi/circ_num)*i
        x = cx + r * cos(a)
        y = cy + r * sin(a)
        cc = Circle(Point(x,y), rr)
        cc.draw(win)
        # p = Point(x,y)
        # p.draw(win)
    
    p = Point(cx,cy)
    p.draw(win)
    c = Circle(Point(cx,cy), r-rr)
    c.draw(win)


def line_drawer():
    win = GraphWin("Made by Drew", 800, 800)
    cen_point = Point(400, 400)
    lx = 0
    ly = 0
    while lx <= 700 and ly <= 700:
        x_point = randint(0, 1)   # random() #choose if x is positive or neutral for this iteration
        y_point = randint(0, 1)   # random()
        for i in range(10):  # change end point depending on random result
            lx += x_point*10
            ly += y_point*10
            line = Line(cen_point, Point(lx, ly))
            colour = color_rgb(0, 170, 250)
            line.setOutline(colour)
            line.draw(win)


def fractal_boi():
    win = GraphWin("Fracboi", 1280, 800)

    def fractal_h(n, s, cenx, ceny):
        draw_h(s, cenx, ceny)
        if n == 1:
            return 0
        x0 = cenx - s / 2
        x1 = cenx + s / 2
        y0 = ceny - s / 2
        y1 = ceny + s / 2
        fractal_h(n - 1, s / 2, x0, y0)
        fractal_h(n - 1, s / 2, x1, y0)
        fractal_h(n - 1, s / 2, x0, y1)
        fractal_h(n - 1, s / 2, x1, y1)

    def draw_h(s, cenx, ceny):
        x0 = cenx - s / 2
        x1 = cenx + s / 2
        y0 = ceny - s / 2
        y1 = ceny + s / 2

        line0 = Line(Point(x0, ceny), Point(x1, ceny))
        line1 = Line(Point(x0, y0), Point(x0, y1))
        line2 = Line(Point(x1, y0), Point(x1, y1))
        line0.draw(win)
        line1.draw(win)
        line2.draw(win)

    fractal_h(6, 300, 640, 400)


def circ_frac():
    win = GraphWin("Circ Test", 1280, 800)
    c0 = Circle(Point(640, 400), 400)
    c0.draw(win)
    def draw_frac(n, cenx, ceny, s):
        if n == 0:
            return 0
        draw_circles(cenx, ceny, s, n)
        #if n % 2 == 0:
        s1 = (-3 + (2 * sqrt(3))) * s
        x = cenx
        y = ceny - ((2*(sqrt(3)*s1))/3)
        draw_frac(n-1, x, y, s1)
        y = ((sqrt(3) * s1) / 3) + ceny
        x = s1 + cenx
        draw_frac(n - 1, x, y, s1)
        x = cenx - s1
        draw_frac(n - 1, x, y, s1)
        #else:
        #    s1 = (-3 + (2 * sqrt(3))) * s
        #    x = cenx
        #    y = ceny + ((2 * (sqrt(3) * s1)) / 3)
        #    draw_frac(n - 1, x, y, s1)
        #    y = ceny - ((sqrt(3) * s1) / 3)
        #    x = s1 + cenx
        #    draw_frac(n - 1, x, y, s1)
        #    x = cenx - s1
        #    draw_frac(n - 1, x, y, s1)

    def draw_circles(cenx, ceny, s, n):
            #if n % 2 == 0:
        s1 = (-3 + (2 * sqrt(3))) * s
        x = cenx
        y = ceny - ((2*(sqrt(3)*s1))/3)
        c1 = Circle(Point(x, y), s1)
        c1.draw(win)
        y = ((sqrt(3) * s1) / 3) + ceny
        x = s1+cenx
        c2 = Circle(Point(x, y), s1)
        c2.draw(win)
        x = cenx - s1
        c3 = Circle(Point(x, y), s1)
        c3.draw(win)
            #else:
            #    s1 = (-3 + (2 * sqrt(3))) * s
            #    x = cenx
            #    y = ceny + ((2 * (sqrt(3) * s1)) / 3)
            #    c1 = Circle(Point(x, y), s1)
            #    c1.draw(win)
            #    y = ceny - ((sqrt(3) * s1) / 3)
            #    x = s1 + cenx
            #    c2 = Circle(Point(x, y), s1)
            #    c2.draw(win)
            #    x = cenx - s1
            #    c3 = Circle(Point(x, y), s1)
            #    c3.draw(win)


    draw_frac(6, 640, 400, 400)


def circ_spi():
    win = GraphWin("Circle Spiral", 1280, 800)

    def circle_spiral(n, cenx, ceny, s, counter=0):
        if n == 0 or s < 0:
            return 0
        Circle(Point(cenx, ceny), s).draw(win)
        cenx += 5 * sin(counter * pi / 6)
        ceny += 5 * cos(counter * pi / 6)
        circle_spiral(n-1, cenx, ceny, s - 5, (counter + 1) % 12)
    circle_spiral(100, 640, 400, 400)


main()




