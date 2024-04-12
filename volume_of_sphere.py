#Function to add volume of sphere
def compute_area_of_circle(radius):
	pi = 3.14
	V = 4/3 * pi * radius*3 
	return V
#define radius
radius1 = 30
V1 = compute_area_of_circle(radius1)
print(f"The volume with radius {radius1} is: {V1}")

#define radius 2 and run again
radius2 = 40
V2 = compute_area_of_circle(radius2)
print(f"The volume with radius {radius2} is: {V2}")
