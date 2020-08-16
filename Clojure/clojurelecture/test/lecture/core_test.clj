(ns lecture.core_test
  (:require [clojure.test :refer :all]
            [lecture.core :refer :all]
            [spy.core :as spy]
            [spy.assert :as assert])
    )

;;;;;;;;;;;;;;;;
;; Unit Tests ;;
;;;;;;;;;;;;;;;;


(deftest spy-tests
  (testing "Spy not called, no responses"
    (def spy-get-num-pizzas (spy/spy read-line))
    (def spy-get-num-pizzas (spy/spy get-num-pizzas))
    (is (= [] (spy/calls (spy/spy spy-get-num-pizzas))))
    (is (= [] (spy/responses spy-get-num-pizzas)))
  )

  ; (testing "A real spy, that's called! (And has no mocked functionality!"
  ;   (with-redefs [get-num-pizzas (spy/spy get-num-pizzas)]
  ;     (get-num-pizzas)
  ;     (is (spy/called? get-num-pizzas))
  ;     (println (spy/responses get-num-pizzas))
  ;   )
  ; )
)

;; Okay, so we've verified that spies are working, cool... now let's stub out get-num-pizzas so our tests won't require user input

(deftest get-num-pizzas-tests
  (testing "get-num-pizzas is stubbed"
    (with-redefs [get-num-pizzas (spy/stub 3)]
      (get-num-pizzas)
      (is (spy/called? get-num-pizzas))
      (is (= [3] (spy/responses get-num-pizzas)))
      (get-num-pizzas)
      (is (= [3 3] (spy/responses get-num-pizzas)))
    )
  )
)

;; Sick, stubs are working! Now we can test that build-order is working...

(deftest build-order-tests
  (testing "build-order with cheese"
    (with-redefs [get-num-pizzas (spy/stub 1) read-line (spy/stub "cheese")]  ;;mock out our dependent methods... Notice that read-line is dependent!!
      (def build-order-spy (spy/spy build-order))
      (build-order-spy)  ;;notice that we have to call on the SPY, not on the method itself
      (is (spy/called? build-order-spy))
      (is (= [{:type "cheese" :num-pizzas 1}] (spy/responses build-order-spy)))
    )
  )

  (testing "build-order with pepperoni"
    (with-redefs [get-num-pizzas (spy/stub 1) read-line (spy/stub "pepperoni")]  ;;mock out our dependent methods... Notice that read-line is dependent!!
      (def build-order-spy (spy/spy build-order))
      (build-order-spy)  ;;notice that we have to call on the SPY, not on the method itself
      (is (spy/called? build-order-spy))
      (is (= [{:type "pepperoni" :num-pizzas 1}] (spy/responses build-order-spy)))
    )
  )

  ;; Can anyone figure out why this is this failing?
  (testing "build-order with hawaiian"
    (with-redefs [get-num-pizzas (spy/stub 3) read-line (spy/stub "hawaiian")]  ;;mock out our dependent methods... Notice that read-line is dependent!!
      (def build-order-spy (spy/spy build-order))
      (build-order-spy)  ;;notice that we have to call on the SPY, not on the method itself
      (is (spy/called? build-order-spy))
      (is (= [{:type "hawaiian" :num-pizzas 2}] (spy/responses build-order-spy)))
    )
  )

  (testing "build-order with deluxe"
    (with-redefs [get-num-pizzas (spy/stub 2) read-line (spy/stub "deluxe")]  ;;mock out our dependent methods... Notice that read-line is dependent!!
      (def build-order-spy (spy/spy build-order))
      (build-order-spy)  ;;notice that we have to call on the SPY, not on the method itself
      (is (spy/called? build-order-spy))
      (is (= [{:type "deluxe" :num-pizzas 2}] (spy/responses build-order-spy)))
    )
  )
)

;; Now you go ahead and write some unit tests for checkout! :)


;;;;;;;;;;;;;;;;;;;;;;
;; Functional Tests ;;  ....sorta
;;;;;;;;;;;;;;;;;;;;;;

;; Can you set up a test allowing us to verify that -main is working properly?
;; Note: I didn't think this one through and it's actually super simple...
;; This will require stubbing read-line and get-num-pizzas for sure (same as above)


;; More fun Spy things!
;; Exceptions can be handled as well...

(deftest exception-test
  (let [f (spy/stub-throws (Exception. "Goodbye World!"))]
        (is (thrown? Exception (f)))
        (is (= 1 (count (spy/responses f))))
        (is (contains? (spy/first-response f) :thrown))
        (is (= "Goodbye World!" (-> (spy/first-response f) :thrown :cause)))
  )
)

(deftest mock-test
  ;; Example mock
  (let [f (spy/mock (fn [x] (if (= 1 x)
                              :one
                              :something-else)))]
        (is (= :one (f 1)))
        (is (spy/called-once? f))
        (is (= :something-else (f 42)))
  )

  ;; Let's mock out an actual function and verify it's behavior now...
  (let [mock (spy/mock (fn [x] (if (= x 1) false true)))]
    (is (= true (calls-mocked))
    (with-redefs [to-be-mocked mock]
      (def main-spy (spy/spy -main))
      (calls-mocked)
      (is (spy/called? mock))
      (is (= (spy/responses mock) [false]))
    )
  )
  )
)
