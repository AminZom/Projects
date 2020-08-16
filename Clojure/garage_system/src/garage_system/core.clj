(ns garage-system.core
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