/*
Jordan Smith
02/21/22
Extension.java
Section C
Project 2
CS 231
*/

public class Extension
{
    //creates a matrix multiplier
    int rows1;
    int cols1;
    int matrix1[][];
    int rows2;
    int cols2;
    int matrix2[][];
    int finalMatrix[][];

    //constructor for the matrix multiplier
    public Extension(int numRows1, int numCols1, int numRows2, int numCols2)
    {
        rows1 = numRows1;
        cols1 = numCols1;
        rows2 = numRows2;
        cols2 = numCols2;
        matrix1 = new int[rows1][cols1];
        matrix2 = new int[rows2][cols2];

        for(int i=0; i<rows1; i++)
        {
            for(int j=0; j<cols1; j++)
            {
                matrix1[i][j] = (int)(Math.random() * 10);
            }
        }
        for(int i=0; i<rows2; i++)
        {
            for(int j=0; j<cols2; j++)
            {
                matrix2[i][j] = (int)(Math.random() * 10);
            }
        }
    }

    //returns the number of rows in the first matrix
    public int getRows1()
    {
        return rows1;
    }

    //returns the number of rows in the second matrix
    public int getRows2()
    {
        return rows2;
    }

    //returns the number of columns in the first matrix
    public int getCols1()
    {
        return cols1;
    }

    //returns the number of columns in the second matrix
    public int getCols2()
    {
        return cols2;
    }

    //multiplies across two matrices once and returns their product
    public int multiplyMatrices(int row, int col)
    {
        int product = 0;
        for(int i=0; i<getCols1(); i++)
        {
            product += matrix1[col][i] * matrix2[i][row];
        }
        return product;
    }

    //returns the matrix that results form multiplying the intial ones together
    public int[][] multiply()
    {
        int newDimensions = 0;
        if(getCols2() != getRows1())
        {
            System.out.println("You cannot multiply these matrices!");
        }
        else
        {
            if(getRows1() < getCols1())
            {
                newDimensions = getRows1();
            }
            else
            {
                newDimensions = getCols1();
            }

            finalMatrix = new int[newDimensions][newDimensions];

            for(int i=0; i<newDimensions; i++)
            {
                for(int j=0; j<newDimensions; j++)
                {
                    finalMatrix[i][j] = multiplyMatrices(i,j);
                }
            }
        }
        return finalMatrix;
    }

    //prints out the matrices into the terminal in a neat manner
    public void displayMatrices()
    {
        System.out.println("Matrix 1: ");
        for(int i=0; i<getRows1(); i++)
        {
            for(int j=0; j<getCols1(); j++)
            {
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }
        
        System.out.println("Matrix 2: ");
        for(int i=0; i<getRows2(); i++)
        {
            for(int j=0; j<getCols2(); j++)
            {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println("Final Matrix: ");
        for(int i=0; i<finalMatrix.length; i++)
        {
            for(int j=0; j<finalMatrix.length; j++)
            {
                System.out.print(finalMatrix[j][i] + " ");
            }
            System.out.println();
        }
    }

    //tests code
    public static void main(String[] args)
    {
        Extension extension = new Extension(2,3,3,2);
        extension.multiply();
        extension.displayMatrices();
    }
}