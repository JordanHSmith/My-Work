package Lab_08;

public class KeyValuePair<Key,Value>
{
    Key key;
    Value value;

    public KeyValuePair(Key k, Value v)
    {
        key = k;
        value = v;
    }

    public Key getKey()
    {
        return key;
    }

    public Value getValue()
    {
        return value;
    }

    public void setValue(Value v)
    {
        value = v;
    }

    public String toString()
    {
        return "The key is " + key + ", and the value is " + value + ".";
    }

    public static void main(String[] args)
    {
        KeyValuePair<String,Integer> keyValuePair = new KeyValuePair<String,Integer>("Key1",10);
        System.out.println("This should be Key1: " + keyValuePair.getKey());
        System.out.println("This should be 10: " + keyValuePair.getValue());
        keyValuePair.setValue(20);
        System.out.println("This should be 20: " + keyValuePair.getValue());
        System.out.println(keyValuePair.toString());
    }
}
