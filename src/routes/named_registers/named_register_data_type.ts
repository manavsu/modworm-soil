import { ModbusDataType } from "$lib/modbus_data_type";

export enum NamedRegisterDataType {
    Int = 'int',
    UInt = 'uint',
    Hex = 'hex',
    Float = 'float',
    String = 'string',
    Bool = 'bool'
}

export function modbus_data_type_to_named_register_data_type(type: ModbusDataType) {
    switch (type) {
        case ModbusDataType.UInt16:
            return NamedRegisterDataType.UInt;
        case ModbusDataType.Int16:
            return NamedRegisterDataType.Int;
        case ModbusDataType.Hex:
            return NamedRegisterDataType.Hex;
        case ModbusDataType.Ascii:
            return NamedRegisterDataType.String;
        case ModbusDataType.Bool:
            return NamedRegisterDataType.Bool;
    }
}