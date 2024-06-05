import { error } from "@sveltejs/kit";

export enum ModbusDataType {
	UInt16 = 'uint16',
	Int16 = 'int16',
	Hex = 'hex',
	Ascii = 'ascii',
	Bool = 'bool'
}

export function data_type(type: ModbusDataType) {
	switch (type) {
		case ModbusDataType.UInt16:
			return 1;
		case ModbusDataType.Int16:
			return 2;
		case ModbusDataType.Hex:
			return 3;
		case ModbusDataType.Ascii:
			return 4;
		case ModbusDataType.Bool:
			return 5;
	}
}

export function int_to_data_type(type: number) {
	switch (type) {
		case 1:
			return ModbusDataType.UInt16;
		case 2:
			return ModbusDataType.Int16;
		case 3:
			return ModbusDataType.Hex;
		case 4:
			return ModbusDataType.Ascii;
		case 5:
			return ModbusDataType.Bool;
	}
	error(400, "Invalid data type");
}
