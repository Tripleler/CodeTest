//https://www.acmicpc.net/problem/1427

char[] s = Console.ReadLine().ToCharArray();
Array.Sort(s);
Console.WriteLine(string.Join("", s.Reverse()));

//Console.Write(Console.ReadLine().OrderByDescending(e => e).ToArray());