- If no opencv in the system use something else...
  need to see what alternative there are and use one of them

+ Need to add some kind of parameter parser so some of the options will be 
  constant untill said otherwise

- Need to check against the v4l2-util what is the supported 
  resulotions and more

+ Need a parameter for where to create all the picturse

- Need a parameter that saves the photos or removes 
  after creating the timelapse

- Need a progress bar to show how much time it's working,
  how much time remaining, how much pictures it took and more stats for geeks

+ Need a parameter for quality

- Need a parameter for compression type

+ Need to check how it works on a windows system and fix it so it will run
  with creating the film afterwards

+ Need to add functionality to stop the timelapse...
  capture some key press so that it can stop if the event stopped before
  the time I thought it would take. (It's done with pressing q)

- In linux need to fix the select so it won't wait until the enter is pressed..
  it should work like it's on windows
