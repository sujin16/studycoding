import java.lang.reflect.Array;
import java.util.*;

public class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] table = new int[100];
        Arrays.fill(table,0);
        table[0] = arr[0];
        table[1] = Math.max(arr[0],arr[1]);
        for(int i=2;i<n;i++){
            table[i] =Math.max(table[i-1],table[i-2]+arr[i]);
        }
        System.out.println(table[-1]);

    }

}
