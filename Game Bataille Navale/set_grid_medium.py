import sys
import pygame
import index
import battle
import json

# setting for the infinity loop
clock = pygame.time.Clock()
FPS = 60

def main():
    import data_map
    listShip = data_map.listShip
    grid = index.Grid(10, (200, 350), listShip)



    with open("players_data.json", "r") as f:
        data = f.read()
        data = json.loads(data)

    if data['mode'] == 'mono':
        button1 = index.Button("Confirm grid", (50, 50), 30)
        button3 = index.Button("WAR", (100, 100), 30)

        running = True

        while running:
            # get the number of target
            target = grid.countTarget()

            clock.tick(FPS)
            index.window.blit(index.bg_img, (0, 0))
            grid.draw()
            if ('grid1' not in data):
                button1.draw()
            if ('grid1' in data):
                button3.draw()
            for ship in listShip:
                ship.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                grid.handle_event(event)
                for ship in listShip:
                    ship.handle_event(event)
                if ('grid1' not in data) and (target == 16):
                    if button1.click(event):
                        data['grid1'] = grid.save()
                        with open("players_data.json", "w") as f:
                            f.write(str(data).replace("\'", "\""))
                        grid.__init__(10, (200, 350), listShip)
                        data_map.reset_listShip()
                        print("Saved Player 1")
                if ('grid1' in data):
                    if button3.click(event):
                        battle.main()

    elif data['mode'] == 'multi':
        button1 = index.Button("Confirm grid of player 1", (50, 50), 30)
        button2 = index.Button("Confirm grid of player 2", (500, 50), 30)
        button3 = index.Button("WAR", (100, 100), 30)

        running = True

        while running:
            # get the number of target
            target = grid.countTarget()

            clock.tick(FPS)
            index.window.blit(index.bg_img, (0, 0))
            grid.draw()
            if ('grid1' not in data):
                button1.draw()
            if ('grid2' not in data):
                button2.draw()
            if ('grid1' in data) and ('grid2' in data):
                button3.draw()
            for ship in listShip:
                ship.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                grid.handle_event(event)
                for ship in listShip:
                    ship.handle_event(event)
                if ('grid1' not in data) and (target == 16):
                    if button1.click(event):
                        data['grid1'] = grid.save()
                        with open("players_data.json", "w") as f:
                            f.write(str(data).replace("\'", "\""))
                        grid.__init__(10, (200, 350), listShip)
                        data_map.reset_listShip()
                if ('grid2' not in data) and (target == 16):
                    if button2.click(event):
                        data['grid2'] = grid.save()
                        with open("players_data.json", "w") as f:
                            f.write(str(data).replace("\'", "\""))
                        grid.__init__(10, (200, 350), listShip)
                        data_map.reset_listShip()
                if ('grid1' in data) and ('grid2' in data):
                    if button3.click(event):
                        battle.main()