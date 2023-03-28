//https://www.acmicpc.net/problem/1269

Console.ReadLine();
var A = new HashSet<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
var B = new HashSet<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
Console.WriteLine(A.Union(B).Except(A.Intersect(B)).Count());

//Console.ReadLine();
//var A = new HashSet<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
//var B = new HashSet<int>(Array.ConvertAll(Console.ReadLine().Split(), int.Parse));
//Console.WriteLine(A.Count() + B.Count() - A.Intersect(B).Count() * 2);