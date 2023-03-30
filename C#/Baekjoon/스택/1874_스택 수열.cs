//https://www.acmicpc.net/problem/1874

using System.Text;

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
var sb = new StringBuilder();
var s = new Stack<int>();
int n = int.Parse(sr.ReadLine()), m = n, input, i = 1, last;
while (n-- > 0)
{
    input = int.Parse(sr.ReadLine());
    while (i <= m + 1)
    {
        
        if (s.TryPeek(out last) && last == input)
        {
            s.Pop();
            sb.AppendLine("-");
            break;
        }
        else
        { 
            s.Push(i); 
            sb.AppendLine("+");
            i++;
        }
    }
}
Console.WriteLine(s.Count == 0 ? sb : "NO");