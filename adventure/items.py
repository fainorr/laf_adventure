
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
						 description = "cause you'd never be caught without your {0}".format(self.type),
						 value = self.value + randint(-3,3),
						 size = 3)


# FARINON ITEMS
# -------------

class banner(item):
	def __init__(self):

		super(banner,self).__init__(name = "Banner",
						 description = "a cheap, homemade club advertisement",
						 value = 22 + randint(-5,5),
						 size = 10)

class fireplace(item):
	def __init__(self):

		super(fireplace,self).__init__(name = "Fireplace",
						 description = "said to be the the sole remains of the Delta Upsilon House that formerly occupied the site",
						 value = 200 + randint(-25,25),
						 size = 35)

class quesadilla(item):
	def __init__(self):

		super(quesadilla,self).__init__(name = "Quesadilla",
						 description = "one of Lower's most popular late-night features",
						 value = 45 + randint(-8,8),
						 size = 4)

class napkin_basket(item):
	def __init__(self):

		super(napkin_basket,self).__init__(name = "Napkin Basket",
						 description = "as an easy target for student theft, these frequently disappear...",
						 value = 10 + randint(-2,2),
						 size = 5)

class newspaper(item):
	def __init__(self):

		headline_choices = ["Incredulous Uber Eats driver receives parking ticket while dropping off pizza at South College",\
		 					"Varsity teams to hold Zoom practices",\
							"Quidditch team wins first major tournament in club history"]
		headline_values = [18, 34, 42]

		i = randint(0,len(headline_choices)-1)
		self.headline = headline_choices[i]
		self.value = headline_values[i]

		super(newspaper,self).__init__(name = "Newspaper",
						 description = "with a headline that reads:\n                               '{0}'".format(self.headline),
						 value = self.value + randint(-3,3),
						 size = 6)


# WATSON COURTS ITEMS
# -------------------

class lead_paint(item):
	def __init__(self):

		super(lead_paint,self).__init__(name = "Lead Paint",
						 description = "a silent killer, abundant and rusty-red in color",
						 value = -10 + randint(-2,2),
						 size = 2)

class toilet_paper(item):
	def __init__(self):

		size_choices = ["4", "4", "4", "6", "6", "rare 8", "supersized 12"]
		size_values = [28, 28, 28, 36, 36, 48, 65]
		size_sizes = [5, 5, 5, 6, 6, 8, 10]

		i = randint(0,len(size_choices)-1)
		self.roll_size = size_choices[i]
		self.value = size_values[i]
		self.size = size_sizes[i]

		super(toilet_paper,self).__init__(name = "Toilet Paper",
						 description = "a {0}-inch roll essential for any pandemic".format(self.roll_size),
						 value = self.value + randint(-5,5),
						 size = self.size)

class RA(item):
	def __init__(self):

		super(RA,self).__init__(name = "RA",
						 description = "an administrative resource for suite-style living",
						 value = 45,
						 size = 16)

class grill(item):
	def __init__(self):

		super(grill,self).__init__(name = "Grill",
						 description = "a classic, charcoal-burning cooking option",
						 value = 85 + randint(-15,15),
						 size = 22)

class brick(item):
	def __init__(self):

		super(brick,self).__init__(name = "Loose Brick",
						 description = "falling out, probably because the courts weren't built as a permanent accomodation...",
						 value = 20 + randint(-4,4),
						 size = 6)


# QUAD ITEMS
# ----------

class adirondack_chair(item):
	def __init__(self):

		color_choices = ["black", "blue", "white", "maroon"]
		color_values = [80, 100, 120, 140]

		i = randint(0,len(color_choices)-1)
		self.color = color_choices[i]
		self.value = color_values[i]

		super(adirondack_chair,self).__init__(name="Adirondack Chair",
						 description="an icon of quad relaxation, painted {0}".format(self.color),
						 value=self.value + randint(-30,30),
						 size=20)

class hammock(item):
	def __init__(self):

		super(hammock,self).__init__(name = "Hammock",
						 description = "perfect for sprawling between two trees",
						 value = 20 + randint(-3,3),
						 size = 5)

class quadler(item):
	def __init__(self):

		self.size = randint(10,14)

		super(quadler,self).__init__(name = "Quadler",
						 description = "one of Lafayette's brightest future students",
						 value = -30 + randint(-10,10),
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
						 description = "a {0} year old tree for sitting beneath (or climbing)".format(self.age),
						 value = self.value + randint(-40,40),
						 size = self.size)

class beer_can(item):
	def __init__(self):

		super(beer_can,self).__init__(name = "Beer Can",
						 description = "a keepsake from Wednesday night's formal at Campus Pizza",
						 value = 10 + randint(-2,2),
						 size = 3)


# PARDEE ITEMS
# ------------

class stained_glass(item):
	def __init__(self):

		window_sizes = [16, 20, 22, 22, 24, 24]

		i = randint(0,len(window_sizes)-1)
		self.size = window_sizes[i]

		super(stained_glass,self).__init__(name = "Stained Glass Window",
						 description = "it's rumoured to be crafted by Lafayette's first leopard mascot",
						 value = 150 + randint(-20,20),
						 size = self.size)

