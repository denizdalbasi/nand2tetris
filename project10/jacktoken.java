import java.util.*;
import java.io.*;

public class jacktoken {
    private List<String> tokens;
    private  int currentTokenIndex;
    private String currentToken;

    public jacktoken(File file){
        tokens = new ArrayList<>();
        currentTokenIndex = -1;
        try{
            Scanner scanner = new Scanner(file);
            String line = "";
            while(scanner.hasNextLine()){
                String temp = scanner.nextLine().split("//")[0].trim();
                line +=temp + " "; 
            }
            String symbols = "{}()[].,;+-*/&|<>=~";
            for (char s: symbols.toCharArray()){
                line = line.replace(String.valueOf(s), " " + s + " ");
            }
            String[] rawTokens = line.split("\\s+"); 
            for(String t: rawTokens){
                if(!t.isEmpty()){
                    tokens.add(t);
                }
            }
        } catch(FileNotFoundException e){
            e.printStackTrace();
        }
    }
    public boolean hasMoreTokens(){return currentTokenIndex <tokens.size() -1;}

    public void advance(){
        if(hasMoreTokens()){
            currentTokenIndex++;
            currentToken = tokens.get(currentTokenIndex);
        }
    }
    public String tokenType(){
        if(currentToken.matches("class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this")){
            return "KEYWORD";
        } else if(currentToken.matches("[{}()\\[\\].,;+-/*&|<>=~]")){
            return "SYMBOL";
        } else if(currentToken.matches("\".*\"")){
            return "STRING_CONST";
        } else if(currentToken.matches("\\d+")){
            return "INT_CONST";
        } else {
            return "IDENTIFIER";
        }
    }
    public String getCurrentToken(){return currentToken;}
    public String nextToken(){
        if(currentTokenIndex + 1 < tokens.size()){
            return tokens.get(currentTokenIndex + 1);
        }
        return null;

    }


}