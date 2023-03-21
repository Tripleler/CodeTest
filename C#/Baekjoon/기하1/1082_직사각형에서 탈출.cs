//https://www.acmicpc.net/problem/1085

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
n[2] -= n[0];
n[3] -= n[1];
Console.Write(n.Min());