class tenured_professor(item):
	def __init__(self):

		super(tenured_professor,self).__init__(name = "Tenured Professor",
						 description = "an essential asset to any liberal arts institution",
						 value = 75 + randint(-15,15),
						 size = 18)

class fire_extinguisher(item):
	def __init__(self):

		super(fire_extinguisher,self).__init__(name = "Fire Extinguisher",
						 description = "can't be over-prepared, considering Pardee's history...",
						 value = 60 + randint(-10,10),
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
						 description = "a way-too-heavy {0} textbook (why would carry this around, anyway?)".format(self.subject),
						 value = self.value + randint(-6,6),
						 size = self.size)

class pencil(item):
	def __init__(self):

		engraving_choices = ["DuoPush Rocks!", "Class of 20-Fun", "Don't Do Drugs", "Live, Laf, Love"]
		engraving_values = [-10, 0, 10, 20]

		i = randint(0,len(engraving_choices)-1)
		self.engraving = engraving_choices[i]
		self.value = engraving_values[i]

		super(pencil,self).__init__(name = "Pencil",
						 description = "a classic wooden pencil, carefully engraved with '{0}'".format(self.engraving),
						 value = self.value + randint(-3,3),
						 size = 2)


# ZETA PSI ITEMS
# --------------

class pool_table(item):
	def __init__(self):

		super(pool_table,self).__init__(name = "Pool Table",
						 description = "fit for any common room",
						 value = 62 + randint(-12,12),
						 size = 24)

class chef(item):
	def __init__(self):

		food_choices = ["grilled cheese", "beef stew", "broccoli cheddar soup", "triple-decker chocolate cake"]
		food_values = [96, 82, 68, 112]

		i = randint(0,len(food_choices)-1)
		self.food = food_choices[i]
		self.value = food_values[i]

		super(chef,self).__init__(name = "Chef",
						 description = "famous for making a gourmet {0}".format(self.food),
						 value = self.value + randint(-15,15),
						 size = 18)

class beer_case(item):
	def __init__(self):

		super(beer_case,self).__init__(name = "Beer Case",
						 description = "flattened and empty, hanging on the wall as some sort of 'trophy'",
						 value = 8 + randint(-2,2),
						 size = 4)

class shampoo(item):
	def __init__(self):

		super(shampoo,self).__init__(name = "Shampoo",
						 description = "a three-in-one bottle of shampoo / conditioner / bodywash",
						 value = 12 + randint(-2,2),
						 size = 3)


# SKILLMAN ITEMS
# --------------

class punchcard(item):
	def __init__(self):

		super(punchcard,self).__init__(name = "Punchcard",
						 description = "enjoy every 10th cup of coffee, on the school",
						 value = 6 + randint(-2,2),
						 size = 2)

class printer(item):
	def __init__(self):

		super(printer,self).__init__(name = "Printer",
					 description = "someone said printing is free... does that include a printer, too?",
					 value = 56 + randint(-12,12),
					 size = 15)

class special_collection(item):
	def __init__(self):

		desc_choices = ["letters written by Marquis de Lafayette during the Revolutionary War",\
		 				"letters written by Marquis de Lafayette during the Revolutionary War",\
						"commemorative stamps from the 19th century depicting the Marquis",\
						"commemorative stamps from the 19th century depicting the Marquis",\
						"commemorative stamps from the 19th century depicting the Marquis",\
						"an embroidered waistcoat worn by Lafayette",\
						"an 18th-century Charleville musket brought by Lafayette to America",\
						"a ring containing a lock of the Marquis's hair"]
		desc_values = [26, 26, 14, 14, 14, 52, 88, 10]
		desc_sizes = [5, 5, 3, 3, 3, 8, 12, 2]

		i = randint(0,len(desc_choices)-1)
		self.desc = desc_choices[i]
		self.value = desc_values[i]
		self.size = desc_sizes[i]

		super(special_collection,self).__init__(name = "Special Collection",
					 description = self.desc,
					 value = self.value + randint(-5,5),
					 size = self.size)

class novel(item):
	def __init__(self):

		topic_choices = ["first love", "bullying", "a murder mystery"]
		topic_values = [12, 8, 22]

		i = randint(0,len(topic_choices)-1)
		self.topic = topic_choices[i]
		self.value = topic_values[i]

		super(novel,self).__init__(name = "Novel",
					 description = "a compelling piece of young adult fiction about {0}".format(self.topic),
					 value = self.value + randint(-2,2),
					 size = 4)

class backpack(item):
	def __init__(self):

		super(backpack,self).__init__(name = "Backpack",
					 description = "unattended and left behind in a study room",
					 value = 20 + randint(-5,5),
					 size = 9)


# MARKLE ITEMS
# ------------

class brochure(item):
	def __init__(self):

		super(brochure,self).__init__(name = "Admissions Brochure",
					 description = "a summary of the facts and figures that all prospective dads love",
					 value = 12 + randint(-3,3),
					 size = 3)

