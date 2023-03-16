//https://www.acmicpc.net/problem/5597

bool[] nums = new bool[30];
for (int i = 0; i < 30; i++)
{
    nums[i] = true;
}
for (int i = 0; i < 28; i++)
{
    nums[int.Parse(Console.ReadLine()) - 1] = false;
}
Console.WriteLine(Array.IndexOf(nums, true) + 1);
Console.WriteLine(Array.LastIndexOf(nums, true) + 1);