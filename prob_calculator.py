import copy
import random

# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = [color for color, count in kwargs.items() for _ in range(count)]

    def draw(self, n):
      new = []
      if n > len(self.contents):
          return self.contents
      for i in range(n):
        removed = self.contents.pop(int(random.random() * len(self.contents)))
        new.append(removed)
      return new

    





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
      expected_copy = copy.deepcopy(expected_balls)
      hat_copy = copy.deepcopy(hat)
      colors_gotten = hat_copy.draw(num_balls_drawn)
      for color in colors_gotten:
        if color in expected_copy:
          expected_copy[color] -= 1

      if all(x <= 0 for x in expected_copy.values()):
        count += 1
        
  return count /num_experiments
          
      

