import pydirectinput
import random
import time

# List of keys to randomly choose from
keys = ['w', 's', 'a', 'd']

print("Script will start in 5 seconds. Switch to the game window!")
time.sleep(5)
print("DirectInput script has started! Press Ctrl+C to stop it.")

try:
    while True:
        # 1. Pick a random key from the WASD list
        key = random.choice(keys)
        
        # 2. Pick a random hold duration (from 1.0 to 5.73 seconds)
        hold_duration = random.uniform(1.0, 5.73)
        
        print(f"Holding key '{key.upper()}' for {hold_duration:.2f} seconds...")
        
        # 3. Press the key using DirectInput
        pydirectinput.keyDown(key)
        time.sleep(hold_duration)
        pydirectinput.keyUp(key)
        
        # Micro-pause for game smoothness
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopping script by user request...")

finally:
    # Safely release all keys on exit
    for k in keys:
        pydirectinput.keyUp(k)
    print("All keys have been released. Script has finished.")