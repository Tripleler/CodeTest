//https://www.acmicpc.net/problem/1966

int n = int.Parse(Console.ReadLine());
while(n-- > 0)
{
    int[] m = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    var q = new Queue<int>(a);
    var p = new Queue<int>();
    for (int i = 0; i < m[0]; i++) p.Enqueue(i);
    Array.Sort(a);
    Array.Reverse(a);  // a는 최댓값 배열
    int j = 0, k = 1;  // j는 인덱스 k 는 출력순서
    while (true)
    {
        if (q.Peek() == a[j])  //
        {
            if (p.Peek() == m[1])
            {
                Console.WriteLine(k);
                break;
            }
            else
            {
                q.Dequeue();
                p.Dequeue();
                k++;
                j++;
            }
        }
        else
        {
            q.Enqueue(q.Dequeue());
            p.Enqueue(p.Dequeue());
        }
    }
}