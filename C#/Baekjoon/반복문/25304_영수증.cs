//https://www.acmicpc.net/problem/25304
int cash = int.Parse(Console.ReadLine());
for (int i = int.Parse(Console.ReadLine()); i > 0; i--)
{
    int[] value = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    cash -= value[0] * value[1];
}
Console.WriteLine(cash == 0 ? "Yes" : "No");