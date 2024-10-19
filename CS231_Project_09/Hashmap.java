/*
Jordan Smith
04/25/22
Hashmap.java
CS231
Section C
Project 9
*/

import java.util.Comparator;
import java.util.ArrayList;

public class Hashmap<K,V> implements MapSet<K,V>
{
    //Makes a hashmap that holds KeyValuePairs
    private HashNode<K,V>[] bucketArray;
    private int capacity;
    private double loadFactor;
    private double size;
    private int numCollisions;
    private ArrayList<K> keySet;
    private ArrayList<V> values;

    public Hashmap(AscendingString ascendingString)
    {
        //Constructor for Hashmap that provides comparator
        bucketArray = new HashNode[16];
        capacity = 16;
        loadFactor = .75;
        size = 0.0;
        numCollisions = 0;
        keySet = new ArrayList<K>();
        values = new ArrayList<V>();
    }

    public Hashmap(Comparator<K> incomp, int capacity)
    {
        //Constructor for Hashmap that provides comparator and allows intitial capacity to be specified
        bucketArray = new HashNode[capacity];
        this.capacity = capacity;
        loadFactor = .75;
        size = 0.0;
        numCollisions = 0;
        keySet = new ArrayList<K>();
        values = new ArrayList<V>();
    }

    public V put(K key, V value) 
    {
        //Inserts a KeyValuePair with key and value
        //Checks if array must be expanded
        if (size == loadFactor * capacity) 
        {
            //Resets informaton and creates new array twice as big
            keySet = new ArrayList<K>();
            values = new ArrayList<V>();
            HashNode<K,V>[] oldBucketArray = (Hashmap.HashNode<K,V>[]) bucketArray;
            capacity *= 2;
            size = 0;
            numCollisions = 0;
            bucketArray = new HashNode[capacity];

            //Adds elements of old array to new array
            for (HashNode<K,V> hashNode: oldBucketArray)
            {
                while (hashNode != null)
                {
                    put(hashNode.getKey(), hashNode.getValue());
                    hashNode = hashNode.next;
                }
            }
        }

        HashNode<K,V> hashNode = new HashNode<>(key, value, null);
        int bucketIndex = getHash(key);

        HashNode<K,V> currentNode = bucketArray[bucketIndex];

        //If nothing at hashcode location, insert node there
        if (currentNode == null)
        {
            bucketArray[bucketIndex] = hashNode;
            size++;
            keySet.add(hashNode.getKey());
            values.add(hashNode.getValue());
        }
        else
        {
            numCollisions++;
            //Iterates through items in the array until it finds an open spot for insertion
            while (currentNode.getNext() != null)
            {
                if (currentNode.key.equals(key))
                {
                    values.remove(currentNode.value);
                    V tempVal = currentNode.value;
                    currentNode.value = value;
                    values.add(value);
                    return tempVal;
                }
                currentNode = currentNode.getNext();
            }
            if (currentNode.key.equals(key))
            {
                values.remove(currentNode.value);
                currentNode.value = value;
                values.add(value);
            }
            else
            {
                currentNode.next = hashNode;
                size++;
                keySet.add(key);
                values.add(value);
            }
        }
        return null;
    }

    public boolean containsKey(K key)
    {
        //Returns true if key is in the hashmap and false otherwise
        if(bucketArray[getHash(key)] != null)
        {
            HashNode<K,V> currentNode = bucketArray[getHash(key)];
            while(currentNode != null)
            {
                if(currentNode.getKey() == key)
                {
                    return true;
                }
                currentNode = currentNode.getNext();
            }
        }
        return false;
    }

    public V get(K key)
    {
        //Returns the value associated with the key
        int bucketIndex = getHash(key);
        HashNode<K, V> bucket = bucketArray[bucketIndex];

        while(bucket != null)
        {
            if(key == bucket.getKey())
            {
                return bucket.getValue();
            }
            bucket = bucket.getNext();
        }
        return null;
    }

    public int size()
    {
        //Returns number of elemenets in the hashmap
        return (int)size;
    }

