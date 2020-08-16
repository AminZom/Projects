# REPL and VS Code Setup for Clojure Tingz

## Make sure you have Java 8 installed!
- This can be either the Oracle or OpenJDK versions
- Ensure that `java` in on your path, or that the environment variable `JAVA_HOME` is set

## First, let's install Clojure!
- All installation instructions pulled from the [official clojure page for doing so](https://clojure.org/guides/getting_started)
- if you don't want to do this, you can use an online REPL through [repl.it](https://repl.it/languages/clojure), you just won't be able to use Leiningen

### Windows
- follow the instructions outlined [here](https://github.com/clojure/tools.deps.alpha/wiki/clj-on-Windows)

### MacOS using Homebrew
- `brew install clojure/tools/clojure`

### Linux
- `curl -O https://download.clojure.org/install/linux-install-1.10.1.536.sh`
- `chmod +x linux-install-1.10.1.536.sh`
- `sudo ./linux-install-1.10.1.536.sh`

## Next, let's install Leiningen!
- Leiningen is a beautiful tool used to automate aspects of coding in Clojure and assist with managing, testing, and setting up your Clojure project. Let's install it!
- follow the instructions outlined on [Leiningen's site](https://leiningen.org/)

## Okay, now that we're set up with Clojure and Leiningen...
- let's verify that we've got Clojure and Leiningen installed correctly

### Clojure
- go to your terminal of choice and verify that running the command `clj` outputs something along the lines of 
    ```
    PS C:\Users\Christian> clj
    Clojure 1.10.1
    user=>
    ```
    This indicates that the Clojure REPL, or Read-Eval-Print-Loop, is working as expected. This can be used to code in clojure directly, or it can be used to run Clojure files by using `clj <path/to/clojure/file>`

### Leiningen
- from your terminal of choice and run
  `lein -version`
  You should view similar output to
  ```
  PS C:\Users\Christian> lein -version
   Leiningen 2.9.1 on Java 1.8.0_171 Java HotSpot(TM) 64-Bit Server VM
  ```
- if either of the above do not work as outlined, ensure that you've restarted your terminal after installing both Clojure and Leiningen. 
- if working via Git Bash on Windows, getting the `clj` command to work may be tricky; however, you can use the REPL through Leiningen by running `lein repl`
- Now, before setting up your first Clojure project, I would _highly_ recommend checking out the [Leiningen tutorial](https://github.com/technomancy/leiningen/blob/stable/doc/TUTORIAL.md), as it has some sweet tips and tricks that will make coding in Clojure infinitely less painful

# VS Code Setup
- Ensure you have a working copy of VS Code installed. Documentation for doing so can be found [here](https://code.visualstudio.com/download)
- Install the following extensions:
    - Calva (ID betterthantomorrow.calva)
      - This will assist with formatting your code and will highlight brackets (!!!), making coding much easier when functions get complex
    - clj-kondo (ID: borkdude.clj-kondo)
        - This will lint your code!
    - Clojure (ID: avli.clojure)
      - This will add nREPL support in VS Code, which will let you you view method documentation on hover, add code-completion, and add function signatures
      - If the repl doesn't automatically
- Ensure that nREPL is running
- If the nREPL IS working, you should see something along the lines of 
  ![nREPL connected](textbook/resources/repl_working.jpg)
  Which will let us see our method signatures on-hover, provide code-completion, and lint our code!
  ![nREPL working](textbook/resources/repl_running_function_header.jpg)
  - If the nREPL is not running, you won't get nify features like code completion whilst coding in Clojure! Let's make sure that it is
  - In the bottom-left of your VS Code window, you should see something like this, if the nREPL is not connected
  ![nREPL not connected](textbook/resources/repl_not_working.jpg)
      - In this case, let's get it running! Click on the `nRepl` button shown in the image above. A window will open displaying the following:
      ![get nREPL connected 1](textbook/resources/start_repl_1.jpg)
      Click on the first highlighted action (or hit enter), which will then display this pop-up:
      ![get nREPL connected 2](textbook/resources/  start_repl_2.jpg)
      Again, click on the highlighted selection.
      - And your nREPL should now be running! Happy coding!
