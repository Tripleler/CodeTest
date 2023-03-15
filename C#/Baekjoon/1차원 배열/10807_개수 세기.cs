//https://www.acmicpc.net/problem/10807

Console.ReadLine();
int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int n = int.Parse(Console.ReadLine());
int cnt = 0;
foreach(int i in nums)
{
    if (n == i) cnt++;
}
Console.WriteLine(cnt);