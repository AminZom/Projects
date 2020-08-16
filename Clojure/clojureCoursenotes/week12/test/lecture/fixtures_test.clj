(ns lecture.fixtures_test
    (:require [clojure.test :refer :all])
)

(defn simple-fixture [f]
    (println "Running before a test!")
    (f)
    (println "Running after a test!")
)


(deftest simple-test
    (println "simple test...")
    (is (= 1 1))
)

(deftest another-test
    (println "another test...")
    (is (= 2 2))
)

; (use-fixtures :once simple-fixture)
(use-fixtures :each simple-fixture)