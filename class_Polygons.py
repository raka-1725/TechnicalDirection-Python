import math
from typing import List, Tuple

class Polygon:
    def __init__(self, vertices: List[Tuple[float, float]]):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        
        self.vertices = vertices
    
    @property
    #return number of sides on polygon
    def num_sides(self) -> int:
        return len(self.vertices)
    

    @property
    #calculates perimeter of polygon
    def perimeter(self) -> float:
        total = 0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total += distance
        return total

    @property
    #calculate the area of polygon
    def area(self) -> float:
        total = 0
        #shoe laces formula
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            total += (x1 * y2) - (x2 * y1)
        return abs(total) / 2

    #native print func in class : call print() to print this
    def __str__(self) -> str:
        #return poly info in str
        return f"Polygon with {self.num_sides} sides, Perimeter: {self.perimeter:.2f}, Area: {self.area:.2f}"
    
    #return vertices info in str
    def __repr__(self):
        return f"Polygon(vertices = {self.vertices})"
        


if __name__ == "__main__":
        while True:
            try:
                num_sides = int(input("How many sides does the polygon have? (Minimum : 3)") )
                if num_sides < 3:
                    print("Polygon must have at least 3 sides Please try again")
                    continue
                break
            except ValueError:
                print("Invalid input!! Enter a valid number")

        vertices = []
        print(f"\nEnter {num_sides} vertices as (x,y) pairs:")

        for i in range (num_sides):
            while True:
                try:
                    vertex_input = input(f"Vertex {i + 1}: ")
                    x, y = map(float, vertex_input.split(","))
                    vertices.append((x,y))
                    break
                except ValueError:
                    print("Invalid Input!. Enter in valid format (x,y)")


        try:
            polygon = Polygon(vertices)
            print("\n" + str(polygon))
            print(f"Number of sides: {polygon.num_sides}")
            print(f"Perimeter : {polygon.perimeter:.2f}")
            print(f"Area : {polygon.area:.2f}")
        except ValueError as e:
            print("Error: {e}")
