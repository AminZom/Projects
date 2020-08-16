---
title: "Working with Files and Directories in Clojure"
layout: article
---

# FILE IO

This chapter covers working with files and directories from Clojure,
using functions in the `clojure.java.io` namespace as well as parts of
the JDK via interoperability.

References: 

<a href="https://github.com/clojuredocs/guides">clojuredocs cookbooks</a>

<a href="https://www.oreilly.com/library/view/clojure-cookbook/9781449366384/ch04.html">o'reilly clojure-cookbook</a>


## Preliminaries

Note that for the examples below, "io" is an alias for
`clojure.java.io`. That is, it's assumed your `ns` macro contains:

``` clojure
(:require [clojure.java.io :as io])
```

or in the repl you've loaded it as so:

``` clojure
(require '[clojure.java.io :as io])
```

or you can type clojure.java.io wherever there is `io`, I don't care.

## Reading Files

Clojure's file read function is (slurp source).

Slurp opens a reader on source and reads all its contents, returning a string.

### Read a file into a string variable

``` clojure
(def string (slurp "foo.txt"))
; sets the contents within foo.txt to variable string
```

You can also read in urls:
```clojure
(slurp "http://clojuredocs.org")
;returns the html of the website
```


### Read a file one line at a time

Suppose you'd like to read every line in a file,
and return the result sequence:

``` clojure
(with-open [r (clojure.java.io/reader "foo.txt")]
  (doseq [line (line-seq r)]
    (println line)))
```
 - with-open opens the file and ensures it is closed at the end
 - io/reader creates a Java reader 
 - line-seq returns the lines of text from rdr as a lazy sequence of strings


 If you want to call on function on every line in a file and return the sequence:

 ```clojure
(with-open [rdr (io/reader "foo.txt")]
  (doall (map function (line-seq rdr))))
 ```
 - this maps the function call to each line and does them all

## Writing Files

Clojure's file read function is (spit location data).

Spit opens location with writer, writes content, then closes location.

### Write a string out to a new file

``` clojure
(spit "foo.txt"
      "A long
multi-line string.
Bye.")
```
Spit crates a file if it doesn't exist.
Spit overwrites the file if it already exists. To append, use the :append flag

``` clojure
(spit "foo.txt" "file content" :append true)
```


### Write a file one line at a time

Suppose you'd like to write out every item in a vector, one item per
line:

``` clojure
(with-open [wrtr (io/writer "foo.txt")]
  (doseq [item my-vec]
    (.write wrtr item)
    (.newLine wrtr)))
```

 - with-open opens the file and ensures it is closed at the end
 - io/writer creates a java writer (in this case called wrtr) to allow you to write to file
 - doseq is looping through the vector and associating the current element in the vector as i
 - .write is a Java method that allows you to add your data to the writer, in this case adding the element and a newline into the writer

## Other File Functions

### Copy files

Invoke clojure.java.io/copy, passing it the source and destination files:

```clojure
(clojure.java.io/copy
  (clojure.java.io/file "./source.txt")
  (clojure.java.io/file "./destination-copy.txt"))
```
The input argument to copy doesn’t have to be a file; it can be an InputStream, a Reader, a byte array, or a string:

```clojure
(clojure.java.io/copy
  "some text"
  (clojure.java.io/file "./destination-copy.txt"))
```
if the destination file already exists, it will be overwritten

### Delete file

```clojure
(io/delete-file "foo.txt")
```

### Check if a file exists

``` clojure
(.exists (io/file "filename.txt"))
```

### Is it a directory? 

``` clojure
(.isDirectory (io/file "path/to/something"))
```

An io/file is a java.io.File object (a file or a directory). You can
call a number of functions on it, including:

    exists        Does the file exist?
    isDirectory   Is the File object a directory?
    getName       The basename of the file.
    getParent     The dirname of the file.
    getPath       Filename with directory.
    mkdir         Create this directory on disk.

