import json

import pygame
from config import Color, DialogueBoxConfig, Font
from gui.base_sprite import BaseSprite

class DialogueBoxSprite(BaseSprite):
    """
    Render the dialogue box and text within it.
    """
    def set_text(self, text):
        self.text = text
    def render(self, screen, *args, **kwargs):
        super().render(screen, *args, **kwargs)
        if not self.text:
            return
        x = self.rect.x + DialogueBoxConfig.PADDING_X
        y = self.rect.y + DialogueBoxConfig.PADDING_Y + DialogueBoxConfig.LINE_HEIGHT
        screen.blit(
            Font.FREESANSBOLD_14.render(self.text, True, Color.TEXT_DIALOGUE_SUBJECT),
            (x, y),
        )


repr(repr(repr(json)))
{
    "name": "Cô Nga",
    "dialogues": [
      [
        {
          "Subject": "Cô Nga",
          "Line": "Xin chào em! Em tên là gì?"
        },
        {
          "Subject": "Táy Máy",
          "Line": "Xin chào cô! Em tên là Táy Máy. Em là thực tập sinh mới ạ."
        },
        {
          "Subject": "Cô Nga",
          "Line": "Ồ, tốt quá. Em có thể nhặt hộ cô những viên kẹo bị đánh rơi được không?"
        },
        {
          "Subject": "Táy Máy",
          "Line": "Được ạ!"
        }
      ],
      [
        {
          "Subject": "Cô Nga",
          "Line": "Em nhặt được hết kẹo chưa?"
        }
      ]
    ]
}

NPC_DIALOGUE_END = pygame.event.custom_type()