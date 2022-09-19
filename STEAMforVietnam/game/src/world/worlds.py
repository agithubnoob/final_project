def get_trampolines(self) -> List[BaseEntity]:
    return [
        entity
        for entity in self.entities.values()
        if entity.entity_type == EntityType.TRAMPOLINE
    ]


self.add_entity(
    EntityType.TRAMPOLINE,
    76,
    612,
)

if self.is_loading:
    self.loading_percent += LevelLoadingBarConfig.STEP
    util.draw_loading_bar(self.screen, self.loading_percent)
    if self.loading_percent >= 100:
        self.is_loading = False
    self.is_loading = True
    ball = self.world.get_entity(ball_id)
    if self.get_flip_x():
        ball.move_left()
    else:
        ball.move_right()


    def _handle_throw(self):
        """
        Spawns a ball at Player position, around the shoulder-level.
        Set it motions to go left or right depending on the facing of Player.
        :return:
        """
        self.set_action(ActionType.THROW, duration_ms=PlayerConfig.THROW_DURATION_MS)
        ball_id = self.world.add_entity(
            EntityType.PLAYER_BULLET,
            self.rect.centerx,
            self.rect.centery - 30,
        )