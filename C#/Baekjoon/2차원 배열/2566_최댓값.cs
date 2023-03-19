//https://www.acmicpc.net/problem/2566

int max = 0;
int row = 0;
int col = 0;
for (int i = 0; i < 9; i++)
{
    int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    for (int j = 0; j < 9; j++)
    {
        if (max < nums[j])
        {
            max = nums[j];
            row = i;
            col = j;
        }
    }
}
Console.WriteLine($"{max}\n{row + 1} {col + 1}");