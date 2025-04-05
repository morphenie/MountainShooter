from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


# mediação entre entidades - colisões
class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # método privado, underline dupla
        if isinstance(ent, Enemy): # destruição do inimigo
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # esse método está recebendo todas as entidades
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)  # para testar se a entidade bateu no limite da tela

    @staticmethod
    def verify_health(entity_list: list[Entity]): # destruição do inimigo
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)