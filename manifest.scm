(use-modules
 (gnu packages image-processing))


(concatenate-manifests
 (list
  (specifications->manifest
   '("paraview"
     "python"
     "python-numpy"
     "python-scipy"
     "python-pandas"))))
