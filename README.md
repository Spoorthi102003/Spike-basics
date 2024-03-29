# Features of SPIKE simulator:
* Spike is an instruction set simulator which is not clock accurate
* Spike is a function simulator which omits all internal delays such as cache misses, memory transactions, IO accesses.

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
riscv64-unknown-elf-gcc --print-multi-lib
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

# For a C code involving loop

![Screenshot from 2024-03-10 16-48-03](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/4ce9ba02-f27c-4c7a-8824-6e8ca612a9bb)


![Screenshot from 2024-03-10 16-46-13](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/8a1cb294-5e8b-4db0-8d61-38b85c886420)


![Screenshot from 2024-03-10 16-48-36](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/ba4c6bf4-e376-446f-bd88-6a1f6a8a71b3)


To get the log or trace file, use the following command:
```
spike -l pk add_float.o 2>spike.txt

```
![Screenshot from 2024-03-22 13-39-17](https://github.com/Spoorthi102003/Spike-basics/assets/143829280/35f691b3-d917-451f-bcb0-eaef8ea19a51)

To get objdump in .txt format,use the following command:
```
riscv64-unknown-elf-objdump -d add_float.o > objdump.txt
```



































































 
