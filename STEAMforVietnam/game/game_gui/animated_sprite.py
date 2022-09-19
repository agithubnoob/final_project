import pygame as pygame

def _load_sprites(
        sprites_dir: Path, scale: float = 0.1
) -> Dict[ActionType, List[pygame.Surface]]:
    """
    Load all images from directory and convert into a Dictionary
    which maps ActionType to list of Surface
    """
    sprites: List[pygame.Surface] = []

    for image_file in sprites_dir.iterdir():
        image = pygame.image.load(str(image_file))
        sprites.append(util.scale_image(image, scale))
    return sprites

def render(self, screen: pygame.Surface, *args, **kwargs) -> None:
    """
    Redraw at every Game tick
    """
    # Change to the next sprite in the sequence corresponding to the current action
    # (note that there are multiple sequences to choose from)
    current_ms = pygame.time.get_ticks()
    if current_ms - self.last_animation_ms > self.animation_interval_ms:
        self.last_animation_ms = current_ms
        self.sprite_index = (self.sprite_index + 1) % len(self.sprites[self.action])
    self.image = self.sprites[self.action][self.sprite_index]
    super().render(screen, flip_x=self.flip_x, *args, **kwargs)


