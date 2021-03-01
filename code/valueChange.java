import com.sun.jmx.snmp.internal.SnmpSubSystem;

import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.IntStream;

public class valueChange{
    public static int k;
    public  static int solution(Integer[] a,Integer[]b){
        int answer=0;
        Arrays.sort(a);
        Arrays.sort(b,Collections.reverseOrder());
        int i=0;
        while(i<k){
            if(a[i]<b[i]){
                int temp = a[i];
                a[i] =b[i];
                b[i] =temp;
            }
            i+=1;
        }
        for(Integer num: a) answer+=num;
        return answer;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        k = sc.nextInt();
        Integer [] a =new Integer[n];
        Integer [] b =new Integer[n];
        for(int i =0;i<n;i++) a[i] = sc.nextInt();
        for(int i =0;i<n;i++) b[i] = sc.nextInt();
        System.out.println(solution(a,b));
    }

}
