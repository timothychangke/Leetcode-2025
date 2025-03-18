def solution(n, m, startCorner, indent, fullRotations):
    indent += 1
    grid = [["0" for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if startCorner == 1:
        x, y, dir_idx = 0, 0, 0
    elif startCorner == 2:
        x, y, dir_idx = 0, m - 1, 1
    elif startCorner == 3:
        x, y, dir_idx = n - 1, m - 1, 2
    elif startCorner == 4:
        x, y, dir_idx = n - 1, 0, 3
    top, bottom, left, right = 0, n - 1, 0, m - 1
    turns = 0
    
    while (turns // 4) < fullRotations:
        grid[x][y] = "1"
        dx, dy = d[dir_idx]
        nx, ny = x + dx, y + dy
        
        
        if not (top <= nx <= bottom and left <= ny <= right):
            if turns > 1:
                if dir_idx == 2:
                    top += indent
                elif dir_idx == 3:
                    right -= indent
                elif dir_idx == 0:
                    bottom -= indent
                elif dir_idx == 1:
                    left += indent
            dir_idx = (dir_idx + 1) % 4
            dir = d[dir_idx]
            dx, dy = dir
            turns += 1
            nx, ny = x + dx, y + dy
            if not (top <= nx <= bottom and left <= ny <= right): break
        x, y = nx, ny
    return grid

n = 18
m = 9
startCorner = 2
indent = 2
fullRotations = 2

result = solution(n, m, startCorner, indent, fullRotations)

for row in result:
    print(' '.join(row))
    
    
    
""" 
Artur has an n × m piece of paper on which he wants to draw a spiral. He'll start the spiral at one of the corners and draw clockwise. The turns of the spiral he's drawing must be separated by indent squares. In total, Artur wants to draw fullRotations full rotations of the spiral, but he isn't sure that he can do it on this piece of paper. You can help him draw this spiral!

You have two integers, n and m, that define the size of the paper. You also have the corner startCorner where the spiral starts (1 for top-left, 2 for top-right, 3 for bottom-right, and 4 for bottom-left), an indent between turns, and fullRotations that defines the number of full rotations (4 turns of 90 degrees each) that Artur wants to draw. Return an array of length n that contains char arrays of length m composed of '0's and '1's , where the '1's represent the spiral. If the paper is too small to contain the given number of full rotations, Artur should draw as many 90 degree turns as possible.

Example

    For n = 18, m = 9, startCorner = 1, indent = 1, and fullRotations = 2, the output should be

    solution(n, m, startCorner, indent, fullRotations) = [
         ['1', '1', '1', '1', '1', '1', '1', '1', '1'],
         ['0', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '1', '1', '1', '1', '1', '1', '0', '1'],
         ['1', '0', '0', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '0', '0', '0', '1', '0', '1'],
         ['1', '0', '1', '1', '1', '1', '1', '0', '1'],
         ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '1', '1', '1', '1', '1', '1', '1', '1']]

    The spiral starts at the top-left corner of the paper and goes right. The spiral ends after two full rotations.

    For n = 18, m = 9, startCorner = 2, indent = 2, and fullRotations = 2, the output should be

    solution(n, m, startCorner, indent, fullRotations) = [
         ['1', '1', '1', '1', '1', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '1', '0', '0', '1'],
         ['1', '0', '0', '1', '1', '1', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
         ['1', '1', '1', '1', '1', '1', '1', '1', '1']]

    The spiral starts at the top-right corner of the paper and goes down. Unfortunately, there isn't space for two full rotations, so the spiral ends after the first part of the second rotation.

Input/Output

    [execution time limit] 4 seconds (py3)

    [memory limit] 1 GB

    [input] integer n

    The height of the paper.

    Guaranteed constraints:
    3 ≤ n ≤ 100.

    [input] integer m

    The width of the paper.

    Guaranteed constraints:
    3 ≤ m ≤ 100.

    [input] integer startCorner

    The corner where the spiral starts. 1 represents the top-left corner, 2 the top-right corner, 3 the bottom-right corner, and 4 the bottom-left corner.

    Guaranteed constraints:
    1 ≤ startCorner ≤ 4.

    [input] integer indent

    The amount of indentation between the spiral's turns.

    Guaranteed constraints:
    1 ≤ indent ≤ 10.

    [input] integer fullRotations

    The number of full rotations the spiral should be composed of, if possible.

    Guaranteed constraints:
    1 ≤ rotations ≤ 20.

    [output] array.array.char

    An array of length n that contains char arrays of length m composed of 0s and 1s, where the 1s represent the spiral.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name


"""