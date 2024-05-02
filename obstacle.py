class Obstacle:
    def __init__(self, x, y, img_file, obstacle_type):
        """
        Initializes the obstacle object
        args:
            - x : int - starting x coordinate
            - y : int - starting y coordinate
            - img_file : str - path to img file
            - obstacle_type : str - type of obstacle (e.g., "box", "butterfly")
        """
        self.x = x
        self.y = y
        self.img_file = img_file
        self.obstacle_type = obstacle_type

    def update_position(self, new_x, new_y):
        """
        Updates the position of the obstacle
        args:
            - new_x : int - new x coordinate
            - new_y : int - new y coordinate
        return: None
        """
        self.x = new_x
        self.y = new_y

    def get_type(self):
        """
        Returns the type of the obstacle
        args: None
        return: str
        """
        return self.obstacle_type