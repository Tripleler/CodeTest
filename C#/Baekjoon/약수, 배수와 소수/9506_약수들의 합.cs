//https://www.acmicpc.net/problem/9506

int n;
while ((n = int.Parse(Console.ReadLine())) != -1)
{
    List<int> f = new List<int>();
    f.Add(1);
    int s = (int)Math.Sqrt(n);
    for (int i = 2; i <= s; i++)
    {
        if (n % i == 0)
        {
            f.Add(i);
            f.Add(n / i);
        }
    }
    f.Sort();
    Console.WriteLine(f.Sum() == n ? $"{n} = {string.Join(" + ", f)}" : $"{n} is NOT perfect.");
}