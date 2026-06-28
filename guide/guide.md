# JAVA++ (JPP) — Esoteric Programming Language

**Java++** is an imperative, interpreted esoteric programming language designed and implemented by **NoyName**. 

Despite its esoteric nature and syntax, the language is fully functional and computationally powerful enough to implement complex algorithms, including a fully working. The reference interpreter is written entirely in Python.

---

## 1. File Structure & Directives

All source files must use the `.jpp` extension. 

You can use the `@USING::` directive at the beginning of your lines to import modules (currently works as a stub for future library support).

```guide.jpp
@USING::STD
@USING::POS
```

---

## 2. Variables and Constants

The interpreter manages data using a dynamic storage model under the hood. Do not specify data types when creating variables; the parser handles types automatically based on the assigned value.

### Creating Variables
```var.jpp
// Syntax: new.variables.create.stack [name] = [value]
new.variables.create.stack age = 25
```

### Creating Constants
Constants are immutable and will throw an error if you attempt to overwrite them.
```const.jpp
// Syntax: new.constant.create.stack [name] = [value]
new.constant.create.stack name = "Hello, Mike"
```

---

## 3. Arrays

### Initialization
Java++ supports both dynamic arrays and padded, fixed-size arrays.

```Array.jpp
// Dynamic array (unlimited length)
new.array items _ = {10, 20, 30}

// Padded array (automatically padded with zeros up to length 5)
new.array items 5 = {10, 20}
```

### Modification & Reading
* **Append:** Use `.append(value)` to push an element to the end of the array.
* **Read:** Access elements using standard `array[index]` syntax with a specific integer index.

---

## 4. Control Flow

Conditional branching is handled via the `new.if.typedefender` statement.

```if.jpp
new.if.typedefender (age == 25) {
    print.consolewrite.puts("Age is exactly 25"!)
}
```

---

## 5. Loops

### For Loop
The loop statement requires the `type.integer` keyword for the iterator variable. Code block modification utilizes `plusplus` (+1) or `minmin` (-1) keywords.

```looping.jpp
new.for.looping (type.integer i = 0; i < 3; i plusplus) {
    print.consolewrite.puts(i)
}
```

### While Loop
Runs continuously as long as the specified condition remains true.
```while.jpp
new.looping (condition)
```

---

## 6. Input and Output

### Print to Console
Evaluates the expression inside `( )` and outputs it to the terminal. To print a clean string without raw quotes appearing in the console, terminate your string with `"!`.

```hello.jpp
print.consolewrite.puts("Hello, world"!)
```

### User Input
Reads terminal input from the user and assigns it directly to a variable.
```input.jpp
input.new.users.putss(counter)
```

---

## 7. Execution Control

To immediately terminate program execution with a specific exit code, use `quit.program.uwu`.

```exit.jpp
quit.program.uwu(0)
```

---

## 8. Function

```func.jpp
@USING::STD

new.function.script Test() {
    @USING::STD
    print.consolewrite.puts("Hello, Java++");
}
Test();
Test();
Test();
quit.program.uwu(0);
```

## Credits
Developed by **NoyName** (2026).
