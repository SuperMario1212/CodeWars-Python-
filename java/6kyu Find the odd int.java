// <Instructions>

// Given an array of integers, find the one that appears an odd number of times.
// There will always be only one integer that appears an odd number of times.

// --> My Solution <--

+---------------------------------+
public class FindOdd {
  public static int findIt(int[] a) {
    int size = a.length;
    int res = 0;

    for (int i = 0; i < size; i++) {
      res = res ^ a[i];

    }
    return res;
  }
}

+----------------------------------+
  
// <Other Solution>

import static java.util.Arrays.stream;

public class FindOdd {
  public static int findIt(int[] arr) {
    return stream(arr).reduce(0, (x, y) -> x ^ y);
  }
}
