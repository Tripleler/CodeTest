//https://www.acmicpc.net/problem/3052

List<int> nums = new List<int>();
for (int i = 0; i < 10; i++)
{
    nums.Add(int.Parse(Console.ReadLine()) % 42);
}
Console.WriteLine(nums.Distinct().Count());

//bool[] nums = new bool[42];
//int cnt = 0;
//for (int i = 0; i < 10; i++)
//{
//    int n = int.Parse(Console.ReadLine()) % 42;
//    if (nums[n] == false)
//    {
//        nums[n] = true; cnt++;
//    }
//}
//Console.WriteLine(cnt);