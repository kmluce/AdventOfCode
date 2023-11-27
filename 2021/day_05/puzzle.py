class Puzzle:
    fileName: str

    def __init__(self, file_name):
        self.fileName = file_name
        self.line_coords = []
        self.max_x = 0
        self.max_y = 0
        self.grid = []
        self.slope = []


    def parse(self):
        with open(self.fileName) as file:
            for line in file:
                line = line.rstrip()
                vals = line.split('->')
                self.line_coords.append([int(n) for m in [i.split(',') for i in vals] for n in m])
                x1 = self.line_coords[-1][0]
                x2 = self.line_coords[-1][2]
                y1 = self.line_coords[-1][1]
                y2 = self.line_coords[-1][3]
                self.max_x = max(x1, x2, self.max_x)
                self.max_y = max(y1, y2, self.max_y)
                self.slope.append([y2 - y1, x2 - x1])

        #self.print_object()

    def print_object(self):
        print ("Coordinates:")
        for i in self.line_coords:
            print(i)
        print("Max x is", self.max_x, "; max y is", self.max_y)
        print("Slope:")
        for i in self.slope:
            print(i)
        print ("Grid:")
        for i in self.grid:
            print(i)

    def solvea(self):
        self.grid = [[0 for i in range(self.max_y+1)] for j in range(self.max_x+1)]
        for line in self.line_coords:
            print ("drawing line for line:", line)
            x1 = line[0]
            x2 = line[2]
            y1 = line[1]
            y2 = line[3]
            if x1 - x2 == 0:  #slope is vertical
                print("vertical line")
                if y2 < y1:
                    step = -1
                    extent = y2-1
                else:
                    step = 1
                    extent = y2 + 1
                for i in range(y1, extent, step):
                    print("incrementing grid", [i], x1 )
                    self.grid[i][x1] += 1
            elif y1 -y2 == 0:
                print("horizontal line")
                if x2 < x1:
                    step = -1
                    extent = x2 - 1
                else:
                    step = 1
                    extent = x2 + 1
                for i in range(x1, extent, step):
                    print("incrementing grid", y1, [i] )
                    self.grid[y1][i] += 1
            else:
                print("slope not horizontal or vertical for", line)
        self.print_object()
        intersections = [i for line in self.grid for i in line if i >= 2]
        print(intersections)
        return len([i for line in self.grid for i in line if i >= 2])

    def solveb(self):
        self.grid = [[0 for i in range(self.max_y+1)] for j in range(self.max_x+1)]
        for line in self.line_coords:
            line_grid = [[0 for i in range(self.max_y+1)] for j in range(self.max_x+1)]
            print ("drawing line for line:", line)
            x1 = line[0]
            x2 = line[2]
            y1 = line[1]
            y2 = line[3]
            if x1 - x2 == 0:  #slope is vertical
                #print("    vertical line")
                if y2 < y1:
                    step = -1
                    extent = y2-1
                else:
                    step = 1
                    extent = y2 + 1
                for i in range(y1, extent, step):
                    #print("        incrementing grid", [i], x1 )
                    self.grid[i][x1] += 1
                    line_grid[i][x1] += 1
                #for i in line_grid:
                    #print("    ", i)
            elif y1 -y2 == 0:
                #print("    horizontal line")
                if x2 < x1:
                    step = -1
                    extent = x2 - 1
                else:
                    step = 1
                    extent = x2 + 1
                for i in range(x1, extent, step):
                #    print("        incrementing grid", y1, [i] )
                    self.grid[y1][i] += 1
                    line_grid[y1][i] += 1
                #for i in line_grid:
                #    print("    ", i)
            elif abs(x1 - x2) == abs(y1 -y2):
                #print("    diagonal line", y2)
                if x2 < x1:
                    x_step = -1
                    x_extent = x2 - 1
                else:
                    x_step = 1
                    x_extent = x2 + 1
                if y2 < y1:
                    y_step = -1
                    y_extent = y2 - 1
                else:
                    y_step = 1
                    y_extent = y2 + 1
                x = x1
                #print("    diagonal range from ", y1, "to", y_extent, "by", y_step)
                for y in range(y1, y_extent, y_step):
        #           for x in range(x1, x_extent, x_step):
                #    print("        incrementing grid", y, x)
                    self.grid[y][x] += 1
                    line_grid[y][x] += 1
                    x += x_step
                #for i in line_grid:
                #    print ("    ", i)
            else:
                print("slope not horizontal, vertical, or diagonal for", line)
        self.print_object()
        intersections = [i for line in self.grid for i in line if i >= 2]
        print(intersections)
        return len([i for line in self.grid for i in line if i >= 2])