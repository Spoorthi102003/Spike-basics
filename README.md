# Spike model includes:
* Model a RISC-V hart
* Processor stepping, including fetch and execution.
* Optional: MMU for VA->PA
* Trap Handling including exception and interrupt handling.
  
# Features of SPIKE simulator:
* Spike is an instruction set simulator which is not clock accurate
* Spike is a function simulator which omits all internal delays such as cache misses, memory transactions, IO accesses.
* It uses a multi core framework
* Spike tries to model architecture of hart, CSR(Control and status register), pc, registers and floating point registers.
* The cache used is write back type. It uses lfsr to find the victim when a replacement happens.

# Memory herarchy:
![image](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/263e4e9a-d6d9-4f97-93ef-531a707f0d9a)

![image](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/1adbd15b-1f15-430c-b6d7-44fdd34d5f78)

# Extensions supported by Spike:
Integer Multiplication and Division (M)
Atomic Operations (A) 
Single Precision Floating-Point (F)
Double Precision Floating-Point (D)
Compressed Instructions (C)
Vector (V)
Bit Manipulation (B)
Floating-Point Vector (V)
Quad-Precision Floating-Point (Q)
Decimal Floating-Point (L)









