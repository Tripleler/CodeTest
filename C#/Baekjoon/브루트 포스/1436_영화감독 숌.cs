//https://www.acmicpc.net/problem/1436

int i = 665, n = int.Parse(Console.ReadLine());
while (n > 0)
{
    i++;
    if (i.ToString().Contains("666")) n -= 1;
}
Console.Write(i);