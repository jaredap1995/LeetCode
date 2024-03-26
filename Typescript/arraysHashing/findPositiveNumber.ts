var solution = function(nums: number[]): number {
     var swap = (arr: number [], i: number, j: number) => {
        [arr[i], arr[j]] = [arr[j], arr[i]]
     }

     for (let i = 0; i< nums.length; i++){
        while (nums[i] > 0 && nums[i] <= nums.length && nums[i] !== nums[nums[i] - 1]) {
            swap(nums, i, nums[i] - 1);
        }
     }


     for (let i = 0; i< nums.length; i++){
        if (nums[i] !== i +1) return i + 1
     }

     return nums.length + 1
}