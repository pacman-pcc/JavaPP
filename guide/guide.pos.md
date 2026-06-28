# POS LIBS in Java++

## 1. change.directory(new_path);

<pre>
@USING::STD
@USING::POS

change.directory("/mnt/basic/Javapp/Loxe");

quit.program.uwu(0);
</pre>

## 2. create.makedirectory(mkdir_path);

<pre>
@USING::STD
@USING::POS

create.makedirectory("/mnt/basic/Javapp/NewFolder");

quit.program.uwu(0);
</pre>

## 3. create.fullydirectory(mkfull_path);

<pre>
@USING::STD
@USING::POS

create.fullydirectory("/mnt/basic/Javapp/Nested/Folder/Tree");

quit.program.uwu(0);
</pre>

## 4. ls.in(ls_path);

<pre>
@USING::STD
@USING::POS

new.variables.in.stack files = ls.in("/mnt/basic/Javapp");

print.consolewrite.puts(files);

quit.program.uwu(0);
</pre>

## 5. delete.in.terminate(del_path);

<pre>
@USING::STD
@USING::POS

delete.in.terminate("/mnt/basic/Javapp/file.txt");

quit.program.uwu(0);
</pre>

## 6. rename.file(r_src, dst);

<pre>
@USING::STD
@USING::POS

rename.file("old.txt", "new.txt");

quit.program.uwu(0);
</pre>

## 7. oh.my.cwd();

<pre>
@USING::STD
@USING::POS

new.variables.in.stack current_dir = oh.my.cwd();

print.consolewrite.puts(current_dir);

quit.program.uwu(0);
</pre>

## 8. walk.in(walk_path);

<pre>
@USING::STD
@USING::POS

new.variables.in.stack dir_tree = walk.in("/mnt/basic/Javapp");

print.consolewrite.puts(dir_tree);

quit.program.uwu(0);
</pre>

## 9. ready.system.console.text(command);

<pre>
@USING::STD
@USING::POS

ready.system.console.text("clear");

quit.program.uwu(0);
</pre>

## 10. pos.name.os();

<pre>
@USING::STD
@USING::POS

new.variables.in.stack os_platform = pos.name.os();

print.consolewrite.puts(os_platform);

quit.program.uwu(0);
</pre>
