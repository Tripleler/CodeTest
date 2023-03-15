//https://www.acmicpc.net/problem/10810

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] box = new int[n[0]];
for (int i = 0;i < n[1]; i++)
{
    int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    for (int j = nums[0] - 1; j < nums[1]; j++)
    {
        box[j] = nums[2];
    }
}
Console.WriteLine(string.Join(" ", box));