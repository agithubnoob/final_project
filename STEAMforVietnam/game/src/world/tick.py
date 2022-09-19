from asyncio import events

import pygame as pygame

from game.src.entities import self


class EventType:
    pass


for e in events:
    if e.is_type(EventType.START_GAME):
        self.start_or_resume_game(level_id=e.event.level_id, force_start=True)
    elif e.is_type(EventType.RESTART_LEVEL):
        self.start_or_resume_game(level_id=self.level_id, force_start=True)
    elif e.is_type(EventType.RESUME_GAME):
        self.start_or_resume_game(level_id=self.level_id, force_start=False)
    elif e.is_type(EventType.LEVEL_END):
        self.start_or_resume_game(level_id=self.level_id + 1)
    elif e.is_key_up(pygame.K_ESCAPE) and self.active_world == self.WORLD_GAME:
        self.active_world = self.WORLD_MENU