//https://www.acmicpc.net/problem/3009

int[] x = new int[3];
int[] y = new int[3];
for (int i = 0; i < 3; i++)
{
    string[] n = Console.ReadLine().Split();
    x[i] = int.Parse(n[0]);
    y[i] = int.Parse(n[1]);
}
Console.Write($"{(x[0] == x[1] ? x[2] : x[0] == x[2] ? x[1] : x[0])} {(y[0] == y[1] ? y[2] : y[0] == y[2] ? y[1] : y[0])}");

//int x = 0, y = 0;
//for (var i = 0; i < 3; i++)
//{
//    int[] n = Console.ReadLine().Split().Select(int.Parse).ToArray();
//    x ^= n[0];
//    y ^= n[1];
//}

//Console.Write(x + " " + y);