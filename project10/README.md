# Project 10: Jack Language Syntax Analyzer

This project is a foundational compiler tool built in Java. Its primary goal is to take human-readable source code written in the Jack language and "deconstruct" it into a structured XML format. By doing this, it creates a visual map of the code's hierarchy—essentially showing exactly how a computer understands the syntax, logic, and structure of a program.

Think of this as the "under-the-hood" look at how programming languages are parsed before they are turned into machine code.

---

## structure

This analyzer is organized into three specialized "workers" (Java classes) that handle different stages of the process:

* **`JackAnalyzer.java` (The Manager):** This is the entry point. Its job is to handle the file system. Whether you feed it a single file or an entire folder of code, it orchestrates the process and makes sure everything gets sent to the right place.
* **`jacktoken.java` (The Translator):** Before you can analyze grammar, you have to break sentences into words. This class reads your raw code, cleans out comments and extra spaces, and chops it up into meaningful "tokens"—like recognizing that `class` is a keyword or that `+` is a symbol.
* **`CompilationEngine.java` (The Architect):** This is where the heavy lifting happens. It takes the stream of tokens from the translator and builds the final product. Using a technique called "recursive descent parsing," it reads through the tokens and carefully writes an XML file that maps out the structure of classes, methods, and logic statements.