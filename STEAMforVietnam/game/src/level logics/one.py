# After talking to this NPC (the last NPC in level 1), level 1 should end.
from game.src.common import event
from game.src.common.event import EventType
from game.src.entities import GameEvent

if event.get_sender_id() == npc_chu_nhan_id and event.is_type(EventType.NPC_DIALOGUE_END):
    GameEvent(EventType.LEVEL_END).post()

