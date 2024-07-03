import { writable } from 'svelte/store';
import { Socket } from '$lib/network'
import type { TableStore } from "$lib/modbus_table.ts";

export const Working = writable(false);

export const ConnectedSocket= writable<Socket|null>();

export const CurrentTable=writable<TableStore|null>();