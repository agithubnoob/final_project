MAX_HP: int = 3


class PlayerHpConfig:
    X: int = 10
    Y: int = 30
    X_STEP: int = 60  # distance between 2 consecutive hearts
    FULL_HEART_PATH: Path = ASSET_DIR / "items" / "full_heart.png"
    EMPTY_HEART_PATH: Path = ASSET_DIR / "items" / "empty_heart.png"

class PlayerInventoryConfig:
    X: int = 290