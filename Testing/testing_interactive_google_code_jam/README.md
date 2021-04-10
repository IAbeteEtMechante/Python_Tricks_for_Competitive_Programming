#see this comment:
https://codeforces.com/blog/entry/66578?#comment-512288

basically for each interactive problem from google code jam, they will provide a local_testing_tool.py that can generate test cases and act as a judge. 

This version of called codeforces_interactive.py will help to synchornize your solution (called your_solution.py) with that judge and give a nice display for debugging

# How to use

1. Download the file local_testing_tool.py corresponding to your problem and place it in this folder
2. Put your solution, in this folder and rename it solution.py
3. Launch ./test

If all go well, you will see the whole output, ending with:

`
Judge return code: 0
Judge standard error: 
Solution return code: 0
Solution standard error:
`

