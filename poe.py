'''
Rarities: Normal, Magic, Rare, Unique
'''

class item:

	def __init__ (self, item_class='null', rarity='null', generated_name='null', item_name='null', item_type='null', phys_dmg=[0,0], crit_chance=0.00, attacks_per_second=0.00, weapon_range=[False,0], level_req=0, attribute_req=[0,0,0], sockets='null', ilvl=0, implicit='null', prefix_list=[], suffix_list=[], note=''):
		self.item_class = item_class
		self.rarity = rarity
		self.generated_name = generated_name
		self.item_name = item_name

		self.item_type = item_type
		self.phys_dmg = phys_dmg
		self.crit_chance = crit_chance
		self.attacks_per_second = attacks_per_second
		self.weapon_range = weapon_range

		self.level_req = level_req
		self.attribute_req = attribute_req

		self.sockets = sockets

		self.ilvl = ilvl

		self.implicit = implicit

		self.prefix_list = prefix_list
		self.suffix_list = suffix_list

		self.note = note

	def print_item(self):
		output = 'Item Class: ' + str(self.item_class) + '\nRarity: ' + str(self.rarity) + '\n'
		if self.rarity != 'Normal':
			output += str(self.generated_name) + '\n'
		output += str(self.item_name) + '\n--------\n'
		output += str(self.item_type) + '\nPhysical Damage: ' + str(self.phys_dmg[0]) + '-' + str(self.phys_dmg[1]) + '\nCritical Strike Chance: ' + str('%.2f' % self.crit_chance) + '%\nAttacks per Second: ' + str('%.2f' % self.attacks_per_second) + '\n'
		if self.weapon_range[0] == True:
			output += 'Weapon Range: ' + str(self.weapon_range[1]) + '\n'
		if self.level_req != 1:
			output += '--------\nRequirements:\nLevel: ' + str(self.level_req) + '\n'
			if self.attribute_req[0] != 0:
				output += 'Str: ' + str(self.attribute_req[0]) + '\n'
			if self.attribute_req[1] != 0:
				output += 'Dex: ' + str(self.attribute_req[1]) + '\n'
			if self.attribute_req[2] != 0:
				output += 'Int: ' + str(self.attribute_req[2]) + '\n'
		output += '--------\n'
		output += 'Sockets: ' + str(self.sockets) + '\n--------\n'
		output += 'Item Level: ' + str(self.ilvl) + '\n--------\n'
		output += str(self.implicit) + ' (implicit)'
		if self.prefix_list or self.suffix_list:
			output += '\n--------'
		for self.prefix in self.prefix_list:
			output += '\n' + str(self.prefix)
		for self.suffix in self.suffix_list:
			output += '\n' + str(self.suffix)
		print(output)


def createItemList():

	item_list = []

	# One Handed Maces
	item_list.append(item('One Handed Maces', 'Normal', '', 'Driftwood Club', 'One Handed Mace', [6,8], 5.00, 1.45, [True,11], 1, [14,0,0], 'R', 4, '10% reduced Enemy Stun Threshold'))
	item_list.append(item('One Handed Maces', 'Normal', '', 'Tribal Club', 'One Handed Mace', [8,13], 5.00, 1.40, [True,11], 5, [26,0,0], 'R', 8, '10% reduced Enemy Stun Threshold'))
	item_list.append(item('One Handed Maces', 'Normal', '', 'Spiked Club', 'One Handed Mace', [13,16], 5.00, 1.45, [True,11], 10, [41,0,0], 'R', 16, '10% reduced Enemy Stun Threshold'))
	item_list.append(item('One Handed Maces', 'Normal', '', 'Stone Hammer', 'One Handed Mace', [15,27], 5.00, 1.45, [True,11], 15, [56,0,0], 'R', 20, '15% reduced Enemy Stun Threshold'))

	return item_list

for item in createItemList():
	item.print_item()