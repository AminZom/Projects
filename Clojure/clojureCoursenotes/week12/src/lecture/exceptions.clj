(ns lecture.exceptions)

(defn throwsOnNegOrZero
    "I'm gonna throw an exception"
    [x]
    (if (< x 0) 
        (throw (Exception. "You dun messed up")) 
        (if (= x 0) 
            (throw (Exception. "You dun messed up HARD")) 
            (println "You dun not messed up")
        )
    )
)