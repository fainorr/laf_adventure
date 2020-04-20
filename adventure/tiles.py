
# --------------------------------------------
# describes the world space as a grid of tiles
# --------------------------------------------

import items, actions, world
import random

# The base class for all map tiles

class map_tile(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    # determine all possible actions to move to adjacent tiles
    def adjacent_moves(self):

        moves = []

        if world.tile_exists(self.x + 1, self.y):
            tile_name = world.tile_exists(self.x + 1, self.y)
            moves.append(actions.action_move_east(tile_name))
        if world.tile_exists(self.x - 1, self.y):
            tile_name = world.tile_exists(self.x - 1, self.y)
            moves.append(actions.action_move_west(tile_name))
        if world.tile_exists(self.x, self.y - 1):
            tile_name = world.tile_exists(self.x, self.y - 1)
            moves.append(actions.action_move_north(tile_name))
        if world.tile_exists(self.x, self.y + 1):
            tile_name = world.tile_exists(self.x, self.y + 1)
            moves.append(actions.action_move_south(tile_name))

        return moves

    # return all available actions in room (by checking for adjacent moves and adding inventory actions)
    def available_actions(self, id):

        self.id = id

        moves = self.adjacent_moves()
        moves.append(actions.drop_item())
        moves.append(actions.pickup_item())
        moves.append(actions.end_hunt())

        return moves


class campus_space(map_tile, object):
    def __init__(self, x, y, available_items):
        self.items = available_items
        super(campus_space, self).__init__(x, y)
        super(campus_space, self).available_actions(self.id)


# STARTING ROOM: GATES
# --------------------

class starting_room(campus_space):
    def __init__(self, x, y):
        self.id = "Gates"
        tile_items = [items.phone()]

        super(starting_room, self).__init__(x, y, tile_items)

    def intro_text(self):
        return """
        You wake up in Gates hall, your dorm room... Today is the day.
        By sunset, you must collect Lafayette's most valuable items - it's President Byerly's request.
        As you exit, you start taking in your environment like never before.

        Before you leave, remember to take your phone! Try picking it up with 'p'.
        """

    def welcome_text(self):
        return """

        ----------------------------------------------
        Welcome to the Virtual Lafyette Treasure Hunt!
        ----------------------------------------------

        Fit for anyone familiar with the quips and quirks of Lafayette College, this interactive
        choose-your-own-adventure will take you all around campus (as if you were there in person!).

        More specifically, your task is a treasure hunt, one of collecting the greatest riches the
        campus has to offer.  You will need to make choices about where to travel and what to keep
        in your backpack - you only have limited inventory space. When your search is complete, you
        will present your bounty to President Byerly for her to judge. Good luck!
        """


# FARINON
# -------

class farinon(campus_space):
    def __init__(self, x, y):
        self.id = "Farinon"
        tile_items = [items.banner()]

        chosen_items = []
        for pick in range(0,len(tile_items)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(farinon, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Farinon with its hand-painted banners, napkin baskets, and unhealty food options.
        Nothing beats it.
        """

# THE QUAD
# --------

class quad(campus_space):
    def __init__(self, x, y):
        self.id = "The Quad"
        tile_items = [items.adirondack_chair(), items.hammock(), items.quadler(), items.quad_elm(), items.beer_can()]

        chosen_items = []
        for pick in range(0,len(tile_items)-1):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(quad, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Ah yes, the quad... The sun is shining and it is filled with student.
        Most importantly, you notice the adirondack chairs and numerous camping hammocks.
        """

# PARDEE
# ------

class pardee(campus_space):
    def __init__(self, x, y):
        self.id = "Pardee"
        tile_items = [items.stained_glass(), items.tenured_professor(), items.pencil(), items.fire_extinguisher(), items.textbook()]

        chosen_items = []
        for pick in range(0,len(tile_items)-1):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(pardee, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Pardee is home to the most academic departments on campus!
        """
