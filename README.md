# GIAA
Gesture Interfaced Automobile Array

GIAA is the solution to on the road communication that is intuitive and does not distract from safe driving. The LED Array I used was purchased off of Amazon and uses
a Max7219 driver library to display messages to other drivers on the road. The messages that are displayed are as follows: 
1) Thank You!
2) Left Lane is for Passing!
3) Learn to Drive!
4) Thank You!

Of course these messages are easily editable via the codebase.

The display is "Gesture Interfaced." The LED array is controlled by gestures performed over top of a different raspberry pi... The Gestures 
are detected by a Skywriter by Pimoroni. The gesture commands send a cmd to the other pi connected via ssh.  
