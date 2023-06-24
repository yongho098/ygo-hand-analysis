import pyperclip
import json
import pprint

with open("decklists/example_decklist.json") as json_file:
        json_data = json.load(json_file)

oldtest = """Monster
1 Dinowrestler Pankratops
2 Kashtira Fenrir
1 Wandering Gryphon Rider
3 Icejade Ran Aegirine
3 Marincess Blue Tang
2 Marincess Pascalus
3 Marincess Springirl
3 Water Enchantress of the Temple
3 Marincess Sea Horse
2 Marincess Mandarin
Spell
3 Dark Ruler No More
2 Icejade Cradle
2 Marincess Dive
1 Rite of Aramesir
3 Triple Tactics Talent
3 Enemy Controller
1 Fateful Adventure
1 Marincess Battle Ocean
1 Dracoback, the Rideable Dragon
Trap
1 Marincess Wave"""
newtest2 = """Monster
1 Kashtira Ogre
2 Kashtira Unicorn
3 Kashtira Fenrir
1 Scareclaw Kashtira
3 Dimension Shifter
1 Raidraptor - Tribute Lanius
2 Kashtira Riseheart
1 Raider's Wing
2 Ash Blossom & Joyous Spring
Spell
3 Kashtiratheosis
3 Pot of Prosperity
1 Terraforming
3 Triple Tactics Talent
3 Enemy Controller
3 Kashtira Birth
3 Pressured Planet Wraitsoth
Trap
3 Infinite Impermanence
1 Kashtira Big Bang
1 Kashtira Preparations
Extra
1 Baronne de Fleur
2 Divine Arsenal AA-ZEUS - Sky Thunder
1 Kashtira Arise-Heart
1 Dark Armed, the Dragon of Annihilation
1 Mecha Phantom Beast Dracossack
1 Number 11: Big Eye
1 Raidraptor - Arsenal Falcon
2 Kashtira Shangri-Ira
1 Evilswarm Nightmare
1 Number F0: Utopic Draco Future
1 Number F0: Utopic Future
1 Donner, Dagger Fur Hire
1 Infinitrack Goliath
Side
3 Ghost Belle & Haunted Mansion
3 Droll & Lock Bird
3 Cosmic Cyclone
3 Evenly Matched
3 Solemn Judgment
"""
output = {}
outputmd = {}
deck_list = []
newtest = """Monster
1 Dinowrestler Pankratops
2 Kashtira Fenrir
1 Wandering Gryphon Rider
3 Icejade Ran Aegirine
3 Marincess Blue Tang
2 Marincess Pascalus
3 Marincess Springirl
3 Water Enchantress of the Temple
3 Marincess Sea Horse
2 Marincess Mandarin
Spell
3 Dark Ruler No More
2 Icejade Cradle
2 Marincess Dive
1 Rite of Aramesir
3 Triple Tactics Talent
3 Enemy Controller
1 Fateful Adventure
1 Marincess Battle Ocean
1 Dracoback, the Rideable Dragon
Trap
1 Marincess Wave"""
ls = newtest2.split("\n")
#print(ls)

pprint.pprint({})