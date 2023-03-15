//https://www.acmicpc.net/problem/2562

int[] nums = new int[9];
for (int i = 0; i < 9; i++)
{
    nums[i] = int.Parse(Console.ReadLine());
}
Console.WriteLine($"{nums.Max()}");
Console.WriteLine($"{Array.IndexOf(nums, nums.Max()) + 1}");