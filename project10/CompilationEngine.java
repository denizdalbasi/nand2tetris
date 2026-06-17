import java.util.*;
import java.io.*;


public class CompilationEngine {
    private jacktoken tokenizer;
    private PrintWriter writer;
    private int indentLevel = 0;
    public CompilationEngine(File inputFile, File outputFile)  {
        this.tokenizer = new jacktoken(inputFile);
        try{
            this.writer = new PrintWriter(outputFile);

        }catch(FileNotFoundException e){
            e.printStackTrace();
        }
    }
    // Helper method to write XML with proper indentation
    private void writeTag(String tag, String content){
        String indent = "  ".repeat(indentLevel);
        if(content.equals("<")) content = "&lt;";
        else if(content.equals(">")) content = "&gt;";
        else if(content.equals("&")) content = "&amp;";
        else if(content.equals("\"")) content = "&quot;";
        else if(content.equals("'")) content = "&apos;";
        writer.println(indent + "<" + tag + "> " + content + " </" + tag + ">");
    }

    private void openTag(String tag){
        writer.println("  ".repeat(indentLevel) + "<" + tag + ">");
        indentLevel++;
    }

    private void closeTag(String tag){
        indentLevel--;
        writer.println("  ".repeat(indentLevel) + "</" + tag + ">");
    }
     
    private void processToken(){
        String token = tokenizer.getCurrentToken();
        switch(tokenizer.tokenType()){
            case "KEYWORD":
                writeTag("keyword", token);
                break;
            case "SYMBOL":
                writeTag("symbol", token);
                break;
            case "IDENTIFIER":
                writeTag("identifier", token);
                break;
            case "INT_CONST":
                writeTag("integerConstant", token);
                break;
            case "STRING_CONST":
                writeTag("stringConstant", token.substring(1, token.length() - 1)); // Remove quotes
                break;
        }
    }

    private void compileSubroutine(){
        openTag("subroutine");
        processToken(); // subroutine type (constructor/function/method)
        
        tokenizer.advance();
        processToken(); // return type
        
        tokenizer.advance();
        processToken(); // subroutine name
        
        tokenizer.advance();
        processToken(); // '('
        
        tokenizer.advance();
        // TODO: compile parameter list
        
        tokenizer.advance();
        processToken(); // ')'
        
        tokenizer.advance();
        // TODO: compile subroutine body
        
        closeTag("subroutine");
    }

    public void compileClass(){
        tokenizer.advance(); // 'class'
        openTag("class");
        processToken(); // class name

        tokenizer.advance(); // '{'
        processToken(); // '{'

        tokenizer.advance();

        while(tokenizer.hasMoreTokens()){
            String token = tokenizer.getCurrentToken();
            if(token.equals("static")||token.equals("field")){
                compileClass();
            }
            else if(token.equals("constructor")||token.equals("function")||token.equals("method")){
                compileSubroutine();
            }
            else if(token.equals("}")){
                processToken(); // '}'
                break;
            }
            else{
                tokenizer.advance();
            }
        }
        closeTag("class");
        writer.close();
    }

    public void compileClassVarDec(){
        openTag("classVarDec");

        processToken(); // 'static' or 'field'

        do {
            tokenizer.advance();
            processToken(); // type

        } while(!tokenizer.nextToken().equals(";"));
        tokenizer.advance();
        processToken(); // ';'
        closeTag("classVarDec");
    }

    public void compileSubroutineDec(){
        openTag("subroutineDec");
        processToken(); // 'constructor' or 'function' or 'method'

        do{
            tokenizer.advance();
            processToken(); // return type or subroutine name

        }while(!tokenizer.nextToken().equals("("));
        tokenizer.advance();
        processToken(); // '('
        // TODO: compile parameter list
        tokenizer.advance();
        processToken(); // ')'
        // TODO: compile subroutine body
        closeTag("subroutineDec");
    }

    public void compileSubroutineList(){
        openTag("subroutineBody");
        processToken(); // '{'

        while(!tokenizer.getCurrentToken().equals("}")){
            tokenizer.advance();
            processToken();
        }
        tokenizer.advance();
        processToken(); // '}'
        closeTag("subroutineBody");
        compileSubroutine();
    }

    public void compileParameter(){
        openTag("parameterList");
        while(true){
            String token = tokenizer.getCurrentToken();
            if(token.equals("let")) compileLet();
            else if(token.equals("if")) compileIf();
            else if(token.equals("while")) compileWhile();
            else if(token.equals("do")) compileDo();
            else if(token.equals("return")) compileReturn();
            else break;
        }
        closeTag("parameterList");
    }

