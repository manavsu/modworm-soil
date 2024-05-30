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
