import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class JackAnalyzer {
    public static void main(String[] args){
       File source = new File(args[0]);
       File[] files  = source.isDirectory() ? source.listFiles((dir, name) -> name.endsWith(".jack")) : new File[]{source}; 

       for(File f: files){
        File outFile = new File(f.getAbsolutePath().replace(".jack", "T.xml"));
        jacktoken tokenizer = new jacktoken(f);
        CompilationEngine engine = new CompilationEngine(f, outFile);
        engine.compileClass();
       }
    }
}