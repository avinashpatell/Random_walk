from random import choice

class RandomWalk():
	"""A class to generate random walk points."""
	
	def __init__(self,num_points=5000):
		"""initialize attributes for walk."""
		self.num_points=num_points
		
		#All walk starts at (0,0).
		
		self.x_values=[0]
		self.y_values=[0]
		
	def fill_walk(self):
		"""calculate all the points in walk"""
		#keep walking under the walk reaches desired distance.
		while len(self.x_values) < self.num_points:
		
			#decide which direction to go and how far to move in that direction.
			
			x_direction=choice([1,-1])
			x_distance=choice([0,1,2,3,4])
			x_step=x_direction*x_distance
			
			y_direction=choice([1,-1])
			y_distance=choice([0,1,2,3,4])
			y_step=y_direction*y_distance
			
			#rejects move that go nowhere.
			
			if x_step==0 and y_step==0:
				continue
			
			#calculate the next x and y values.
			next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)

			