    public ArrayList<K> keySet()
    {
        //Returns an ArrayList of all the keys in the map
        return keySet;
    }

    public ArrayList<V> values()
    {
        //Returns an ArrayList of all the values in the map
        return values;
    }

    public ArrayList<KeyValuePair<K,V>> entrySet()
    {
        //Returns an ArrayList of all the KeyValuePairs in the map
        ArrayList<KeyValuePair<K,V>> entrySet = new ArrayList<KeyValuePair<K,V>>();
        for(int i=0; i<keySet.size(); i++)
        {
            KeyValuePair<K,V> keyValuePair = new KeyValuePair(keySet.get(i),values.get(i));
            entrySet.add(keyValuePair);
        }
        return entrySet;
    }

    private int getBucketSize()
    {
        //Returns the length of the array
        return bucketArray.length;
    }

    private int getHash(K key)
    {
        //Gets a hashcode for a given key
        return Math.abs(myHashCode(key)) % getBucketSize();
    }

    public void clear()
    {
        //Resets data for the hashmap
        bucketArray = new HashNode[16];
        capacity = 16;
        loadFactor = .75;
        size = 0.0;
        keySet = new ArrayList<K>();
        values = new ArrayList<V>();
    }

    public int getDepth()
    {
        //Returns the number of collisions that occurred during insertion
        return numCollisions;
    }

    public int myHashCode(K key)
    {
        //Custom hashcode function
        int hash = 13;
        hash = 17 * hash + key.hashCode();
        hash += 23;
        return hash;
    }

    static class HashNode<K, V>
    {
        //Makes a node for the hashmap
        K key;
        V value;
        HashNode<K, V> next;

        public HashNode(K key, V value, HashNode<K,V> next)
        {
            //Constructor for HashNode
            this.key = key;
            this.value = value;
            this.next = next;
        }

        public HashNode<K,V> getNext()
        {
            //Returns next node
            return next;
        }

        public K getKey()
        {
            //Returns the key
            return key;
        }

        public V getValue()
        {
            //Returns the value
            return value;
        }

        public String toString()
        {
            //Returns a string saying what the key and value of the node
            return "The key is" + key + ", and the value is" + value + ".";
        }
    }


