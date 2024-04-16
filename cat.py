class Cat:
    def __init__(self, x, y, img_file):
        """
        Initializes the cat object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
        """
        self.x = x
        self.y = y
        self.img_file = img_file

    def update_position(self, new_x, new_y):
        """
        Updates the position of the cat
        args:
            - new_x : int - new x coordinate
            - new_y : int - new y coordinate
        return: None
        """
        self.x = new_x
        self.y = new_y

    def jump(self):
        """
        Makes the cat jump
        args: None
        return: None
        """
        # Implementation to make the cat jump

    def duck(self):
        """
        Makes the cat duck
        args: None
        return: None
        """
        # Implementation to make the cat duck