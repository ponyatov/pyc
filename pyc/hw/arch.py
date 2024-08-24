## @file
## @brief architecture

## @defgroup arch arch
## @brief architecture
## @ingroup hw

from pyc.hw import HW

## @brief architecture
## @ingroup arch
class ARCH(HW): pass

## @defgroup x86 x86
## @brief x86: Intel 80x86
## @ingroup arch

## @ingroup x86
class X86(ARCH): pass

## @ingroup x86
class i386(X86): pass

## @ingroup x86
class amd64(X86): pass

## @defgroup arm arm
## @brief ARM: Advanced RISC Machine
## @ingroup arch

## @ingroup arm
class ARM(ARCH): pass

## @ingroup arm
class CortexM(ARM): pass

## @ingroup arm
class CortexM0(CortexM): pass
## @ingroup arm
class CortexM1(CortexM): pass
## @ingroup arm
class CortexM3(CortexM): pass
## @ingroup arm
class CortexM4(CortexM): pass

## @ingroup arch
class CortexA(ARM): pass

## @ingroup arch
class ARM8(ARM): pass

## @ingroup arch
class ARM11(ARM): pass

## @ingroup arch
class AVR(ARCH): pass

## @ingroup arch
class ATmega(AVR): pass

## @ingroup arch
class ATtiny(AVR): pass

## @ingroup arch
class MIPS(ARCH): pass

## @ingroup arch
class RiscV(ARCH): pass
