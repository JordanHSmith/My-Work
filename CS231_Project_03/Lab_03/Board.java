/*
Jordan Smith
03/11/22
Board.java
CS231 B
Project 03/04
*/

package Lab_03;
import java.io.*;

public class Board
{
    public boolean read(String filename) {
        try
        {
        // assign to a variable of type FileReader a new FileReader object, passing filename to the constructor
            FileReader fileReader = new FileReader(filename);
          // assign to a variable of type BufferedReader a new BufferedReader, passing the FileReader variable to the constructor
            BufferedReader bufferedReader = new BufferedReader(fileReader);
          // assign to a variable of type String line the result of calling the readLine method of your BufferedReader object.
            String line = bufferedReader.readLine();
          // start a while loop that loops while line isn't null
          while(line != null)
          {
              // assign to an array of type String the result of calling split on the line with the argument "[ ]+"
              String[] str = new String[10];
              str = line.split("[ ]+");
              // print the String (line)
              System.out.println(line);
              // print the size of the String array (you can use .length)
              System.out.println(str.length);
              // assign to line the result of calling the readLine method of your BufferedReader object.
              line = bufferedReader.readLine();
          }
          // call the close method of the BufferedReader
          bufferedReader.close();
          // return true
          return true;
        }
        catch(FileNotFoundException ex) {
          System.out.println("Board.read():: unable to open file " + filename );
        }
        catch(IOException ex) {
          System.out.println("Board.read():: error reading file " + filename);
        }
    
        return false;
      }

    public static void main(String[] args)
    {
        Board board1 = new Board();
        board1.read(args[0]);
    }
}
