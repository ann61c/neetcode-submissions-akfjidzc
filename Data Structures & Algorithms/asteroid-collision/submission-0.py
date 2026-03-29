class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            #last in, first out
            while stack and asteroid < 0 and stack[-1] >0:
                size = abs(asteroid)
                if size == stack[-1]:
                    asteroid = 0
                    stack.pop()
                elif size > stack[-1]:
                    stack.pop()
                else:
                    asteroid = 0


            if asteroid:
                stack.append(asteroid)
        return stack