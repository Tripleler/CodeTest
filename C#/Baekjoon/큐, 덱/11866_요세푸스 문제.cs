//https://www.acmicpc.net/problem/11866

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse), m = new int[n[0]];
int i = 0;
var q = new Queue<int>();
while (i++ < n[0]) q.Enqueue(i);
while (i-- > 1)
{
    for (int j = 1; j < n[1]; j++)
    {
        q.Enqueue(q.Dequeue());
    }
    m[n[0] - i] = q.Dequeue();
}
Console.Write($"<{string.Join(", ", m)}>");