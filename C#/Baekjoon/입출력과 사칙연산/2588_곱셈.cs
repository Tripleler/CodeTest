//https://www.acmicpc.net/problem/2588
int s1 = int.Parse(Console.ReadLine());
string s2 = Console.ReadLine();
for (int i = 0; i < 3; i++)
{
    Console.WriteLine(s1 * int.Parse(s2.Substring(2 - i, 1)));
}
Console.WriteLine(s1 * int.Parse(s2));