class add_drop(item):
	def __init__(self):

		super(add_drop,self).__init__(name = "Add/Drop Form",
					 description = "for when you're still figuring out your course plan",
					 value = -4 + randint(-2,2),
					 size = 2)

class tour_guide(item):
	def __init__(self):

		year_choices = ["freshman", "sophomore", "junior", "senior"]
		year_values = [58, 72, 80, 98]

		i = randint(0,len(year_choices)-1)
		self.year = year_choices[i]
		self.value = year_values[i]

		super(tour_guide,self).__init__(name = "Tour Guide",
					 description = "a {0} student, master of charisma and dealing with tricky parents".format(self.year),
					 value = self.value + randint(-8,8),
					 size = 16)

class flag(item):
	def __init__(self):

		super(flag,self).__init__(name = "Flag",
					 description = "lettered with 'Lafayette', hanging as a pennant of prestige",
					 value = 34 + randint(-6,6),
					 size = 12)


# FISHER FIELD ITEMS
# ------------------

class football(item):
	def __init__(self):

		super(football,self).__init__(name = "Football",
					 description = "not even a game ball",
					 value = 22 + randint(-3,3),
					 size = 6)

class bleacher(item):
	def __init__(self):

		super(bleacher,self).__init__(name = "Bleacher Seat",
					 description = "a section of metal bleacher from the vibrant student section",
					 value = 98 + randint(-10,10),
					 size = 28)

class goalpost(item):
	def __init__(self):

		size_choices = [5, 10, 10, 10, 12, 15, 20]
		size_values = [14, 34, 48, 56, 74, 78, 82]

		i = randint(0,len(size_choices)-1)
		self.size = size_choices[i]
		self.value = size_values[i]

		super(goalpost,self).__init__(name = "Goal Post",
					 description = "just a piece - a primary target of theft at the old Rivalry games",
					 value = self.value + randint(-5,5),
					 size = self.size)

class mascot(item):
	def __init__(self):

		super(mascot,self).__init__(name = "Mascot",
					 description = "the leopard outfit, first designated as mascot in 1924",
					 value = 98 + randint(-10,10),
					 size = 18)

class helmet(item):
	def __init__(self):

		super(helmet,self).__init__(name = "Helmet",
					 description = "invented during the 1894 season by Lafayette's running back",
					 value = 70 + randint(-6,6),
					 size = 9)


# BUSHKILL LOT ITEMS
# ------------------

class car(item):
	def __init__(self):

		car_choices = ["Jeep", "Prius", "Ford Fiesta", "Range Rover"]
		car_values = [125, 82, 145, 162]

		i = randint(0,len(car_choices)-1)
		self.car = car_choices[i]
		self.value = car_values[i]

		super(car,self).__init__(name = "Car",
					 description = "a student's used {0} abiding by the parking policies".format(self.car),
					 value = self.value + randint(-16,16),
					 size = 32)

class parking_pass(item):
	def __init__(self):

		super(parking_pass,self).__init__(name = "Parking Pass",
					 description = "a permit secured through Bruce Hill valid for Bushkill lot",
					 value = 6 + randint(-3,3),
					 size = 2)

class security_cam(item):
	def __init__(self):

		super(security_cam,self).__init__(name = "Security Camera",
					 description = "for monitoring the lot 24/7 in case of vandalism, perhaps",
					 value = 65 + randint(-12,12),
					 size = 10)


# COLLEGE HILL TAVERN ITEMS
# -------------------------

class pint(item):
	def __init__(self):

		beer_choices = ["Guinness", "Guinness", "Guinness", "Blue Moon", "Yuengling", "Bud Light"]
		beer_values = [32, 32, 32, 25, 18, 0]

		i = randint(0,len(beer_choices)-1)
		self.beer = beer_choices[i]
		self.value = beer_values[i]

		super(pint,self).__init__(name = "Pint",
					 description = "a cold glass of {0}, fresh from the tap".format(self.beer),
					 value = self.value + randint(-5,5),
					 size = 5)

class fake_id(item):
	def __init__(self):

		state_choices = ["West Virginia", "South Dakota", "Idaho", "New Hampshire", "Rhode Island"]
		state_values = [-14, -8, -2, 4, 8]

		i = randint(0,len(state_choices)-1)
		self.state = state_choices[i]
		self.value = state_values[i]

		super(fake_id,self).__init__(name = "Fake ID",
					 description = "from the unconvincing state of {0}".format(self.state),
					 value = self.value + randint(-2,2),
					 size = 2)

class karaoke(item):
	def __init__(self):

		super(karaoke,self).__init__(name = "Karaoke Machine",
					 description = "an essential for CHT's youngest demographic",
					 value = 35 + randint(-4,4),
					 size = 9)


# ACOPIAN ITEMS
# -------------



# ROCKWELL ITEMS
# --------------



# WATSON ITEMS
# ------------



# MARCH FIELD ITEMS
# -----------------



# MARQUIS ITEMS
# -------------



# KIRBY ITEMS
# -----------



# SOUTH ITEMS
# -----------



# ARTS CAMPUS ITEMS
# -----------------
