import java.util.*;
public class Time{
    public static void main(String args[]){
        int h =1;
        int count =0;
        for(int i=0;i<h+1;i++){
            for(int j=0;j<60;j++){
                for(int k=0;k<=60;k++){
                    String time = Integer.toString(i)+Integer.toString(j)+Integer.toString(k);
                    if(time.contains("3")) count+=1;
                }
            }
        }
        System.out.println(count);

    }
}
