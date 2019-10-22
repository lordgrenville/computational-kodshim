#TODO
# should there be a korban parent that everything inherits from?
# kodsheikodshim/kalim - hierarchy doesn't make sense
# consts
M = 'male'
F = 'female'
GOAT = 'goat'
SHEEP = 'sheep'
BIRD = 'bird'
COW = 'cow'
KODSHEI_KODSHIM = 'kodshei_kodshim'
KODSHIM_KALIM = 'kodshim_kalim'
N = 'north'
ANY = 'anywhere in Azara'

class AnimalKorban:
    def __init__(self, species, gender):
        self.species = species
        self.gender = gender


class KodsheiKodshim(AnimalKorban):
    def __init__(self, species, gender):
        self.place_slaughtered = N
        self.place_blood_received = N
        self.matanot_disqualify_if_missing = 'any'
        self.place_remainder_sprinkled = 'Altar base (West)'
        self.remainder_pouring_disqualifies = False
        super().__init__(species=species, gender=gender)


class KodshimKalim(AnimalKorban):
    def __init__(self, species, gender):
        self.place_slaughtered = ANY
        self.place_blood_received = ANY
        self.matanot_disqualify_if_missing = 'any'
        self.place_remainder_sprinkled = 'Altar base (West)'
        self.remainder_pouring_disqualifies = False
        super().__init__(species=species, gender=gender)


class Olah(KodsheiKodshim):
    def __init__(self, species, gender):
        assert species in [BIRD, COW, SHEEP, GOAT], 'Olah must be bird, cow, sheep or goat'
        assert gender == M, 'Olah must be male'
        self.eaten = False
        super().__init__(species=species, gender=gender)


class Mincha:
    pass

class Shlamim(KodshimKalim):
    def __init__(self, species, gender):
        assert species in [COW, SHEEP, GOAT], 'Shlamim must be cow, sheep or goat'
        super().__init__(species=species, gender=gender)


class Chatas(KodsheiKodshim):
    def __init__(self, species, gender):
        super().__init__(species=species, gender=gender)


class InnerChatas(Chatas):
    def __init__(self, species, gender):
        self.eaten = False
        super().__init__(species=species, gender=gender)


class OuterChatas(Chatas):
    def __init__(self, species, gender):
        super().__init__(species=species, gender=gender)


class Seirhamishtaleach:
    def __init__(self):
        self.species = GOAT
        self.gender = M

#tamid
morning_tamid = Olah(SHEEP, M)
afternoon_tamid = Olah(SHEEP, M)

# musaf
par_musaf = Olah(COW, M)
ayil_musaf = Olah(GOAT, M)  # this *is* the ayil of vayikra 16:5!
kivsei_musaf = [Olah(SHEEP, M) for k in range(1, 7)]
seir_musaf = OuterChatas(GOAT, M)

# korbanos hayom
par_kohen_gadol = InnerChatas(COW, M)
ayil_kohen_gadol = Olah(GOAT, M)

seir_haam = InnerChatas(GOAT, M)
seir_hamishtaleyach = Seirhamishtaleach()


#class Asham(AnimalKorban):
#    pass
#
#
#class Oleh_vYored(AnimalKorban):
#    pass
#
#
#class Pesach(Shlamim):
#    pass
#
#
## https://he.wikisource.org/wiki/%D7%A1%D7%A4%D7%A8%D7%90_%D7%A2%D7%9C_%D7%95%D7%99%D7%A7%D7%A8%D7%90_%D7%90#%D7%A4%D7%A1%D7%95%D7%A7_%D7%99%D7%91_(%D7%9B%D7%9C_%D7%94%D7%A4%D7%A8%D7%A7)(%D7%9B%D7%9C_%D7%94%D7%A4%D7%A1%D7%95%D7%A7)
