//https://www.acmicpc.net/problem/2231

int x = 0, n = int.Parse(Console.ReadLine());
for (int i = 1; i < n; i++)
{
    int m = i + i.ToString().ToCharArray().Sum(x => x - 48);
    if (m == n)
    {
        x = i;
        break;
    }
}
Console.Write(x);

//int f(int m)
//{
//    int sum = m;
//    while (m != 0)
//    {
//        sum += m % 10;
//        m /= 10;
//    }

//    return sum;
//}

//int n = int.Parse(Console.ReadLine());
//bool flag = false;

//for (int m = n - 54; m <= n; m++)
//{
//    if (n == f(m))
//    {
//        Console.Write(m);
//        flag = true;
//        break;
//    }
//}

//if (!flag) Console.Write(0);