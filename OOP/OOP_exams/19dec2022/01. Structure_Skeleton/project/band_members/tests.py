# from project.concert_tracker_app import ConcertTrackerApp
#
# musician_types = ["Singer", "Drummer", "Guitarist"]
# names = ["George", "Alex", "Lilly"]
#
# app = ConcertTrackerApp()

from project.band_members.singer import Singer

s = Singer("Pesho", 90)
print(type(s))
















#
# for i in range(3):
#     print(app.create_musician(musician_types[i], names[i], 20))
#
# print(app.musicians[0].learn_new_skill("sing high pitch notes"))
# print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
# print(app.musicians[2].learn_new_skill("play rock"))
#
# print(app.create_band("RockName"))
# # print(app.create_musician('pjp', "Lilly", 90))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
# # print(app.create_concert("Jazz", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))
# # print(app.remove_musician_from_band('George', 'RockName'))
# # print(app.create_musician('Singer', "Pesho", 90))
# print(app.create_musician('Singer', "Pesho", 90))
# print(app.create_musician('Singer', "GOsho", 90))
# print(app.create_musician('Singer', "Stamat", 90))
# print(app.add_musician_to_band('Stamat', 'RockName'))
# print(app.remove_musician_from_band('Stamat', 'RockName'))
# # print(p.learn_new_skill("sing high pitch notes"))
# # print(app.add_musician_to_band('Pesho','RockName'))
# # print(app.add_musician_to_band('Pesho1','RockName'))
# # print(app.remove_musician_from_band("Pesho", 'RockName'))
# # print(len(app.bands[0].members))
# # print(app.add_musician_to_band('Pesho1','RockName'))
# # print(app.musicians[3].learn_new_skill("sing high pitch notes"))
# # print(app.musicians[3].learn_new_skill("sing low pitch notes"))
# # print(app.create_concert("Jazz", 20, 5.20, 56.7, "Plovdiv"))
# # print(app.create_concert("Rock", 20, 5.20, 56.7, "Pernik"))
# # print(app.bands[0].members[1].skills)
# # print(app.musicians[1].learn_new_skill("play the drums with drum brushes"))
# # print(app.musicians[2].learn_new_skill("play jazz"))
# # print(app.remove_musician_from_band("Lilly", 'RockName'))
#
# # print(app.start_concert('Plovdiv', 'RockName'))
# # print(app.start_concert("Sofia", "RockName"))

