
# ---------------------------------------
# define actions that the player can make
# ---------------------------------------

from player import Player

# the base class for all actions

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
	def __init__(self, tile_name):
		super(action_move_north,self).__init__(name="move north to '" + tile_name.id + "'", method=Player.move_north, hotkey="n")

class action_move_south(action):
	def __init__(self, tile_name):
		super(action_move_south,self).__init__(name="move south to '" + tile_name.id + "'", method=Player.move_south, hotkey="s")

class action_move_east(action):
	def __init__(self, tile_name):
		super(action_move_east,self).__init__(name="move east to '" + tile_name.id + "'", method=Player.move_east, hotkey="e")

class action_move_west(action):
	def __init__(self, tile_name):
		super(action_move_west,self).__init__(name="move west to '" + tile_name.id + "'", method=Player.move_west, hotkey="w")


# INVENTORY ACTIONS
# -----------------

class drop_item(action):
	def __init__(self):
		super(drop_item,self).__init__(name='drop item', method=Player.drop, hotkey="d")

class pickup_item(action):
	def __init__(self):
		super(pickup_item,self).__init__(name='pick up item', method=Player.pickup, hotkey="p")


# GAME ACTIONS
# ------------

class end_hunt(action):
	def __init__(self):
		super(end_hunt,self).__init__(name='treasure hunt', method=Player.end, hotkey="end")
