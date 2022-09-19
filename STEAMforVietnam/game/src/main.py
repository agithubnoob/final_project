def _activate(self):
    """
    Manipulates the dialogue box entity.
    """
    logger.info("NPC Activated")
    if not self.dialogue_box_id:
        self.dialogue_box_id = self.world.add_entity(EntityType.DIALOGUE_BOX)
    dialogue_box = self.world.get_entity(self.dialogue_box_id)
    dialogue_box.sprite.set_text("Xin chào!")
