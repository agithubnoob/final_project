from __future__ import annotations
from config import GameConfig, NpcConfig
from game_entities.base import BaseEntity
class FriendlyNpc(BaseEntity):
    """
    Non-playable character, will talk and interact with Player.
    """
    def __init__(self, npc_config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Shift position up to above the ground tile, since Npc is taller than standard tile size.
        self.rect.bottom = self.rect.y + GameConfig.TILE_SIZE
        self.npc_config: NpcConfig = npc_config