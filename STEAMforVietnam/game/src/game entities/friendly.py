from __future__ import annotations
from config import GameConfig, NpcConfig
from game_entities.base import BaseEntity


from typing import Sequence

import pygame

from game.src.common.event import EventType
from game.src.entities import GameEvent, World, self


def update(self, events: Sequence[GameEvent], world: World) -> None:
    self.events = events
    self.world = world
    self._handle_events()
    if self.is_near_player:
        self._highlight() // 'Xuất hiện Dấu chấm hỏi'
    else:
        self._unhighlight() // 'Nếu Player đi xa khỏi NPC, mất dấu chấm hỏi'
    super().update(events, world)

PLAYER_ACTIVATE_NPC = pygame.event.custom_type()

str_quest_name = next_dialogue_item.get("QuestToStart")
