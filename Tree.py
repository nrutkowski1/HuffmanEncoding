
class Tree:

    def __init__(self, left_val, right_val, current_val):

        # left, right, current is either a number or character
        # bottom nodes will have a current value which is the character at that spot
        # if the current is a character than the left and right will be None
        self.left = left_val
        self.right = right_val
        self.current = current_val

    def get_current(self): return self.current

    def set_current(self, curr): self.current = curr

    def get_left(self): return self.left

    def set_left(self, lef): self.left = lef

    def get_right(self): return self.right

    def set_right(self, rght): self.right = rght
