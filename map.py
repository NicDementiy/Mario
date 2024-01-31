class Map:
    def __init__(self, filename, height) -> None:
        self.filename=filename
        self.height=height
        self.load_map()
    def load_map(self):
        self.map = []
        with open(self.filename, 'r') as file:
            for line in file:
                self.map.append([int(char) for char in line.strip()])





m=Map("map.txt",600)
print(m)