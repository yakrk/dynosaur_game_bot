from PIL import ImageGrab, ImageOps
import pyautogui

restart_button_x = 930
restart_button_y = 530
cactus_x = 710
cactus_y = 590
game_over_text_x = 890
game_over_text_y = 475
dark_color = 83

# press restart button
def restart_game():
    global is_game_on
    pyautogui.moveTo(restart_button_x, restart_button_y, duration=0.1)
    pyautogui.click(clicks=1, button='left')
    is_game_on = True

restart_game()
# while game is on,
while is_game_on:
# check if there is a dark area in front of dino
    pix = pyautogui.pixel(cactus_x, cactus_y)
    print(pix)
    if pix[0] == dark_color:
        # if dark area, jump (UP)
        pyautogui.press("up")
    game_over_text = pyautogui.pixel(game_over_text_x, game_over_text_y)
    if game_over_text[0] == dark_color:
        is_game_on = False
        restart_game()