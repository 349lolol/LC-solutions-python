class Solution:
    def trap(self, height: List[int]) -> int:
        left_height = height[0]
        left_peak = 1
        right_height = height[len(height) - 1]
        right_peak = len(height) - 2
        indices = []
        water = 0
        while(left_peak <= right_peak):
            if(left_height <= right_height):
                if(left_height > height[left_peak]):
                    water = water + left_height - height[left_peak]
                    indices.append(left_peak)
                else:
                    left_height = height[left_peak]
                left_peak = left_peak + 1
            else:
                if(right_height > height[right_peak]):
                    water = water + right_height - height[right_peak]
                    indices.append(right_peak)
                else:
                    right_height = height[right_peak]
                right_peak = right_peak - 1
        return water

