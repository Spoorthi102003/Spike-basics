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
* Integer Multiplication and Division (M)
* Atomic Operations (A) 
* Single Precision Floating-Point (F)
* Double Precision Floating-Point (D)
* Compressed Instructions (C)
* Vector (V)
* Bit Manipulation (B)
* Floating-Point Vector (V)
* Quad-Precision Floating-Point (Q)
* Decimal Floating-Point (L)

# Installation
<details>
<summary> RISC-V toolchain </summary>
  
https://github.com/kunalg123/riscv_workshop_collaterals/blob/master/run.sh

* Download the run.sh
  
* Open terminal

* cd Downloads

* ./run.sh
</details>

# Compiling a C code using RISC-V GCC compiler

Create a C code using gedit:

```
gedit sum1ton.c
```
Type the following floating point addition code:
```
# include<stdio.h>
int main()
{
  float d=10.889, e=11.266;
	float f;
	f=d+e;
	printf("Sum of numbers is %f\n",f);
	return 0;
}
```

![Screenshot from 2024-03-06 19-14-42](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/b4818258-14b5-4650-8687-665db7e083a9)


To compile at unoptimized level using a RISC-V GCC compiler with only base instructions run the following commands:
```
export PATH=~/riscv_toolchain/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14/bin:$PATH
export PATH=~/riscv_toolchain/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14/riscv-unknown-elf/bin:$PATH
riscv64-unknown-elf-gcc -O0 -mabi=lp64 -march=rv64i -o add_float.o add_float.c
```
To run the assembly code generated on spike we give the following command:
```
spike pk add_float.o
```

![Screenshot from 2024-03-06 19-20-49](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/7f047a72-2330-4574-a3b2-ef4d4df83839)


To check the object dump file give the command:
```
riscv64-unknown-elf-objdump -d add_float.o | less
```

![Screenshot from 2024-03-06 19-21-55](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/03a6935a-5f96-4616-819f-8cb2dff092fb)

# To enable or disable an extension and count the number of instructions retired:

To check the extensions available give the following command:
```
riscv64-unknown-elf-gcc -O1 -mabi=lp64 -march=rv64i -o add_float.o add_float.c --print-multi-lib
```

![Screenshot from 2024-03-06 19-44-13](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/76a29e47-b3ad-4e9e-ac25-79e6dcb24b49)

Modify the C code to check the number of clock cycles taken:
```
# include<stdio.h>
int read_cycles(void)
{
int cycles;
asm volatile ("rdcycle %0" : "=r" (cycles));
return cycles;
}
int main()
{
       float d=10.889, e=11.266;
	float f;
	int a= read_cycles();
	f=d+e;
	int b= read_cycles();
	int c=b-a;
	printf("Sum of numbers is %f\n",f);
	printf("The total number of clock cycles taken is %d\n",c);
	return 0;
}
```
Run the C code by enabling different extensions and optimization levels and check the number of clock cycles

For unoptimized or O0 optimization:

![Screenshot from 2024-03-06 20-01-50](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/8426efd1-ae93-4721-99ad-405df923c9c3)

For O3 optimization:

![Screenshot from 2024-03-06 20-04-02](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/217c37fd-3e25-4df6-8452-8dd6eac91f06)

