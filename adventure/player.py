
# ---------------------------------------------
# characterize the player and his/her inventory
# ---------------------------------------------

import items, world
import random

class Player():

	def __init__(self):
		self.inventory = [items.textbook("math"), items.phone("Android")]
		self.location_x, self.location_y = world.starting_position
		self.hunt_over = False

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)


	# move to adjacent tile
	# ---------------------

	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy

		tile_name = world.tile_exists(self.location_x, self.location_y)

		# count characters in tile_name.id and print intro text
		num_char = len(tile_name.id)
		print("\n" + "-"*(num_char+6))
		print("-- " + tile_name.id + " --")
		print("-"*(num_char+6))
		print(tile_name.intro_text())

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)


	# view inventory
	# --------------

	def print_inventory(self):
		print("\n        -=( INVENTORY ) =- \n")
		for item in self.inventory:
			print("        " + item.__str__())
		print("\n")


	# check tile for items
	# --------------------

	def check_for_items(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		print("\n        " + tile_name.id + " contains:")
		for item in range(0,len(tile_name.items)):
			print("        - " + tile_name.items[item].__str__())
		print("\n")


	# DROP ITEM FROM INVENTORY
	# ------------------------

	def drop(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		# create string of items available for dropping to show the player
		items_for_drop = ("")
		num_items = len(self.inventory)
		index = 0

		if num_items > 0:
			for item in self.inventory:
				index += 1
				if index < num_items:
					items_for_drop += " '" + item.name + "'"
					if num_items > 2:
						items_for_drop += ","
				else:
					items_for_drop += " or '" + item.name + "'"

			# show player available items and request string input of choice
			print("\n        (options are:" + items_for_drop + ")")

			requested_drop = raw_input("\n        DROP - type the name of item you would like to drop: ")
			item_match = False

			# check choice against tile's items; if match, remove from inventory and add to tile
			for item in self.inventory:
				if requested_drop.lower() == item.name.lower():
					self.inventory.remove(item)
					tile_name.items.append(item)
					item_match = True

			# if input does not match any of the available items, print error message
			if item_match == True:
				print("\n        SUCCESS: you dropped your " + requested_drop + "!\n")
			else:
				print("\n        ERROR: '" + requested_drop + "' does not exist in your inventory...\n")

		else:
			print("\n        Sorry, your inventory does not contain any more items...\n")


	# PICK UP ITEM FROM TILE
	# ----------------------

	def pickup(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		# create string of items available for pick-up to show the player
		items_for_pickup = ("")
		num_items = len(tile_name.items)
		index = 0

		if num_items > 0:
			for item in tile_name.items:
				index += 1
				if index < num_items:
					items_for_pickup += " '" + item.name + "'"
					if num_items > 2:
						items_for_pickup += ","
				else:
					items_for_pickup += " or '" + item.name + "'"

			# show player available items and request string input of choice
			print("\n        (options are:" + items_for_pickup + ")")

			requested_pickup = raw_input("\n        PICK UP - type the name of item you would like to pick up: ")
			item_match = False

			# check choice against tile's items; if match, add to inventory and remove from tile
			for item in tile_name.items:
				if requested_pickup.lower() == item.name.lower():
					self.inventory.append(item)
					tile_name.items.remove(item)
					item_match = True

			# if input does not match any of the available items, print error message
			if item_match == True:
				print("\n        SUCCESS: you pick up one " + requested_pickup + "!\n")
			else:
				print("\n        ERROR: '" + requested_pickup + "' does not exist in " + tile_name.id + "...\n")

		else:
			print("\n        Sorry, " + tile_name.id + " does not contain any more items...\n")


	# END TREASURE HUNT
	# -----------------

	def end(self):

		final_score = 0
		for item in self.inventory:
			final_score += item.value

		self.hunt_over = True

		print("\n        After a long day of treasure hunting across campus, President Byerly awards you...\n")
		print("        ------------")
		print("        FINAL SCORE:    -= [  {}  POINTS  ] =-").format(final_score)
		print("        ------------\n")
