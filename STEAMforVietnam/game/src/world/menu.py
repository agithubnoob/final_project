def _update_dx_dy_based_on_obstacles(self, obstacles):
    """
    Knowing the positions of all obstacles and the would-be position of this subject
    (self.rect.x + self.dx, self.rect.y + self.dy), check if the would-be position
    is colliding with any of the obstacles.
    If collision happens, restrict the movement by modifying self.dx and(or) self.dy.
    """
    # The obstacle check in the following for loop will determine
    # whether the subject is_landed, so we first reset it.
    self.is_landed = False
    for obstacle in obstacles:
        if obstacle.rect.colliderect(
                self.rect.x + self.dx,
                self.rect.y,
                self.rect.width,
                self.rect.height,
        ):
            # Hitting an obstacle horizontally, prevent horizontal movement altogether:
            self.dx = 0
        if obstacle.rect.colliderect(
                self.rect.x,
                self.rect.y + self.dy,
                self.rect.width,
                self.rect.height,
        ):
            # Hitting an obstacle vertically, reduce vertical movement:
            if self.dy < 0:
                # the gap between player's head and obstacle above
                self.dy = obstacle.rect.bottom - self.rect.top
            else:
                self.is_landed = True
                # the gap between player's feet and ground
                self.dy = obstacle.rect.top - self.rect.bottom

