import java.lang.reflect.Array;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int []table = new int[n];
        Arrays.fill(table,0);
        table[0] =1;
        int cur = arr[0];
        for( int i=1;i<n;i++){
            if(cur<arr[i]) table[i] =table[i-1]+1;
            else table[i] = table[i-1];
            cur = table[i];
        }
        System.out.println(n-table[-1]);
    }

}
