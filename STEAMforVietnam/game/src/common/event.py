import enum

import pygame


class EventType(enum.Enum):
    [...]
    LEVEL_END = pygame.event.custom_type()

QUEST_START = pygame.event.custom_type()
QUEST_END = pygame.event.custom_type()
BOSS_DIE = pygame.event.custom_type()
