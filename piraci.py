from dis import dis
import math

class Pirate:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.distance = 0
		
		self.money = 0
		self.lost_money = 0

		self.year = 1902
		self.month = 10
		self.day = 1
		self.weekday = 2 # sroda

		self.enemies = 0
	
	def clear(self):
		self.x = 0
		self.y = 0
		self.distance = 0
		self.money = 0
		self.year = 1902
		self.month = 10
		self.day = 1
		self.weekday = 2
		self.enemies = 0
		self.lost_money = 0

	def calculate_date(self):
		is_leap_year = (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0

		self.weekday += 1
		self.weekday %= 7

		self.day += 1
		if self.month in [1, 3, 5, 7, 8, 10, 12]:
			if self.day > 31:
				self.day = 1
				self.month += 1
		elif self.month in [4, 6, 9, 11]:
			if self.day > 30:
				self.day = 1
				self.month += 1
		elif self.month == 2:
			if is_leap_year:
				if self.day > 29:
					self.day = 1
					self.month += 1
			else:
				if self.day > 28:
					self.day = 1
					self.month += 1
		
		if self.month > 12:
			self.month = 1
			self.year += 1
	
	def add_day(self):

		self.y += 8
		self.x += 11
		self.distance += 19

		daily_money = len(str(self.y))

		if self.day == 3:
			daily_money += 2
		
		self.money += daily_money

		if daily_money >= 4:
			#print(self.y/8, daily_money)
			self.enemies += daily_money

		self.x -= daily_money

		self.distance += daily_money

		if self.weekday == 5:
			gambling = int(self.money * 0.1)
			self.money -= gambling
			self.lost_money += gambling

		self.calculate_date()


	def search_by_day(self, year, month, day):
		while self.year != year or self.month != month or self.day != day:
			# print(self.year, self.month, self.day)
			self.add_day()
		x, y = self.x, self.y
		self.clear()
		return x, y
	
	def fast_forward(self, days):
		for i in range(days):
			self.add_day()
		distance = self.distance
		money = self.money
		lost_money = self.lost_money
		enemies = self.enemies
		self.clear()
		return distance, money, lost_money, enemies
	
	def distance_from_river(self):
		return math.fabs(self.x-self.y)
	
	def all_distances_from_river(self, days):
		distances = []
		for i in range(days):
			self.add_day()
			distances.append(self.distance_from_river())
		return distances


pirate = Pirate()
print(pirate.search_by_day(1902, 12, 25)) # (687, 680)
print(pirate.fast_forward(150)[0]) # 3323
print(pirate.fast_forward(150)[2]) # 613
print(pirate.fast_forward(150)[3]) # 389
river = pirate.all_distances_from_river(150)
avg = sum(river) / 150
print(avg) # 8.13

import matplotlib.pyplot as plt
plt.bar(range(150), river)
plt.show()