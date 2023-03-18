//https://www.acmicpc.net/problem/25206

Dictionary<string, float> score = new Dictionary<string, float>()
{
    {"A+", 4.5f },
    {"A0", 4.0f },
    {"B+", 3.5f },
    {"B0", 3.0f },
    {"C+", 2.5f },
    {"C0", 2.0f },
    {"D+", 1.5f },
    {"D0", 1.0f },
    {"F", 0.0f }
};
float sum = 0;
float cnt = 0;
for (int i = 0; i < 20; i++)
{
    string[] s = Console.ReadLine().Split();
    if (s[2] != "P")
    {
        sum += float.Parse(s[1]) * score[s[2]];
        cnt += float.Parse(s[1]);
    }
}
Console.WriteLine(sum / cnt);