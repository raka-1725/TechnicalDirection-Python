import math
from typing import List, Tuple
#imports to use later

class Polygon:
    #A class representing a polygon with vertices in 2D space.
    #A Tuple is a collection of elemets and used to store data
    def __init__(self, vertices: List[Tuple[float, float]]):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices")
        
        self.vertices = vertices
    
    @property
    #defines a method but you can access it like an attribute
    def num_sides(self) -> int:
        #Return the number of sides in the polygon
        return len(self.vertices)
    
    @property
    def perimeter(self) -> float:
        #Calculate and return the perimeter of the polygon
        total = 0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total += distance
        return total
    
    @property
    def area(self) -> float:
        #Calculate the area of the polygon using the Shoelace formula.
        total = 0
        for i in range(self.num_sides):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % self.num_sides]
            total += x1 * y2 - x2 * y1
        return abs(total) / 2
    
    def __str__(self) -> str:
        #Return a string representation of the polygon
        return f"Polygon({self.num_sides} sides, area={self.area:.2f}, perimeter={self.perimeter:.2f})"
    
    def __repr__(self) -> str:
        #Return a detailed representation of the polygon
        return f"Polygon(vertices={self.vertices})"


# Example usage
if __name__ == "__main__":
    #Get number of sides from user
    while True:
        try:
            num_sides = int(input("How many sides does the polygon have? (minimum 3): "))
            if num_sides < 3:
                print("A polygon must have at least 3 sides. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    #Get vertices from user
    vertices = []
    print(f"\nEnter {num_sides} vertices as (x, y) coordinates:")
    for i in range(num_sides):
        while True:
            try:
                vertex_input = input(f"Vertex {i + 1}: ")
                x, y = map(float, vertex_input.split(","))
                vertices.append((x, y))
                break
            except ValueError:
                print("Invalid format. Please enter as: x, y (e.g., 0, 0)")
    
    #Create and display polygon
    try:
        polygon = Polygon(vertices)
        print(f"\n{polygon}")
        print(f"Number of sides: {polygon.num_sides}")
        print(f"Perimeter: {polygon.perimeter:.2f}")
        print(f"Area: {polygon.area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")