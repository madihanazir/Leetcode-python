class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            hashmap = {p: s for p, s in zip(position, speed)}  
            sorted_positions = sorted(hashmap.keys(), reverse=True)  # Sort positions in reverse order
            
            stack = []
            for p in sorted_positions:  # Iterate over sorted positions
                s = hashmap[p]  # Get the speed for the current position
                stack.append((target - p) / s)  # Calculate time to reach target
                if len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()
            
            return len(stack)


        