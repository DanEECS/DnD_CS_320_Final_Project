from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Character(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_made = models.DateTimeField(default=timezone.now())
    # Character identity
    characterName = models.CharField(max_length=52)
    playerName = models.CharField(max_length=52)
    Class = models.TextField()
    race = models.TextField()
    background = models.TextField()
    level = models.IntegerField()
    alignment = models.TextField()
    experience = models.IntegerField()
    # Stats and modifiers
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    strengthMod = models.IntegerField()
    dexterityMod = models.IntegerField()
    constitutionMod = models.IntegerField()
    intelligenceMod = models.IntegerField()
    wisdomMod = models.IntegerField()
    charismaMod = models.IntegerField()

    racialFeatures = models.TextField()
    classFeatures = models.TextField()
    backgroundFeatures = models.TextField()
    # Combat stats
    armorClass = models.IntegerField()
    initiative = models.IntegerField()
    speed = models.IntegerField()
    maxHitPoints = models.IntegerField()
    hitDiceAmount = models.IntegerField()
    hitDiceType = models.IntegerField()
    # Stat proficiencies
    proficiencyBonus = models.IntegerField()

    strengthSavePro = models.BooleanField()
    dexteritySavePro = models.BooleanField()
    constitutionSavePro = models.BooleanField()
    intelligenceSavePro = models.BooleanField()
    wisdomSavePro = models.BooleanField()
    charismaSavePro = models.BooleanField()

#    strengthSaveBon = models.IntegerField()
#    dexteritySaveBon = models.IntegerField()
#    constitutionSaveBon = models.IntegerField()
#    intelligenceSaveBon = models.IntegerField()
#    wisdomSaveBon = models.IntegerField()
#    charismaSaveBon = models.IntegerField()
    # Skill proficiencies
    acrobaticsPro = models.BooleanField()
    animalHandlingPro = models.BooleanField()
    arcanaPro = models.BooleanField()
    athleticsPro = models.BooleanField()
    deceptionPro = models.BooleanField()
    historyPro = models.BooleanField()
    insightPro = models.BooleanField()
    intimidationPro = models.BooleanField()
    investigationPro = models.BooleanField()
    medicinePro = models.BooleanField()
    naturePro = models.BooleanField()
    perceptionPro = models.BooleanField()
    performancePro = models.BooleanField()
    persuasionPro = models.BooleanField()
    religionPro = models.BooleanField()
    sleightOfHandPro = models.BooleanField()
    stealthPro = models.BooleanField()
    survivalPro = models.BooleanField()

#    acrobaticsSkill = models.IntegerField()
#    animalHandlingSkill = models.IntegerField()
#    arcanaSkill = models.IntegerField()
#    athleticsSkill = models.IntegerField()
#    deceptionSkill = models.IntegerField()
#    historySkill = models.IntegerField()
#    insightSkill = models.IntegerField()
#    intimidationSkill = models.IntegerField()
#    investigationSkill = models.IntegerField()
#    medicineSkill = models.IntegerField()
#    natureSkill = models.IntegerField()
#    perceptionSkill = models.IntegerField
#    performanceSkill = models.IntegerField()
#    persuasionSkill = models.IntegerField()
#    religionSkill = models.IntegerField()
#    sleightOfHandSkill = models.IntegerField()
#    stealthSkill = models.IntegerField()
#    survivalSkill = models.IntegerField()
    # Character personality
    personalityTraits = models.TextField()
    ideals = models.TextField()
    bonds = models.TextField()
    flaws = models.TextField()
    featuresAndTraits = models.TextField()
    # Equipment
    weapons = models.TextField()
    armor = models.TextField()
    miscEquipment = models.TextField()
    money = models.TextField()


# Create your models here.
