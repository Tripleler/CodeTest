//https://www.acmicpc.net/problem/5622

string s = Console.ReadLine();
int cnt = 0;
foreach (char c in s)
{
    if (new string("ABC").Contains(c.ToString()))
    {
        cnt += 3;
    }
    else if (new string("DEF").Contains(c.ToString()))
    {
        cnt += 4;
    }
    else if (new string("GHI").Contains(c.ToString()))
    {
        cnt += 5;
    }
    else if (new string("JKL").Contains(c.ToString()))
    {
        cnt += 6;
    }
    else if (new string("MNO").Contains(c.ToString()))
    {
        cnt += 7;
    }
    else if (new string("PQRS").Contains(c.ToString()))
    {
        cnt += 8;
    }
    else if (new string("TUV").Contains(c.ToString()))
    {
        cnt += 9;
    }
    else
    {
        cnt += 10;
    }
}
Console.WriteLine(cnt);

//string[] a = { "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" };
//string s = Console.ReadLine();
//int cnt = 0;
//foreach (char c in s)
//{
//    foreach(string s2 in a)
//    {
//        if (s2.Contains(c.ToString()))
//        {
//            cnt += Array.IndexOf(a, s2) + 3;
//        }
//    }
//}
//Console.WriteLine(cnt);