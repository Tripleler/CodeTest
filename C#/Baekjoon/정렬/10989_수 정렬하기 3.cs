//https://www.acmicpc.net/problem/10989

StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int n = int.Parse(sr.ReadLine());
int[] a = new int[10001];
for (int i = 0; i < n; i++)
{
    a[int.Parse(sr.ReadLine())] += 1;
}
for (int i = 0; i < 10001; i++)
{
    for (int j = a[i]; j > 0; j--)
    {
        sw.WriteLine(i);
    }
}
sw.Close();
sr.Close();