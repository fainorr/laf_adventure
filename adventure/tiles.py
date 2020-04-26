
# --------------------------------------------
# describes the world space as a grid of tiles
# --------------------------------------------

import items, actions, world
import random

# the base class for all map tiles

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


# STARTING ROOM: McKEEN
# ---------------------

class starting_room(campus_space):
    def __init__(self, x, y):
        self.id = "McKeen"
        tile_items = [items.phone()]

        super(starting_room, self).__init__(x, y, tile_items)

    def intro_text(self):
        return """
        You wake up in McKeen hall, your dorm room... Today is the day.
        By sunset, you must collect Lafayette's most valuable items - it's President Byerly's request.
        As you exit, you start taking in your environment like never before.

        Before you leave, remember to take your phone! Try picking it up with 'p' (note: all commands are not case-sensitive)
        """

    def welcome_text(self):
        return """

        -----------------------------------------------
        Welcome to the Virtual Lafayette Treasure Hunt!
        -----------------------------------------------

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
        tile_items = [items.banner(), items.fireplace(), items.napkin_basket(), items.quesadilla(), items.newspaper()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(farinon, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        With its hand-painted banners hanging in the atrium and tasty food options available
        through midnight, the student center is a bustling hub for the student body.
        """

# WATSON COURTS
# -------------

