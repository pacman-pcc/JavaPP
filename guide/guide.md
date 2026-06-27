# JAVA++ - Language guide.

This is the official guide to Java++.

## 1. File Structure.

All files must end with the `.jpp` extension.

### Directives

You can use `@USING::` at the beginning of lines. (For now, this is a stub, to be honest, but later there will be libraries, if there are any at all.)

```guide.jpp
@USING::STD
@USING::MATH
```

## 2. Varibles and Constants

The interpreter uses simple storage under the hood to keep your data.

### Creating Variables

```var.jpp
// new.variables.create.stack [type] [name];
new.variables.create.stack type.integer age = 25;
```

- Type: type.integer (int), type.floating (float), type.stringer(string), type.boolean(bool).

### Creating constant

```const.jpp
// new.constant.create.stack [type] [name];
new.constant.create.stack type.stringer name = "Hello, Mike";
```

## 3. Arrays

### Initialization

```Array.jpp
// Dynamic array
new.array items _ = {10, 20, 30};

// Padded array
new.array items 5 = {10, 20};
```
### Modify
* **Append**: Use `.append(value)` to add something to the end of your array.
* **Read**: Read elements using standard `array[index]` syntax. You can also pass a variable inside the brackets.

## 4. Control Flow

```if.jpp
new.if.typedefender (age == 25) {
    print.console.writeline.puts("It is 25!); // Print 
}
```

### 5. Loops

* **While**: `new.looping (condition)` runs until the condition inside brackets becomes false.
* **For**: `new.for.looping (type.integer i = 0; i < 10; i plusplus)` splits the block by semicolons, creates the variable, checks the condition, and modifies it using `plusplus` (+1) or `minmin` (-1) keywords when it hits the closing `}` bracket.

```looping.jpp
new.for.looping (type.integer i = 0; i < 3; i plusplus) {
    print.consolewrite.puts(i);
}
```

### 6. Input and Output

### Print to Console
Takes whatever is inside `( )`, evaluates the value (whether it's a string, a number, a variable, or an array element), and prints it out.
```hello.jpp
print.consolewrite.puts("Hello, world"!);
```

### User Input
Reads a string or number typed by the user in the terminal and puts it straight into your variable.
```json.jpp
input.new.users.putss(counter)
```


### 7. Exit program

To stop the execution completely at any point, use `quit.program.uwu` with an exit code inside the brackets.
```exit.jpp
quit.program.uwu(0);
```
