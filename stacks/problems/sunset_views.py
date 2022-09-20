# east ---> right 
# west <--- left

# buildings = [3, 5, 4, 4, 3, 1, 3, 2]
# sunset_buildings = []
# index 0
# index 1 - 7

# sunset_buildings = [1]
# index 1
# index 2 - 7

# sunset_buildings = [1]
# index 2
# index 3 - 7

def sunsetViews(buildings, direction):
    # Write your code here.
    sunset_buildings = []
    start_idx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else - 1

    idx = start_idx
    running_max_height = 0
    while idx >= 0 and idx < len(buildings):
        building_height = buildings[idx]

        if building_height > running_max_height:
            sunset_buildings.append(idx)
        
        running_max_height = max(building_height, running_max_height)
        idx += step
    
    if direction == "EAST":
        return sunset_buildings[::-1]

    return sunset_buildings

if __name__ == '__main__':
    print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2], "East"))