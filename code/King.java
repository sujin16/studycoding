import java.util.*;
public class King{
    public static void main(String args[]){
        int r =2;
        int c ='c' -'a'+1;
        int count =1;
        int steps[][] ={{-2,1},{-2,-1},{2,1},{2,-1},{-1,2},{1,2},{1,-2},{-1,-2}};
        for(int step[] : steps){
            int nextr =r +step[0];
            int nextc =r +step[1];
            if (nextr>=1 && nextr<=8 && nextc>=1 && nextc<=8){
                count+=1;
            }
        }
        System.out.println(count);
    }

}
