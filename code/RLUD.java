import java.util.*;
public class Main{
    public static void main(String args[]){
        String[] arr ={"R","R","R","U","D","D"};
        int[] cur ={1,1};
        int i=0;
        int n=5;
        while(i<arr.length){
            int[] add =cur.clone();
            if(arr[i].equals("R")) add[1] +=1;
            if(arr[i].equals("L")) add[1] -=1;
            if(arr[i].equals("U")) add[0] -=1;
            if(arr[i].equals("D")) add[0] +=1;
            if(add[0]>=1 && add[0]<=n && add[1]>=1 && add[1]<=n){
                cur =add.clone();
            }
            i+=1;
        }
        System.out.println(Arrays.toString(cur));
    }
}
