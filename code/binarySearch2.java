import java.util.*;

public class Main {

    public static int lowerBound(int[] data, int target) {
        int begin = 0;
        int end = data.length;

        while(begin < end) {
            int mid = (begin + end) / 2;
            if(data[mid] >= target) end=mid;
            else begin = mid + 1;
        }
        return end;
    }

    public static int upperBound(int[] data, int target) {
        int begin = 0;
        int end = data.length;

        while(begin < end) {
            int mid = (begin + end) / 2;
            if(data[mid] <= target) begin=mid+1;
            else end = mid;
        }
        return end;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int num = sc.nextInt();

        // 각 떡의 개별 높이 정보
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        int result = upperBound(arr,num) - lowerBound(arr,num);
        if(result==0)System.out.println(-1);
        else System.out.println(result);
    }

}
