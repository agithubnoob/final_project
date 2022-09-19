from collections.abc import Sequence


class GameConfig:
    pass
class self:
    pass


class GameEvent:
    pass


class World:
    pass


def update(self, events: Sequence[GameEvent], world: World) -> None:
        super().update(events, world)
        # Knowing the current state of the subject, we calculate the amount of changes
        # - dx and dy - that should occur to the player position during this current game tick.
        # Step 1: calculate would-be dx, dy when unobstructed
        self.dx = 0
        if self.is_landed:
            self.dy = 0
        self.dy += GameConfig.GRAVITY
        if self.moving_left:
            self.dx = -self.speed
        if self.moving_right:
            self.dx = self.speed
        # Step 2:
        self._update_dx_dy_based_on_obstacles(self.world.get_obstacles())
        # Step 3: update current position by the deltas
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        
class Player:
    def _update_screen_offset(self):
        """Logics for horizontal world scroll based on player movement"""
        delta_screen_offset = 0
        at_right_edge = self.rect.right >= GameConfig.WIDTH
        at_right_soft_edge = self.rect.right > GameConfig.WIDTH - GameConfig.PLAYER_SOFT_EDGE_WIDTH
        at_left_edge = self.rect.left <= 0
        at_left_soft_edge = self.rect.left < GameConfig.PLAYER_SOFT_EDGE_WIDTH
        if (
                at_left_edge
                or at_right_edge
                or (at_left_soft_edge and not self.world.at_left_most())
                or at_right_soft_edge
        ):
            # Undo player position change (player walks in-place)
            self.rect.x -= self.dx
            delta_screen_offset = -self.dx
        self.world.update_screen_offset(delta_screen_offset)


    # Step 1: calculate would-be dx, dy when unobstructed
    self.dx = 0
    self.dy += GameConfig.GRAVITY

    if self.moving_left:
        self.dx = -self.speed
    if self.moving_right:
        self.dx = self.speed

    # Step 2: update current position by the deltas
    self.rect.x += self.dx
    self.rect.y += self.dy

    self.is_landed = False

if self.rect.bottom >= GameConfig.GROUND_LEVEL:
    self.rect.bottom = GameConfig.GROUND_LEVEL


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