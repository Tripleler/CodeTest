//https://www.acmicpc.net/problem/10101

int[] n = new int[3];
for (int i = 0; i < 3; i++) n[i] = int.Parse(Console.ReadLine());
Array.Sort(n);
if (n.Sum() != 180) Console.Write("Error");
else if (n[0] == 60 && n[1] == 60) Console.Write("Equilateral");
else if (n[0] == n[1] || n[1] == n[2]) Console.Write("Isosceles");
else Console.Write("Scalene");