To read about more available methods, see [the java.io.File
docs](http://docs.oracle.com/javase/7/docs/api/java/io/File.html).


### Get a list of the files and dirs in a given directory

As `File` objects:

``` clojure
(.listFiles (io/file "path/to/some-dir"))
```

Same, but just the *names* (strings), not File objects:

``` clojure
(.list (io/file "path/to/some-dir"))
```

or you can use (file-seq dir) to return a tree seq on java.io.Files

```clojure
(def f (clojure.java.io/file "c:\\clojure-1.2.0")) ;f is directory
(def fs (file-seq f)) ;fs is file sequence in directory
(first fs) ;the first element in fs is the root, so it's the same directory
(clojure.pprint/pprint (take 10 fs)) ;takes the first 10 files/directories in the given directory
```

### Rebinding STDOUT

By default, the print and println functions will print content passed to them to STDOUT:

``` clojure
(println "This text will be printed to STDOUT.")
;; *out*
;; This text will be printed to STDOUT.
```

You can rebind the output to go to STDERR:

``` clojure
(binding [*out* *err*]
  (println "Error!"))
```
The bound value of *out* is not restricted to operating system streams; \*out\* can be any stream-like object.
This means that it can be used to write to files as well:

``` clojure
;; Create a writer to file test.txt and print to it.
(def foo-file (clojure.java.io/writer "foo.txt"))
(binding [*out* foo-file]
  (println "Foo bar."))

;; Nothing is printed to *out*.

;;close the file.
(.close foo-file)
```

### Using temporary files

Use the built in Java method createTempFile, which takes a prefix and suffix parameter:

``` clojure
(def temp-file (java.io.File/createTempFile "filename" ".txt"))
```

You can then write to the temporary file like you would to any other file.

To get the full path and filename of the temporary file:
``` clojure
(.getAbsolutePath temp-file)
```

To mark the temporary file to be deleted automatically when the JVM exits:
``` clojure
(.deleteOnExit temp-file)
```

To delete temporary files immediately when they are no longer being used:
``` clojure
(.delete temp-file)
```


## Different File types

### CSV Data

Use clojure.data.csv/read-csv to lazily read CSV data from a String or java.io.Reader:

```clojure
(clojure.data.csv/read-csv "a,b\nc,d" )
;; -> (["a" "b"] ["c" "d"])
```
```clojure
(with-open [in-file (clojure.java.io/reader "file.csv")]
  (doall
    (clojure.data.csv/read-csv in-file)))
;; -> (["a" "b"] ["c" "d"])
```

to write to a csv:
```clojure
(with-open [out-file (clojure.java.io/writer "file.csv")]
            (clojure.data.csv/write-csv out-file [["a" "b"] ["c" "d"]]))
```

### JSON Data

Use the clojure.data.json/read-str function to read a string of JSON as Clojure data:

```clojure
(require '[clojure.data.json :as json])

(json/read-str "[{\"name\":\"Sam\",\"age\":23}]")
;; -> [{"name" "Sam", "age" 23}]
```

To write data to JSON, use the clojure.data.json/write-str function with Clojure data:
```clojure
(with-open [writer (clojure.java.io/writer "foo.json")
  (json/write-str [{"name" "Sam", "age" 23}] writer)
```
### XML Data

If you have an xml file like this:
```xml
<simple>
  <item id="1">First</item>
  <item id="2">Second</item>
</simple>
```
Pass the file to clojure.xml/parse to get a Clojure map representing the structure of an XML file.

```clojure
(require '[clojure.xml :as xml])
(clojure.xml/parse (clojure.java.io/file "simple.xml"))
;; -> {:tag :simple, :attrs nil, :content [
;;    {:tag :item, :attrs {:id "1"}, :content ["First"]}
;;    {:tag :item, :attrs {:id "2"}, :content ["Second"]}]}
```
### other file types

You can make a PDF with the clj-pdf library:
```clojure
(require '[clj-pdf.core :as pdf])
(pdf/pdf [{:title "Hello World"} "Hello, World."] "hello-world.pdf")
```

Read or write a file compressed with gzip:
```clojure
;; decompress
(with-open [in (java.util.zip.GZIPInputStream.
                (clojure.java.io/input-stream
                 "file.txt.gz"))]
  (slurp in))

;; compress
(with-open [w (-> "output.gz"
                  clojure.java.io/output-stream
                  java.util.zip.GZIPOutputStream.
                  clojure.java.io/writer)]
  (binding [*out* w]
    (println "This will be compressed.")))
```


## See also

  * <https://github.com/Raynes/fs>
  * the I/O section of the [cheatsheet](http://clojure.org/cheatsheet)