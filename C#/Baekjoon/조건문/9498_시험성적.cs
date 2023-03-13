//https://www.acmicpc.net/problem/9498
int score = int.Parse(Console.ReadLine());
Console.WriteLine((score >= 90) ? "A" : (score >= 80) ? "B" : (score >= 70) ? "C" : (score >= 60) ? "D" : "F");