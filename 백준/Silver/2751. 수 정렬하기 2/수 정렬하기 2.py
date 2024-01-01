import sys
arr = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

print(*sorted(arr), sep='\n')