<script lang="ts">
    import "$lib/app.css";
    import { onMount } from 'svelte';
    import Register from "./register.svelte";
    import { ModbusDataType, data_type, int_to_data_type } from "$lib/modbus_data_type";
    import { ReadRegisters } from "$lib/modbus_client";
    import type { RegisterStore } from "$lib/register_store";
    import LoadingSnake from '$lib/loading_snake.svelte';
	import Error from "$lib/error.svelte";

	export let ip: string;
	export let port: string;
	export let func_code: number;
	export let address: number;
	export let count: number;
	export let type: number;

	let read_error: any;
	let registers: Array<RegisterStore> = [];
	
	async function ReadAllRegisters() {
		try {
 			if(registers.length != count || (registers[0]?.address != address ?? 0)) registers = [];
			const result = await ReadRegisters(ip, port, func_code, address, count, type);
			let data_type = int_to_data_type(type);
			for (let i = 0; i < count; i++) {
				registers[i] = { address: Number(address) + i, value: result[i], type: data_type};
			}
			registers = [...registers];
			read_error = null;
		} catch (error) {
			read_error = error;
		}
	}

	let intervalId: number;
	onMount(() => {
		intervalId = setInterval(async () => {
			await ReadAllRegisters();
		}, 1000);
		return () => {
			clearInterval(intervalId);
		};
	});
</script>

<style lang="postcss">
	.grid-col-fill {
		grid-template-columns: repeat(auto-fill, minmax(104px, 1fr));
	}
</style>

{#if read_error != null}
<Error message={read_error.body.error}/>
{:else if registers.length == 0}
    <LoadingSnake />
{:else}
	<div class="grid grid-col-fill justify-items-center">
		{#each registers as reg, _}
			<Register address={reg.address} value={reg.value} type={reg.type} />
		{/each}
	</div>
{/if}