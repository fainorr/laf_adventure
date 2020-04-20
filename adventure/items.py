
# ----------------------------------------------
# defines the items encountered in the adventure
# ----------------------------------------------

from random import *

# The base classes for all items

class item(object):

	def __init__(self, name, description, value, size):
		self.name = name
		self.description = description
		self.value = value
		self.size = size

	def __str__(self):
		return "{0} (size = {1}): {2}".format(self.name, self.size, self.description)


# STARTING ITEMS
# --------------

class phone(item):
	def __init__(self):

		phone_choices = ["iPhone", "Android", "flip phone"]
		phone_values = [20, 10, -10]

		i = randint(0,len(phone_choices)-1)
		self.type = phone_choices[i]
		self.value = phone_values[i]

		super(phone,self).__init__(name = "Cell Phone",
						 description = "cause you'd never be caught without your {0}.".format(self.type),
						 value = self.value,
						 size = 3)


# FARINON ITEMS
# -------------

class banner(item):
	def __init__(self):

		super(banner,self).__init__(name = "Banner",
						 description = "a cheap, homemade club advertisement.",
						 value = 6,
						 size = 10)


# QUAD ITEMS
# ----------

class adirondack_chair(item):
	def __init__(self):

		color_choices = ["black", "blue", "white", "maroon"]
		color_values = [80, 100, 150, 200]

		i = randint(0,len(color_choices)-1)
		self.color = color_choices[i]
		self.value = color_values[i]

		super(adirondack_chair,self).__init__(name="Adirondack Chair",
						 description="an icon of quad relaxation, painted {0}.".format(self.color),
						 value=self.value,
						 size=20)

class hammock(item):
	def __init__(self):

		super(hammock,self).__init__(name = "Hammock",
						 description = "perfect for sprawling between two trees.",
						 value = 20,
						 size = 5)

class quadler(item):
	def __init__(self):

		self.size = randint(10,14)

		super(quadler,self).__init__(name = "Quadler",
						 description = "one of Lafayette's brightest students.",
						 value = -40,
						 size = self.size)

class quad_elm(item):
	def __init__(self):

		age_choices = [20, 20, 20, 20, 20, 65, 65, 145]
		age_values = [160, 160, 160, 160, 160, 300, 300, 480]
		age_sizes = [40, 40, 40, 40, 40, 50, 50, 65]

		i = randint(0,len(age_choices)-1)
		self.age = age_choices[i]
		self.value = age_values[i]
		self.size = age_sizes[i]

		super(quad_elm,self).__init__(name = "Quad Elm",
						 description = "a {0} year old tree for sitting beneath (or climbing).".format(self.age),
						 value = self.value,
						 size = self.size)

class beer_can(item):
	def __init__(self):

		super(beer_can,self).__init__(name = "Beer Can",
						 description = "a keepsake from Wednesday night's formal at Campus Pizza",
						 value = 10,
						 size = 2)


# PARDEE ITEMS
# -------------

class stained_glass(item):
	def __init__(self):

		window_sizes = [16, 20, 22, 22, 24, 24]

		i = randint(0,len(window_sizes)-1)
		self.size = window_sizes[i]

		super(stained_glass,self).__init__(name = "Stained Glass Window",
						 description = "it's rumoured to be crafted by Lafayette's first leopard mascot.",
						 value = 150,
						 size = self.size)

class tenured_professor(item):
	def __init__(self):

		super(tenured_professor,self).__init__(name = "Tenured Professor",
						 description = "an essential asset to any liberal arts institution.",
						 value = 25,
						 size = 18)

class fire_extinguisher(item):
	def __init__(self):

		super(fire_extinguisher,self).__init__(name = "Fire Extinguisher",
						 description = "can't be over-prepared, considering Pardee's history...",
						 value = 60,
						 size = 12)

class textbook(item):
	def __init__(self):

		subject_choices = ["math", "biology", "neuroscience", "mechanical engineering"]
		subject_sizes = [8, 12, 6, 4]
		subject_values = [35, 45, 35, 45]

		i = randint(0,len(subject_choices)-1)
		self.subject = subject_choices[i]
		self.size = subject_sizes[i]
		self.value = subject_values[i]

		super(textbook, self).__init__(name = "Textbook",
						 description = "a way-too-heavy {0} textbook (why would carry this around, anyway?).".format(self.subject),
						 value = self.value,
						 size = self.size)

class pencil(item):
	def __init__(self):

		engraving_choices = ["DuoPush Rocks!", "Don't Do Drugs", "Live, Laf, Love"]
		engraving_values = [-10, 10, 20]

		i = randint(0,len(engraving_choices)-1)
		self.engraving = engraving_choices[i]
		self.value = engraving_values[i]

		super(pencil,self).__init__(name = "Pencil",
						 description = "a classic wooden pencil, carefully engraved with '{0}'.".format(self.engraving),
						 value = self.value,
						 size = 2)
