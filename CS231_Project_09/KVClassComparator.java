import java.util.Comparator;

class KVTestComparator implements Comparator<KeyValuePair<Integer,Float>> {
    public int compare( KeyValuePair<Integer,Float> i1, KeyValuePair<Integer,Float> i2 ) {
        // returns negative number if i2 comes after i1 lexicographically
        float diff = i1.getValue() - i2.getValue();
        if (diff == 0.0)
            return 0;
        if (diff > 0.0)
            return 1;
        else
            return -1;
    }
}