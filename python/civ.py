#!/usr/bin/env python3
"""
bronze_age_sim.py

Simple civilization simulation inspired by Dwarf Fortress but at a larger scale.
No external libraries. Run: python bronze_age_sim.py
"""

import random
import math
from collections import defaultdict

# ----- CONFIG -----
MAP_W = 32
MAP_H = 12
NUM_SETTLEMENTS = 6
INITIAL_SEED = 42
TURNS = 60 # number of seasons/years to simulate
RANDOM = random.Random(INITIAL_SEED)

# Resource yields by tile type per farming worker per turn
YIELD_BY_TILE = {
    "plains": {"food": 4, "timber": 0, "stone": 0},
    "coast": {"food": 2, "timber": 0, "stone": 0},
    "hills": {"food": 2, "timber": 1, "stone": 1},
    "forest": {"food": 2, "timber": 3, "stone": 0},
    "mountain": {"food": 0, "timber": 0, "stone": 3},
}

# Prices (simple units) used for trade (base)
BASE_PRICE = {
    "food": 1.0,
    "timber": 1.2,
    "stone": 1.0,
    "copper": 5.0,
    "tin": 6.0,
    "bronze": 15.0,
    "pottery": 2.0,
    "textiles": 3.0,
}

# ----- MAP & TILES -----
TILE_TYPES = ["plains", "coast", "hills", "forest", "mountain"]
COAST_CHANCE = 0.15
FOREST_CHANCE = 0.15
MOUNTAIN_CHANCE = 0.10
HILLS_CHANCE = 0.20

def generate_map(w, h, rnd):
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            r = rnd.random()
            if r < COAST_CHANCE and (y == 0 or y == h-1 or x == 0 or x == w-1):
                t = "coast"
            elif r < COAST_CHANCE + FOREST_CHANCE:
                t = "forest"
            elif r < COAST_CHANCE + FOREST_CHANCE + MOUNTAIN_CHANCE:
                t = "mountain"
            elif r < COAST_CHANCE + FOREST_CHANCE + MOUNTAIN_CHANCE + HILLS_CHANCE:
                t = "hills"
            else:
                t = "plains"
            row.append(t)
        grid.append(row)
    # ensure some coast exists
    for x in range(w):
        grid[0][x] = "coast"
    return grid

# ----- SETTLEMENT -----
class Settlement:
    def __init__(self, name, x, y, tile_type, coastal, rnd):
        self.name = name
        self.x = x
        self.y = y
        self.tile = tile_type
        self.coastal = coastal
        self.population = rnd.randint(150, 400) # people
        # workforce split fractions (farmers, artisans, sailors, priests)
        self.workforce = {"farmers": 0.45, "artisans": 0.25, "sailors": 0.15 if coastal else 0.03, "priests": 0.05}
        self.stores = defaultdict(float)
        # initial stores
        self.stores["food"] = self.population * 2.5 # initial food supply
        self.stores["timber"] = 100.0
        self.stores["stone"] = 60.0
        self.stores["copper"] = 8.0 if rnd.random() < 0.3 else 0.0
        self.stores["tin"] = 6.0 if rnd.random() < 0.2 else 0.0
        self.stores["bronze"] = 0.0
        self.stores["pottery"] = 0.0
        self.stores["textiles"] = 0.0
        self.wealth = rnd.uniform(50, 250) # tradeable wealth
        self.happiness = 0.5
        self.age = 0
        self.history = []

    def pop_workers(self):
        # approximate workforce counts
        return {k: max(1, int(self.population * v)) for k, v in self.workforce.items()}

    def summary(self):
        return (f"{self.name}@({self.x},{self.y}) pop={self.population} food={int(self.stores['food'])} "
                f"bronze={self.stores['bronze']:.1f} wealth={self.wealth:.1f}")

