(defproject untitled_unmastered "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.8.0"]
                 [enlive "1.1.6"]
                 [http-kit "2.1.18"]
                 [clj-tagsoup "0.3.0" :exclusions [org.clojure/clojure]]
                 [org.clojure/core.async "1.0.567"]]
  :repl-options {:init-ns untitled-unmastered.core})