# class Car:
#     def __init__(self, name, year):
#         self.name=name
#         self.year=year
#         print('Car init')
#     def gas_pedal(self,down):
#         if down:
#             print('vroom')
#         else:
#             print('go and push the gas pedal')
# volvo=Car('idk', 1950)
# print(volvo.name)
# volvo.gas_pedal(True)
# volvo.gas_pedal(False)

# class Other_car(Car):
#     def __init__(self, whatever):
#         Car.__init__
#         self.whatever=whatever
#     def gas_pedal_other(self, down):
#         if down:
#             print('')
# other_volvo=Other_car('eeeee')
# print(other_volvo.whatever)
# other_volvo.gas_pedal(True)
# other_volvo.gas_pedal_other(True)
class BetterInt(int):
	def __init__(self, number):
		int.__init__(number)
		self.number=number
	def __call__(self, arg):
		return self.number*arg
print(BetterInt(3)(10))