# ----- CIVILIZATION -----
class Civilization:
    def __init__(self, grid, rnd):
        self.grid = grid
        self.rnd = rnd
        self.settlements = []
        self.global_log = []
        self.turn = 0
        self.generate_settlements(NUM_SETTLEMENTS)

    def random_coastal_tile(self):
        h = len(self.grid); w = len(self.grid[0])
        tries = 0
        while tries < 200:
            x = self.rnd.randrange(w)
            y = self.rnd.randrange(h)
            if self.grid[y][x] == "coast":
                return x, y
            tries += 1
        # fallback
        return self.rnd.randrange(w), self.rnd.randrange(h)

    def generate_settlements(self, n):
        h = len(self.grid); w = len(self.grid[0])
        used = set()
        for i in range(n):
            tries = 0
            while True:
                x = self.rnd.randrange(w)
                y = self.rnd.randrange(h)
                if (x,y) not in used and self.grid[y][x] != "mountain":
                    used.add((x,y))
                    break
                tries += 1
                if tries > 300:
                    break
            tile = self.grid[y][x]
            coastal = (tile == "coast")
            name = f"S{i+1}"
            s = Settlement(name, x, y, tile, coastal, self.rnd)
            self.settlements.append(s)

    def step(self):
        self.turn += 1
        logs = []
        # seasonal production & consumption
        for s in self.settlements:
            s.age += 1
            workers = s.pop_workers()
            # Food production
            farm_yield_per_worker = YIELD_BY_TILE.get(s.tile, {}).get("food", 1)
            produced_food = workers["farmers"] * farm_yield_per_worker * (0.9 + 0.2 * self.rnd.random())
            s.stores["food"] += produced_food
            logs.append(f"{s.name} produced {int(produced_food)} food (tile={s.tile})")
            # Timber & stone from artisans if near resources
            timber_yield = workers["artisans"] * YIELD_BY_TILE.get(s.tile, {}).get("timber", 0) * (0.5 + self.rnd.random())
            stone_yield = workers["artisans"] * YIELD_BY_TILE.get(s.tile, {}).get("stone", 0) * (0.4 + self.rnd.random())
            s.stores["timber"] += timber_yield
            s.stores["stone"] += stone_yield
            # Crafting: artisans convert raw goods into pottery/textiles
            craft_capacity = int(workers["artisans"] * (0.3 + 0.4 * self.rnd.random()))
            pottery_made = min(craft_capacity, int(s.stores["stone"] // 2))
            textiles_made = max(0, craft_capacity - pottery_made)
            s.stores["pottery"] += pottery_made
            s.stores["textiles"] += textiles_made
            s.stores["stone"] -= pottery_made * 1.5
            logs.append(f"{s.name} made {pottery_made} pottery and {textiles_made} textiles")
            # Bronze production if both copper and tin present
            # simple smelting: 1 bronze = 1 copper + 0.4 tin
            possible_bronze = min(s.stores["copper"], s.stores["tin"] / 0.4)
            smelted = min(possible_bronze, craft_capacity * 0.5)
            if smelted >= 1:
                s.stores["bronze"] += smelted
                s.stores["copper"] -= smelted
                s.stores["tin"] -= smelted * 0.4
                logs.append(f"{s.name} smelted {smelted:.1f} bronze")
            # Consumption
            food_needed = s.population * 1.0 # simple per person
            if s.stores["food"] >= food_needed:
                s.stores["food"] -= food_needed
                s.happiness = min(1.0, s.happiness + 0.01)
            else:
                deficit = food_needed - s.stores["food"]
                s.stores["food"] = 0
                # starvation -> population loss
                loss = int(min(s.population * 0.25, math.ceil(deficit / 1.0)))
                s.population = max(10, s.population - loss)
                s.happiness -= 0.15
                logs.append(f"FAMINE at {s.name}: lost {loss} people")
            # Trade attempt: if surplus food, ship to others; if lacking bronze, try to buy
            if s.stores["food"] > s.population * 3:
                surplus = int(s.stores["food"] - s.population*2)
                s.stores["food"] -= surplus
                # find needy settlement nearby
                dest = self.find_needy(s, "food")
                if dest:
                    transfer = min(surplus, int((dest.population*2 - dest.stores["food"])))
                    if transfer > 0:
                        dest.stores["food"] += transfer
                        s.wealth += transfer * BASE_PRICE["food"] * 0.2 # they sell for some goods
                        logs.append(f"{s.name} traded {transfer} food to {dest.name}")
            # Luxury upkeep: priests increase happiness if enough pottery or textiles
            if s.stores["pottery"] >= 2 and s.stores["textiles"] >= 1:
                s.happiness = min(1.0, s.happiness + 0.02)
                s.stores["pottery"] = max(0, s.stores["pottery"] - 2)
                s.stores["textiles"] = max(0, s.stores["textiles"] - 1)
            # Natural population growth (or decline)
            growth_rate = 0.01 + (s.happiness - 0.5) * 0.02
            pop_change = int(s.population * growth_rate)
            s.population = max(10, s.population + pop_change)
            # small wealth change by production
            s.wealth += (produced_food * 0.05 + timber_yield * 0.3 + stone_yield * 0.2)
        # Random events
        ev = self.random_event()
        if ev:
            logs.append(ev)
        # End-turn housekeeping
        self.global_log.extend(logs)
        return logs

    def find_needy(self, src, resource_key):
        # naive: return closest settlement that has resource < desired threshold
        best = None
        best_dist = 1e9
        for s in self.settlements:
            if s is src: continue
            if resource_key == "food":
                need = s.population*1.8 - s.stores["food"]
                if need > 5:
                    d = abs(s.x - src.x) + abs(s.y - src.y)
                    if d < best_dist:
                        best_dist = d
                        best = s
        return best

    def random_event(self):
        # small chance per turn
        r = self.rnd.random()
        if r < 0.04:
            # earthquake: random settlement loses buildings and stores
            target = self.rnd.choice(self.settlements)
            loss_food = int(target.stores["food"] * self.rnd.uniform(0.2, 0.6))
            target.stores["food"] = max(0, target.stores["food"] - loss_food)
            pop_loss = int(target.population * self.rnd.uniform(0.05, 0.2))
            target.population = max(5, target.population - pop_loss)
            msg = f"EARTHQUAKE at {target.name}! Lost {loss_food} food and {pop_loss} people."
            return msg
        elif r < 0.08:
            # Storm affecting a coastal settlement
            coasts = [s for s in self.settlements if s.coastal]
            if not coasts: return None
            t = self.rnd.choice(coasts)
            lost = int(t.stores["timber"] * self.rnd.uniform(0.2, 0.7))
            t.stores["timber"] = max(0, t.stores["timber"] - lost)
            return f"STORM hit {t.name}, lost {lost} timber from docks."
        elif r < 0.11:
            # Plague - reduces pop across settlements
            victim = self.rnd.choice(self.settlements)
            loss = int(victim.population * self.rnd.uniform(0.08, 0.18))
            victim.population = max(5, victim.population - loss)
            return f"PLAGUE in {victim.name}, lost {loss} people."
        elif r < 0.15:
            # Trade caravan opportunity: one settlement gains wealth
            s = self.rnd.choice(self.settlements)
            gain = int(20 + self.rnd.random() * 80)
            s.wealth += gain
            return f"Trade caravan visited {s.name} (+{gain} wealth)."
        return None

    def ascii_map(self):
        # produce simple ascii map showing tile types & settlements
        h = len(self.grid); w = len(self.grid[0])
        out = []
        sym = {"plains": ".", "coast": "~", "hills": "^", "forest": "♣", "mountain": "M"}
        # create marker map for settlements
        marker = {}
        for i, s in enumerate(self.settlements):
            marker[(s.x, s.y)] = s.name
        for y in range(h):
            row = ""
            for x in range(w):
                if (x,y) in marker:
                    # single char (S1 -> 1)
                    lab = marker[(x,y)]
                    ch = lab[-1]
                else:
                    ch = sym.get(self.grid[y][x], "?")
                row += ch
            out.append(row)
        return "\n".join(out)

    def print_status(self):
        print("="*72)
        print(f"Turn {self.turn}")
        print(self.ascii_map())
        print("-"*72)
        for s in sorted(self.settlements, key=lambda z: z.name):
            print(s.summary())
        print("-"*72)
        # civilization-wide totals
        totals = defaultdict(float)
        for s in self.settlements:
            totals["population"] += s.population
            for k, v in s.stores.items():
                totals[k] += v
            totals["wealth"] += s.wealth
        print(f"TOTAL POP: {int(totals['population'])} FOOD: {int(totals['food'])} BRONZE: {totals['bronze']:.1f} WEALTH: {totals['wealth']:.1f}")
        print("="*72)

# ----- RUN SIMULATION -----
def main():
    rnd = RANDOM
    grid = generate_map(MAP_W, MAP_H, rnd)
    civ = Civilization(grid, rnd)
    print("Initial map and settlements:")
    civ.print_status()
    for t in range(TURNS):
        logs = civ.step()
        # print summary every few turns
        if (t+1) % 5 == 0 or t < 5:
            civ.print_status()
            # also print important logs from last turn
            for L in logs:
                if any(k in L for k in ["FAMINE", "EARTHQUAKE", "PLAGUE", "Trade", "smelted"]):
                    print(" >", L)
    # final log excerpt
    print("\nRecent logs:")
    for line in civ.global_log[-20:]:
        print(" -", line)

if __name__ == "__main__":
    main()
