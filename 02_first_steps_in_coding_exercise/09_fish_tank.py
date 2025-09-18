length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = length * width * height
volume_liters = aquarium_volume * 0.001
occupied_space = percent / 100
liters_needed = volume_liters * (1 - occupied_space)

print(liters_needed)
