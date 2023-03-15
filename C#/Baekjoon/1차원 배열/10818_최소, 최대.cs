//https://www.acmicpc.net/problem/10818
Console.ReadLine();
int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
Console.WriteLine($"{nums.Min()} {nums.Max()}");