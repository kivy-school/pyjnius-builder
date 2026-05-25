
since we now can wrap whole libraries without needing the .java directly and example onesignal and admob examples 
both needs content from "android" we should have wrapped example of it..

and just allow wrapper to accept python modules (name/path) and when "android" is used it should not need to 
write example Intent in each class...

later we can write a real "android" repo for py wrapper of it, and you just adds it as dep to the pyproject.toml
and all should be good in examples ect them self when refer to Intent ect.. 

but for now make the examples just import our temp "android" / ref to it by pyproject.toml
once its made...