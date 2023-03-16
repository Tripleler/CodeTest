//https://www.acmicpc.net/problem/10813

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] nums = Enumerable.Range(1, n[0]).ToArray();
int temp;
for (int i = 0; i < n[1]; i++)
{
    int[] id = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    temp = nums[id[0] - 1];
    nums[id[0] - 1] = nums[id[1] - 1];
    nums[id[1] - 1] = temp;
}
Console.WriteLine(string.Join(" ", nums));