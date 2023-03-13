//https://www.acmicpc.net/problem/2884
string[] s = Console.ReadLine().Split();
int hour = int.Parse(s[0]);
int minute = int.Parse(s[1]);
if (minute >= 45)
{
    Console.WriteLine($"{hour} {minute - 45}");
}
else if (hour >= 1)
{
    Console.WriteLine($"{hour - 1} {minute + 15}");
}
else
{
    Console.WriteLine($"23 {minute + 15}");
}