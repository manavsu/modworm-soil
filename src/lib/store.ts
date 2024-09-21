import { writable } from 'svelte/store';
import { Socket } from '$lib/network'
import type { TableStore } from "$lib/modbus_table.ts";
import { ModbusDataType } from '$lib/modbus_data_type';
import type { RegisterStore } from './register_store';

export const Working = writable(false);

export const ConnectedSocket= writable<Socket|null>();

export const CurrentTable=writable<TableStore|null>();

export const SelectedDataType=writable<ModbusDataType>(ModbusDataType.Hex);

export const SelectedRegisters=writable<RegisterStore[]>([]);

export const NamedRegisters=writable<RegisterStore[]>([]);