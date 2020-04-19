
# ---------------------------------------
# define actions that the player can make
# ---------------------------------------

from player import Player

# base class for all options

class action(object):

	def __init__(self, name, method, hotkey, **kwargs):

		# method = the function to execute to perform this action
		# hotkey = the keyboard key the player should use to initiate this action

		self.name = name
		self.method = method
		self.hotkey = hotkey
		self.kwargs = kwargs

	def __str__(self):
		return "{0}: {1}".format(self.hotkey, self.name)


# MOVING ACTIONS
# --------------

class action_move_north(action):
	def __init__(self):
		super(action_move_north,self).__init__(name='move north', method=Player.move_north, hotkey="n")

class action_move_south(action):
	def __init__(self):
		super(action_move_south,self).__init__(name='move south', method=Player.move_south, hotkey="s")

class action_move_east(action):
	def __init__(self):
		super(action_move_east,self).__init__(name='move east', method=Player.move_east, hotkey="e")

class action_move_west(action):
	def __init__(self):
		super(action_move_west,self).__init__(name='move west', method=Player.move_west, hotkey="w")


# INVENTORY ACTIONS
# -----------------

class view_inventory(action):
	def __init__(self):
		super(view_inventory,self).__init__(name='view inventory', method=Player.print_inventory, hotkey="i")

class check_place_for_items(action):
	def __init__(self):
		super(check_place_for_items,self).__init__(name='check for items', method=Player.check_for_items, hotkey="c")

class drop_item(action):
	def __init__(self):
		super(drop_item,self).__init__(name='drop item', method=Player.drop, hotkey="d")

class pickup_item(action):
	def __init__(self):
		super(pickup_item,self).__init__(name='pick up item', method=Player.pickup, hotkey="p")
