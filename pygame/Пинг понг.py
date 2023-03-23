# Қыдырғалиева Әйгерім МИ-001, пинг-понг ойыны
from tkinter import *
# random кітапханасын импорттаймыз
import random

# Глобальді айнымалыларды еңгіземіз

# глобальді айнымалылар
# терезе параметрлері
WIDTH = 1300
HEIGHT = 500
# ратетка параметрлері

# ракетка ұзындығы
PAD_W = 20
# ракетка биіктігі
PAD_H = 150

# доп параметрлері
# әр соққы сайын доптың жылдамдығының қаншалықты артуы
BALL_SPEED_UP = 1.05
# доптың максималды жылдамдығы
BALL_MAX_SPEED = 100
# доптың радиусы
BALL_RADIUS = 40

INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

# Ойыншылар ұпайлары
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

# Қашықтыққа жауапты глобальді айнымалыны қосу
# ойын алаңының оң жақ шетіне дейін
right_line_distance = WIDTH - PAD_W


def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        c.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1

        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


def spawn_ball():
    global BALL_X_SPEED
    # Допты центрге қою
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    # Допты жеңілген ойыншының жағына қою,
    # бірақ жылдамдыған басқапқыға дейін төмендетеміз
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)


# доптың серпіліс(отскок) функциясы
def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    # ракеткамен ұру
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED


# терезе орнату
root = Tk()
root.title("Kydyrgalieva Aigerim MI-001, ping-pong game")

# анимация аймағы
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

# ойын алаң элементтері

# сол жақ сызық
c.create_line(PAD_W, 0, PAD_W, HEIGHT, fill="black")
# оң жақ сызық
c.create_line(WIDTH - PAD_W, 0, WIDTH - PAD_W, HEIGHT, fill="black")
# ортаңғы сызық
c.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="black")

# ойын объектілерін орнату

# допты орнату
BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")

# сол жақ ракетка
LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=PAD_W, fill="red")

# оң жақ ракетка
RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="blue")

p_1_text = c.create_text(WIDTH - WIDTH / 6, PAD_H / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 40",
                         fill="white")

p_2_text = c.create_text(WIDTH / 6, PAD_H / 4,
                         text=PLAYER_2_SCORE,
                         font="Arial 40",
                         fill="white")

# доптың жылдамдығы үшін глобальді айнымалылар енгізу
# көлденеңнен
BALL_X_CHANGE = 20
# тігінен
BALL_Y_CHANGE = 0


def move_ball():
    # доптың қабырғаларының және центрінің координаталарын анықтау
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2

    # вертикальді серпіліс
    # Егерде вертикаль сызықтарынан алыс болса - онда допты жылжытыңыз
    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # Егер доп алаң шекарасының оң немесе сол жағына тиіп кетсе
    elif ball_right == right_line_distance or ball_left == PAD_W:
        if ball_right > WIDTH / 2:
            # Егер доп ракетканың ішінде болса, секіреді
            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:
                update_score("left")
                spawn_ball()
        else:
            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()
    # Доптың ойын алаңынан ұшып кетуі мүмкін жағдайын тексеру.
    # Бұл жағдайда допты алаңның шекарасына жылжытамыз.
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left + PAD_W, BALL_Y_SPEED)
    # горизонтальный отскок
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")


# ракеткалардың жылдамдығы үшін глобальді айнымалы мәндерді орнату
# ракеткалардың қозғалыс жылдамдығы
PAD_SPEED = 20
# сол жақ ракетка жылдамдығы
LEFT_PAD_SPEED = 0
# оң жақ ракетка жылдамдығы
RIGHT_PAD_SPEED = 0


# ракеткалардың қозғалыс функциясы
def move_pads():
    # ыңғайлылық үшін сөздік жасаймыз, ракеткаға жылдамдығы сәйкес болғанда
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    # ракеткаларды сұрыптау
    for pad in PADS:
        # ракетканы берілген жылдамдықпен жылжыту
        c.move(pad, 0, PADS[pad])
        # егер ракетка ойын алаңынан шығып кетсе, оны орнына қайтарыңыз
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])


def main():
    move_ball()
    move_pads()
    # әрбір 30 миллисекунд сайын өзін шақырады
    root.after(30, main)


# Фокусты Canvas параметріне ол пернелерді басуға жауап беретіндей етіп орнатыңыз
c.focus_set()


# Пернелерді басу функциясын жазыңыз
def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if (event.keysym == "w") or (event.keysym == "ц"):
        LEFT_PAD_SPEED = -PAD_SPEED
    elif (event.keysym == "s") or (event.keysym == "ы"):
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED

# Бұл функцияны Canvas-қа байланыстыру
c.bind("<KeyPress>", movement_handler)

# Клавишті жібергенде жауап беретін функция жасау
def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0

# Бұл функцияны Canvas-қа байланыстыру
c.bind("<KeyRelease>", stop_pad)

# қозғалысты бастау
main()

# терезенің жұмысын бастау
root.mainloop()
