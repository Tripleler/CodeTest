//https://www.acmicpc.net/problem/1546

int n = int.Parse(Console.ReadLine());
float[] score = Array.ConvertAll(Console.ReadLine().Split(), float.Parse);
float max = score.Max();
for (int i = 0;i<n; i++)
{
    score[i] = score[i]/max*100;
}
Console.WriteLine(score.Average());