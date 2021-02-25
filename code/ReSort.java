import java.util.*;
public class ReSort{
    public static boolean isNumeric(String str) {
        try {
            Double.parseDouble(str);
            return true;
        } catch(NumberFormatException e){
            return false;
        }
    }

    public static void main(String args[]){
        String answer = "K1KA5CB7";
        String[] arr = answer.split("");
        List<String> list =new ArrayList<String>();
        int result=0;
        for(String word: arr){
            if(isNumeric(word)) result+=Integer.parseInt(word);
            else list.add(word);
        }
        Collections.sort(list);
        list.add(Integer.toString(result));
        StringBuilder str = new StringBuilder();
        for (String w : list) str.append(w);
        System.out.println(str);

    }

}
