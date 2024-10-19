/*
Jordan Smith
04/12/22
KeyValuePair.java
CS231
Section C
Project 8
*/

public class KeyValuePair<Key,Value>
{
    //Creates a key-value pair
    Key key;
    Value value;

    public KeyValuePair(Key k, Value v)
    {
        //Constructor for key-value pair
        key = k;
        value = v;
    }

    public Key getKey()
    {
        //Returns key
        return key;
    }

    public Value getValue()
    {
        //Returns value
        return value;
    }

    public void setValue(Value v)
    {
        //Sets value
        value = v;
    }

    public String toString()
    {
        //toString method for KeyValuePair
        return "The key is " + key + ", and the value is " + value + ".";
    }

    public static void main(String[] args)
    {
        //Test code
        KeyValuePair<String,Integer> keyValuePair = new KeyValuePair<String,Integer>("Key1",10);
        System.out.println("This should be Key1: " + keyValuePair.getKey());
        System.out.println("This should be 10: " + keyValuePair.getValue());
        keyValuePair.setValue(20);
        System.out.println("This should be 20: " + keyValuePair.getValue());
        System.out.println(keyValuePair.toString());
    }
}
