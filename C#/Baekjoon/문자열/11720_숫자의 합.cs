//https://www.acmicpc.net/problem/11720

int n = int.Parse(Console.ReadLine());
string s = Console.ReadLine();
int cnt = 0;
foreach (char c in s)
{
    cnt += int.Parse(c.ToString());
}
Console.WriteLine(cnt);

// 아스키코드 숫자0이 48이므로 48을 빼서 합을 구함
//Console.ReadLine();
//Console.WriteLine(Console.ReadLine().Sum(x => x - 48));