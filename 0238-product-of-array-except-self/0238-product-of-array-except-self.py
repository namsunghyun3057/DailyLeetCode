class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
    
        # Fill the left_products array
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
    
        print(left_products)
    
        # Fill the right_products array
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
    
        print(right_products)
    
        # Calculate the final answer using left_products and right_products
        answer = [left_products[i] * right_products[i] for i in range(n)]
    
        return answer
        