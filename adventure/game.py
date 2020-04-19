
# ------------------------------------------------------------
# execute game in pre-set map; reward expert treasure hunters!
# ------------------------------------------------------------

import world
from player import Player

def play():

    world.load_tiles()
    player = Player()
    tile_name = world.tile_exists(player.location_x, player.location_y)

    # count characters in tile_name.id and print intro text
    num_char = len(tile_name.id)
    print("\n" + "-"*(num_char+6))
    print("-- " + tile_name.id + " --")
    print("-"*(num_char+6))
    print(tile_name.intro_text())

    while player.hunt_over == False:

        tile_name = world.tile_exists(player.location_x, player.location_y)

        print("Choose an action: \n----------------- ")
        available_actions = tile_name.available_actions(tile_name.id)

        for action in available_actions:
            print(action)

        action_input = str(raw_input("\nACTION: "))

        action_match = False
        for action in available_actions:
            if action_input == action.hotkey:
                player.do_action(action, **action.kwargs)
                action_match = True

        if action_match == False:
            print("\n        ERROR: '" + action_input + "' is not a valid action in " + tile_name.id + "...\n")


if __name__ == "__main__":
    play()
