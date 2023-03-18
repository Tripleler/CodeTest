//https://www.acmicpc.net/problem/10812

string[] s = Console.ReadLine().Split();
int[] box = Enumerable.Range(1, int.Parse(s[0])).ToArray();
for (int i = 0; i < int.Parse(s[1]); i++)
{
    int[] id = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    int start = id[0];
    int end = id[1];
    int mid = id[2];
    int[] temp = box[(start - 1)..end];
    for (int j = 0; j < end - start + 1; j++)
    {
        int k = (mid - start + j) % (end - start + 1);
        box[j + start - 1] = temp[k];
    }
}
Console.WriteLine(string.Join(" ", box));