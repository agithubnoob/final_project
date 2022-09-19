def draw_loading_bar(screen: Surface, loading_percent: int):
    draw_pct_bar(
        screen,
        fraction=loading_percent / 100,
        x=(GameConfig.WIDTH - LevelLoadingBarConfig.WIDTH) / 2,
        y=(GameConfig.HEIGHT - LevelLoadingBarConfig.HEIGHT) / 2,
        width=LevelLoadingBarConfig.WIDTH,
        height=LevelLoadingBarConfig.HEIGHT,
        margin=10,
        color=Color.LOADING_BAR,
    )


def draw_pct_bar(screen: Surface, fraction: float, x, y, width, height, margin, color: Color):
    """
    Draw a bar at given position, filled up to the given `fraction`.
    """
    fraction = min(fraction, 1)
    pygame.draw.rect(screen, color, (x, y, width, height), 2)
    pygame.draw.rect(
        screen,
        color,
        (x + margin, y + margin, int(fraction * (width - 2 * margin)), height - 2 * margin),
    )
