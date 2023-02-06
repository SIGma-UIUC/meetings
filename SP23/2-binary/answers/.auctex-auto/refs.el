(TeX-add-style-hook
 "refs"
 (lambda ()
   (LaTeX-add-bibitems
    "book:lorem_ipsum"
    "site:xkcd"
    "TAOCP4A"))
 :bibtex)

