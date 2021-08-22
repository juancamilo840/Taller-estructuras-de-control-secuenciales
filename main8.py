int P, Q;
    Console.WriteLine("Escribir si los datos P y Q satisfacen la expresion P^3 +Q^4 −2P^2 <680");
    P = int.Parse(Console.ReadLine());
    Console.WriteLine("El valor de P es:" + P);
    Q = int.Parse(Console.ReadLine());
    Console.WriteLine("El valor de Q es:" + Q);

    if ((P ^ 3 + Q ^ 4) - (2 * P ^ 2) < 680)
    {
        Console.WriteLine(" Los valores P y Q satisfacen la expresion dada");
    }
    else
    {
        Console.WriteLine("No cumplen con los valores ");
    }
    Console.WriteLine();
    Console.ReadKey();