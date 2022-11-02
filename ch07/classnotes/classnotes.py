class Point:
  def __init__(self, x=0, y=0, color="red"):
    self.x = x
    self.y = y
    if color == "green":
      print("You are a bad person")
      color = "blue"
    self.color = color

  def set_to_complimentary_color(self):
    red_comp =  255- self.color[0]
    blue_comp =  255- self.color[1]
    green_comp =  255- self.color[2]
    self.color =  [red_comp, blue_comp, green_comp]

  def __str__(self):
    return f"({self.x}, {self.y})"

class Graph:
  def __init__(self, title="My Graph"):
    self.points = []
    self.title = title
    self.points.append(p)

  def add_point(self, p):
    self.points.append(p)

  def __str__(self):
    point_str = ""
    for p in self.points:
        point_str += str(p)
    return f"{self.title}: {point_str}"

def main():
  g = Graph()
  #print(g)
  p = Point(5, 2)
  p2 = Point(3,4)
  g.add_point(p)
  g.add_point(p2)
  print(g)

main()
