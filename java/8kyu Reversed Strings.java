/*
 --> Instructions <--
 Complete the solution so that it reverses the string passed into it.
 
'world'  =>  'dlrow'
*/

// <My Solution> #1

public class Kata {

  public static String solution(String str) {
    // Your code here...
    StringBuffer reverseStr = new StringBuffer(str).reverse();
    String newStr = reverseStr.toString();
    return newStr;
  }

}

+------------------------------------------------------------------+

// --> Best Solution <-- #2

public class Kata {

  public static String solution(String str) {
    return new StringBuilder(str).reverse().toString();
  }

}

+-------------------------------------------------------------------+
 
// --> Other Smart Solution <-- #3

public class Kata {

  public static String solution(String str) {
    // Your code here...
    String newcad="";
    
    for(int i = str.length()-1; i >= 0; i--){
      newcad += str.charAt(i);
    }
    
    return newcad;
  }

}
