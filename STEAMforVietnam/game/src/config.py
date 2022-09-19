from dataclasses import dataclass
from pathlib import Path

from game.src.common.types import EntityType

GameConfig.FPS = 60

@dataclass
class NpcConfig:
    entity_type: EntityType
    scale: float = 0.07
    animation_interval_ms: int = 900
    default_alpha: int = 180  # 255 is fully opaque
    def __post_init__(self, ASSET_DIR=None):
        self.sprite_path = ASSET_DIR / "npcs" / self.entity_type.name.lower()

class PlayerInventoryConfig:
    X: int = 290
    Y: int = 30
    X_STEP: int = 60  # distance between 2 consecutive items
    # the simple vertical divider
    SPRITE_PATH: Path = ASSET_DIR / "items" / "player_inventory.png"
    SCALE: int = 1
    TILE_SIZE: int = 34

class LevelLoadingBarConfig:
    WIDTH: int = 600
    HEIGHT: int = 100
    STEP = 3 if not GameConfig.DEBUG else 10  # how fast the loading bar goes

class PlayerBulletConfig:
    SPRITE_PATH: Path = ASSET_DIR / "items" / "player_bullet.png"
    SCALE: float = 0.7
    SPEED: int = 35
    GRAVITY: int = 2
    DAMAGE: int = 10
    # initial vertical movement
    INIT_DY: int = -10
    # the time between creation and deletion of entities of this type
    TTL_MS: int = 400 * 60 // GameConfig.FPS

