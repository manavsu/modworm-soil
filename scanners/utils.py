def Signed(ushort):
    if ushort >> 15 == 1:
        return -(ushort ^ 0xFFFF) - 1
    return ushort

def Hex(ushort):
    return f"0x{ushort:04X}"

def Binary(ushort):
    return f"0b{ushort:016b}"

def ASCII(ushort):
    return chr(ushort)

def Bool(ushort):
    return bool(ushort)

def Scaled(scale_factor):
    return 10**scale_factor

def SignedScaledToDouble(short, scale_factor):
    return Signed(short) * Scaled(scale_factor)

def UnsignedScaledToDouble(ushort, scale_factor):
    return ushort * Scaled(scale_factor)

def DecodeBitfield(bitfield, bitfieldEnum):
    faults = []
    for fault in bitfieldEnum:
        if (bitfield & fault.value) == fault.value:
            faults.append(fault)
    return faults