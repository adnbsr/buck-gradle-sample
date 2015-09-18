### Buck and Gradle

There are lots of discussion how slow Gradle is while build Android projects.However, Facebook's [Buck](https://buckbuild.com/) is better solution to boost development process although there is not sufficient support as *Annotation Processing*, *Android Studio (IDE)*.

I tried to implement a sample to experiment *buck* since **1-2 minutes** up-to 5 are long to debug apps. 


Cons of buck are serious :
 
 - No butterknife
 - No library to implement fast config files
 - No Google library support (download and use as in eclipse ant build)
 - Small community
 
 Pros:
 
 - Really very fast **3-10 seconds** (install and run debug) 
  - reusabilty focused
 - native (c/c++) support
 - Pythonic Syntax  