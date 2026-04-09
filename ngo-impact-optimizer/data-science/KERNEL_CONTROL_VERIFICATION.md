Kernel Control Verification

A Jupyter Notebook named kernel_control_demo.ipynb was created to demonstrate kernel management.

Execution Order
Multiple code cells were executed sequentially to show how variables persist across cells.

Interrupt Demonstration
A long-running cell using a loop was executed and manually interrupted using the kernel interrupt option.

Kernel Restart
The kernel was restarted to clear all variables and reset the environment.

State Reset Verification
After restarting, previously defined variables were no longer available, confirming that the kernel state was cleared.

Re-execution
Cells were executed again from the top to restore the state and produce correct outputs.

Conclusion
This demonstrates proper understanding of kernel control, including execution order, interruption, restart, and state management.