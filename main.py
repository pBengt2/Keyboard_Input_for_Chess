import pyautogui
import keyboard

# First time running, use '1' -> '2' -> '3' to set top-left -> top-right -> bottom right positioning of board (click when mouse is over the corners).
SAVED_POS = None  # [2121, 3057, 230, 1168]

X_MAPPING = {'u': 0, 'i': 1, 'o': 2, 'p': 3, 'j': 4, 'k': 5, 'l': 6, ';': 7}
Y_MAPPING = {'q': 0, 'w': 1, 'e': 2, 'r': 3, 'a': 4, 's': 5, 'd': 6, 'f': 7}
CONFIRM_KEYS = 'Space'


def select_board_pos():
    b1, b2, b3 = None, None, None
    while True:
        if b1 and b2 and b3:
            break
        if keyboard.is_pressed('1'):
            b1 = pyautogui.position()
        if keyboard.is_pressed('2'):
            b2 = pyautogui.position()
        if keyboard.is_pressed('3'):
            b3 = pyautogui.position()

    print("(needs to be manually set) SAVED_POS = : [" + str(b1.x) + ", " + str(b2.x) + ", " + str(b1.y) + ", " + str(b3.y) + "]")
    return b1.x, b2.x, b1.y, b3.y


def main():
    if SAVED_POS is None:
        x1, x2, y1, y2 = select_board_pos()
    else:
        x1, x2, y1, y2 = SAVED_POS

    x_inc = (x2 - x1) / 8
    y_inc = (y2 - y1) / 8

    start_x = x1 + (x_inc / 2)
    start_y = y1 + (y_inc / 2)

    cur_y = start_y

    pos = []
    for r in range(8):
        row = []
        cur_x = start_x
        for c in range(8):
            row.append((cur_x, cur_y))
            cur_x += x_inc
        pos.append(row)
        cur_y += y_inc

    x_index = 0
    y_index = 0
    while True:
        if keyboard.is_pressed('Esc'):
            break

        if keyboard.is_pressed('Space'):
            pyautogui.click()
            continue

        pressed = False
        for current_key in X_MAPPING.keys():
            if keyboard.is_pressed(current_key):
                if current_key in X_MAPPING:
                    x_index = X_MAPPING[current_key]
                    pressed = True
                    break

        for current_key in Y_MAPPING.keys():
            if keyboard.is_pressed(current_key):
                if current_key in Y_MAPPING:
                    y_index = Y_MAPPING[current_key]
                    pressed = True
                    break

        if pressed:
            pyautogui.moveTo(pos[x_index][y_index])


if __name__ == '__main__':
    main()
