//https://www.acmicpc.net/problem/25305

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] s = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
Array.Sort(s);
Console.Write(s[n[0] - n[1]]);

//int k = int.Parse(Console.ReadLine().Split()[1]);
//int[] num = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//Array.Sort(num);
//Console.Write(num[^k]);