    public void compileLet(){
        openTag("letStatement");
        processToken(); // 'let'

        tokenizer.advance();
        processToken(); // varName

        if(tokenizer.getCurrentToken().equals("[")){
            processToken(); // '['
            tokenizer.advance();
            processToken(); // expression
            compileClass();
            compileParameter();
            processToken(); // ']'
            tokenizer.advance();
        }
        processToken(); // '='
        tokenizer.advance();
        processToken(); // expression
        compileClass();
        processToken(); // ';'
        closeTag("letStatement");
    }

    public void compileIf(){
        openTag("ifStatement");
        processToken(); // 'if'

        tokenizer.advance();
        processToken(); // '('
        tokenizer.advance();
        processToken(); // expression

        tokenizer.advance();
        processToken(); // ')'
        tokenizer.advance();
        processToken(); // '{'

        if(tokenizer.getCurrentToken().equals("else")){
            processToken(); // '}'
            tokenizer.advance();
            processToken(); // 'else'
            tokenizer.advance();
            processToken(); // '{'
            compileClass();
        }
        closeTag("ifStatement");
    }

    public void compileWhile(){
        openTag("whileStatement");
        processToken(); // 'while'
        tokenizer.advance();
        processToken(); // '('
        tokenizer.advance();
        processToken(); // expression

        tokenizer.advance();
        processToken(); // ')'
        tokenizer.advance();
        processToken(); // '{'
    }

    public void compileDo(){
        openTag("doStatement");
        processToken(); // 'do'
        while(!tokenizer.getCurrentToken().equals(";")){
             tokenizer.advance();
             processToken();
            tokenizer.advance();
            processToken(); // subroutine call
            if(tokenizer.getCurrentToken().equals(";")){
                break;
            }
        }
        tokenizer.advance();
        processToken(); // ';'
        closeTag("doStatement");
    }

    public void compileReturn(){
        openTag("returnStatement");
        processToken(); // 'return'
        if(!tokenizer.nextToken().equals(";")){
            tokenizer.advance();
            processToken(); // expression
            compileClass();
        }
        tokenizer.advance();
        processToken(); // ';'
        closeTag("returnStatement");
    }

    public void compileExpression(){
        openTag("expression");
        processToken(); // term
        while(tokenizer.nextToken().matches("[+\\-*/&|<>=]")){
            tokenizer.advance();
            processToken(); // op
            tokenizer.advance();
            processToken(); // term
        }
        closeTag("expression");
    }

    public void compileTerm(){
        openTag("term");
        String token = tokenizer.getCurrentToken();
        String nextToken = tokenizer.nextToken();
        if(tokenizer.tokenType().equals("IDENTIFIER") && nextToken.equals("[")){
            processToken(); // varName
            tokenizer.advance();
            processToken(); // '['
            tokenizer.advance();
            processToken(); // expression
            compileClass();
            processToken(); // ']'
        }
        else if(tokenizer.tokenType().equals("IDENTIFIER") && (nextToken.equals("(") || nextToken.equals("."))){
            processToken(); // subroutineName or className or varName
            if(nextToken.equals(".")){
                tokenizer.advance();
                processToken(); // '.'
                tokenizer.advance();
                processToken(); // subroutineName
            }
            tokenizer.advance();
            processToken(); // '('
            compileExpressionList();
            processToken(); // ')'
        }
        else if(tokenizer.tokenType().equals("INT_CONST") || tokenizer.tokenType().equals("STRING_CONST") || tokenizer.tokenType().equals("KEYWORD")){
            processToken(); // integerConstant or stringConstant or keywordConstant
        }
        else if(tokenizer.tokenType().equals("IDENTIFIER")){
            processToken(); // varName
        }
        else if(token.equals("(")){
            processToken(); // '('
            compileExpression();
            processToken(); // ')'
        }
        else if(token.equals("-") || token.equals("~")){
            processToken(); // unaryOp
            tokenizer.advance();
            compileTerm();
        }
        closeTag("term");

    }

    public int compileExpressionList(){
        openTag("expressionList");
        int expressionCount = 0;
        if(!tokenizer.nextToken().equals(")")){
            compileExpression();
            expressionCount++;
            while(tokenizer.nextToken().equals(",")){
                tokenizer.advance();
                processToken(); // ','
                tokenizer.advance();
                compileExpression();
                expressionCount++;
            }
        }
        closeTag("expressionList");
        return expressionCount;
    }
    
}