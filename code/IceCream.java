import java.util.*;
public class IceCream{
    static int n,m;
    static int[][] graph = new int[1000][1000];
    static boolean dfs(int a, int b){
        //주어진 범위를 벗어나는 경우
        if (a<0 || a>n-1 || b<0 || b>n-1 ) return false;
        if(graph[a][b] ==0){
            graph[a][b] =1;
            dfs(a, b-1);
            dfs(a, b-1);
            dfs(a+1, b);
            dfs(a, b+1);
            return true;
        }
        return false;
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        n =sc.nextInt();
        m = sc.nextInt();
        for (int i=0;i<n;i++){
            String str = sc.nextLine();
            for(int j=0;j<m;j++){
                graph[i][j] = str.charAt(i)-'0';
            }
        }
        int result=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if (dfs(i,j)) result+=1;
            }
        }
        System.out.println(result);

    }

}
