import numpy as np

class Engine:
	def __init__(self, data):
		self.data = data
		
	def rank(self):
		'''Ranks Students from the best to worst
		returns --> object'''
		total = np.sum(self.data, axis=1)
		return np.argsort(total)[::-1]
		
	def grade(self):
		'''Classifies subject and student mean score:
                Range   Grade

                ≥ 85    A
                70–84   B
                50–69   C
                < 50    F 
        returns --> dict'''
		pass
		
	def summary(self):
		data = self.data
		print(f"Rank \t\t ID \t\t Name \t\t Score")
		for i in enumerate(data):
			sum = np.sum(i[0][3])
			print(f"{i[0]} \t\t {i[1][0]} \t\t {i[1][1]} \t\t {sum[i[0]]}")
			
			
if __name__ == '__main__':
	from data_loader import DataLoader
	dl = DataLoader()
	data = dl.load_data()
	
	e = Engine(data=data)
	
	e.summary()
