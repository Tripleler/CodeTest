//https://www.acmicpc.net/problem/2525
string[] time = Console.ReadLine().Split();
int t = int.Parse(Console.ReadLine());
int minute = (int.Parse(time[1]) + t) % 60;
int hour = (int.Parse(time[0]) + (int.Parse(time[1]) + t) / 60) % 24;
Console.WriteLine($"{hour} {minute}");