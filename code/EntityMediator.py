from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


# mediação entre entidades - colisões
class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # método privado(somente acessado nessa classe), underline dupla
        if isinstance(ent, Enemy):  # destruição do inimigo
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and ent2.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'PlayerShot':
            for ent in entity_list:
                if ent.name == 'Player':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # esse método está recebendo todas as entidades
        for i in range(len(entity_list)):
            test_entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity1)  # para testar se a entidade bateu no limite da tela

            for j in range(i + 1,
                           len(entity_list)):  # comparar uma c todas as outras entidades para testar se há colisão
                test_entity2 = entity_list[j]  # "i+1" para evitar colisões duplicadas/redundâncias
                EntityMediator.__verify_collision_entity(test_entity1, test_entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # destruição do inimigo
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
