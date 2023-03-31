//https://www.acmicpc.net/problem/2164

int i = 0, n = int.Parse(Console.ReadLine());
var q = new Queue<int>();
while (i++ < n) q.Enqueue(i);
while (i-- > 2)
{
    q.Dequeue();
    q.Enqueue(q.Dequeue());
}
Console.Write(q.Dequeue());