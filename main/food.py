import random
import os
import game_config as gc

from pygame import image, transform

foods_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_foods():
    return [food for food, count in foods_count.items() if count < 2]

class Food:
    def __init__(self, index):
        self.index = index
        self.name = random.choice(available_foods())
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.skip = False
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))

        foods_count[self.name] += 1
