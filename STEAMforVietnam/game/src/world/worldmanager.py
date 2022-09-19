def start_or_resume_game(self, level_id: int, force_start: bool):
    self.active_world = self.WORLD_GAME
    if force_start or not self.worlds[self.active_world] or level_id != self.level_id:
        logger.info(f"Current level: {self.level_id} -> (Re)starting level: {level_id}")
        self.level_id = level_id
        self.worlds[self.active_world] = World(self.screen, level_id=level_id)
        # TODO: this could be optimized instead of initiating a new Menu instance somehow?
        self.worlds[self.WORLD_MENU] = Menu(self.screen, can_resume=True)
    elif e.is_type(EventType.LEVEL_END):
        e.event.level_id = self.level_id
        if self.level_id < 10:
            # Player finishes a main story level, go to next level
            GameEvent(EventType.START_GAME, level_id=self.level_id + 1).post()
        else:
            # Player finishes a bonus level, show a congrats screen
            self.start_scene(BonusLevelEnd)