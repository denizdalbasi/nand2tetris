import java.io.*;

public class CompilationEngine {
    private JackTokenizer tokenizer;
    private PrintWriter writer;

    public CompilationEngine(JackTokenizer tokenizer, File outFile) {
        this.tokenizer = tokenizer;
        try { this.writer = new PrintWriter(outFile); } catch (Exception e) {}
    }

    // Helper to write tokens with XML tags
    private void writeToken() {
        String type = tokenizer.tokenType();
        String val = "";
        
        if (type.equals("KEYWORD")) val = tokenizer.keyword();
        else if (type.equals("SYMBOL")) val = escape(tokenizer.symbol());
        else if (type.equals("IDENTIFIER")) val = tokenizer.identifier();
        else if (type.equals("INT_CONST")) val = String.valueOf(tokenizer.intVal());
        else if (type.equals("STRING_CONST")) val = tokenizer.stringVal();
        
        writer.println("<" + type.toLowerCase() + "> " + val + " </" + type.toLowerCase() + ">");
    }

    private String escape(String symbol) {
        if (symbol.equals("<")) return "&lt;";
        if (symbol.equals(">")) return "&gt;";
        if (symbol.equals("&")) return "&amp;";
        if (symbol.equals("\"")) return "&quot;";
        return symbol;
    }

    public void compileClass() {
        tokenizer.advance(); // consume 'class'
        writer.println("<class>");
        writeToken(); // 'class'
        
        tokenizer.advance();
        writeToken(); // className
        
        tokenizer.advance();
        writeToken(); // '{'

        // Loop for ClassVarDecs and SubroutineDecs
        while (true) {
            tokenizer.advance();
            String lookAhead = tokenizer.keyword();
            if (lookAhead.equals("field") || lookAhead.equals("static")) {
                compileClassVarDec();
            } else if (lookAhead.equals("constructor") || lookAhead.equals("function") || lookAhead.equals("method")) {
                compileSubroutine();
            } else {
                break; // Should be '}'
            }
        }
        
        writeToken(); // '}'
        writer.println("</class>");
        writer.close();
    }

    public void compileStatements() {
        writer.println("<statements>");
        while (true) {
            tokenizer.advance();
            String kw = tokenizer.keyword();
            if (kw.equals("let")) compileLet();
            else if (kw.equals("if")) compileIf();
            else if (kw.equals("while")) compileWhile();
            else if (kw.equals("do")) compileDo();
            else if (kw.equals("return")) compileReturn();
            else { 
                // Backtrack or break if no statement found
                break; 
            }
        }
        writer.println("</statements>");
    }

    // Example of a specific statement
    public void compileDo() {
        writer.println("<doStatement>");
        writeToken(); // 'do'
        tokenizer.advance();
        writeToken(); // identifier (subroutineName)
        // ... continue logic for (expressionList);
        writer.println("</doStatement>");
    }
    public void compileClassVarDec() {
        writer.println("<classVarDec>");
        writeToken(); // static or field
        tokenizer.advance(); writeToken(); // type
        tokenizer.advance(); writeToken(); // varName
        tokenizer.advance();
        while (tokenizer.symbol().equals(",")) {
            writeToken(); // ,
            tokenizer.advance(); writeToken(); // varName
            tokenizer.advance();
        }
        writeToken(); // ;
        writer.println("</classVarDec>");
    }

    public void compileSubroutine() {
        writer.println("<subroutineDec>");
        writeToken(); // constructor, function, or method
        tokenizer.advance(); writeToken(); // void or type
        tokenizer.advance(); writeToken(); // subroutineName
        tokenizer.advance(); writeToken(); // (
        compileParameterList();
        writeToken(); // )
        compileSubroutineBody();
        writer.println("</subroutineDec>");
    }

    public void compileParameterList() {
        writer.println("<parameterList>");
        // Check if next is ')'
        // If not, read type varName, then loop for (, type varName)
        writer.println("</parameterList>");
    }

    public void compileSubroutineBody() {
        writer.println("<subroutineBody>");
        tokenizer.advance(); writeToken(); // {
        // Compile varDecs while they exist
        while (/* next token is 'var' */) { compileVarDec(); }
        compileStatements();
        tokenizer.advance(); writeToken(); // }
        writer.println("</subroutineBody>");
    }

    public void compileLet() {
        writer.println("<letStatement>");
        writeToken(); // let
        tokenizer.advance(); writeToken(); // varName
        if (/* next is '[' */) {
            tokenizer.advance(); writeToken(); // [
            compileExpression();
            tokenizer.advance(); writeToken(); // ]
        }
        tokenizer.advance(); writeToken(); // =
        compileExpression();
        tokenizer.advance(); writeToken(); // ;
        writer.println("</letStatement>");
    }

    public void compileIf() {
        writer.println("<ifStatement>");
        writeToken(); // if
        tokenizer.advance(); writeToken(); // (
        compileExpression();
        tokenizer.advance(); writeToken(); // )
        tokenizer.advance(); writeToken(); // {
        compileStatements();
        tokenizer.advance(); writeToken(); // }
        // Handle optional else
        writer.println("</ifStatement>");
    }

    public void compileExpression() {
        writer.println("<expression>");
        compileTerm();
        // While current is op, consume and compile next term
        writer.println("</expression>");
    }

    public void compileTerm() {
        writer.println("<term>");
        // Implement logic for integerConstant, stringConstant, identifier, 
        // unaryOp, or (expression)
        writer.println("</term>");
    }
    
    // Implement compileLet, compileWhile, compileIf, etc. similarly
}