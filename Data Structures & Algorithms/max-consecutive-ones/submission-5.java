class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLength=0, l=0;

        if(nums.length==1)
        return nums[0];

        for(int i=0;i<nums.length;i++){
            if(nums[i]==1){
                l++;
                if(l>=maxLength)
                 maxLength=l;
            }

            if(nums[i]==0){

                if(l>=maxLength)
                 maxLength=l;

                 l=0;

            }
        }
        
        return maxLength;
    }
}