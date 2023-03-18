//https://www.acmicpc.net/problem/2444

int n = int.Parse(Console.ReadLine());
int i = 1;
for (; i < n; i++)
{
    Console.WriteLine($"{new string(' ', n - i)}{new string('*', 2 * i - 1)}");
}
for (; i > 0; i--)
{
    Console.WriteLine($"{new string(' ', n - i)}{new string('*', 2 * i - 1)}");
}