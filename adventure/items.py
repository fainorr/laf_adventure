
# ----------------------------------------------
# defines the items encountered in the adventure
# ----------------------------------------------

# The base classes for all items

class item(object):

    def __init__(self, name, description, value, size):
        self.name = name
        self.description = description
        self.value = value
        self.size = size

    def __str__(self):
        return "{0} (size = {1}): {2}".format(self.name, self.size, self.description)

class item_list():
    def __init__(self, name, list):
        self.name = name
        self.list = list


# STARTING ITEMS
# --------------

class textbook(item):
    def __init__(self, subject):

        self.subject = subject

        super(textbook, self).__init__(name = "Textbook",
                         description = "a way-too-heavy {0} textbook (why do you carry this around, anyway?).".format(self.subject),
                         value = 1,
                         size = 8)


# class phone_list(item_list):
#     def __init__(self):
#         super().__init__("Phone List", ["Android","iPhone"])

class phone(item):
    def __init__(self, type):

        self.type = type

        if self.type == "Android":
            self.value = 1
        if self.type == "iPhone":
            self.value = 8

        super(phone,self).__init__(name = "Cell Phone",
                         description = "cause you'd never be caught without your " + self.type + ".",
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
    def __init__(self, color):

        self.color = color
        if self.color == "black":
            self.value = 2
        if self.color == "blue":
            self.value = 5
        if self.color == "white":
            self.value = 10
        if self.color == "maroon":
            self.value = 15

        super(adirondack_chair,self).__init__(name="Adirondack Chair",
                         description="an icon of quad relaxation, painted " + self.color + ".",
                         value=self.value,
                         size=20)

class hammock(item):
    def __init__(self):

        super(hammock,self).__init__(name = "Hammock",
                         description = "for sprawling between two trees.",
                         value = 8,
                         size = 4)

# PARDEE ITEMS
# -------------

class tenured_professor(item):
    def __init__(self):

        super(tenured_professor,self).__init__(name = "Tenured Professor",
                         description = "an essential asset to any liberal arts institution.",
                         value = 25,
                         size = 18)
