import time
import os
import random

WIDTH = 20
HEIGHT = 20

def main():
    snake = [[10, 10], [10, 11], [10, 12]]
    direction = 'UP'
    food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
    score = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if i == 0 or i == HEIGHT-1 or j == 0 or j == WIDTH-1:
                    print('#', end='') 
                elif [i, j] == snake[0]:
                    print('O', end='') 
                elif [i, j] in snake[1:]:
                    print('o', end='') 
                elif i == food[0] and j == food[1]:
                    print('*', end='') 
                else:
                    print(' ', end='')
            print()
            
        print(f"Score: {score}")
        print("Game chalane ke liye Ctrl+C se exit karein abhi.")
        
        head = snake[0].copy()
        if direction == 'UP': head[0] -= 1
        elif direction == 'DOWN': head[0] += 1
        
        snake.insert(0, head) 
        
        if snake[0] == food:
            score += 1
            food = [random.randint(1, HEIGHT-2), random.randint(1, WIDTH-2)]
        else:
            snake.pop() 
            
        if snake[0][0] == 0 or snake[0][0] == HEIGHT-1 or snake[0][1] == 0 or snake[0][1] == WIDTH-1:
            print("GAME OVER!!!")
            break
            
        time.sleep(0.2) 

if __name__ == "__main__":
    main()