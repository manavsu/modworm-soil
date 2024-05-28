export enum ModbusTable {
    Coils = "coils",
    DiscreteInputs = "discrete inputs",
    HoldingRegisters = "holding registers",
    InputRegisters = "input registers",
}

export function function_code(table: ModbusTable) {
    switch (table) {
        case ModbusTable.Coils:
            return 1;
        case ModbusTable.DiscreteInputs:
            return 2;
        case ModbusTable.HoldingRegisters:
            return 3;
        case ModbusTable.InputRegisters:
            return 4;
    }
}