SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 768


class WorldData:
    level_id: int
    data: Optional[List] = None
    def __post_init__(self):
        with open(DATA_DIR / "levels" / f"{self.level_id}.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            self.data = [
                [EntityType(int(tile or EntityType.EMPTY.value)) for tile in row] for row in reader
            ]


class World:
    def load_level(self, level_id):
        data = WorldData(level_id=level_id).data
        for i, row in enumerate(data):
            for j, entity_type in enumerate(row):
                if entity_type == EntityType.EMPTY:
                    continue
                x = j * GameConfig.TILE_SIZE
                y = i * GameConfig.TILE_SIZE
                self.add_entity(
                    entity_type=entity_type,
                    x=x,
                    y=y,
                )