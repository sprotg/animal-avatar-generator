from animal_avatar import Avatar
import random

#Generate a random seed string:
avatar = Avatar("".join(random.sample("abcdefghijklmnopqrstuvxyz0123456789", 10)))

svg = avatar.create_avatar()

svg_file = open("animal.svg", "w")
svg_file.write(svg)
svg_file.close()
