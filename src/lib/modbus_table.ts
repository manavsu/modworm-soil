export enum ModbusTable {
    Coils = "Coils",
    DiscreteInputs = "Discrete Inputs",
    HoldingRegisters = "Holding Registers",
    InputRegisters = "Input Registers",
}

export interface TableStore {
    register_list: number[][];
    type: ModbusTable;
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