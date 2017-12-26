class Banner():
	def __init__(self, width, height, border=False):
		self.width = width
		self.height = height
		self.border = border
		self.container = [" " for x in range(width*height)]

	def insert(self, data, pos_x = 0, pos_y = 0):
		# check if data is wider from the area
		if self.width < self.getWidth(data) or self.height < self.getHeight(data):
			raise AssertionError("Out of bounds: Input is wider and/or higher than the container")
		# check if position is in bounds
		if pos_x > self.width-1 or pos_y > self.height:
			raise AssertionError("Out of bounds: Position is not in bounds of the container")
		# check if data will fit
		if pos_x+self.getWidth(data) > self.width or pos_y+self.getHeight(data) > self.height:
			raise AssertionError("Out of bounds: Data too wide/high to fit with current starting coordinates")

		# insert the data into the container
		data_split = data.split("\n")
		for lst, rel_y in zip(data_split, range(len(data_split))):
			for char, rel_x in zip(lst, range(len(lst))):
				if char != " ":
					rel_y_compensation = (rel_y*self.width) + (pos_y*self.width)
					self.container[rel_y_compensation + rel_x + pos_x] = str(char)
		
	def get(self):
		container = self.container.copy()
		width = self.width
		height = self.height
		if self.border == True:
			container = self.borderGen(container)
			width += 2
			height += 2

		for pr in range(0, width*height, width):
			print ("".join(container[pr:pr+width]))

	def borderGen(self, container):
		[container.insert(x, "|") for x in range(len(container), 0, -self.width)]
		[container.insert(x-(self.width+1), "|") for x in range(len(container), 0, -(self.width+1))]
		[container.insert(0, "+") for c in range(2)]
		[container.insert(1, "-") for c in range(self.width)]
		[container.append("+") for c in range(2)]
		[container.insert(len(container)-1, "-") for c in range(self.width)]
		return container

	def getWidth(self, data):
		return len(max(data.split('\n'), key=len))

	def getHeight(self, data):
		return len(data.split('\n'))
