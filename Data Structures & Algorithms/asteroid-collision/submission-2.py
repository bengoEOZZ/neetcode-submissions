class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while alive and ast < 0 and stack and stack[-1] > 0:
                if -ast > stack[-1]:
                    stack.pop()
                elif -ast == stack[-1]:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(ast)
        return stack