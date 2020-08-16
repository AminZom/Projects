# First Mini Project in Clojure

This chapter will cover how to set up a mini project in Clojure, using all of the information learned in previous chapters.

## Leiningen & VSCode
- Make sure you already have Leiningen and VSCode up and running.
- To learn how to do this, please refer to the `REPL & VSCode` chapter in the textbook.

## New Application
Let's create a simple program that will manage a garage with different types of cars. We can use Leiningen to create a new project for us using the `app` template by typing "`lein new app garage_system`" in the terminal:

```
PS C:\Users\Amin Taheri\Desktop\Clojure> lein new app garage_system
Generating a project called garage_system based on the 'app' template.
```
This will create a new project for us, if we move into the new `garage_system` folder and use the `ls` command we can see all of the folders Leiningen has generated.

```
PS C:\Users\Amin Taheri\Desktop\Clojure\garage_system> ls


    Directory: C:\Users\Amin Taheri\Desktop\Clojure\garage_system


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        4/18/2020   4:13 PM                doc
d-----        4/18/2020   4:13 PM                resources
d-----        4/18/2020   4:13 PM                src
d-----        4/18/2020   4:13 PM                test
-a----        4/18/2020   4:13 PM            124 .gitignore
-a----        4/18/2020   4:13 PM            164 .hgignore
-a----        4/18/2020   4:13 PM            804 CHANGELOG.md
-a----        4/18/2020   4:13 PM          14476 LICENSE
-a----        4/18/2020   4:13 PM            414 project.clj
-a----        4/18/2020   4:13 PM           1033 README.md
```

Within the `src` folder, there will be a `core.clj` file, which is essentially what is ran when this project runs. If we view what is in `core.clj`, we can see a simple "Hello, World" program as shown below:

``` clojure
(ns garage-system.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))
```
This is where we can write our simple garage system application using knowledge we have gained from previous chapters. Here is the code:

```clojure
(:gen-class)
	(:require [clojure.java.io :as io]))

(defn -main [& args]
	(def carList [])
	(def input "")
	(def quitFlag 0)
	(while (not= quitFlag 1)
		(println "What would you like to do?: ")
		(println "    (1) Enter a car into the system. ")
		(println "    (2) Print all of the cars in the system. ")
		(println "    (3) Save all of the cars in a file. ")
		(println "    (quit) Close program. ")
		(def input (read-line))
		(if (= input "1") (do
			(println "Enter a car name: ")
			(def input (read-line))
			(def carList (conj carList input))
		))
		(if (= input "2") (println carList))
		(if (= input "3") (do
			(println "Enter a file name: ")
			(def fileName (read-line))
			(with-open [fileWriter (io/writer fileName)]
				(doseq [car carList]
					(.write fileWriter car)
					(.newLine fileWriter)))
		))
		(if (= input "quit") (def quitFlag 1))
	)
)
```
This simple program will ask for user input, and the user can either:
1. Enter a car into the system
2. Print all of the cars in the system
3. Save all the cars in a file
4. Close the program

In order to run this program, we need to simply tell Leiningen to run this application for us. We can accomplish this by entering `"lein run garage_system"` in the terminal. Make sure your current directory is the project name you are trying to run before running this command. Here is a simple use of this program:

```
PS C:\Users\Amin Taheri\Desktop\Clojure\garage_system> lein run garage_system
What would you like to do?: 
    (1) Enter a car into the system. 
    (2) Print all of the cars in the system.
    (3) Save all of the cars in a file.
    (quit) Close program.
1
Enter a car name: 
BMW M5
What would you like to do?: 
    (1) Enter a car into the system.
    (2) Print all of the cars in the system.
    (3) Save all of the cars in a file.
    (quit) Close program.
1
Enter a car name:
Audi RS5
What would you like to do?:
    (1) Enter a car into the system.
    (2) Print all of the cars in the system.
    (3) Save all of the cars in a file.
    (quit) Close program.
2
[BMW M5 Audi RS5]
What would you like to do?:
    (1) Enter a car into the system.
    (2) Print all of the cars in the system.
    (3) Save all of the cars in a file.
    (quit) Close program.
quit
```
Congratulations! You now know how to set up and run a project in Clojure using Leiningen. To learn more about the complicated features Leiningen has to offer, you may enter `"lein help"` in the terminal, or visit the official Leiningen site [here](https://Leiningen.org/).