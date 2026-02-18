## Making Changes While in Debug Mode

You can make changes to files while halted at a breakpoint, just like you normally would. However, the debug session will not know that those changes have been made until you restart the session. 

You can add more breakpoints while in debug mode and the current mode will respect them, you do not need to restart. 

## Debugging Jupyter Notebooks

Jupyter notebooks can also run in Debugger Mode if run inside of Cursor. To do so, simply select “Run in Debug Mode” from the dropdown menu of the Play Button next to the cell you want to execute.

## Nuances

Sometimes the debugger seems to be doing odd things, I hope this section helps dispel some of that mystery.

1. Say you have a breakpoint set on the following line:
    
    `[ x for x in list_of_things if x == 'thing I want' ]`
    
    After the program halts here, if you press the Continue button, you’ll notice the debugger seems to not advance to the next executable line like you’d expect it would. This is because the breakpoint on this line is triggered at every loop of the contained list comprehension, each iteration of list_of_things.
    
2. If you are stepping through a logic block like an if statement:
    
    `if this_should_be_true == True:`
    
    `print(”hooray!”)`
    
    Say the debugger is halted on the if statement condition line. Pressing Step will advance the debugger to the print line. Pressing Step again will execute the print, and then advance back up to the if condition line. Pressing Step one more time will advance the debugger out of the logic block.
    
3. The debugger is active across all computation Threads. Therefore, if you have breakpoints set in a parallelized piece of code, you may see your debugger suddenly halt at other breakpoints that may not make sense for the bug you are trying to investigate. To reduce this, serialize your computation while debugging.