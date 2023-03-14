//https://www.acmicpc.net/problem/10950
for (int i = int.Parse(Console.ReadLine()); i > 0; i--)
{
    Console.WriteLine(Array.ConvertAll(Console.ReadLine().Split(), int.Parse).Sum());
}