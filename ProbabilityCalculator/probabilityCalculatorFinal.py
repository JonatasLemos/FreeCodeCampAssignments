import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for key, value in self.kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number_of_draws):
        if number_of_draws >= len(self.contents):
            return self.contents
        removed_balls = []
        for i in range(number_of_draws):
            choice = random.randrange(len(self.contents))
            removed_balls.append(self.contents.pop(choice))
        return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiment = 0
    for i in range(num_experiments):
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_drawn = hat_copy.draw(num_balls_drawn)
        for color in colors_drawn:
            if color in expected_balls_copy and expected_balls_copy[color] > 0:
                expected_balls_copy[color] -= 1
            if all(x == 0 for x in expected_balls_copy.values()):
                successful_experiment += 1
                break
    return successful_experiment / num_experiments

hat = Hat(yellow=3, blue=2, red=4)
expected_balls = {"blue": 2, "red": 1}
print(experiment(hat, expected_balls, 4, 100000))