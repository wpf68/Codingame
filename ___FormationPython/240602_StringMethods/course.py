# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    course.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/02 14:26:06 by pwolff            #+#    #+#              #
#    Updated: 2024/06/02 15:53:33 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import time


from pynput import keyboard
# import threading

import pygame



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

# while True:
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         print("w")
#     if keys[pygame.K_s]:
#         print("s")
#     if keys[pygame.K_a]:
#         print("a")
#     if keys[pygame.K_d]:
#         print("d")







# def clavier():
#     def on_press(key):
#         try:
#             print("Alphanumeric key pressed: {0} ".format(key.char))
#         except AttributeError:
#             print("special key pressed: {0}".format(key))


#     def on_release(key):
#         print("Key released: {0}".format(key))
#         if key == keyboard.Key.esc:
#             # Stop listener
#             return False


#     # Collect events until released
#     # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     #     listener.join()
#     touche = keyboard.Listener(on_press=on_press, on_release=on_release)
#     print("*********", touche)
    
#     return (0)





def route():
    route = "- *                         * -"
    posVehicule = 10
    def displayRoute(posX):
        time.sleep(0.02)
        print(route.rjust(posX + len(route)))

    y = 0
    while y < 200000:
        # x = random.randint(-1,1)
        x = clavier()
        # print(x)
        if posVehicule > 0 and posVehicule < 30:
            posVehicule += x
        elif posVehicule == 0:
            posVehicule += 1
        elif posVehicule == 30:
            posVehicule -= 1
        displayRoute(posVehicule)
        y += 1



route()
# t1 = threading.Thread(target = route(posVehicule))
# t2 = threading.Thread(target = clavier)
# t1.start()
# t2.start()