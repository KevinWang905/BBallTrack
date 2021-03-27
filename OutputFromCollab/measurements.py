# constant values corresponding to shooters (values don't actually matter, just unique identifier)
DAME = 0
KAT = 1
STEPH = 2
ALEX = 3
CHRIS = 4
THOMAS = 5

# constant values corresponding to body parts (values don't actually matter, just unique identifier)
HAND = 0
FOREARM = 1
UPPER_ARM = 2
FOREARM_HAND = 3
TOTAL_ARM = 4
FOOT = 5
SHANK = 6
THIGH = 7
FOOT_SHANK = 8
TOTAL_LEG = 9
HEAD_NECK = 10
SHOULDER_MASS = 11
THORAX = 12
ABDOMEN = 13
PELVIS = 14
THORAX_ABDOMEN = 15
ABDOMEN_PELVIS = 16
TRUNK = 17
TRUNK_HEAD_NECK = 18

# global variables used for mapping
BodyParts = []
Shooters = []

# class corresponding to body parts
class BodyPart:
    id = 0
    name = ""
    length_factor = 0   # vertical length (didn't add horizontal length bc not sure if needed)
    weight_factor = 0
    com_prox_factor = 0
    com_dist_factor = 0
    radgy_com_factor = 0
    radgy_prox_factor = 0
    radgy_dist_factor = 0

    def __init__(self, _id, _name, _length_factor, _weight_factor, _com_prox_factor, _com_dist_factor,
        _radgy_com_factor, _radgy_prox_factor, _radgy_dist_factor):
        self.id = _id
        self.name = _name
        self.length_factor = _length_factor
        self.weight_factor = _weight_factor
        self.com_prox_factor = _com_prox_factor
        self.com_dist_factor = _com_dist_factor
        self.radgy_com_factor = _radgy_com_factor
        self.radgy_prox_factor = _radgy_prox_factor
        self.radgy_dist_factor = _radgy_dist_factor

# class corresponding to shooter physical data
class Shooter:
    id = 0      # corresponding to constant values defined above
    name = ""   # full names for reference
    height = 0  # metres
    weight = 0  # kg 
    hand = 'R'  # L/R

    def __init__(self, _id, _name, _height, _weight, _hand):
        self.id = _id
        self.name = _name
        self.height = _height
        self.weight = _weight
        self.hand = _hand

    # functions for anthropometric segment data
    def get_name(self, body_part_id):
        return BodyParts[body_part_id].name
    def get_length(self, body_part_id):
        return self.height * BodyParts[body_part_id].length_factor
    def get_weight(self, body_part_id):
        return self.weight * BodyParts[body_part_id].weight_factor
    def get_com_prox(self, body_part_id):
        return self.height * BodyParts[body_part_id].com_prox_factor
    def get_com_dist(self, body_part_id):
        return self.height * BodyParts[body_part_id].com_dist_factor
    def get_radgy_com(self, body_part_id):
        return self.height * BodyParts[body_part_id].radgy_com_factor
    def get_radgy_prox(self, body_part_id):
        return self.height * BodyParts[body_part_id].radgy_prox_factor
    def get_radgy_dist(self, body_part_id):
        return self.height * BodyParts[body_part_id].radgy_dist_factor

# instantiate BodyParts, a list of all body parts with indices corresponding to body part id
BodyParts.append(BodyPart(HAND, "hand", 0.108, 0.006, 0.506, 0.494, 0.297, 0.587, 0.577))
BodyParts.append(BodyPart(FOREARM, "forearm", 0.146, 0.016, 0.43, 0.57, 0.303, 0.526, 0.647))
BodyParts.append(BodyPart(UPPER_ARM, "upper arm", 0.186, 0.028, 0.436, 0.564, 0.322, 0.542, 0.645))
BodyParts.append(BodyPart(FOREARM_HAND, "forearm & hand", 0.146+0.108, 0.022, 0.682, 0.318, 0.468, 0.827, 0.565))
BodyParts.append(BodyPart(TOTAL_ARM, "total arm", 0.186+0.146+0.108, 0.05, 0.53, 0.47, 0.368, 0.645, 0.596))
BodyParts.append(BodyPart(FOOT, "foot", 0.039, 0.0145, 0.5, 0.5, 0.475, 0.69, 0.69))
BodyParts.append(BodyPart(SHANK, "shank", 0.285-0.039, 0.0465, 0.433, 0.567, 0.302, 0.528, 0.643))
BodyParts.append(BodyPart(THIGH, "thigh", 0.53-0.039, 0.1, 0.433, 0.567, 0.323, 0.54, 0.653))
BodyParts.append(BodyPart(FOOT_SHANK, "foot & shank", 0.285, 0.061, 0.606, 0.394, 0.416, 0.735, 0.572))
BodyParts.append(BodyPart(TOTAL_LEG, "total leg", 0.53, 0.161, 0.447, 0.553, 0.326, 0.56, 0.65))
BodyParts.append(BodyPart(HEAD_NECK, "head & neck", 1-0.818, 0.081, 1, 0, 0.495, 1.116, 0))
BodyParts.append(BodyPart(SHOULDER_MASS, "shoulder mass", 0, 0, 0, 0, 0, 0, 0))      # don't think we need
BodyParts.append(BodyPart(THORAX, "thorax", 0, 0, 0, 0, 0, 0, 0))                    # don't think we need
BodyParts.append(BodyPart(ABDOMEN, "abdomen", 0, 0, 0, 0, 0, 0, 0))                  # don't think we need
BodyParts.append(BodyPart(PELVIS, "pelvis", 0, 0, 0, 0, 0, 0, 0))                    # don't think we need
BodyParts.append(BodyPart(THORAX_ABDOMEN, "thorax & abdomen", 0, 0, 0, 0, 0, 0, 0))  # don't think we need
BodyParts.append(BodyPart(ABDOMEN_PELVIS, "abdomen & pelvis", 0, 0, 0, 0, 0, 0, 0))  # don't think we need
BodyParts.append(BodyPart(TRUNK, "trunk", 0, 0, 0, 0, 0, 0, 0))                      # don't think we need
BodyParts.append(BodyPart(TRUNK_HEAD_NECK, "trunk head neck", 0, 0, 0, 0, 0, 0, 0))  # don't think we need

# instantiate Shooters, a list of all shooters with indices corresponding to shooter id
Shooters.append(Shooter(DAME, "Damian Lillard", 1.88, 88, 'R'))
Shooters.append(Shooter(KAT, "Karl-Anthony Towns", 2.11, 112, 'R'))
Shooters.append(Shooter(STEPH, "Stephen Curry", 1.91, 86, 'R'))
Shooters.append(Shooter(ALEX, "Alex Dolmaya", 1.78, 87, 'R'))
Shooters.append(Shooter(CHRIS, "Christopher Calogero", 1.83, 76, 'R'))
Shooters.append(Shooter(THOMAS, "Thomas Nguyen", 1.85, 73, 'L'))

# testing
# print(Shooters[DAME].get_length(HAND))
# print(Shooters[ALEX].get_length(HAND))
# print(Shooters[CHRIS].get_length(HAND))
# print(Shooters[THOMAS].get_length(HAND))