//https://www.acmicpc.net/problem/14681
int x = int.Parse(Console.ReadLine());
int y = int.Parse(Console.ReadLine());
if (x > 0)
{
    Console.WriteLine((y > 0) ? "1" : "4");
}
else
{
    Console.WriteLine((y > 0) ? "2" : "3");
}