(ns lecture.core (:gen-class))

;; global map of pizzuh info
(def pizza-types {
  :cheese {:toppings ["tomato sauce" "cheese"] :price 10}
  :pepperoni {:toppings ["tomato sauce" "cheese" "pepperoni"] :price 14}
  :deluxe {:toppings ["tomato sauce" "cheese" "pepperoni" "green pepper"] :price 16}
  :hawaiian {:toppings ["tomato sauce" "cheese" "ham" "pineapple"] :price 18}
  :meatlover {:toppings ["tomato sauce" "cheese" "pepperoni" "sausage" "ground beef" "bacon"] :price 20}
})

(defn get-num-pizzas
  "Grabs the number of pizzas the order will have"
  []
  (println "How many pizzas would you like?")
  (let [num-pizzas (Integer/parseInt (read-line))] num-pizzas)
)

(defn checkout
  "Calculates the price of a pizza order and displays all toppings"
  [order]
  (let [total (* (get order :num-pizzas) (get-in pizza-types [(keyword (get order :type)) :price]))]
    (println "Your order total comes to $" total)
    (println "Your pizzas will have the following toppings: " (get-in pizza-types [(keyword (get order :type)) :toppings]))
  total)
)

(defn build-order
  "Builds a pizza order."
  []
  (println "What kind of pizza(s) would you like? Valid options are cheese, deluxe, pepperoni, hawaiian, and meatlover")
  (let [order {:type (read-line) :num-pizzas (get-num-pizzas)}] order)
)

(defn -main 
  "Entry point to the pizza program"
  []
  (println "Welcome to Beans' Garbage Pizzeria!")
  (println (checkout (build-order)))
)

(defn to-be-mocked
  "A method that we're gonna mock!"
  [x]
  (if 
    (= x 1)
    true
    false
  )
)

(defn calls-mocked
  []
  (to-be-mocked 1)
)