//https://www.acmicpc.net/problem/5086

while (true)
{
    int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    if (n[0] == 0) break;
    if (n[0] % n[1] == 0) Console.WriteLine("multiple");
    else if (n[1] % n[0] == 0) Console.WriteLine("factor");
    else Console.WriteLine("neither");
}