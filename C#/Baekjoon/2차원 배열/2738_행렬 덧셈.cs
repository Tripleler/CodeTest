//https://www.acmicpc.net/problem/2738

using System.Text;

int[] size = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[,,] matrix = new int[2, size[0], size[1]];
StringBuilder sb = new StringBuilder();
for (int m = 0; m < 2; m++)
{
    for (int i = 0; i < size[0]; i++)
    {
        int[] row = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
        for (int j = 0; j < size[1]; j++)
        {
            matrix[m, i, j] = row[j];
        }
    }
}
for (int i = 0; i < size[0]; i++)
{
    for (int j = 0; j < size[1]; j++)
    {
        sb.Append($"{matrix[0, i, j] + matrix[1, i, j]} ");
    }
    sb.Append('\n');
}
Console.Write(sb);