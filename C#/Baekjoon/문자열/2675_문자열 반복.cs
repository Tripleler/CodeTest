//https://www.acmicpc.net/problem/2675

int n = int.Parse(Console.ReadLine());
for (int i = 0; i < n; i++)
{
    string[] s = Console.ReadLine().Split();
    foreach (char c in s[1])
    {
        for (int j = 0; j < int.Parse(s[0]); j++)
        {
            Console.Write(c);
        }
    }
    Console.Write("\n");
}

//int n = int.Parse(Console.ReadLine());
//for (int i = 0; i < n; i++)
//{
//    string[] s = Console.ReadLine().Split();
//    foreach (char c in s[1])
//    {
//        Console.Write(new string(c, int.Parse(s[0])));
//    }
//    Console.Write("\n");
//}