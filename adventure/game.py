
# ------------------------------------------------------------
# execute game in pre-set map; reward expert treasure hunters!
# ------------------------------------------------------------

import os
import webbrowser
import world, leaderboard
from player import Player

def play():

    world.load_tiles()
    player = Player()
    tile_name = world.tile_exists(player.location_x, player.location_y)

    os.system('cls' if os.name == 'nt' else 'clear')

    map_url = 'https://drive.google.com/file/d/1Cf2d9SXhKff3Lf30xqqnwsrIPWQNUYrQ/view?usp=sharing'
    webbrowser.open(map_url, new=2, autoraise=True)

    print(tile_name.welcome_text())
    leaderboard.show_leaderboard('intro', 0)
    action_input = str(raw_input("Please type 'go' to start your treasure hunt: "))

    if action_input == "go":
        os.system('cls' if os.name == 'nt' else 'clear')
        player.move(0,0)
    else:
        print("\nGoodbye!\n")
        player.hunt_over = True


    while player.hunt_over == False:

        tile_name = world.tile_exists(player.location_x, player.location_y)

        print("        Choose an action:")
        print("        ----------------- ")
        available_actions = tile_name.available_actions(tile_name.id)

        for action in available_actions:
            print("        " + action.__str__())

        action_input = str(raw_input("\n        ACTION: "))

        action_match = False
        for action in available_actions:
            if action_input.lower() == action.hotkey:
                player.do_action(action, **action.kwargs)
                action_match = True

        if action_match == False:
            print("\n        ERROR: '" + action_input + "' is not a valid action in " + tile_name.id + "...\n\n")


if __name__ == "__main__":
    play()
