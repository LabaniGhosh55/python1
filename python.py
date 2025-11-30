# write your code here

# write your code here
class FeeCalculator:
	def SetDetails(self, name, rollno, fee, percentage):
		self.name=name
		self.rollno=rollno
		self.fee=fee
		self.percentage=percentage
	def TotalFee(self):
		if self.percentage<=50:
			return self.fee +(0.20 *self.fee)
		elif self.percentage<=75:
			return self.fee +(0.15 *self.fee)
		else:
			return self.fee

name = input()
rollno = int(input())
fee = int(input())
percentage = float(input())

# Create object and print result
student1 = FeeCalculator()
student1.SetDetails(name, rollno, fee, percentage)
print(f"{student1.TotalFee():.1f}")
