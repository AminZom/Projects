(ns lecture.exceptions_test
  (:require [clojure.test :refer :all]
            [lecture.exceptions :refer :all]))

(deftest exceptTests
  (testing "Throws exception with negative"
    (is (thrown? Exception (throwsOnNegOrZero -1)))
  )
  (testing "Throws exception with zero"
    (is (thrown? Exception (throwsOnNegOrZero 0)))
  )
  (testing "Throws no exception with positive"
    (is (= (throwsOnNegOrZero 1) nil))
  )
)

;; So we know an exception was thrown... how can we determine WHICH exception was thrown?
;; thrown-with-msg? to the rescue!
;; Exercise time! Everyone try and write the same tests above, but verify that the two unique exceptions occurred!
;; Refer to slide 9, or https://clojure.github.io/clojure/clojure.test-api.html for hints


; Your answer here :) 


;; Can use the following to run all tests in the current namespace
; (println (run-tests))

;;OR you can specify a namespace:
; (println (run-tests 'lecture.exceptions_test))

;; OR you can run ALL tests in ALL namespaces
; (println (run-all-tests))