import numpy as np
import random

class Map:
    def __init__(self, map_size, num_bots, num_treasures, num_traps, rounds, treasure_evaporation_rate, trap_evaporation_rate, bot_positions=None):
        self.map_size = map_size
        self.map = self._initialize_map(map_size, num_bots, num_treasures, num_traps)
        self.rounds = rounds
        self.num_bots = num_bots
        self.num_treasures = num_treasures
        self.num_traps = num_traps

        self.treasure_evaporation_rate = treasure_evaporation_rate
        self.trap_evaporation_rate = trap_evaporation_rate

        # Generate random initial positions for every bot
        self.bot_positions = ...

    def _initialize_map(self, map_size, num_bots, num_treasures, num_traps):
        # Initialize map
        raw_map = np.zeros((map_size, map_size))

        # Generate unique positions for bots, tresures, traps
        positions = set()
        while len(positions) < (num_bots + num_treasures + num_traps):
            position = (random.randint(0, self.map_size-1), random.randint(0, self.map_size-1))
            positions.add(position)
        
        positions_arr = np.array(list(positions))
        
        # Bot positions
        bot_positions = positions_arr[ :num_bots]
        # Treasure positions
        treasure_positions = positions_arr[num_bots : num_bots + num_traps]
        # Trap positions
        trap_positions = positions_arr[num_bots + num_traps: ]

        # Actualize positions into maps
        for position in bot_positions: 
            raw_map[position[0]][position[1]] = 99

        for position in treasure_positions: 
            raw_map[position[0]][position[1]] = 1 

        for position in trap_positions: 
            raw_map[position[0]][position[1]] = -1 

        return raw_map
    
    def update(self):
        for i in range(self.map_size): 
            for j in range(self.map_size):
                # Treasure update
                if 0 < self.map[i][j] <= 1:
                    self.map[i][j] -=self.treasure_evaporation_rate
                # Treasure update
                elif -1 < self.map[i][j] < 0:
                    self.map[i][j] +=self.trap_evaporation_rate
                


map_instance = Map(
    map_size=5,
    num_bots=2,
    num_treasures=2,
    num_traps=2,
    rounds=10,
    treasure_evaporation_rate=0.1,
    trap_evaporation_rate=0.1
)

print(map_instance.map)

map_instance.update()

print(map_instance.map)