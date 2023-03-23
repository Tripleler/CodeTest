//https://www.acmicpc.net/problem/2839

int cnt = 0, n = int.Parse(Console.ReadLine());
if (n == 4 || n == 7) Console.Write(-1);
else
{
    while (true)
    {
        if (n % 3 == 0)
        {
            int k = n / 3;
            if (k > 4) k -= k / 5 * 2;
            cnt += k;
            break;
        }
        n -= 5;
        if (n < 0) break;
        cnt++;
    }
    Console.Write(cnt);
}

//int n = int.Parse(Console.ReadLine()), f = n / 5 + 1;
//while (f-- > 0)
//{
//    if ((n - f * 5) % 3 == 0)
//    {
//        Console.Write(f + (n - f * 5) / 3);
//        return;
//    }
//}
//Console.Write(-1);