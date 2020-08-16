(ns lecture.test_runner 
    (:require [clojure.test :refer :all]
              [lecture.exceptions_test :refer :all]
              [lecture.core_test :refer :all]
    )
)
(println (run-tests 'lecture.exceptions_test))
; (println (run-tests 'lecture.core_test))
