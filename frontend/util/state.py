from typing import Any 

def update_states(entities: list[Any]):
    for entity in entities:
        entity.update()

def update_state(entity: Any):
    entity.update()

def draw_states(entities: list[Any]):
    for entity in entities:
        entity.draw()

def draw_state(entity: Any) -> None:
    entity.draw()

def cleanup_states(entities: list[Any]) -> None:
    for _ in range(len(entities) - 1, -1, -1):
        if not entities[_].is_alive:
            del entities[_]

def cleanup_state(entity: Any) -> None:
    if not entity.is_alive:
        del entity
