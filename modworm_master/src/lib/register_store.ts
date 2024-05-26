import { ModbusDataType } from './modbus_data_type';
export interface RegisterStore {
    value: string;
    address: number;
    type: ModbusDataType;
}