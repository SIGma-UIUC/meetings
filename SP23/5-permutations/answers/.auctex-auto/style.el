(TeX-add-style-hook
 "style"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("mathdesign" "charter" "cal=cmcal") ("XCharter" "scaled=.96" "sups") ("geometry" "margin=0.75in") ("xcolor" "dvipsnames" "usenames" "cmyk") ("fontenc" "T1") ("inputenc" "utf8") ("parskip" "indent") ("biblatex" "backend=biber" "style=alphabetic")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "mathdesign"
    "XCharter"
    "sourcesanspro"
    "inconsolata"
    "amsmath"
    "latexsym"
    "amsthm"
    "thmtools"
    "stmaryrd"
    "mathtools"
    "physics"
    "centernot"
    "braket"
    "xfrac"
    "optidef"
    "geometry"
    "xcolor"
    "setspace"
    "datetime2"
    "titlesec"
    "fontenc"
    "inputenc"
    "microtype"
    "indentfirst"
    "parskip"
    "float"
    "framed"
    "graphicx"
    "enumitem"
    "listofitems"
    "biblatex"
    "hyperref"
    "cleveref"
    "manfnt")
   (TeX-add-symbols
    '("newqed" ["argument"] 1)
    '("cycle" ["argument"] 1)
    '("quest" 1)
    '("littleoStar" 1)
    '("bigOStar" 1)
    '("littleoT" 1)
    '("bigOT" 1)
    '("bigOmega" 1)
    '("bigTheta" 1)
    '("littleo" 1)
    '("bigO" 1)
    '("ceil" 1)
    '("floor" 1)
    '("Sfrac" 2)
    '("Frac" 2)
    "etal"
    "ie"
    "eg"
    "vitae"
    "apriori"
    "aposteriori"
    "Benes"
    "Bezier"
    "Bjorner"
    "Bochis"
    "Boruvka"
    "Bragger"
    "Bronnimann"
    "Herve"
    "Bruckner"
    "Caratheodory"
    "Chvatal"
    "Vasek"
    "Joao"
    "Cortes"
    "Dujmovic"
    "Fredo"
    "Erdos"
    "Frechet"
    "Furedi"
    "Grobner"
    "Grunbaum"
    "Hanoi"
    "Jarnik"
    "Komlos"
    "Kovari"
    "Lovasz"
    "Matousek"
    "Mnev"
    "Mobius"
    "Mucke"
    "ODunliang"
    "Oleinik"
    "Janos"
    "Palasti"
    "Belen"
    "Petrovskii"
    "Pinar"
    "Plucker"
    "Poincare"
    "Gunter"
    "Sacristan"
    "Saskin"
    "Schomer"
    "Schonhardt"
    "Sos"
    "Stackel"
    "Szekely"
    "Szemeredi"
    "Toth"
    "Turan"
    "Ungor"
    "Voronoi"
    "Godel"
    "argmax"
    "argmin"
    "Sum"
    "Prod"
    "Bigcup"
    "Bigcap"
    "Bigvee"
    "Bigwedge"
    "Int"
    "Lim"
    "Max"
    "Min"
    "Argmax"
    "Argmin"
    "Sup"
    "Inf"
    "Limsup"
    "Liminf"
    "N"
    "Z"
    "Q"
    "R"
    "C"
    "F"
    "E"
    "e"
    "true"
    "false"
    "defeq"
    "into"
    "onto"
    "inonto"
    "from"
    "tofrom"
    "fromto"
    "sample"
    "notimplies"
    "acts"
    "normal"
    "pluseq"
    "timeseq"
    "minuseq"
    "diveq"
    "child"
    "ancestor"
    "contains"
    "containseq"
    "containsneq"
    "gen"
    "prod"
    "coprod"
    "circledS"
    "boldmath"
    "Pal"
    "Zoltan"
    "Laszlo"
    "Jiri"
    "SavedDoubleVert"
    "thiccsymbol"
    "thiccsum"
    "thiccprod")
   (LaTeX-add-environments
    "ddanger"
    "danger")
   (LaTeX-add-lengths
    "thicc")
   (LaTeX-add-saveboxes
    "thicc")
   (LaTeX-add-thmtools-declaretheoremstyles
    "theorem"
    "solution")
   (LaTeX-add-thmtools-declaretheorems
    "thrm"
    "lem"
    "exercise"
    "pf"))
 :latex)

