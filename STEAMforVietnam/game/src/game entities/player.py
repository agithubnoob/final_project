from venv import logger

import pygame

class self:
    pass

class GameEvent:
    pass


class World:
    pass


for event in self.events:
    if event.is_key_down(pygame.K_LEFT, pygame.K_a):
        self.move_left(True)
    elif event.is_key_down(pygame.K_RIGHT, pygame.K_d):
        self.move_right(True)
    elif event.is_key_down(pygame.K_UP, pygame.K_SPACE, pygame.K_w):
        self.jump()
    elif event.is_key_up(pygame.K_LEFT, pygame.K_a):
        self.move_left(False)
    elif event.is_key_up(pygame.K_RIGHT, pygame.K_d):
        self.move_right(False)
    elif event.is_key_down(pygame.K_f):
        self._handle_throw()

def jump(self):
    if self.is_landed:
        self.is_landed = False
        self.dy = -self.jump_vertical_speed

self._handle_get_hit()


def handle_get_hit(self)->None:
    for shadow in self.world.get_entities(EntityType.SHADOW):
        if self.collide(shadow):
            self._take_damage(1)


def take_damage(self, damage: int) -> None:
    if now() - self.last_hit_t > PlayerConfig.INVULNERABLE_DURATION_MS:
        self.last_hit_t = now()
        self.hp -= damage


def _pick_item_near_by(self):
    """
    If Player collides with a collectable entity, remove that entity from World,
    while adding that entity to the self.inventory list.
    """
    for entity in self.world.get_collectable_tiles():
        if self.collide(entity):
            self.world.remove_entity(entity.id)
            self.inventory.append(entity)
            logger.info(f"Player picked up 1 {entity.entity_type}")

def _update_inventory_entity(self):
    """
    This Player entity directly manages a PlayerInventory entity.
    """
    if not self.inventory_entity_id:
        self.inventory_entity_id = self.world.add_entity(EntityType.PLAYER_INVENTORY)
    self.world.get_entity(self.inventory_entity_id).set_inventory(self.inventory)

def _maybe_jump_with_trampoline(self):
    for trampoline in self.world.get_trampolines():
        if self.collide(trampoline) and self.rect.bottom > trampoline.rect.top:
            trampoline.set_action(ActionType.JUMP)
            self.jump_with_trampoline()
        else:
            trampoline.set_action(ActionType.IDLE)

def update(self, events: Sequence[GameEvent], world: World) -> None:
    super().update(events, world)
    self._update_npc_near_by()
    self._pick_item_near_by()
    self._handle_events()
    self._update_screen_offset()
    # highlight this call only
    self._maybe_jump_with_trampoline()
    # Manage the dependent entities.
    self._update_inventory_entity()
    ball = self.world.get_entity(ball_id)


def render(self, screen: pygame.Surface, *args, **kwargs):
    super().render(screen, *args, **kwargs)

    for i in range(0, PlayerConfig.MAX_HP):
        if i < self.hp:
            screen.blit(
                pygame.image.load(PlayerHpConfig.FULL_HEART_PATH),
                (PlayerHpConfig.X + i * PlayerHpConfig.X_STEP, PlayerHpConfig.Y),
            )
        else:
            screen.blit(
            pygame.image.load(PlayerHpConfig.EMPTY_HEART_PATH),
            (PlayerHpConfig.X + i * PlayerHpConfig.X_STEP, PlayerHpConfig.Y),
            )


