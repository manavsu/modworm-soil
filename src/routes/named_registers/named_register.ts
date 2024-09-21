import type { ModbusTable } from "$lib/modbus_table";
import type { RegisterStore } from "$lib/register_store";
import type { NamedRegisterDataType } from "./named_register_data_type";

export interface NamedRegisters {
    name: string;
    registers: RegisterStore[];
    value: string;
    type: NamedRegisterDataType;
    table: ModbusTable;
}

