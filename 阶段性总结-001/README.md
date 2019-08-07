1、可以使用C++、Java、Python等编程语言进行刷题，推荐使用C++/Java，如果有困难可以使用python

2、创建自己的GitHub，并进行刷题总结，格式参考
https://github.com/wanghao07456/ChinaHadoop_AI_Offer

3、需要在微信群内提交题目accepted截图

Hi all,

7月25日：

阶段性总结

要求大家对过往做过的题目进行解法总结，今日总结双指针。要求在规定时间8-10分钟AC题目，并提交总结报告。有困难的同学在小群沟通。Tips：1、本次阶段性总结结束之后会进行dp的专项练习。之后会循环复习，不再有专门总结时间。2、除了咱们做过的相关题目，可以找对应LeetCode推荐的项目题目总结练习，数量2-3个为佳

Two Pointers:
1、相向双指针：两根指针一头一尾，向中间靠拢直到相遇，时间复杂度 O(n)
Two Sum 类：哈希表和双指针，双指针更快
Partition 类：
 # partition模板
while left <= right:
 while left <= right and nums[left] 应该在左侧:
  left +=1 
 while left <= right and nums[right] 应该在右侧:
  right -=1
 if left <= right:
  # 找到了一个不该在左侧的不该在右侧的，交换他们
  nums[left], nums[right] = nums[right], nums[left]
  left += 1
  right -= 1

 2、同向双指针：两根指针一前一后，直到前面的指针走过头，时间复杂度 O(n)

如果需要保证最少修改次数如何做？ 
使用 Partition 的方法可以做到交换次数最优 

不需要维持相对顺序 vs 需要维持相对顺序 算法有什么区别？ 
不需要维护相对顺序，可以使用 Partition 的方法，时空复杂度和交换次数都是最优的 需要维护相对顺序的，只能使用同向双指针的方法，时空复杂度最优，但是交换次数不是最优 的
