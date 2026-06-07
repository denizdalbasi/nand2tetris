import java.io.*;
import java.util.*;

public class JackTokenizer {
    private List<String> tokens;
    private int currentTokenIndex;
    private String currentToken;

    public JackTokenizer(File file) {
        tokens = new ArrayList<>();
        currentTokenIndex = -1;
        try {
            Scanner scanner = new Scanner(file);
            String content = "";
            // Read and strip comments
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine().split("//")[0].trim();
                content += line + " ";
            }
            // Add spaces around symbols so we can split them
            String symbols = "{}()[].,;+-*/&|<>=~";
            for (char s : symbols.toCharArray()) {
                content = content.replace(String.valueOf(s), " " + s + " ");
            }
            // Split by whitespace and store
            String[] rawTokens = content.split("\\s+");
            for (String t : rawTokens) {
                if (!t.isEmpty()) tokens.add(t);
            }
        } catch (Exception e) { e.printStackTrace(); }
    }

    public boolean hasMoreTokens() { return currentTokenIndex < tokens.size() - 1; }

    public void advance() {
        if (hasMoreTokens()) {
            currentTokenIndex++;
            currentToken = tokens.get(currentTokenIndex);
        }
    }

    public String tokenType() {
        if (currentToken.matches("class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return")) return "KEYWORD";
        if (currentToken.matches("[{}()[\\].,;+\\-*/&|<>=~]")) return "SYMBOL";
        if (currentToken.matches("\\d+")) return "INT_CONST";
        if (currentToken.startsWith("\"")) return "STRING_CONST";
        return "IDENTIFIER";
    }

    public String keyword() { return currentToken; }
    public String symbol() { return currentToken; }
    public String identifier() { return currentToken; }
    public int intVal() { return Integer.parseInt(currentToken); }
    public String stringVal() { return currentToken.replace("\"", ""); }
}