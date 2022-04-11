GIT and VCS related stuff
Setup git account via PyCharm -> you should be able to pull/push commits within your IDE
Add a .gitignore file to your repo
after updating your local repo from portal, for any further refactoring or development create a separate brunch; e.g. for today's refactoring create refactoring_Apr_10 brunch Do not create merge requests yet, simply add you changes in different branches Tip -> first checkout new brunch, than start coding
try to switch between branches and try to spot the difference
Refactoring of the existing code base
Rename file into main.py [x]

Add default python design via if name == main :

IDE raises error for main function -> define a corresponding func
You can use pass keyword for now
Split the range size input number with the thousand separator (Make a commit here) Tip - look for underscore sign

Format the output of object size to use a thousand separator (e.g. 2,800,496 bytes) ; Tip - look for f-string internal syntax formatting

Combine 2 print calls on lines 16-17 into 1, the strings should be still displayed on separate lines Tip - look for sep parameter

Round your execution duration output to only 4 decimal places

Return to this point after going through point 1 of the next section

Resolve an issue with shadowing built-in objects
Ongoing tasks and further development
Call list and tuple conversions several times more after line 10
After you resolve the issue - create a new brunch from your main - feature_Apr_10 and continue developing
Prettify the output - add a header line of 79 equality signs as the first output
Repeat the same line as the bottom of the output, e.g.:
================ your prints
Repeat your memory measurement but now use list comprehension expression for list and generator expression for tuple
Display results for all 4 cases
