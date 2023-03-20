//https://www.acmicpc.net/problem/9020

using System.Text;

StringBuilder sb = new StringBuilder();
bool[] p = new bool[10001];
p[0] = true;
p[1] = true;
for (int i = 2; i < 10001; i++)
{
    if (p[i] == false)
    {
        for (int j = i; j * i < 10001; j++)
        {
            p[j * i] = true;
        }
    }
}

int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    int m = int.Parse(Console.ReadLine());
    for (int j = m / 2; j > 1; j--)
    {
        if (p[j] == false && p[m - j] == false)
        {
            sb.AppendLine($"{j} {m - j}");
            break;
        }
    }
}
Console.WriteLine(sb);

// 소수작업 더 빠른거 같은데 실제 차이는 없음

//using System.Text;

//StringBuilder sb = new StringBuilder();
//bool[] p = new bool[10001];
//p[0] = true;
//p[1] = true;
//for (int i = 4; i < 10001; i += 2) p[i] = true;
//for (int i = 3; i < 5000; i += 2)
//{
//    if (p[i] == false)
//    {
//        for (int j = i * 2; j < 10001; j += i)
//        {
//            p[j] = true;
//        }
//    }
//}

//int n = int.Parse(Console.ReadLine());
//for (int i = 0; i < n; i++)
//{
//    int m = int.Parse(Console.ReadLine());
//    for (int j = m / 2; j > 1; j--)
//    {
//        if (p[j] == false && p[m - j] == false)
//        {
//            sb.AppendLine($"{j} {m - j}");
//            break;
//        }
//    }
//}
//Console.Write(sb);