//https://www.acmicpc.net/problem/10798

using System.Text;

string[,] s = new string[5, 15];
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 5; i++)
{
    string input = Console.ReadLine();
    for (int j = 0; j < input.Length; j++)
    {
        s[i, j] = input[j].ToString();
    }
}
for (int j = 0;j < 15; j++)
{
    for (int i = 0; i < 5; i++)
    {
        sb.Append($"{s[i, j]}");
    }
}
Console.Write(sb);