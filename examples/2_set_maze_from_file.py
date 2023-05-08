from mcpi.minecraft import Minecraft
import time

SERVER = "127.0.0.1"
PORT = 4711

MAZE_FILENAME = "examples/assets/maze.txt"

# Set this to your player postion
START_POSITION = (0, 4, 0)

def load_maze_file_contents(filename):
    maze_file_contents = None
    with open(filename) as maze_file:
        maze_file_contents = maze_file.read()
    return maze_file_contents

def convert_maze_file_to_coordinates(maze_file_contents):
    coordinates = []
    count_x = 0
    count_y = 0
    for line in maze_file_contents.split("\n"):
        for letter in line:
            if letter != " ":
                coordinates.append((count_x, count_y))
            count_x += 1
        count_y += 1
        count_x = 0
    return coordinates

def generate_maze_from_coordinates(start_position, coordinates, block_type=1, sleep=True):
    # connect to minecraft server
    mc = Minecraft.create(SERVER, PORT)

    mc.postToChat("Deploying a maze in :")
    for i in range(3):
        mc.postToChat(f"{i}")
        time.sleep(1)

    start_x, start_y, start_z = start_position
    count = 0
    for coordinate in coordinates:
        c_x, c_z = coordinate
        if count == 10 and sleep:
            time.sleep(0.1)
            count = 0
        count += 1
        mc.setBlock(c_x + start_x, start_y, c_z + start_z, block_type)
        mc.setBlock(c_x + start_x, start_y + 1, c_z + start_z, block_type)
        mc.setBlock(c_x + start_x, start_y + 2, c_z + start_z, block_type)

    
def main():
    # load maze file contents
    print("loading maze file contents")
    maze_file_contents = load_maze_file_contents(MAZE_FILENAME)
    # convert the contents of the maze to coordinates
    print("converting maze file contents to coordinates")
    coordinates = convert_maze_file_to_coordinates(maze_file_contents)
    # add contents to minecraft world
    print("generate maze")
    generate_maze_from_coordinates(START_POSITION, coordinates, 49, False)

if __name__ == '__main__':
    main()
