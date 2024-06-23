import { writable } from 'svelte/store';
import { Socket } from '$lib/network'

export const Working = writable(false);

export const ConnectedSocket= writable<Socket|null>();

export const CurrentTable=writable<number[][]|null>();