class watson_courts(campus_space):
    def __init__(self, x, y):
        self.id = "Watson Courts"
        tile_items = [items.brick(), items.grill(), items.lead_paint(), items.toilet_paper(), items.RA()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(watson_courts, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Initially constructed as temporary housing units, the 'Courts' are now just as temporary
        as March Hall is beginning to seem...
        """

# THE QUAD
# --------

class quad(campus_space):
    def __init__(self, x, y):
        self.id = "The Quad"
        tile_items = [items.adirondack_chair(), items.hammock(), items.quadler(), items.quad_elm(), items.beer_can()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(quad, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Filled with students on a warm spring day, this green space is home to frisbee games,
        slacklining lessons, hammocking hangouts, and old tree climbs.
        """

# PARDEE
# ------

class pardee(campus_space):
    def __init__(self, x, y):
        self.id = "Pardee"
        tile_items = [items.stained_glass(), items.tenured_professor(), items.pencil(), items.fire_extinguisher(), items.textbook()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(pardee, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Not only home to the most academic departments on campus, Pardee is also rumoured to
        contain emergency firearms on its mysterious and unreachable 5th floor.
        """

# ZETA PSI
# --------

class zeta_psi(campus_space):
    def __init__(self, x, y):
        self.id = "Zeta Psi"
        tile_items = [items.pool_table(), items.chef(), items.keg(), items.shampoo(), items.speaker()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(zeta_psi, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Lafayette's newest fraternity, re-chartered in 2018 after a five-year suspension, is
        back in full-swing with its house dog Miss Pineapple!
        """

# SKILLMAN
# --------

class skillman(campus_space):
    def __init__(self, x, y):
        self.id = "Skillman"
        tile_items = [items.novel(), items.punchcard(), items.printer(), items.special_collection(), items.backpack()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(skillman, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        The recently rennovated library where a sole 3-D printer endlessly makes unrecognizable
        objects, students file through the cafe for yet-another coffee, and numerous study rooms
        sit occupied with only a set of unattended books.
        """

# MARKLE
# ------

class markle(campus_space):
    def __init__(self, x, y):
        self.id = "Markle"
        tile_items = [items.flag(), items.tour_guide(), items.add_drop(), items.brochure()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(markle, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        An observatory-turned-admissions building, Markle's visitation office welcomes thousands
        of families so prospective students can find their next four-year home.
        """

# FISHER FIELD
# ------------

class fisher_field(campus_space):
    def __init__(self, x, y):
        self.id = "Fisher Field"
        tile_items = [items.helmet(), items.football(), items.goalpost(), items.bleacher(), items.mascot()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(fisher_field, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Home to the Patriot League runner-ups of the 2019 football season, Fisher Field hosts
        roughly six games each season with less-than-impressive attendance.  It may come as no
        surprise, then, that the field's west end was once the site of the Easton City Dump!
        """

# BUSHKILL LOT
# ------------

class bushkill_lot(campus_space):
    def __init__(self, x, y):
        self.id = "Bushkill Lot"
        tile_items = [items.car(), items.parking_pass(), items.security_cam()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,1)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(bushkill_lot, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Lafayette's newest and furthest option for parking, a real upgrade for no-one.
        """

# COLLEGE HILL TAVERN
# -------------------

class cht(campus_space):
    def __init__(self, x, y):
        self.id = "College Hill Tavern"
        tile_items = [items.pint(), items.fake_id(), items.karaoke(), items.townie(), items.neon_sign()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(cht, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        More than just your local neighborhood bar, this infamous host of Wednesday night karaoke
        is a popular destination for Lafayette's drinking elite to gather and mingle.
        """

# ACOPIAN
# -------

class acopian(campus_space):
    def __init__(self, x, y):
        self.id = "Acopian"
        tile_items = [items.calculator(), items.formula_car(), items.steel_bridge(), items.oscilloscope(), items.raspberry_pi(), items.printer_3D()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(acopian, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Priding itself as the nation's 11th best undergraduate engineering program for schools
        where doctorates are not offered, Lafayette's engineering program inhabits this Frankenstein
        of a building, offering formal coursework, high-tech equipment, and even overnight lodging!
        """

# ROCKWELL
# --------

class rockwell(campus_space):
    def __init__(self, x, y):
        self.id = "Rockwell"
        tile_items = [items.beaker(), items.microscope(), items.pink_chair(), items.smoothie(), items.water_bottle()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(rockwell, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        The largest capital project in Lafayette's history provides students with impressive study
        spaces and new classroom environments - all while consuming minimal energy.
        """

# WATSON
# ------

class watson(campus_space):
    def __init__(self, x, y):
        self.id = "Watson"
        tile_items = [items.microwave(), items.first_year(), items.toothbrush()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,1)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(watson, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        One of Lafayette's first-year housing options and the site of 'wellness housing', this
        dorm is one of the most photographed locations on campus.
        """

# MARCH FIELD
# -----------

class march_field(campus_space):
    def __init__(self, x, y):
        self.id = "March Field"
        tile_items = [items.flower(), items.lawnmower(), items.frisbee()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,1)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(march_field, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        The original host of Lafayette athletics, this treeless yard is now surrounded by
        student residences and fraternity houses.
        """

# MARQUIS
# -------

class marquis(campus_space):
    def __init__(self, x, y):
        self.id = "Marquis"
        tile_items = [items.crepe(), items.cookie(), items.mint(), items.wings(), items.squash()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(marquis, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        As the largest dining hall on campus, Marquis also offers the most diverse menu in
        a nice and homey environment - just don't get there late for lunch.
        """

# KIRBY
# -----

class kirby(campus_space):
    def __init__(self, x, y):
        self.id = "Kirby"
        tile_items = [items.painting(), items.history_book(), items.bust(), items.ladder(), items.globe()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(kirby, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Donated by a highly successful entrepreneur, this building was a controversial Lafayette
        enterprise that has now turned into an iconic site for the government and law department,
        featuring a grand library and historical artifacts.
        """

# SOUTH
# -----

class south(campus_space):
    def __init__(self, x, y):
        self.id = "South"
        tile_items = [items.piano(), items.sign_420(), items.shower_curtain(), items.red_solo()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,1)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(south, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        South hall is the largest residence hall on campus, originally designed and constructed
        by Lafayette's first president George Junkin in the 1830s.  Now it offers large rooms
        and equally large freshmen gatherings in its new basement.
        """

# ARTS CAMPUS
# -----------

class arts_campus(campus_space):
    def __init__(self, x, y):
        self.id = "The Arts Campus"
        tile_items = [items.paintbrush(), items.pottery_wheel(), items.drafting_table(), items.student_film(), items.music_stand()]

        chosen_items = []
        for pick in range(0,len(tile_items)-random.randint(0,2)):
            choice = random.choice(tile_items)
            tile_items.remove(choice)
            chosen_items.append(choice)

        super(arts_campus, self).__init__(x, y, chosen_items)

    def intro_text(self):
        return """
        Comprised of four buildings, the arts campus off the hill offers collarborative studio spaces
        for film, performing arts, and visual arts and showcases plenty of student artwork year-round.
        """
