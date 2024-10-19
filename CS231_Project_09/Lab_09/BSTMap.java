package Lab_09;

/*
Jordan Smith
04/25/22
BSTMap.java
CS231
Section C
Project 9
*/

import java.util.ArrayList;
import java.util.Comparator;

public class BSTMap<K,V> implements MapSet<K,V>
{
    //Makes a binary search tree with keys of type K and values of type V
    private TNode root;
    private int size;
    private Comparator<K> comp;
    private ArrayList<K> keys;
    private ArrayList<V> values;
    private ArrayList<KeyValuePair<K,V>> keyValuePairList;

    public BSTMap(Comparator<K> comp)
    {
        //Constructor for BSTMap
        this.comp = comp;
        root = null;
        keys = new ArrayList<K>();
        values = new ArrayList<V>();
        keyValuePairList = new ArrayList<KeyValuePair<K,V>>();
        size = 0;
    }

    public V put(K key, V value)
    {
        //Inserts a node at the correct positon in the BST
        //if the tree is not empty, call the Node's put method
        if (root != null)
        {
            V val = root.get(key, comp);
			root.put(key,value,comp);
            return val;
		}
        //if the tree is empty create a new node with key and value
        else
        {
            size++;
			root = new TNode(key,value);
            return null;
		}
    }

    public boolean containsKey(K key)
    {
        //Checks if BST contains key
        TNode check = root;
        while(true)
        {
            if(check == null)
            {
                return false;
            }
            else if(comp.compare(key,check.getKeyValuePair().getKey()) < 0)
            {
                check = check.getLeft();
            }
            else if(comp.compare(key,check.getKeyValuePair().getKey()) > 0)
            {
                check = check.getRight();
            }
            else
            {
                return true;
            }
        }
    }

    public V get(K key)
    {
        //Returns the value associated with key or Null if the key is
        //not in the tree
        TNode check = root;
        while(true)
        {
            if(!containsKey(key))
            {
                return null;
            }
            else if(comp.compare(key,check.getKeyValuePair().getKey()) < 0)
            {
                check = check.getLeft();
            }
            else if(comp.compare(key,check.getKeyValuePair().getKey()) > 0)
            {
                check = check.getRight();
            }
            else
            {
                return check.getKeyValuePair().getValue();
            }
        }
    }

    public ArrayList<K> keySet()
    {
        //Returns an arraylist of keys in preorder
        keys = new ArrayList<K>();
        addKeys(root);
        return keys;
    }

    public void addKeys(TNode node)
    {
        //iterates through the keys in preorder
        if(node != null)
        {
            keys.add(node.getKeyValuePair().getKey());
            addKeys(node.left);
            addKeys(node.right);
        }
    }

    public ArrayList<V> values()
    {
        //Returns an arraylist of values in preorder
        values = new ArrayList<V>();
        addValues(root);
        return values;
    }

    public void addValues(TNode node)
    {
        //iterates through the values in preorder
        if(node != null)
        {
            values.add(node.getKeyValuePair().getValue());
            addValues(node.left);
            addValues(node.right);
        }
    }

    public ArrayList<KeyValuePair<K,V>> entrySet()
    {
        //Returns an arraylist of key-value pairs in preorder
        keyValuePairList = new ArrayList<KeyValuePair<K,V>>();
        ArrayList<K> keySet = keySet();
        ArrayList<V> values = values();

        for(int i=0; i<keySet.size(); i++)
        {
            KeyValuePair<K,V> keyValuePair = new KeyValuePair<K,V>(keySet.get(i), values.get(i));
            keyValuePairList.add(keyValuePair);
        }
        
        return keyValuePairList;
    }

    public int size()
    {
        //Returns the number of nodes in the BST
        return size;
    }

    public void clear()
    {
        //Empties the BST
        root = null;
        root.left = null;
        root.right = null;
        size = 0;
    }

    private class TNode
    {
        //Makes a node of the BST
        KeyValuePair<K,V> keyValuePair;
        TNode left;
        TNode right;

        public TNode(K k, V v)
        {
            //Constructor for TNode
            keyValuePair = new KeyValuePair<K,V>(k, v);
            left = null;
            right = null;
        }

        public V put(K key, V value, Comparator<K> comparator)
        {
            //Recursively searches through the tree in order to put the key
            //value pair in the correct location
            if(comparator.compare(key,this.keyValuePair.getKey()) < 0)
            {
                if(this.left != null)
                {
                    return this.left.put(key, value, comparator);
                }
                else
                {
                    size++;
                    this.left = new TNode(key,value);
                    return null;
                }
            }
            else if(comparator.compare(key,this.keyValuePair.getKey()) > 0)
            {
                if(this.right != null)
                {
                    return this.right.put(key, value, comparator);
                }
                else
                {
                    size++;
                    this.right = new TNode(key,value);
                    return null;
                }
            }
            else
            {
                V val = this.keyValuePair.getValue();
                this.keyValuePair.setValue(value);
                return val;
            }
        }

        public V get(K key, Comparator<K> comparator)
        {
            //Gets the value associated with the key or Null if the key
            //is not in the BST
            if(!containsKey(key))
            {
                return null;
            }
            else if(comparator.compare(key,this.keyValuePair.getKey()) < 0)
            {
                return this.left.get(key, comparator);
            }
            else if(comparator.compare(key,this.keyValuePair.getKey()) > 0)
            {
                return this.right.get(key, comparator);
            }
            else
            {
                return this.keyValuePair.getValue();
            }
        }

        public KeyValuePair<K,V> getKeyValuePair()
        {
            //Returns the keyValuePair associated with this TNode
            return keyValuePair;
        }

        public TNode getLeft()
        {
            //Returns the left child node
            return left;
        }

        public TNode getRight()
        {
            //Returns the right child node
            return right;
        }
    }

    public static void main(String[] args)
    {
        //Test Code
        BSTMap<String, Integer> bst = new BSTMap<String, Integer>( new AscendingString() );

        bst.put( "twenty", 20 );
        bst.put("twenty", 50);
        bst.put( "ten", 10 );
        bst.put( "eleven", 11 );
        bst.put( "five", 5 );
        bst.put("fifteen", 15);
        bst.put( "six", 6 );
        bst.put("seventeen", 17);

        System.out.println( "Eleven bst.get: " + bst.get( "eleven" ) );
        System.out.println( "Twenty bst.get (should be 50): " + bst.get( "twenty" ) );

        System.out.println( "six bst.get: " + bst.get( "six" ) );

        bst.put( "twenty", 20 );

        ArrayList<String> testKeySet = bst.keySet();
        System.out.println("KeySet Size: " + testKeySet.size());
        for(String key: testKeySet)
        {
            System.out.println("Key: " + key);
        }

        ArrayList<Integer> valuesTest = bst.values();
        System.out.println("Values Size: " + valuesTest.size());
        for(Integer value: valuesTest)
        {
            System.out.println("Value: " + value);
        }

        ArrayList<KeyValuePair<String,Integer>> entrySetTest = bst.entrySet();
        System.out.println("EntrySet Size: " + entrySetTest.size());
        for(KeyValuePair<String,Integer> keyValuePair: entrySetTest)
        {
            System.out.println("Key: " + keyValuePair.getKey());
            System.out.println("Value: " + keyValuePair.getValue());
        }
    }
}
