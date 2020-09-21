class Solution:
    def trap(self, height) -> int:
        if len(height) <= 2:
            return 0
        max_h = max(height[1:-1])
        pos = height[1:-1].index(max_h) + 1
        if max_h <= height[0] and max_h <= height[-1]:
            return min(height[0],height[-1])*(len(height)-2) - sum(height[1:-1])
        else:
            left = self.trap(height[0:pos + 1])
            right = self.trap(height[pos:])
            return left + right



if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))