
# -----------------------------------
# generate leaderboard from text file
# -----------------------------------

def show_leaderboard(new_name, new_score):

    names, scores = gen_leaderboard()

    # check to see if the new entry made the leaderboard
    replaced = False
    replaced_index = 6

    for i in range(0,len(names)):

        if (float(new_score) > float(scores[i]) and replaced == False):
            names.insert(i, new_name)
            scores.insert(i, new_score)
            replaced = True
            replaced_index = i

    # limit entries to 5
    if len(names) > 5:
        names = names[0:5]
        scores = scores[0:5]

    # show leaderboard
    print("        LEADERBOARD")
    print("        -----------")

    for i in range(0,len(names)):
        name_length = len(names[i])
        if i == replaced_index:
            print("     *** {}.) {}".format(i+1,names[i]) + " "*(25-name_length) + "{} ***".format(scores[i]))
        else:
            print("         {}.) {}".format(i+1,names[i]) + " "*(25-name_length) + "{}".format(scores[i]))

    print("")


def gen_leaderboard():

    with open('resources/scores.txt', 'r') as f:
        full = f.readlines()

    entries = len(full)

    if entries >= 5:
        entries = 5

    names = []
    scores = []

    for i in range(0,entries):
        row = full[i].split()

        names.append(row[0])
        scores.append(row[1])

    return names, scores
