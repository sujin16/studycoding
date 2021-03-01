import java.util.*;

public class Main{
    public  static int Solution(int[] arr,int n,int m){
        int result=0;
        int start =0;
        int end = Arrays.stream(arr).max().getAsInt();
        while (start<=end){
            int sum=0;
            int mid = (start+end)/2;
            for(int num: arr){
                if (num>mid) sum+=num-mid;
            }
            if(sum<m) end=mid-1;
            else{
                result= mid;
                start=mid+1;
            }
        }
        return result;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        int m = sc.nextInt();
        int [] arr =new int[n];
        for(int i =0;i<n;i++) arr[i] = sc.nextInt();
        System.out.println(Solution(arr,n,m));
    }

}
