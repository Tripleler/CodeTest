//https://www.acmicpc.net/problem/19532

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
double a = n[0], b = n[1], c = n[2], d = n[3], e = n[4], f = n[5];
double x = (e * c - b * f) / (a * e - b * d);
double y = (a * f - c * d) / (a * e - b * d);
Console.Write($"{(int)x} {(int)y}");