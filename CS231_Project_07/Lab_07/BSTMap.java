package Lab_07;

import java.util.ArrayList;
import java.util.Comparator;

public class BSTMap<K,V> implements MapSet<K,V>
{
    TNode root;
    int size;
    Comparator<K> comp;

    public BSTMap(Comparator<K> comp)
    {
        this.comp = comp;
        root = null;
        int size = 0;
    }

    public V put(K key, V value)
    {
        if (root != null)
        {
            V val = root.get(key, comp);
			root.put(key,value,comp);
            return val;
		}
        else
        {
            size++;
			root = new TNode(key,value);
            return null;
		}
    }

    public boolean containsKey(K key)
    {
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
        ArrayList<K> keyList = new ArrayList<K>();
        ArrayList<TNode> tempList = new ArrayList<TNode>();
        TNode current = root;
        int currentIndex = 0;
        
        tempList.add(current);
        while(keyList.size() < size)
        {
            current = tempList.get(currentIndex);

            if(current.getLeft() != null && current.getRight() != null)
            {
                keyList.add(current.getLeft().getKeyValuePair().getKey());
                tempList.add(current.getLeft());
                keyList.add(current.getRight().getKeyValuePair().getKey());
                tempList.add(current.getRight());
                currentIndex += 1;
            }
            if(current.getLeft() != null)
            {
                keyList.add(current.getKeyValuePair().getKey());
                tempList.add(current.getLeft());
                currentIndex += 1;
            }
            else if(current.getRight() != null)
            {
                keyList.add(current.getKeyValuePair().getKey());
                tempList.add(current.getRight());
                currentIndex += 1;
            }
            else
            {
                keyList.add(current.getKeyValuePair().getKey());
                tempList.remove(current.getKeyValuePair().getKey());
            }
        }
        return keyList;
    }

    public ArrayList<V> values()
    {
        ArrayList<V> values = new ArrayList<V>();
        ArrayList<TNode> tempList = new ArrayList<TNode>();
        TNode current = root;
        int currentIndex = 0;
        
        tempList.add(current);
        while(values.size() < size)
        {
            current = tempList.get(currentIndex);

            if(current.getLeft() != null && current.getRight() != null)
            {
                values.add(current.getLeft().getKeyValuePair().getValue());
                tempList.add(current.getLeft());
                values.add(current.getRight().getKeyValuePair().getValue());
                tempList.add(current.getRight());
                currentIndex += 1;
            }
            if(current.getLeft() != null)
            {
                values.add(current.getKeyValuePair().getValue());
                tempList.add(current.getLeft());
                currentIndex += 1;
            }
            else if(current.getRight() != null)
            {
                values.add(current.getKeyValuePair().getValue());
                tempList.add(current.getRight());
                currentIndex += 1;
            }
            else
            {
                values.add(current.getKeyValuePair().getValue());
                tempList.remove(current.getKeyValuePair().getValue());
            }
        }
        return values;
    }

    public ArrayList<KeyValuePair<K,V>> entrySet()
    {
        ArrayList<KeyValuePair<K,V>> keyValuePairList = new ArrayList<KeyValuePair<K,V>>();
        ArrayList<K> keySet = keySet();
        ArrayList<V> values = values();

        for(int i=0; i<keySet.size()-1; i++)
        {

            if(comp.compare(keySet.get(i),keySet.get(i+1)) > 0)
            {
                K tempKey = keySet.get(i+1);
                V tempVal = values.get(i+1);
                keySet.set(i+1,keySet.get(i));
                values.set(i+1,values.get(i));
                keySet.set(i,tempKey);
                values.set(i,tempVal);
                i = -1;
            }
        }

        for(int i=0; i<keySet.size()-1; i++)
        {
            KeyValuePair<K,V> keyValuePair = new KeyValuePair<K,V>(keySet.get(i), values.get(i));
            keyValuePairList.add(keyValuePair);
        }
        
        return keyValuePairList;
    }

    public int size()
    {
        return size;
    }

    public void clear()
    {
        root = null;
        root.left = null;
        root.right = null;
        int size = 0;
    }

    private class TNode
    {
        KeyValuePair<K,V> keyValuePair;
        TNode left;
        TNode right;

        public TNode(K k, V v)
        {
            keyValuePair = new KeyValuePair<K,V>(k, v);
            left = null;
            right = null;
        }

        public V put(K key, V value, Comparator<K> comparator)
        {
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
            return keyValuePair;
        }

        public TNode getLeft()
        {
            return left;
        }

        public TNode getRight()
        {
            return right;
        }
    }

    public static void main(String[] args)
    {
        // create a BSTMap
        BSTMap<String, Integer> bst = new BSTMap<String, Integer>( new AscendingString() );

        bst.put( "twenty", 20 );
        bst.put("twenty", 50);
        bst.put( "ten", 10 );
        bst.put( "eleven", 11 );
        bst.put( "five", 5 );
        bst.put("fifteen", 15);
        bst.put( "six", 6 );
        //bst.put("seventeen", 17);

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
        System.out.println("Values Size: " + entrySetTest.size());
        for(KeyValuePair<String,Integer> keyValuePair: entrySetTest)
        {
            System.out.println("Key: " + keyValuePair.getKey());
            System.out.println("Value: " + keyValuePair.getValue());
        }
    }
}
