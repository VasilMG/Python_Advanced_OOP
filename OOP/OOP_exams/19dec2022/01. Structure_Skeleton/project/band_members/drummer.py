from project.band_members.musician import Musician


class Drummer(Musician):
    DRUMMER_AVAILABLE_SKILLS = (
        "play the drums with drumsticks",
        "play the drums with drum brushes",
        "read sheet music",
    )

    def learn_new_skill(self, new_skill):
        if new_skill not in self.DRUMMER_AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."



# class Drummer(Musician):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.skill_set = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
#
#     def learn_new_skill(self, skill):
#         return super().learn_new_skill(skill)