//https://www.acmicpc.net/problem/14215

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
Array.Sort(n);
Console.Write(n[0] + n[1] > n[2] ? n.Sum() : 2 * (n[0] + n[1]) - 1);