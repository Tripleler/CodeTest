//https://www.acmicpc.net/problem/10988

string s = Console.ReadLine();
if (s.Length % 2 == 0)
{
    Console.WriteLine(s[..(s.Length / 2)] == new string(s[(s.Length / 2)..].Reverse().ToArray()) ? "1" : "0");
}
else
{
    Console.WriteLine(s[..(s.Length / 2)] == new string(s[(s.Length / 2 + 1)..].Reverse().ToArray()) ? "1" : "0");
}

//char[] c = Console.ReadLine().ToCharArray();
//for (int i = 0; i < c.Length / 2; i++)
//{
//    if (c[i] != c[c.Length - i - 1])
//    {
//        Console.Write(0);
//        return;
//    }
//}
//Console.Write(1);