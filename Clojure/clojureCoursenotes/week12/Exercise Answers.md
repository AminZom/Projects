# Exceptions answer (found in `week12\test\lecture\exceptions_test.clj`):
```
(deftest exceptWithMsgTests
  (testing "Throws exception with negative"
    (is (thrown-with-msg? Exception #"You dun messed up" (throwsOnNegOrZero -1)))
  )
  (testing "Throws exception with zero"
    (is (thrown? Exception #"You dun messed up HARD"(throwsOnNegOrZero 0)))
  )
)
```


# Checkout test (found in `week12\test\lecture\core_test.clj`):
```
(deftest checkout-tests
  (testing "checkout works as expected with a 1-cheese-pizza order"
    (def checkout-spy (spy/spy checkout))
    (def test-map {:type "cheese" :num-pizzas 1})
    (checkout-spy test-map)
    (is (spy/called? checkout-spy))
    (assert/called-with? checkout-spy test-map)
    (is (= (spy/responses checkout-spy) [10]))
  )
)
```

# Functional test (found in `week12\test\lecture\core_test.clj`):
```
(deftest main-test
  (with-redefs [get-num-pizzas (spy/stub 1) read-line (spy/stub "deluxe")]
    (def main-spy (spy/spy -main))
    (main-spy)
    (is (spy/called? main-spy))
    (is (= (spy/responses main-spy) [nil]))
  )
)
```

