//https://www.acmicpc.net/problem/10811

int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] box = Enumerable.Range(1, nums[0]).ToArray();
for (int i = 0; i < nums[1]; i++)
{
    int[] id = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    var reverse = box[(id[0] - 1)..id[1]].Reverse().ToArray();

    for (int j = id[0] - 1, k = 0; j < id[1]; j++, k++)
    {
        box[j] = reverse[k];
    }
}
Console.WriteLine(string.Join(" ", box));