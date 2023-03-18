//https://www.acmicpc.net/problem/3003

int[] chess = new int[6] { 1, 1, 2, 2, 2, 8 };
int[] peice = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
for (int i = 0; i < 6; i++)
{
    Console.Write($"{chess[i] - peice[i]} ");
}