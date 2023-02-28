(TeX-add-style-hook
 "algo"
 (lambda ()
   (TeX-run-style-hooks
    "ntabbing")
   (TeX-add-symbols
    "for"
    "while"
    "iif"
    "elseif"
    "elif"
    "eelse"
    "return"
    "Comment")
   (LaTeX-add-environments
    '("nalgo" LaTeX-env-args ["argument"] 0)
    '("algo" LaTeX-env-args ["argument"] 0)
    '("nalgorithm" 1)
    '("algorithm" 1)))
 :latex)

