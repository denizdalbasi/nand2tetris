import java.io.*;

public class JackAnalyzer {
    public static void main(String[] args) {
        File source = new File(args[0]);
        File[] files = source.isDirectory() ? source.listFiles((dir, name) -> name.endsWith(".jack")) 
                                            : new File[]{source};

        for (File f : files) {
            File outFile = new File(f.getAbsolutePath().replace(".jack", ".xml"));
            JackTokenizer tokenizer = new JackTokenizer(f);
            CompilationEngine engine = new CompilationEngine(tokenizer, outFile);
            engine.compileClass(); // Entry point for the grammar
        }
    }
}