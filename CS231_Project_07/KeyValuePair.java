/*
Jordan Smith
04/11/22
KeyValuePair.java
CS231
Section C
Project 7
*/

public class KeyValuePair<Key,Value>
{
    //Creates a key-value pair
    private Key key;
    private Value value;

    public KeyValuePair(Key k, Value v)
    {
        //constructor for key-value pair
        key = k;
        value = v;
    }

    public Key getKey()
    {
        //returns key
        return key;
    }

    public Value getValue()
    {
        //returns value
        return value;
    }

    public void setValue(Value v)
    {
        //sets value
        value = v;
    }

    public String toString()
    {
        //toString method for KeyValuePair
        return "The key is " + key + ", and the value is " + value + ".";
    }

    public static void main(String[] args)
    {
        //Test Code
        KeyValuePair<String,Integer> keyValuePair = new KeyValuePair<String,Integer>("Key1",10);
        System.out.println("This should be Key1: " + keyValuePair.getKey());
        System.out.println("This should be 10: " + keyValuePair.getValue());
        keyValuePair.setValue(20);
        System.out.println("This should be 20: " + keyValuePair.getValue());
        System.out.println(keyValuePair.toString());
    }
}