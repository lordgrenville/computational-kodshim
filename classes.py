import names as n

# kodsheikodshim/kalim - hierarchy doesn't make sense

class Hekdesh:
    def __init__(self):
        self.has_meila = True
        self.redeemable = None

    def redeem(self):
        if self.redeemable:
            return "Redeemable, add a fifth (external)"
        else:
            return "Not redeemable"


class KedushasDamim(Hekdesh):
    def __init__(self):
        self.redeemable = True


class KedushasHaguf(Hekdesh):
    def __init__(self, has_mum=False):
        if not has_mum:
            self.redeemable = False


class OrganicKorban(KedushasHaguf):
    def __init__(self):
        self.needs_kedushas_kli = True


class AnimalKorban(KedushasHaguf):
    def __init__(self, species, gender):
        self.species = species
        self.gender = gender


class KodsheiKodshim(AnimalKorban):
    def __init__(self, species, gender):
        self.place_slaughtered = n.NORTH
        self.place_blood_received = n.NORTH
        self.matanot_disqualify_if_missing = 'any'
        self.place_remainder_sprinkled = 'Altar base (West)'
        self.remainder_pouring_disqualifies = False
        super().__init__(species=species, gender=gender)


class KodshimKalim(AnimalKorban):
    def __init__(self, species, gender):
        self.place_slaughtered = n.ANY
        self.place_blood_received = n.ANY
        self.matanot_disqualify_if_missing = 'any'
        self.place_remainder_sprinkled = 'Altar base (West)'
        self.remainder_pouring_disqualifies = False
        super().__init__(species=species, gender=gender)


class Olah(KodsheiKodshim):
    def __init__(self, species, gender):
        assert species in [n.BIRD, n.COW, n.SHEEP, n.GOAT], 'Olah must be bird, cow, sheep or goat'
        assert gender == n.MALE, 'Olah must be male'
        self.eaten = False
        super().__init__(species=species, gender=gender)


class Mincha:
    pass

class Shlamim(KodshimKalim):
    def __init__(self, species, gender):
        assert species in [n.COW, n.SHEEP, n.GOAT], 'Shlamim must be cow, sheep or goat'
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
        self.species = n.GOAT
        self.gender = n.MALE

#tamid
morning_tamid = Olah(n.SHEEP, n.MALE)
afternoon_tamid = Olah(n.SHEEP, n.MALE)

# musaf
par_musaf = Olah(n.COW, n.MALE)
ayil_musaf = Olah(n.GOAT, n.MALE)  # this *is* the ayil of vayikra 16:5!
kivsei_musaf = [Olah(n.SHEEP, n.MALE) for k in range(1, 7)]
seir_musaf = OuterChatas(n.GOAT, n.MALE)

# korbanos hayom
par_kohen_gadol = InnerChatas(n.COW, n.MALE)
ayil_kohen_gadol = Olah(n.GOAT, n.MALE)

seir_haam = InnerChatas(n.GOAT, n.MALE)
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
print('hello world')