    public static void main(String[] args)
    {
        //Test code
        Hashmap<String, Integer> hashMap = new Hashmap<String, Integer>(new AscendingString());

        hashMap.put("Jordan",1643);
        hashMap.put("Smith", 12);
        hashMap.put("Bible",1643);
        hashMap.put("Hub",23);
        hashMap.put("Siuuu",234);
        hashMap.put("No siuuu",2345);
        hashMap.put("asdfasdf",1643);
        hashMap.put("kswndo",1643);
        hashMap.put("pwip",123);
        hashMap.put("xcvzxcv",1643);
        hashMap.put("xcvzxcv",1843);
        hashMap.put("qwer",1643);
        hashMap.put("fghj",1643);
        hashMap.put("heaven",1643);
        hashMap.put("asdfasdfasdfsadfasdfsadf",1643);
        hashMap.put("asdfasdfasdf",1643);
        hashMap.put("sdfasdfasdfasdfasdfsdf", 12);
        hashMap.put("ddddddd",1643);
        hashMap.put("fffffffffff",23);
        hashMap.put("gggggggggggggggggg",234);
        hashMap.put("asdfasdfo siuuu",2345);
        hashMap.put("assdfdfasdf",1643);
        hashMap.put("dfaddddd2ddddsdf",1643);
        hashMap.put("asdsssss2sssssssf",123);
        hashMap.put("xcffffff2fffffvzxcv",1643);
        hashMap.put("qwggggg2gggggger",1643);
        hashMap.put("feeeeeee2eeeeghj",1643);
        hashMap.put("qw3242er",1643);
        hashMap.put("jotous",1643);
        hashMap.put("asdfasdd2fasdfasdffasdfsadfasdfsadf",1643);
        hashMap.put("asdfasd2f",1643);
        hashMap.put("Smasdfas2dfith", 12);
        hashMap.put("Poasdfas2dfasdfasdfrn",1643);
        hashMap.put("Huasdfasd2fasdfb",23);
        hashMap.put("Siasdfasd2fasdfasduuu",234);
        hashMap.put("No sfasdfa2sdfasiuuu",2345);
        hashMap.put("asdfdfas2dfasdfasdf",1643);
        hashMap.put("dfaasdf2asdfsdf",1643);
        hashMap.put("asasdfa2sddf",123);
        hashMap.put("xcfasdfv2z2xcv",1643);
        hashMap.put("qwasdfas2der",1643);
        hashMap.put("fgasdfasdfh2j",1643);
        hashMap.put("qwasdfas2d2faer",1643);
        hashMap.put("fucfasdf2asdfasdfking hell",1643);
        hashMap.put("asdfasd2fasdfsdfasdfsadfasdfsadf",1643);
        hashMap.put("fas2df",1643);
        hashMap.put("sdfaasdfasdfa2sdfasdfasdfasdfsdfasdfasdfasdfsdf", 12);
        hashMap.put("ddddasdfas22dfasdfddd",1643);
        hashMap.put("fffffffff2ffffffffffffffffffffffffff",23);
        hashMap.put("ggggggggg2gggggggggggggggggggggg",234);
        hashMap.put("asdfasasd2ddddddasdfasdfdfo siuuu",2345);
        hashMap.put("assdfdfa2sdfasdf asdf",1643);
        hashMap.put("dfadddda2svcxcvdddddsdf",1643);
        hashMap.put("asdsssss2s ssssssf",123);
        hashMap.put("xcffffff2ff fffvzxcv",1643);
        hashMap.put("qwgggg2gggg ggger",1643);
        hashMap.put("feeeee2eee eeeghj",1643);
        hashMap.put("qw32 24er",1643);
        hashMap.put("dcjddbchbfhvbdhsjxa",1643);
        hashMap.put("asdf2asddfa sdfasdffasdfsadfasdfsadf",9876);
        hashMap.put("jigfkf",7466);
    
        System.out.println("Should be 60. Size: " + hashMap.size());
        System.out.println("Should be 9876. Value: " + hashMap.get("asdf2asddfa sdfasdffasdfsadfasdfsadf"));
        hashMap.put("asdf2asddfa sdfasdffasdfsadfasdfsadf",6789);
        System.out.println("Should be 6789. Value: " + hashMap.get("asdf2asddfa sdfasdffasdfsadfasdfsadf"));
        System.out.println("Should be true. Contains key asdf2asddfa sdfasdffasdfsadfasdfsadf: " + hashMap.containsKey("asdf2asddfa sdfasdffasdfsadfasdfsadf"));
        System.out.println("Should be false. Contains key asdf2asddfa: " + hashMap.containsKey("asdf2asddfa"));
        System.out.println("Should be true. Contains key gggggggggggggggggg: " + hashMap.containsKey("gggggggggggggggggg"));

        System.out.println("Should be true. Contains key xcvzxcv: " + hashMap.containsKey("xcvzxcv"));
        ArrayList<String> keyTest = hashMap.keySet();
        System.out.println("Should be 60. keySet Size: " + keyTest.size());
        for(String key: keyTest)
        {
            System.out.println("Key: " + key);
        }

        ArrayList<Integer> valuesTest = hashMap.values();
        System.out.println("Should be 60. values Size: " + valuesTest.size());
        for(Integer value: valuesTest)
        {
            System.out.println("Value: " + value);
        }

        ArrayList<KeyValuePair<String,Integer>> entryTest = hashMap.entrySet();
        System.out.println("Should be 60. entryTest Size: " + entryTest.size());
        for(KeyValuePair<String,Integer> entry: entryTest)
        {
            System.out.println("Key: " + entry.getKey());
            System.out.println("Value: " + entry.getValue());
        }
        System.out.println("Num Collisions: " + hashMap.getDepth());
    }
}