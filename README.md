#CentOS Liquidsoap 1.0.1 RPM

##Instructions

After pulling, make sure to run 

`mkdir -p {BUILD,RPMS,SOURCES,SPECS,SRPMS}`

in the base git repository to create all necessary directories.

You can run 

`rpmbuild -ba SPECS/liquidsoap.spec` 

from the base directory to build the package. Do *not* run this as root.
