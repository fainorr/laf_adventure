
# --------------------------------------------
# describes the world space as a grid of tiles
# --------------------------------------------

import items, actions, world

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
            moves.append(actions.action_move_east())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.action_move_west())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.action_move_north())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.action_move_south())

        return moves

    # return all available actions in room (by checking for adjacent moves and adding inventory actions)
    def available_actions(self, id):

        self.id = id

        moves = self.adjacent_moves()
        moves.append(actions.view_inventory())

        if self.id == "Starting Room":
            pass
        else:
            moves.append(actions.check_place_for_items())
            moves.append(actions.drop_item())
            moves.append(actions.pickup_item())

        return moves


class starting_room(map_tile):
    def __init__(self, x, y):
        self.id = "Starting Room"
        super(starting_room, self).__init__(x, y)
        super(starting_room, self).available_actions(self.id)

    def intro_text(self):
        return """
        You wake up in Gates hall, your dorm room... Today is the day.
        By sunset, you must collect Lafayette's most valuable items - it's President Byerly's request.
        As you exit, you start taking in your environment like never before.
        """


class campus_space(map_tile, object):
    def __init__(self, x, y, available_items):
        self.items = available_items
        super(campus_space, self).__init__(x, y)
        super(campus_space, self).available_actions(self.id)


# FARINON
# -------

class farinon(campus_space):
    def __init__(self, x, y):
        self.id = "Farinon"
        super(farinon, self).__init__(x, y, [items.banner()])

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
        super(quad, self).__init__(x, y, [items.adirondack_chair("maroon"), items.hammock()])

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
        super(pardee, self).__init__(x, y, [items.tenured_professor()])

    def intro_text(self):
        return """
        Pardee is home to the most academic departments on campus!
        """
