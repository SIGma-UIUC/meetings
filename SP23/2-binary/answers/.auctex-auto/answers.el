(TeX-add-style-hook
 "answers"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "letterpaper")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "style"
    "algo"
    "quiver")
   (LaTeX-add-bibliographies
    "refs"))
 :latex)

