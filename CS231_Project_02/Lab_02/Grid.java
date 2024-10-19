package Lab_02;

public class Grid
{
    public static void main(String[] args)
    {
        int yogi;
        int booboo;
        char[][] ranger;

        if(args.length == 0)
        {
            System.out.println("usage: $ java Grid 42 96 81 hut hut.");
            System.out.println("The program prints out 42, 96, etc. based on their order. The arguments are elements in an array.");
            return;
        }
        else
        {
            for(int i=0; i<args.length; i++)
            {
                System.out.println("Element " + i + ": " + args[i]);
            }
        }
        yogi = Integer.parseInt(args[0]);
        booboo = Integer.parseInt(args[1]);
        System.out.println(yogi);
        System.out.println(booboo);
        System.out.println(yogi + booboo);

        ranger = new char[yogi][booboo];
        for(int i=0; i<yogi; i++)
        {
            for(int j=0; j<booboo; j++)
            {
                ranger[i][j] = (char)(Math.random() * 255);
            }
        }
        for(int i=0; i<yogi; i++)
        {
            for(int j=0; j<booboo; j++)
            {
                System.out.println("The element at row " + (i+1) + " and column " + (j+1) + " is " +
                ranger[i][j] + ".");
            }
        }
    }
}