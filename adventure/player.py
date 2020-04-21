
# ---------------------------------------------
# characterize the player and his/her inventory
# ---------------------------------------------

import os
import items, world, scoreboard
import random

class Player():

	def __init__(self):
		self.inventory = []
		self.location_x, self.location_y = world.starting_position
		self.hunt_over = False

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)


	# MOVE TO ADJACENT TILE
	# ---------------------

	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy

		tile_name = world.tile_exists(self.location_x, self.location_y)

		os.system('cls' if os.name == 'nt' else 'clear')

		# count characters in tile_name.id and print intro text
		num_char = len(tile_name.id)
		print("\n" + "-"*(num_char+6))
		print("-- " + tile_name.id + " --")
		print("-"*(num_char+6))
		print(tile_name.intro_text())

		self.check_for_items()
		self.print_inventory()

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)


	# VIEW INVENTORY
	# --------------

	def print_inventory(self):

		inv_filled = 0
		for item in self.inventory:
			inv_filled += item.size

		print("\n        CURRENT INVENTORY: (" + str(inv_filled) + "/100 full)")
		for item in self.inventory:
			print("        - " + item.__str__())
		print("\n")


	# CHECK TILE FOR ITEMS
	# --------------------

	def check_for_items(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		print("        " + tile_name.id.upper() + " CONTAINS:")
		for item in range(0,len(tile_name.items)):
			print("        - " + tile_name.items[item].__str__())


	# DROP ITEM FROM INVENTORY
	# ------------------------

	def drop(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		# create string of items available for dropping to show the player
		items_for_drop = ("")
		num_items = len(self.inventory)
		index = 0

		if num_items > 0:
			if num_items > 1:
				for item in self.inventory:
					index += 1
					if index < num_items:
						items_for_drop += " '" + item.name + "'"
						if num_items > 2:
							items_for_drop += ","
					else:
						items_for_drop += " or '" + item.name + "'"
			else:
				items_for_drop += " '" + self.inventory[0].name + "'"

			# show player available items and request string input of choice
			print("\n        (options include:" + items_for_drop + ")")

			requested_drop = raw_input("\n        DROP - type the name of item you would like to drop: ")
			item_match = False

			# check choice against tile's items
			for item in self.inventory:
				if requested_drop.lower() == item.name.lower():
					item_match = True
					dropped_item = item

			# if input matches, remove from inventory and add to tile; otherwise, print error message
			if item_match == True:
				self.inventory.remove(dropped_item)
				tile_name.items.append(dropped_item)
				print("\n        SUCCESS: you dropped your '" + dropped_item.name + "'!\n\n")
				self.move(0,0)
			else:
				print("\n        ERROR: '" + requested_drop + "' does not exist in your inventory...\n\n")

		else:
			print("\n        Sorry, your inventory does not contain any more items...\n\n")


	# PICK UP ITEM FROM TILE
	# ----------------------

	def pickup(self):

		tile_name = world.tile_exists(self.location_x, self.location_y)

		# create string of items available for pick-up to show the player
		items_for_pickup = ("")
		num_items = len(tile_name.items)
		index = 0

		if num_items > 0:
			if num_items > 1:
				for item in tile_name.items:
					index += 1
					if index < num_items:
						items_for_pickup += " '" + item.name + "'"
						if num_items > 2:
							items_for_pickup += ","
					else:
						items_for_pickup += " or '" + item.name + "'"
			else:
				items_for_pickup += " '" + tile_name.items[0].name + "'"

			# show player available items and request string input of choice
			print("\n        (options include:" + items_for_pickup + ")")

			requested_pickup = raw_input("\n        PICK UP - type the name of item you would like to pick up: ")
			item_match = False
			space_left = False

			inv_filled = 0
			for item in self.inventory:
				inv_filled += item.size

			# check choice against tile's items and inventory space
			for item in tile_name.items:
				if requested_pickup.lower() == item.name.lower():
					item_match = True
					pickup_item = item
					if item.size + inv_filled < 100:
						space_left = True

			# if input matches, add to inventory if space left and remove from tile; otherwise, print error message
			if item_match == True:
				if space_left == True:
					self.inventory.append(pickup_item)
					tile_name.items.remove(pickup_item)
					print("\n        SUCCESS: you pick up one '" + pickup_item.name + "'!\n\n")
					self.move(0,0)
				else:
					print("\n        ERROR: not enough space in inventory for '" + pickup_item.name + "'!\n\n")
			else:
				print("\n        ERROR: '" + requested_pickup + "' does not exist in " + tile_name.id + "...\n\n")

		else:
			print("\n        Sorry, '" + tile_name.id + "' does not contain any more items...\n\n")


	# END TREASURE HUNT
	# -----------------

	def end(self):

		os.system('cls' if os.name == 'nt' else 'clear')

		# calculate final score
		final_score = 0
		for item in self.inventory:
			final_score += item.value

		player_name = str(raw_input("\nPlease enter your name: "))

		# send final score for leaderboard
		scoreboard.send_score(player_name, final_score, self.inventory)

		self.hunt_over = True

		print("\n        After a long day of treasure hunting across campus, President Byerly awards you...\n")
		print("        ------------")
		print("        FINAL SCORE:    -= [  {}  POINTS  ] =-").format(final_score)
		print("        ------------\n")
