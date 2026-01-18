import time
import os

puppy_frames = [
r"""
   /\_/\ 
  ( o o )   ♪
   > ^ <  ♪
   /   \
""",
r"""
   /\_/\ 
  ( o o )  ♫
   < ^ > ♫
   \   /
""",
r"""
   /\_/\ 
  ( o o )   ♪
   > ^ <  ♪
   /   \
"""
]

while True:
    for frame in puppy_frames:
        os.system("cls" if os.name == "nt" else "clear")
        print(frame)
        time.sleep(0.2)
        
