from mcpi.minecraft import Minecraft

server = "127.0.0.1"
port = 4711

mc = Minecraft.create(server, port)
# You must make sure your character is in the game
pos = mc.player.getPos()

print(f"x: {pos.x}\ny: {pos.y}\nz: {pos.z}")
