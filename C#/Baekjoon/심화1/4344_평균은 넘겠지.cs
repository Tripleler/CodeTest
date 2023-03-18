//https://www.acmicpc.net/problem/4344

int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    float[] score = Array.ConvertAll(Console.ReadLine().Split(), float.Parse).Skip(1).ToArray();
    float mean = score.Sum() / score.Length;
    Console.WriteLine("{0:F3}%", (float)score.Count(x => x > mean) / score.Length * 100);
}